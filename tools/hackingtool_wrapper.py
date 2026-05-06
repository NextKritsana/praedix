import subprocess
import shlex
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Configuration ---
ALLOWED_TOOLS = [
    # Core Scanners
    "nmap", "sqlmap", "nikto", "dirb", "whois",
    # Reconnaissance
    "dig", "wafw00f", "traceroute",
    # Web/Network Analysis
    "sslscan", "curl",
]

# Per-tool timeout (seconds)
TOOL_TIMEOUTS = {
    "nmap":         300,
    "nikto":        300,
    "dirb":         300,
    "sqlmap":       300,
    "whois":        30,
    "whatweb":      120,
    "dnsrecon":     120,
    "dig":          30,
    "theHarvester": 180,
    "wafw00f":      60,
    "traceroute":   60,
    "sslscan":      120,
    "wapiti":       300,
    "curl":         30,
}

@app.route('/run', methods=['POST'])
def execute_tool():
    """
    Endpoint to execute a security tool.
    Expects JSON: {"command": "nmap -sV scanme.nmap.org"}
    """
    data = request.json
    if not data or 'command' not in data:
        return jsonify({"error": "No command provided"}), 400

    tool_command = data['command']
    
    try:
        # Use shlex.split to properly handle quoted arguments (e.g., sqlmap URLs)
        args = shlex.split(tool_command)
        base_cmd = args[0]
        
        if base_cmd not in ALLOWED_TOOLS:
            return jsonify({"error": f"Tool '{base_cmd}' is not allowed in this sandbox."}), 403

        timeout = TOOL_TIMEOUTS.get(base_cmd, 120)

        print(f"[*] Executing: {args} (timeout: {timeout}s)")

        # Execute the tool using shell=True for complex commands with pipes/redirects
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "status": "success"
        })
    
    except subprocess.TimeoutExpired as e:
        # Capture partial output from timed-out commands
        stdout = e.stdout.decode('utf-8', errors='replace') if e.stdout else ""
        stderr = e.stderr.decode('utf-8', errors='replace') if e.stderr else ""
        return jsonify({
            "error": f"Command timed out after {timeout} seconds",
            "stdout": stdout,
            "stderr": stderr,
            "exit_code": -1
        }), 200
    except Exception as e:
        return jsonify({"error": str(e), "stdout": "", "stderr": "", "exit_code": -1}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "online", "tools": ALLOWED_TOOLS})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
