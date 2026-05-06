import json
import os
from contextlib import contextmanager
from datetime import datetime

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor, Json
except ImportError:  # Allows local syntax checks before dependencies are installed.
    psycopg2 = None
    RealDictCursor = None
    Json = None


def _database_url():
    db_url = os.getenv("DB_URL")
    if db_url:
        return db_url

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    name = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST", "db")
    if user and password and name:
        return f"postgresql://{user}:{password}@{host}:5432/{name}"
    return None


def enabled():
    return psycopg2 is not None and _database_url() is not None


@contextmanager
def connection():
    if not enabled():
        yield None
        return

    conn = psycopg2.connect(_database_url())
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    if not enabled():
        return False

    schema = """
    CREATE TABLE IF NOT EXISTS targets (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        target_type TEXT DEFAULT 'unknown',
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

    CREATE TABLE IF NOT EXISTS scans (
        id TEXT PRIMARY KEY,
        target_id INTEGER REFERENCES targets(id),
        target TEXT NOT NULL,
        stream_type TEXT NOT NULL DEFAULT 'local_vm',
        workflow_status TEXT NOT NULL DEFAULT 'queued',
        research_scope JSONB NOT NULL DEFAULT '{}'::jsonb,
        scope_approved BOOLEAN NOT NULL DEFAULT FALSE,
        status TEXT NOT NULL,
        current_step INTEGER NOT NULL DEFAULT 0,
        max_steps INTEGER NOT NULL DEFAULT 15,
        kb_loaded INTEGER NOT NULL DEFAULT 0,
        report TEXT,
        report_file TEXT,
        error TEXT,
        started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        finished_at TIMESTAMPTZ,
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

    CREATE TABLE IF NOT EXISTS tool_runs (
        id SERIAL PRIMARY KEY,
        scan_id TEXT NOT NULL REFERENCES scans(id) ON DELETE CASCADE,
        step INTEGER NOT NULL,
        command TEXT NOT NULL,
        status TEXT NOT NULL,
        exit_code INTEGER,
        stdout TEXT,
        stderr TEXT,
        output_preview TEXT,
        started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        finished_at TIMESTAMPTZ,
        metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
        UNIQUE(scan_id, step)
    );

    CREATE TABLE IF NOT EXISTS reports (
        id SERIAL PRIMARY KEY,
        scan_id TEXT NOT NULL UNIQUE REFERENCES scans(id) ON DELETE CASCADE,
        target_id INTEGER REFERENCES targets(id),
        filename TEXT NOT NULL,
        path TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

    CREATE TABLE IF NOT EXISTS findings (
        id SERIAL PRIMARY KEY,
        scan_id TEXT NOT NULL REFERENCES scans(id) ON DELETE CASCADE,
        target_id INTEGER REFERENCES targets(id),
        title TEXT NOT NULL,
        severity TEXT NOT NULL DEFAULT 'INFO',
        owasp_category TEXT,
        evidence TEXT,
        remediation TEXT,
        confidence NUMERIC(3, 2) DEFAULT 0.50,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

    CREATE TABLE IF NOT EXISTS target_memory (
        id SERIAL PRIMARY KEY,
        target_id INTEGER NOT NULL REFERENCES targets(id) ON DELETE CASCADE,
        memory_type TEXT NOT NULL,
        summary TEXT NOT NULL,
        source_scan_id TEXT REFERENCES scans(id) ON DELETE SET NULL,
        metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );

    CREATE INDEX IF NOT EXISTS idx_scans_status ON scans(status);
    CREATE INDEX IF NOT EXISTS idx_scans_stream_type ON scans(stream_type);
    CREATE INDEX IF NOT EXISTS idx_scans_workflow_status ON scans(workflow_status);
    CREATE INDEX IF NOT EXISTS idx_scans_target ON scans(target);
    CREATE INDEX IF NOT EXISTS idx_tool_runs_scan_step ON tool_runs(scan_id, step);
    CREATE INDEX IF NOT EXISTS idx_findings_target ON findings(target_id);
    CREATE INDEX IF NOT EXISTS idx_target_memory_target ON target_memory(target_id);
    """

    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute(schema)
            cur.execute("ALTER TABLE scans ADD COLUMN IF NOT EXISTS stream_type TEXT NOT NULL DEFAULT 'local_vm'")
            cur.execute("ALTER TABLE scans ADD COLUMN IF NOT EXISTS workflow_status TEXT NOT NULL DEFAULT 'queued'")
            cur.execute("ALTER TABLE scans ADD COLUMN IF NOT EXISTS research_scope JSONB NOT NULL DEFAULT '{}'::jsonb")
            cur.execute("ALTER TABLE scans ADD COLUMN IF NOT EXISTS scope_approved BOOLEAN NOT NULL DEFAULT FALSE")
    return True


