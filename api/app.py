import os
import json
import re
import uuid
import threading
import requests
import ipaddress
from datetime import datetime
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import db

load_dotenv()

app = Flask(__name__)
CORS(app)

# --- OpenRouter Client ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

ALLOWED_TOOLS = [
    "nmap", "sqlmap", "nikto", "dirb", "whois", "dig", "wafw00f",
    "traceroute", "sslscan", "curl", "nuclei", "httpx", "katana",
    "ffuf", "subfinder",
]
VAULT_PATH = "/app/vault"
SCANNER_URL = "http://scan-runner:8001/run"
ONIONCLAW_URL = os.getenv("ONIONCLAW_URL", "http://onionclaw-runner:8002/run")
AI_MODEL = os.getenv("AI_MODEL", "openrouter/auto")
ALLOWED_SINGLE_LABEL_TARGETS = {
    item.strip().lower()
    for item in os.getenv("PRAEDIX_ALLOWED_SINGLE_LABEL_TARGETS", "dvwa,localhost").split(",")
    if item.strip()
}

STREAM_TYPES = {
    "local_vm": {
        "label": "Local VM Testing",
        "start_workflow": "vm_target_ready",
        "scan_workflow": "local_scan",
        "done_workflow": "pre_deploy_report",
    },
    "research": {
        "label": "Vulnerability Research",
        "start_workflow": "research_target_queued",
        "scan_workflow": "recon_and_triage",
        "done_workflow": "awaiting_human_review",
    },
}

SCAN_PROFILES = {
    "standard": {
        "label": "Standard Audit",
        "max_steps": 15,
        "workflow_suffix": "",
        "description": "Balanced recon, web checks, and evidence-backed reporting.",
    },
    "web_deep": {
        "label": "Web App Deep Scan",
        "max_steps": 24,
        "workflow_suffix": "_web_deep",
        "description": "Deeper web app recon using subfinder, httpx, katana, ffuf, and nuclei.",
    },
}

# --- In-memory scan storage ---
scans = {}

DEFAULT_BLOCKED_RESEARCH_TERMS = [
    "buy",
    "sell",
    "carding",
    "drugs",
    "weapon",
    "stolen",
]

try:
    DB_READY = db.init_db()
except Exception as e:
    DB_READY = False
    print(f"[db] Database unavailable; falling back to in-memory state: {e}")

def persist(operation, *args, **kwargs):
    """Best-effort persistence; scanner execution should continue if DB is down."""
    global DB_READY
    if not DB_READY:
        try:
            DB_READY = db.init_db()
        except Exception:
            return None
        if not DB_READY:
            return None
    try:
        return operation(*args, **kwargs)
    except Exception as e:
        print(f"[db] Persistence error in {operation.__name__}: {e}")
        return None

