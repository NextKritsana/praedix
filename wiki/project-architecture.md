# Praedix Project Architecture

**Summary**: Praedix is an AI security operations system that combines a React dashboard, Flask API, isolated scanner runtimes, Postgres structured memory, and an Obsidian-style Markdown vault.

**Last updated**: 2026-05-05

---

## Purpose

Praedix supports two security workflows:

- **Stream A: Vulnerability research** - recon, CVE triage, dark-web/OSINT research, human review, and client advisory drafting.
- **Stream B: Local VM testing** - local or VM-based web app testing, OWASP checks, scan analysis, and pre-deploy reporting.

The product should behave like an AI security operations workspace, not only a scanner. Human approval is required for sensitive research or client-facing output.

## Runtime Structure

- `frontend/` - React + Vite dashboard.
- `api/` - Flask API and AI scan orchestration.
- `api/db.py` - Postgres persistence layer.
- `tools/` - isolated tool runtimes.
- `tools/hackingtool_wrapper.py` - scanner wrapper for tools such as `nmap`, `nikto`, `dirb`, `sqlmap`, `whois`, `dig`, `curl`, `sslscan`, `wafw00f`, and `traceroute`.
- `tools/onionclaw_wrapper.py` - gated OnionClaw/Tor OSINT wrapper for research actions.
- `praedix_cli.py` - terminal client that starts scans through the Flask API and renders status/progress in PowerShell.
- `praedix.cmd` - Windows launcher for the CLI.
- `ascii-image-converter.cmd` - project wrapper for the installed image-to-ASCII converter.
- `make-banner.cmd` - helper that converts an image into `assets/banner.txt`.
- `assets/banner.txt` - editable CLI banner, currently generated from the user's local MJ image.
- `agents/` - older commander scripts and agent runtime files.
- `vault/` - Obsidian-style long-term memory, knowledge base, and generated reports.
- `wiki/` - maintained security intelligence wiki.
- `docker-compose.yml` - local orchestration for frontend, API, Postgres, Redis, scanner, OnionClaw, DVWA, and nginx.

## Data Model

Postgres is now the structured application database. Obsidian/Markdown remains the human-readable knowledge base and report store.

Primary Postgres tables:

- `targets`
- `scans`
- `tool_runs`
- `reports`
- `findings`
- `target_memory`

Important scan fields:

- `stream_type` - identifies the workflow stream, currently `local_vm` or `research`.
- `workflow_status` - identifies the current stage, such as `loading_knowledge`, `local_scan`, `recon_and_triage`, `pre_deploy_report`, or `awaiting_human_review`.
- `research_scope` - JSON scope for research stream work.
- `scope_approved` - boolean gate for research work.

## Hybrid Memory Design

Use the two storage systems differently:

- **Postgres** is the source of truth for scan state, tool runs, findings, target memory, and report metadata.
- **Obsidian vault / Markdown** is the source of truth for human-readable knowledge, wiki pages, notes, and final reports.

When a scan completes, Praedix saves structured records to Postgres and still writes a Markdown report under `vault/Reports`.

## Current API Behavior

Scan lifecycle:

1. `POST /api/scan` creates a scan.
2. API creates or updates the target in Postgres.
3. API records scan status and `workflow_status`.
4. AI chooses allowed scanner tools.
5. Each tool run is saved to `tool_runs`.
6. Final report is saved to Postgres and `vault/Reports`.
7. Coarse findings are extracted into `findings`.
8. Report content is summarized into `target_memory`.

Research endpoints:

- `GET /api/research/onionclaw/status`
- `POST /api/research/onionclaw/run`

Status endpoint:

- `GET /api/status` returns API, scanner, database, and OnionClaw state.

## CLI Behavior

Praedix can now be used from PowerShell without opening the web UI.

Entrypoints:

- `python .\praedix_cli.py`
- `.\praedix.cmd`

Banner customization:

- Default custom banner file: `assets/banner.txt`
- Edit `assets/banner.txt` to draw your own terminal art.
- `ascii-image-converter` is installed via Go under the user's Go bin.
- `ascii-image-converter.cmd` wraps the installed converter for this project.
- `make-banner.cmd` converts an image file into `assets/banner.txt`.
- Use `--banner path\to\banner.txt` for a one-off banner.
- Use `--no-banner` to fall back to the built-in Praedix text banner.

Common commands:

```powershell
.\praedix.cmd --status
.\praedix.cmd -u dvwa
.\praedix.cmd -u scanme.nmap.org -v
.\praedix.cmd -u scanme.nmap.org -v --report-preview
.\praedix.cmd -u ginandjuice.shop --stream research
.\praedix.cmd -u ginandjuice.shop --stream research --dark-web --keywords "ginandjuice.shop,Gin and Juice" --approved-by acer
.\praedix.cmd --status --banner .\assets\banner.txt
.\make-banner.cmd "C:\path\to\poster.jpg" 90
```