def upsert_target(name, target_type="unknown"):
    if not enabled():
        return None

    with connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO targets (name, target_type)
                VALUES (%s, %s)
                ON CONFLICT (name)
                DO UPDATE SET updated_at = NOW()
                RETURNING id
                """,
                (name, target_type),
            )
            return cur.fetchone()["id"]


def create_scan(scan):
    if not enabled():
        return

    target_id = upsert_target(scan["target"])
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO scans (
                    id, target_id, target, stream_type, workflow_status,
                    research_scope, scope_approved, status, current_step,
                    max_steps, kb_loaded, started_at, updated_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
                ON CONFLICT (id)
                DO UPDATE SET
                    stream_type = EXCLUDED.stream_type,
                    workflow_status = EXCLUDED.workflow_status,
                    research_scope = EXCLUDED.research_scope,
                    scope_approved = EXCLUDED.scope_approved,
                    status = EXCLUDED.status,
                    current_step = EXCLUDED.current_step,
                    max_steps = EXCLUDED.max_steps,
                    kb_loaded = EXCLUDED.kb_loaded,
                    updated_at = NOW()
                """,
                (
                    scan["id"],
                    target_id,
                    scan["target"],
                    scan.get("stream_type", "local_vm"),
                    scan.get("workflow_status", "queued"),
                    Json(scan.get("research_scope", {})) if Json else json.dumps(scan.get("research_scope", {})),
                    scan.get("scope_approved", False),
                    scan["status"],
                    scan.get("current_step", 0),
                    scan.get("max_steps", 15),
                    scan.get("kb_loaded", 0),
                    scan.get("started_at", datetime.now().isoformat()),
                ),
            )


def update_scan(scan_id, **fields):
    if not enabled() or not fields:
        return

    allowed = {
        "status",
        "stream_type",
        "workflow_status",
        "research_scope",
        "scope_approved",
        "current_step",
        "max_steps",
        "kb_loaded",
        "report",
        "report_file",
        "error",
        "finished_at",
    }
    updates = []
    values = []
    for key, value in fields.items():
        if key in allowed:
            updates.append(f"{key} = %s")
            values.append(value)

    if not updates:
        return

    updates.append("updated_at = NOW()")
    values.append(scan_id)
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"UPDATE scans SET {', '.join(updates)} WHERE id = %s",
                values,
            )