def is_ip_address(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def validate_scan_target(target):
    lowered = target.lower()
    if lowered in ALLOWED_SINGLE_LABEL_TARGETS or is_ip_address(target):
        return None
    if "." in target:
        return None
    allowed = ", ".join(sorted(ALLOWED_SINGLE_LABEL_TARGETS))
    return (
        f"Unknown single-label target '{target}'. Use a full domain such as "
        f"'example.{target}' or an allowed local alias ({allowed})."
    )

def extract_json(text):
    """Try to extract a JSON object from AI response text."""
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass
    match = re.search(r'```(?:json)?\s*(\{.*\})\s*```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    idx = text.find('{')
    if idx != -1:
        depth = 0
        for i in range(idx, len(text)):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[idx:i+1])
                    except json.JSONDecodeError:
                        break
    return None

def load_knowledge_base():
    """Load knowledge base files for AI context."""
    kb_path = os.path.join(VAULT_PATH, "30_Knowledge_Base")
    knowledge = []
    if not os.path.exists(kb_path):
        return ""
    files = sorted([f for f in os.listdir(kb_path) if f.endswith('.md')])
    for filename in files:
        filepath = os.path.join(kb_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            sections = []
            for section_name in ['How to Detect', 'Common', 'Payloads', 'Tools to Use']:
                pattern = rf'(###?\s*.*{section_name}.*?\n)(.*?)(?=\n###?\s|\n## |$)'
                matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
                for header, body in matches:
                    sections.append(f"{header.strip()}\n{body.strip()}")
            if sections:
                title = filename.replace('.md', '').replace('_', ' ')
                knowledge.append(f"--- {title} ---\n" + "\n".join(sections))
        except Exception:
            pass
    return "\n\n".join(knowledge)

def load_previous_reports(target):
    """Load the most recent report for the specific target to provide historical context."""
    reports_dir = os.path.join(VAULT_PATH, "Reports")
    if not os.path.exists(reports_dir):
        return ""
        
    # Make target safe for filename matching
    safe_target = target.replace("/", "_").replace(":", "_")
    
    # Find all reports for this target
    target_reports = []
    for f in os.listdir(reports_dir):
        if f.endswith('.md') and safe_target in f:
            target_reports.append(f)
            
    if not target_reports:
        return ""
        
    # Sort to get the most recent one (filenames start with timestamp)
    target_reports.sort(reverse=True)
    recent_report = target_reports[0]
    
    try:
        with open(os.path.join(reports_dir, recent_report), 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract just the Summary section to save tokens
        match = re.search(r'## 📋 Summary\n(.*?)(?=\n---\n## 🔧 Tool Execution Log)', content, re.DOTALL)
        if match:
            return f"--- PREVIOUS SCAN FINDINGS (from {recent_report}) ---\n{match.group(1).strip()}"
    except Exception:
        pass
        
    return ""

def execute_tool(command):
    """Send command to the scanner container."""
    try:
        response = requests.post(SCANNER_URL, json={"command": command}, timeout=360)
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Command timed out", "stdout": "", "stderr": "", "exit_code": -1}
    except Exception as e:
        return {"error": str(e), "stdout": "", "stderr": "", "exit_code": -1}

def normalize_research_scope(target, raw_scope):
    raw_scope = raw_scope or {}
    allowed = raw_scope.get("allowed_keywords") or [target]
    if isinstance(allowed, str):
        allowed = [item.strip() for item in allowed.split(",") if item.strip()]

    blocked = raw_scope.get("blocked_keywords") or []
    if isinstance(blocked, str):
        blocked = [item.strip() for item in blocked.split(",") if item.strip()]

    merged_blocked = sorted(set(blocked + DEFAULT_BLOCKED_RESEARCH_TERMS))

    return {
        "enable_dark_web": bool(raw_scope.get("enable_dark_web", False)),
        "client": raw_scope.get("client", ""),
        "allowed_keywords": allowed,
        "blocked_keywords": merged_blocked,
        "allow_onion_fetch": bool(raw_scope.get("allow_onion_fetch", False)),
        "allow_identity_rotation": bool(raw_scope.get("allow_identity_rotation", False)),
        "approved": bool(raw_scope.get("approved", False)),
        "approved_by": raw_scope.get("approved_by", ""),
        "notes": raw_scope.get("notes", ""),
    }

def validate_research_scope(target, scope, require_dark_web=False):
    if require_dark_web and not scope.get("enable_dark_web"):
        return "Dark web / OSINT search must be enabled for OnionClaw actions."
    if not scope.get("enable_dark_web"):
        return None
    if not scope.get("approved"):
        return "Research stream requires a human-approved scope."
    if not scope.get("approved_by"):
        return "Research scope requires approved_by."
    if not scope.get("allowed_keywords"):
        return "Research scope requires at least one allowed keyword."

    target_text = target.lower()
    allowed = [item.lower() for item in scope.get("allowed_keywords", [])]
    if allowed and not any(item in target_text or target_text in item for item in allowed):
        return "Target must be represented in allowed_keywords."
    return None

def execute_onionclaw(action, payload, scope):
    try:
        response = requests.post(
            ONIONCLAW_URL,
            json={"action": action, "scope": scope, **payload},
            timeout=390,
        )
        return response.json(), response.status_code
    except requests.exceptions.Timeout:
        return {"error": "OnionClaw command timed out", "stdout": "", "stderr": "", "exit_code": -1}, 200
    except Exception as e:
        return {"error": str(e), "stdout": "", "stderr": "", "exit_code": -1}, 200

def add_scan_step(scan_id, scan, command):
    step_info = {
        "step": len(scan["steps"]) + 1,
        "command": command,
        "status": "running",
        "output": "",
        "stdout": "",
        "stderr": "",
        "exit_code": None,
        "timestamp": datetime.now().isoformat(),
    }
    scan["steps"].append(step_info)
    persist(db.save_tool_run, scan_id, step_info)
    return step_info

def finish_scan_step(scan_id, step_info, result):
    stdout = result.get("stdout", "") or ""
    stderr = result.get("stderr", "") or ""
    error = result.get("error")
    output = stdout if stdout else stderr
    if error:
        output = f"ERROR: {error}\n{output}".strip()

    step_info["status"] = "done"
    step_info["stdout"] = stdout
    step_info["stderr"] = stderr
    step_info["output"] = output[:3000]
    step_info["exit_code"] = result.get("exit_code", -1)
    step_info["finished_at"] = datetime.now().isoformat()
    persist(db.save_tool_run, scan_id, step_info)
    return output

def run_research_osint(scan_id, scan, target, scope):
    """Run approved OnionClaw OSINT before the normal scanner loop."""
    scan["workflow_status"] = "dark_web_osint"
    persist(db.update_scan, scan_id, workflow_status=scan["workflow_status"])

    if not scope.get("enable_dark_web"):
        return ""

    osint_chunks = []
    actions = [("check_tor", {}, "onionclaw check_tor")]
    for keyword in (scope.get("allowed_keywords") or [target])[:5]:
        actions.append((
            "search",
            {"query": keyword, "max_results": 10},
            f'onionclaw search --query "{keyword}" --max 10',
        ))

    for action, payload, command in actions:
        step_info = add_scan_step(scan_id, scan, command)
        result, _status_code = execute_onionclaw(action, payload, scope)
        output = finish_scan_step(scan_id, step_info, result)
        osint_chunks.append(f"### {command}\nExit Code: {step_info['exit_code']}\n{output[:2500]}")

    if not osint_chunks:
        return ""

    return (
        "--- DARK WEB / OSINT RESEARCH RESULTS ---\n"
        + "\n\n".join(osint_chunks)
        + "\n\nTreat these as OSINT leads only. Do not claim a data leak unless the output contains direct, relevant evidence."
    )

def extract_findings(report):
    """Extract coarse structured findings from the markdown report for DB search."""
    severities = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]
    findings = []
    blocks = re.split(r"\n\s*\n", report or "")

    for block in blocks:
        upper = block.upper()
        severity = next((level for level in severities if level in upper), None)
        if not severity:
            continue

        lines = [line.strip(" -*#\t") for line in block.splitlines() if line.strip()]
        if not lines:
            continue

        title = lines[0][:240]
        owasp_match = re.search(r"(OWASP[\s_-]*A\d{2}[^,\n:;]*)", block, re.IGNORECASE)
        remediation_match = re.search(
            r"(?:remediation|recommendation|fix|mitigation)\s*[:\-]\s*(.+)",
            block,
            re.IGNORECASE | re.DOTALL,
        )

        findings.append({
            "title": title,
            "severity": severity,
            "owasp_category": owasp_match.group(1).strip()[:160] if owasp_match else None,
            "evidence": block[:3000],
            "remediation": remediation_match.group(1).strip()[:2000] if remediation_match else None,
            "confidence": 0.70,
        })

    return findings[:50]

def run_scan_thread(scan_id, target):
    """Run the scan in a background thread."""
    scan = scans[scan_id]
    stream_type = scan.get("stream_type", "local_vm")
    stream_config = STREAM_TYPES.get(stream_type, STREAM_TYPES["local_vm"])
    scan_profile = scan.get("scan_profile", "standard")
    profile_config = SCAN_PROFILES.get(scan_profile, SCAN_PROFILES["standard"])
    research_scope = scan.get("research_scope", {})
    scan["status"] = "loading_kb"
    scan["workflow_status"] = "loading_knowledge"
    persist(
        db.update_scan,
        scan_id,
        status="loading_kb",
        workflow_status=scan["workflow_status"],
    )
    
    # Load knowledge base and previous reports
    knowledge = load_knowledge_base()
    prev_report = load_previous_reports(target)
    target_memory = persist(db.load_target_memory, target) or ""
    
    kb_files = []
    kb_path = os.path.join(VAULT_PATH, "30_Knowledge_Base")
    if os.path.exists(kb_path):
        kb_files = sorted([f for f in os.listdir(kb_path) if f.endswith('.md')])
    scan["kb_loaded"] = len(kb_files)
    scan["max_steps"] = profile_config["max_steps"]
    if stream_type == "research":
        estimated_osint_steps = 0
        if research_scope.get("enable_dark_web"):
            estimated_osint_steps = 1 + min(len(research_scope.get("allowed_keywords", []) or [target]), 5)
        scan["max_steps"] = profile_config["max_steps"] + estimated_osint_steps
    scan["status"] = "scanning"
    scan["workflow_status"] = stream_config["scan_workflow"] + profile_config["workflow_suffix"]
    persist(
        db.update_scan,
        scan_id,
        status="scanning",
        workflow_status=scan["workflow_status"],
        max_steps=scan["max_steps"],
        kb_loaded=scan["kb_loaded"],
    )

    osint_context = ""
    if stream_type == "research":
        osint_context = run_research_osint(scan_id, scan, target, research_scope)
    
    kb_section = ""
    if knowledge or prev_report or target_memory or osint_context:
        kb_section = "\n\nSECURITY CONTEXT:\n"
        if osint_context:
            kb_section += f"{osint_context}\n\n"
        if prev_report:
            kb_section += f"{prev_report}\n(VERIFY these previous findings and look for NEW ones.)\n\n"
        if target_memory:
            kb_section += f"--- TARGET MEMORY ---\n{target_memory}\n(USE THIS MEMORY to avoid repeating failed paths and to verify recurring findings.)\n\n"
        if knowledge:
            kb_section += f"{knowledge}\n(USE THIS KNOWLEDGE to guide your scanning.)"

    stream_section = ""
    if stream_type == "research":
        scope_keywords = ", ".join(research_scope.get("allowed_keywords", [])) or target
        stream_section = f"""

WORKFLOW STREAM: Vulnerability Research
- Prioritize reconnaissance, CVE mapping, severity triage, and client advisory quality.
- OnionClaw/Tor OSINT has already been run for the approved scope and is included in SECURITY CONTEXT.
- Include a dedicated "Dark Web / OSINT Exposure" section in the final report.
- Do not claim that data leaked unless the OnionClaw output contains direct, relevant evidence.
- Approved research scope keywords: {scope_keywords}
- Keep findings evidence-driven and mark anything that needs human review before notification."""
    else:
        stream_section = """

WORKFLOW STREAM: Local VM Testing
- Prioritize local/VM web application testing, OWASP Top 10 coverage, and pre-deploy remediation.
- Treat the output as a pre-deploy report for developers before production release."""

    if scan_profile == "web_deep":
        profile_section = f"""

SCAN PROFILE: Web App Deep Scan
- Use the modern web recon tools before writing the final report when the target exposes HTTP/HTTPS.
- For public root domains, run subdomain discovery with: subfinder -d {target} -silent
- Probe live web services with direct URLs, for example: httpx -u http://{target} -status-code -title -tech-detect -follow-redirects
- Crawl reachable web apps with: katana -u http://{target} -silent -depth 2 -jc
- Discover common paths with a controlled wordlist run: ffuf -u http://{target}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc all -fc 404 -t 20 -rate 50
- Run nuclei safely with rate limiting: nuclei -u http://{target} -severity low,medium,high,critical -exclude-tags intrusive,dos -rl 10 -no-color
- Do not use shell pipes, redirects, command substitution, or chained commands. Run one executable command at a time.
- Prefer non-intrusive checks and avoid destructive exploitation. Escalate severity only when tool output provides direct evidence.
- In the final report, map confirmed findings to OWASP Top 10 and, where relevant, MITRE ATT&CK techniques from the knowledge base."""
    else:
        profile_section = """

SCAN PROFILE: Standard Audit
- Use a balanced scan path. Prefer fast, high-signal checks and write a concise evidence-backed report once enough coverage is collected."""
    
    system_prompt = f"""You are an AGGRESSIVE penetration tester from Praedix AI Security Firm.
Your mission: Find ALL vulnerabilities on {target}. Leave no stone unturned.

AVAILABLE TOOLS AND WHEN TO USE THEM:

[RECONNAISSANCE]
- nmap -F {target}                         → Fast port scan (always start here)
- nmap -sV -p <ports> {target}             → Service version detection (only on open ports)
- nmap --script <script> {target}          → NSE scripts (http-headers, http-enum, http-methods, ssl-cert, vuln)
- dig {target} ANY                         → DNS records (A, MX, NS, TXT, CNAME)
- whois {target}                           → Domain registration info
- traceroute {target}                      → Network path tracing
- wafw00f http://{target}                  → Detect Web Application Firewall (WAF)

[WEB SCANNING]
- nikto -h {target} -maxtime 120           → Web server vulnerability scan
- dirb http://{target} -r                  → Directory brute-force (non-recursive)
- curl -I http://{target}                  → HTTP response headers
- curl -s http://{target}                  → Page content/source code

[MODERN WEB APP RECON / DAST]
- subfinder -d {target} -silent            -> Discover subdomains for public root domains
- httpx -u http://{target} -status-code -title -tech-detect -follow-redirects  -> Probe live HTTP services and detect technologies
- katana -u http://{target} -silent -depth 2 -jc  -> Crawl pages, links, scripts, and endpoints
- ffuf -u http://{target}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc all -fc 404 -t 20 -rate 50  -> Controlled content discovery
- nuclei -u http://{target} -severity low,medium,high,critical -exclude-tags intrusive,dos -rl 10 -no-color  -> Template-based vulnerability checks

[CRYPTO / SSL]
- sslscan {target}                         → SSL/TLS cipher analysis

[EXPLOITATION]
- sqlmap -u "http://{target}/path?param=1" --batch --dbs  → SQL injection test

TOOL ALTERNATIVES - If one tool fails/times out, switch to alternative:
- nikto FAILED? → Use: curl -I http://{target} (for headers) + nmap --script http-enum {target} (for dirs)
- dirb FAILED?  → Use: nmap --script http-enum {target}
- whois FAILED? → Use: dig {target} ANY
- nmap -sV TIMEOUT? → Use: nmap --script banner -p <ports> {target}

ADAPTIVE SCANNING STRATEGY:
1. START: nmap -F {target} → identify open ports and services
2. Based on what you find:
   - Port 80/443 open? → Run nikto, dirb, curl, wafw00f
   - Port 443 open?    → Run sslscan
   - Has web forms?    → Run sqlmap on form URLs
   - Any port open?    → Run nmap -sV on those specific ports
3. ALWAYS run: dig, whois (or alternatives)
4. If a tool fails, try the alternative from the list above
5. After gathering enough evidence, write your report

RULES:
- Run AT LEAST 6 different commands before writing a report.
- If a tool times out or fails, DO NOT retry the same command. Use an ALTERNATIVE instead.
- Be creative: use nmap NSE scripts like http-headers, http-enum, http-methods, ssl-cert.

STRICT EVIDENCE RULES:
- NEVER guess or infer vulnerabilities. ONLY report what tool output ACTUALLY shows.
- If a tool timed out, say "INCONCLUSIVE - tool timed out".
- Every finding MUST include EXACT evidence copy-pasted from tool output.
- Map EVERY confirmed finding to an OWASP Top 10 category.
- Rate each finding as: CRITICAL / HIGH / MEDIUM / LOW / INFO

RESPONSE FORMAT - respond with ONLY a valid JSON object:
To run a tool: {{"action": "tool", "command": "nmap -F {target}"}}
Final report:  {{"action": "report", "content": "Your detailed findings..."}}{stream_section}{profile_section}{kb_section}"""

    history = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Begin the FULL security audit on {target}. Start with nmap -F. Respond with JSON only."}
    ]

    max_steps = scan.get("max_steps", profile_config["max_steps"])
    for step in range(max_steps):
        scan["current_step"] = len(scan["steps"]) + 1
        persist(db.update_scan, scan_id, current_step=scan["current_step"])
        
        try:
            response = client.chat.completions.create(
                model=AI_MODEL,
                messages=history,
                extra_headers={
                    "HTTP-Referer": "https://praedix.ai",
                    "X-Title": "Praedix AI Security",
                }
            )
            
            content = response.choices[0].message.content
            decision = extract_json(content)
            
            if decision is None:
                history.append({"role": "assistant", "content": content})
                history.append({"role": "user", "content": f"Your response was not valid JSON. Respond with ONLY a JSON object like this: {{\"action\": \"tool\", \"command\": \"nmap -sV -p 80 {target}\"}}"})
                continue
            
            history.append({"role": "assistant", "content": json.dumps(decision)})

            if decision.get("action") == "tool":
                cmd = decision.get("command", "")
                step_info = add_scan_step(scan_id, scan, cmd)
                
                result = execute_tool(cmd)
                
                stdout = result.get('stdout', '')
                stderr = result.get('stderr', '')
                exit_code = result.get('exit_code', -1)
                
                finish_scan_step(scan_id, step_info, result)
                
                if "error" in result and exit_code == -1:
                    obs = f"ERROR: {result['error']}"
                else:
                    obs = f"Exit Code: {exit_code}\nSTDOUT:\n{stdout[:3000]}\nSTDERR:\n{stderr[:500]}"
                
                history.append({"role": "user", "content": f"TOOL OUTPUT:\n{obs}\n\nAnalyze this. Run the next tool or provide your final report. Respond with JSON only."})
                    
            elif decision.get("action") == "report":
                report = decision.get("content", "No content")
                scan["report"] = report
                scan["status"] = "done"
                scan["workflow_status"] = stream_config["done_workflow"]
                
                # Save to vault
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                safe_target = target.replace("/", "_").replace(":", "_")
                filename = f"{timestamp}_{safe_target}.md"
                reports_dir = os.path.join(VAULT_PATH, "Reports")
                os.makedirs(reports_dir, exist_ok=True)
                
                md = f"# 🛡️ Security Audit Report\n\n"
                md += f"**Target:** {target}\n"
                md += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                md += f"**Model:** {AI_MODEL}\n\n---\n\n"
                md += f"## 📋 Summary\n\n{report}\n\n---\n\n"
                md += f"## 🔧 Tool Execution Log\n\n"
                for s in scan["steps"]:
                    md += f"### Step {s['step']}: `{s['command']}`\n"
                    md += f"**Exit Code:** {s['exit_code']}\n\n"
                    md += f"```\n{s['output'][:2000]}\n```\n\n"
                md += f"---\n*Generated by Praedix AI Security Firm*\n"
                
                report_path = os.path.join(reports_dir, filename)
                with open(report_path, 'w', encoding='utf-8') as f:
                    f.write(md)
                
                scan["report_file"] = filename
                finished_at = datetime.now().isoformat()
                persist(
                    db.update_scan,
                    scan_id,
                    status="done",
                    workflow_status=scan["workflow_status"],
                    report=report,
                    report_file=filename,
                    finished_at=finished_at,
                )
                persist(db.save_report, scan_id, target, filename, report_path, md)
                persist(db.replace_findings, scan_id, target, extract_findings(report))
                return
            else:
                action = decision.get('action', 'unknown')
                history.append({"role": "assistant", "content": json.dumps(decision)})
                history.append({"role": "user", "content": f"'{action}' is not a valid action. You can ONLY use 'tool' or 'report'. Run your next tool command now. Respond with JSON only."})

        except Exception as e:
            error_step = {
                "step": len(scan["steps"]) + 1,
                "command": f"Error: {str(e)}",
                "status": "error",
                "output": str(e),
                "stdout": "",
                "stderr": str(e),
                "exit_code": -1,
                "timestamp": datetime.now().isoformat()
            }
            scan["steps"].append(error_step)
            persist(db.save_tool_run, scan_id, error_step)
            continue
    
    scan["status"] = "done"
    scan["report"] = "Reached maximum reasoning steps without generating a report."
    scan["workflow_status"] = stream_config["done_workflow"]
    persist(
        db.update_scan,
        scan_id,
        status="done",
        workflow_status=scan["workflow_status"],
        report=scan["report"],
        finished_at=datetime.now().isoformat(),
    )

# ==================== API ROUTES ====================

@app.route('/api/tool/run', methods=['POST'])
def run_single_tool():
    """Run a single tool command (for Tools page)."""
    data = request.json
    command = data.get('command', '').strip()
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    result = execute_tool(command)
    return jsonify(result)

@app.route('/api/research/onionclaw/run', methods=['POST'])
def run_onionclaw():
    """Run an approved OnionClaw OSINT action through the isolated runtime."""
    data = request.json or {}
    target = data.get("target", "").strip()
    if not target:
        return jsonify({"error": "Target is required.", "stdout": "", "stderr": "", "exit_code": -1}), 400
    scope = normalize_research_scope(target, data.get("scope"))
    scope_error = validate_research_scope(target, scope, require_dark_web=True)
    if scope_error:
        return jsonify({"error": scope_error, "stdout": "", "stderr": "", "exit_code": -1}), 403

    action = data.get("action", "")
    payload = {
        "query": data.get("query", ""),
        "url": data.get("url", ""),
        "mode": data.get("mode", "corporate"),
        "max_results": data.get("max_results", 10),
    }
    result, status_code = execute_onionclaw(action, payload, scope)
    return jsonify(result), status_code

@app.route('/api/research/onionclaw/status', methods=['GET'])
def onionclaw_status():
    try:
        response = requests.get(ONIONCLAW_URL.replace("/run", "/status"), timeout=5)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"status": "offline", "error": str(e), "installed": False})

