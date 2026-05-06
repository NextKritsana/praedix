import os
import json
import re
import requests
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter Configuration
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Configuration for the AI (should match hackingtool_wrapper.py)
ALLOWED_TOOLS = ["nmap", "sqlmap", "nikto", "dirb", "whois"]

def extract_json(text):
    """Try to extract a JSON object from AI response text."""
    # Try direct parse first
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass
    
    # Try to find JSON inside markdown code blocks
    match = re.search(r'```(?:json)?\s*(\{.*\})\s*```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    
    # Find the first { and try to parse from there (handles nested objects)
    idx = text.find('{')
    if idx != -1:
        # Try progressively larger substrings
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

class PraedixCommander:
    def __init__(self):
        self.name = "Commander"
        self.role = "Lead Architect & Decision Maker"
        self.model = os.getenv("AI_MODEL", "openrouter/auto")
        self.scanner_url = "http://scan-runner:8001/run"
        self.vault_path = "/app/vault"
        self.tool_logs = []  # Store all tool execution logs
        
    def execute_tool_on_scanner(self, command):
        """Sends a command to the isolated scan-runner container."""
        print(f"[*] Sending command to scanner: {command}")
        try:
            response = requests.post(self.scanner_url, json={"command": command}, timeout=300)
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "Command timed out (5 min limit)", "exit_code": -1}
        except Exception as e:
            return {"error": str(e), "exit_code": -1}

    def load_knowledge_base(self):
        """Load all knowledge base files from the vault to give AI context."""
        kb_path = os.path.join(self.vault_path, "30_Knowledge_Base")
        knowledge = []
        
        if not os.path.exists(kb_path):
            print("[!] Knowledge Base folder not found.")
            return ""
        
        files = sorted([f for f in os.listdir(kb_path) if f.endswith('.md')])
        print(f"[📚] Loading {len(files)} knowledge base files...")
        
        for filename in files:
            filepath = os.path.join(kb_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Extract only key sections: How to Detect + Payloads (keep it concise)
                sections = []
                for section_name in ['How to Detect', 'Common', 'Payloads', 'Tools to Use']:
                    pattern = rf'(###?\s*.*{section_name}.*?\n)(.*?)(?=\n###?\s|\n## |$)'
                    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
                    for header, body in matches:
                        sections.append(f"{header.strip()}\n{body.strip()}")
                
                if sections:
                    title = filename.replace('.md', '').replace('_', ' ')
                    knowledge.append(f"--- {title} ---\n" + "\n".join(sections))
                    print(f"  ✅ Loaded: {filename}")
            except Exception as e:
                print(f"  ❌ Failed to load {filename}: {e}")
        
        return "\n\n".join(knowledge)

    def save_report_to_vault(self, target, report_content):
        """Save the audit report and tool logs to Obsidian vault as Markdown."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        safe_target = target.replace("/", "_").replace(":", "_")
        filename = f"{timestamp}_{safe_target}.md"
        
        reports_dir = os.path.join(self.vault_path, "Reports")
        os.makedirs(reports_dir, exist_ok=True)
        filepath = os.path.join(reports_dir, filename)
        
        # Build Markdown content
        md = f"# 🛡️ Security Audit Report\n\n"
        md += f"**Target:** {target}\n"
        md += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md += f"**Model:** {self.model}\n\n"
        md += f"---\n\n"
        md += f"## 📋 Summary\n\n{report_content}\n\n"
        md += f"---\n\n"
        md += f"## 🔧 Tool Execution Log\n\n"
        
        for i, log in enumerate(self.tool_logs, 1):
            md += f"### Step {i}: `{log['command']}`\n"
            md += f"**Exit Code:** {log['exit_code']}\n\n"
            md += f"```\n{log['output'][:2000]}\n```\n\n"
        
        md += f"---\n*Generated by Praedix AI Security Firm*\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"[💾] Report saved to: vault/Reports/{filename}")
        return filepath

    def run_autonomous_audit(self, target):
        """
        Starts an iterative reasoning loop where the AI decides which tools to run,
        observes the output, and continues until it can provide a final report.
        """
        print(f"\n[🚀] Starting Autonomous Audit for: {target}")
        
        # Load knowledge base
        knowledge = self.load_knowledge_base()
        
        kb_section = ""
        if knowledge:
            kb_section = f"""\n\nSECURITY KNOWLEDGE BASE (use this to guide your scanning):
{knowledge}

USE THIS KNOWLEDGE to decide what to scan for. Match findings against known vulnerability patterns above."""
        
        system_prompt = f"""You are an expert penetration tester from Praedix AI Security Firm.
Your mission: Find ALL vulnerabilities on {target} using a systematic, phase-based approach.

═══════════════════════════════════════
PHASE 1: RECONNAISSANCE (Must do first)
═══════════════════════════════════════
Run these to understand the target:
- nmap -F {target}                          → Discover open ports
- dig {target} ANY                          → DNS records
- whois {target}                            → Domain info

═══════════════════════════════════════
PHASE 2: DECISION (Read nmap results carefully)
═══════════════════════════════════════
After nmap, analyze the open ports and decide next steps:

IF Port 80 open:
  → nikto -h {target} -p 80                → Scan HTTP web server
  → dirb http://{target} -r                → Find hidden directories
  → curl -I http://{target}                → Check HTTP headers
  → wafw00f http://{target}                → Detect WAF

IF Port 443 open:
  → nikto -h {target} -p 443 -ssl          → Scan HTTPS web server
  → sslscan {target}                       → Check SSL/TLS security
  → curl -Ik https://{target}              → Check HTTPS headers

IF Port 8080/8443/other HTTP ports open:
  → nikto -h {target} -p <port>            → Scan that specific port
  → dirb http://{target}:<port> -r         → Find directories on that port

IF ANY port open:
  → nmap -sV -p <ONLY_OPEN_PORTS> {target} → Version detect ONLY open ports (never scan all ports)

═══════════════════════════════════════
PHASE 3: EXPLOITATION (Based on Phase 2 findings)
═══════════════════════════════════════
- If web forms/parameters found → sqlmap -u "http://{target}/page?param=1" --batch --dbs
- If login page found → Note default credential risk
- If interesting dirs found → nmap --script http-enum {target}
- Always check → nmap --script http-headers {target}

═══════════════════════════════════════
PHASE 4: TRIAGE & REPORT
═══════════════════════════════════════
After running 6+ tools, write a comprehensive report.

TOOL FALLBACK RULES (if a tool fails, switch to alternative):
- nikto FAILED?    → Use: curl -I + nmap --script http-enum
- dirb FAILED?     → Use: nmap --script http-enum {target}
- whois FAILED?    → Use: dig {target} ANY
- nmap -sV TIMEOUT?→ Use: nmap --script banner -p <ports> {target}
- DO NOT retry the same failed command. Always switch to alternative.

AVAILABLE TOOLS: nmap, nikto, dirb, sqlmap, whois, dig, curl, sslscan, wafw00f, traceroute

STRICT EVIDENCE RULES (CRITICAL):
- NEVER guess, assume, or infer vulnerabilities.
- ONLY report what tool output ACTUALLY shows.
- If a tool timed out: say "INCONCLUSIVE - tool timed out"
- Every finding MUST include EXACT evidence copied from tool output.
- Do NOT use "Simulated", "Likely", "Probably" — only confirmed facts.
- Map EVERY finding to an OWASP Top 10 category.
- Rate as: CRITICAL / HIGH / MEDIUM / LOW / INFO

RESPONSE FORMAT - respond with ONLY a valid JSON object:
To run a tool: {{"action": "tool", "command": "nmap -F {target}"}}
Final report:  {{"action": "report", "content": "Your detailed findings..."}}{kb_section}"""

        history = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Begin the FULL security audit on {target}. Start with nmap -F. You must use ALL tools before reporting. Respond with JSON only."}
        ]

        max_steps = 15

        for step in range(max_steps):
            print(f"\n[Step {step + 1}/{max_steps}] Thinking...")
            
            try:
                response = client.chat.completions.create(
                    model=self.model,
                    messages=history,
                    extra_headers={
                        "HTTP-Referer": "https://praedix.ai", 
                        "X-Title": "Praedix AI Security", 
                    }
                )
                
                content = response.choices[0].message.content
                print(f"[*] AI raw response: {content[:200]}...")
                
                decision = extract_json(content)
                
                if decision is None:
                    print(f"[!] Could not parse JSON. Asking AI to retry...")
                    history.append({"role": "assistant", "content": content})
                    history.append({"role": "user", "content": f"Your response was not valid JSON. Respond with ONLY a JSON object like this: {{\"action\": \"tool\", \"command\": \"nmap -sV -p 80 {target}\"}}"})
                    continue
                
                history.append({"role": "assistant", "content": json.dumps(decision)})

                if decision.get("action") == "tool":
                    cmd = decision.get("command", "")
                    print(f"[+] AI decided to run: {cmd}")
                    
                    result = self.execute_tool_on_scanner(cmd)
                    
                    if "error" in result and result.get("exit_code") == -1:
                        obs = f"ERROR: {result['error']}"
                    else:
                        stdout = result.get('stdout', '')
                        stderr = result.get('stderr', '')
                        exit_code = result.get('exit_code', -1)
                        obs = f"Exit Code: {exit_code}\nSTDOUT:\n{stdout[:3000]}\nSTDERR:\n{stderr[:500]}"
                    
                    # Save tool log for the report
                    self.tool_logs.append({
                        "command": cmd,
                        "exit_code": result.get('exit_code', 'N/A'),
                        "output": result.get('stdout', '') + result.get('stderr', '')
                    })
                    
                    print(f"[*] Tool finished. (Exit code: {result.get('exit_code', 'N/A')})")
                    history.append({"role": "user", "content": f"TOOL OUTPUT:\n{obs}\n\nAnalyze this. Then run the next tool or provide your final report. Respond with JSON only."})
                    
                elif decision.get("action") == "report":
                    report = decision.get("content", "No content")
                    print("\n" + "=" * 60)
                    print("[🏁] AUDIT COMPLETE! FINAL REPORT:")
                    print("=" * 60)
                    print(report)
                    print("=" * 60)
                    
                    # Save report to Obsidian vault
                    self.save_report_to_vault(target, report)
                    return report
                else:
                    action = decision.get('action', 'unknown')
                    print(f"[!] Unknown action: {action}. Redirecting AI...")
                    history.append({"role": "assistant", "content": json.dumps(decision)})
                    history.append({"role": "user", "content": f"'{action}' is not a valid action. You can ONLY use 'tool' or 'report'. Run your next tool command now. Respond with JSON only."})
            except Exception as e:
                print(f"[!] Error in step {step + 1}: {e}")
                if step < max_steps - 1:
                    print("[*] Retrying...")
                    continue
                break
        
        print("[!] Reached maximum reasoning steps.")
        return None

if __name__ == "__main__":
    import sys
    commander = PraedixCommander()
    print(f"Praedix Commander Online. Using Model: {commander.model}")
    
    # Accept target from command line or prompt
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("\n[?] Enter target (domain or IP): ").strip()
    
    if not target:
        print("[!] No target provided. Exiting.")
    else:
        print(f"[*] Target set to: {target}")
        commander.run_autonomous_audit(target)