def save_tool_run(scan_id, step):
    if not enabled():
        return

    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tool_runs (
                    scan_id, step, command, status, exit_code, stdout, stderr,
                    output_preview, started_at, finished_at, metadata
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (scan_id, step)
                DO UPDATE SET
                    command = EXCLUDED.command,
                    status = EXCLUDED.status,
                    exit_code = EXCLUDED.exit_code,
                    stdout = EXCLUDED.stdout,
                    stderr = EXCLUDED.stderr,
                    output_preview = EXCLUDED.output_preview,
                    finished_at = EXCLUDED.finished_at,
                    metadata = EXCLUDED.metadata
                """,
                (
                    scan_id,
                    step["step"],
                    step.get("command", ""),
                    step.get("status", "running"),
                    step.get("exit_code"),
                    step.get("stdout", ""),
                    step.get("stderr", ""),
                    step.get("output", ""),
                    step.get("timestamp"),
                    step.get("finished_at"),
                    Json(step.get("metadata", {})) if Json else json.dumps(step.get("metadata", {})),
                ),
            )


def save_report(scan_id, target, filename, path, content):
    if not enabled():
        return

    target_id = upsert_target(target)
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO reports (scan_id, target_id, filename, path, content)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (scan_id)
                DO UPDATE SET
                    filename = EXCLUDED.filename,
                    path = EXCLUDED.path,
                    content = EXCLUDED.content
                """,
                (scan_id, target_id, filename, path, content),
            )
            cur.execute(
                """
                INSERT INTO target_memory (
                    target_id, memory_type, summary, source_scan_id, metadata
                )
                VALUES (%s, 'report_summary', %s, %s, %s)
                """,
                (
                    target_id,
                    content[:4000],
                    scan_id,
                    Json({"report_file": filename}) if Json else json.dumps({"report_file": filename}),
                ),
            )


def replace_findings(scan_id, target, findings):
    if not enabled():
        return

    target_id = upsert_target(target)
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM findings WHERE scan_id = %s", (scan_id,))
            for finding in findings:
                cur.execute(
                    """
                    INSERT INTO findings (
                        scan_id, target_id, title, severity, owasp_category,
                        evidence, remediation, confidence
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        scan_id,
                        target_id,
                        finding.get("title", "Untitled finding"),
                        finding.get("severity", "INFO"),
                        finding.get("owasp_category"),
                        finding.get("evidence"),
                        finding.get("remediation"),
                        finding.get("confidence", 0.50),
                    ),
                )


def get_scan(scan_id):
    if not enabled():
        return None

    with connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM scans WHERE id = %s", (scan_id,))
            scan = cur.fetchone()
            if not scan:
                return None
            cur.execute(
                """
                SELECT step, command, status, exit_code, output_preview AS output,
                       started_at AS timestamp
                FROM tool_runs
                WHERE scan_id = %s
                ORDER BY step ASC
                """,
                (scan_id,),
            )
            scan["steps"] = cur.fetchall()
            return _format_scan(scan)


def list_scans():
    if not enabled():
        return None

    with connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM scans ORDER BY started_at DESC LIMIT 100")
            rows = cur.fetchall()
            return [_format_scan(row, include_steps=False) for row in rows]


def load_target_memory(target, limit=5):
    if not enabled():
        return ""

    with connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id FROM targets WHERE name = %s", (target,))
            target_row = cur.fetchone()
            if not target_row:
                return ""
            cur.execute(
                """
                SELECT memory_type, summary, created_at
                FROM target_memory
                WHERE target_id = %s
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (target_row["id"], limit),
            )
            rows = cur.fetchall()

    if not rows:
        return ""
    chunks = []
    for row in rows:
        chunks.append(f"[{row['memory_type']} @ {row['created_at']}]\n{row['summary']}")
    return "\n\n".join(chunks)


def _format_scan(row, include_steps=True):
    started_at = row.get("started_at")
    finished_at = row.get("finished_at")
    return {
        "id": row["id"],
        "target": row["target"],
        "stream_type": row.get("stream_type", "local_vm"),
        "workflow_status": row.get("workflow_status", "queued"),
        "research_scope": row.get("research_scope", {}),
        "scope_approved": row.get("scope_approved", False),
        "status": row["status"],
        "current_step": row.get("current_step", 0),
        "max_steps": row.get("max_steps", 15),
        "steps": row.get("steps", []) if include_steps else [],
        "report": row.get("report"),
        "report_file": row.get("report_file"),
        "kb_loaded": row.get("kb_loaded", 0),
        "started_at": started_at.isoformat() if hasattr(started_at, "isoformat") else started_at,
        "finished_at": finished_at.isoformat() if hasattr(finished_at, "isoformat") else finished_at,
    }