@app.route('/api/scan', methods=['POST'])
def start_scan():
    """Start a new scan."""
    data = request.json
    target = data.get('target', '').strip()
    if not target:
        return jsonify({"error": "No target provided"}), 400
    target_error = validate_scan_target(target)
    if target_error:
        return jsonify({"error": target_error}), 400

    stream_type = data.get("stream_type", "local_vm")
    if stream_type not in STREAM_TYPES:
        return jsonify({"error": "Invalid stream_type"}), 400

    scan_profile = data.get("scan_profile", "standard")
    if scan_profile not in SCAN_PROFILES:
        return jsonify({"error": "Invalid scan_profile"}), 400

    research_scope = normalize_research_scope(target, data.get("research_scope"))
    if stream_type == "research":
        scope_error = validate_research_scope(target, research_scope)
        if scope_error:
            return jsonify({"error": scope_error}), 400
    
    scan_id = str(uuid.uuid4())[:8]
    scans[scan_id] = {
        "id": scan_id,
        "target": target,
        "stream_type": stream_type,
        "scan_profile": scan_profile,
        "workflow_status": STREAM_TYPES[stream_type]["start_workflow"],
        "research_scope": research_scope if stream_type == "research" else {},
        "scope_approved": bool(research_scope.get("approved")) if stream_type == "research" else False,
        "status": "starting",
        "current_step": 0,
        "max_steps": SCAN_PROFILES[scan_profile]["max_steps"],
        "steps": [],
        "report": None,
        "report_file": None,
        "kb_loaded": 0,
        "started_at": datetime.now().isoformat(),
    }
    persist(db.create_scan, scans[scan_id])
    
    thread = threading.Thread(target=run_scan_thread, args=(scan_id, target))
    thread.daemon = True
    thread.start()
    
    return jsonify({"scan_id": scan_id, "status": "started"})