The CLI only talks to the existing API. It does not run scanner tools directly.

If the user passes a full URL such as `http://scanme.nmap.org/`, the CLI normalizes it to the hostname before sending it to `/api/scan`, because the current scanner commands expect a domain/IP/service target rather than a URL with scheme and path.

Target validation:

- Single-label targets are blocked unless explicitly allowed as local aliases.
- Default allowed single-label aliases: `dvwa`, `localhost`.
- This prevents inputs such as `porn` from being treated as the public `.porn` TLD and then drifting into registry infrastructure.
- To allow another local Docker service, set `PRAEDIX_ALLOWED_SINGLE_LABEL_TARGETS`, for example `dvwa,localhost,my-webapp`.
- Public targets should use a full hostname such as `example.com` or `example.porn`.

Final CLI output is intentionally concise by default:

```text
[+] Scan complete
Report file: YYYY-MM-DD_HH-MM-SS_target.md
```

The CLI no longer prints the full report preview unless `--report-preview` is passed.

## OnionClaw Integration

OnionClaw is treated as a high-risk research capability and is isolated in a separate runtime.

Allowed wrapper actions:

- `check_tor`
- `renew`
- `check_engines`
- `search`
- `fetch`
- `pipeline`

Guardrails:

- OnionClaw is optional. `Vulnerability Research` can run without dark web / OSINT search.
- The frontend exposes `Search dark web / OSINT with OnionClaw` as an explicit checkbox.
- If the checkbox is off, research scans skip OnionClaw and do not require detailed scope fields.
- Research work must have approved scope.
- Scope must include `approved=true`, `approved_by`, and `allowed_keywords`.
- `.onion` fetch requires `allow_onion_fetch=true`.
- Tor identity rotation requires `allow_identity_rotation=true`.
- Blocked research keywords are rejected.
- AI should not run arbitrary shell commands against OnionClaw.

## Frontend Behavior

Dashboard:

- Shows total scans.
- Shows active scans.
- Separates Research Stream and Local VM Stream counts.
- Shows active scan `stream_type / workflow_status`.

New Scan:

- Lets the user choose `Local VM Testing` or `Vulnerability Research`.
- Research stream requires scope approval controls before the scan can start.

Sidebar:

- Shows API status.
- Shows scanner status.
- Shows database status.
- Shows OnionClaw status.

## Verification Status

Validated on 2026-05-04:

```powershell
python -m py_compile api\app.py api\db.py tools\onionclaw_wrapper.py
npm.cmd run build
docker compose config
```

All passed.

Validated on 2026-05-05:

```powershell
python -m py_compile praedix_cli.py
.\praedix.cmd --help
.\praedix.cmd --status
.\ascii-image-converter.cmd -h
```

All passed. The CLI status command showed API, database, scanner, and OnionClaw online. The CLI now loads editable terminal art from `assets/banner.txt`, and image-to-ASCII conversion is available through `ascii-image-converter.cmd`.

Additional 2026-05-05 CLI validation:

- `.\praedix.cmd -u scanme.nmap.org -v` completed successfully.
- The generated report was `2026-05-04_18-43-49_scanme.nmap.org.md`.
- CLI final output was changed to show only completion status and report filename by default.
- `--report-preview` was added for optional report preview output.
- `praedix_cli.py` now reads UTF-8, UTF-8 BOM, UTF-16 LE, and UTF-16 BE banner files, because PowerShell redirection can create UTF-16 text files.
- ANSI color banner files are supported; `--no-color` strips ANSI escape sequences.
- CLI and API now reject unknown single-label targets. The API container was force-recreated after this change.

Docker containers were rebuilt and recreated after the OnionClaw updates. `GET /api/status` showed API, database, scanner, and OnionClaw online, with `onionclaw_installed=true`.

Current next work:

- Add stronger web app DAST tools to the scanner runtime.
- Recommended first batch: `nuclei`, `katana`, `ffuf` or `feroxbuster`, `httpx`, `subfinder`, `arjun`, `dalfox`, `whatweb`, and `testssl.sh`.
- Do not add high-risk hackingtool categories such as phishing, DDoS, RAT, payload generation, wireless attacks, or post-exploitation tooling.

Useful checks:

```powershell
curl http://localhost:5000/api/status
curl http://localhost:5000/api/research/onionclaw/status
```

## Security Notes

The `.env` file currently contains real secrets. Rotate exposed keys and do not commit `.env`.