@app.route('/api/scan/<scan_id>', methods=['GET'])
def get_scan(scan_id):
    """Get scan status and results."""
    stored_scan = persist(db.get_scan, scan_id)
    if stored_scan:
        if scan_id in scans and scans[scan_id].get("status") not in ("done", "error"):
            stored_scan["steps"] = scans[scan_id].get("steps", stored_scan.get("steps", []))
        return jsonify(stored_scan)

    scan = scans.get(scan_id)
    if not scan:
        return jsonify({"error": "Scan not found"}), 404
    return jsonify(scan)

@app.route('/api/scans', methods=['GET'])
def list_scans():
    """List all scans."""
    stored_scans = persist(db.list_scans)
    if stored_scans is not None:
        live = {scan["id"]: scan for scan in scans.values()}
        merged = []
        seen = set()
        for scan in stored_scans:
            current = live.get(scan["id"])
            merged.append(current if current and current.get("status") != "done" else scan)
            seen.add(scan["id"])
        merged.extend(scan for scan_id, scan in live.items() if scan_id not in seen)
        return jsonify(merged)
    return jsonify(list(scans.values()))

@app.route('/api/reports', methods=['GET'])
def list_reports():
    """List all saved reports."""
    reports_dir = os.path.join(VAULT_PATH, "Reports")
    if not os.path.exists(reports_dir):
        return jsonify([])
    files = sorted(os.listdir(reports_dir), reverse=True)
    reports = []
    for f in files:
        if f.endswith('.md'):
            reports.append({
                "filename": f,
                "path": os.path.join(reports_dir, f),
                "size": os.path.getsize(os.path.join(reports_dir, f))
            })
    return jsonify(reports)

@app.route('/api/reports/<filename>', methods=['GET'])
def get_report(filename):
    """Get a specific report content."""
    filepath = os.path.join(VAULT_PATH, "Reports", filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "Report not found"}), 404
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return jsonify({"filename": filename, "content": content})

@app.route('/api/knowledge', methods=['GET'])
def list_knowledge():
    """List knowledge base files."""
    kb_path = os.path.join(VAULT_PATH, "30_Knowledge_Base")
    if not os.path.exists(kb_path):
        return jsonify([])
    files = sorted(os.listdir(kb_path))
    return jsonify([{"filename": f} for f in files if f.endswith('.md')])

@app.route('/api/status', methods=['GET'])
def api_status():
    """API health check."""
    # Check scanner connectivity
    scanner_ok = False
    try:
        r = requests.get("http://scan-runner:8001/status", timeout=5)
        scanner_ok = r.status_code == 200
    except:
        pass

    onionclaw_ok = False
    onionclaw_installed = False
    try:
        r = requests.get(ONIONCLAW_URL.replace("/run", "/status"), timeout=5)
        onionclaw_status_data = r.json()
        onionclaw_ok = r.status_code == 200 and onionclaw_status_data.get("status") == "online"
        onionclaw_installed = bool(onionclaw_status_data.get("installed"))
    except:
        pass

    stored_scans = persist(db.list_scans)
    status_scans = stored_scans if stored_scans is not None else list(scans.values())
    
    return jsonify({
        "status": "online",
        "scanner": "online" if scanner_ok else "offline",
        "onionclaw": "online" if onionclaw_ok else "offline",
        "onionclaw_installed": onionclaw_installed,
        "database": "online" if DB_READY else "offline",
        "model": AI_MODEL,
        "total_scans": len(status_scans),
        "active_scans": sum(1 for s in status_scans if s["status"] == "scanning"),
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
