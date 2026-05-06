import os
import re
import subprocess
import sys
from urllib.parse import urlparse

from flask import Flask, request, jsonify

app = Flask(__name__)

ONIONCLAW_DIR = os.getenv("ONIONCLAW_DIR", "/opt/onionclaw")
PYTHON_BIN = os.getenv("PYTHON_BIN", sys.executable)

ALLOWED_ACTIONS = {
    "check_tor": {"script": "check_tor.py", "timeout": 45},
    "renew": {"script": "renew.py", "timeout": 45},
    "check_engines": {"script": "check_engines.py", "timeout": 60},
    "search": {"script": "search.py", "timeout": 180},
    "fetch": {"script": "fetch.py", "timeout": 120},
    "pipeline": {"script": "pipeline.py", "timeout": 360},
}

BLOCKED_KEYWORDS = {
    "buy",
    "sell",
    "carding",
    "drugs",
    "weapon",
    "exploit market",
    "stolen",
}


def _scope_error(scope):
    if not isinstance(scope, dict):
        return "Research scope is required."
    if not scope.get("approved"):
        return "Research scope must be approved by a human before OnionClaw can run."
    return None


def _contains_any(text, keywords):
    haystack = (text or "").lower()
    return any((keyword or "").lower() in haystack for keyword in keywords if keyword)


def _validate_scope_text(scope, text):
    error = _scope_error(scope)
    if error:
        return error

    blocked = set(scope.get("blocked_keywords") or []) | BLOCKED_KEYWORDS
    if _contains_any(text, blocked):
        return "Request includes blocked research terms."

    allowed = scope.get("allowed_keywords") or []
    if allowed and not _contains_any(text, allowed):
        return "Request is outside the approved research keywords."
    return None


def _validate_fetch(scope, url):
    if not scope.get("allow_onion_fetch"):
        return "Fetching .onion URLs requires allow_onion_fetch=true in the approved scope."

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return "Fetch requires a valid http(s) URL."
    if not parsed.netloc.endswith(".onion"):
        return "OnionClaw fetch is limited to .onion hosts in this runtime."
    return _validate_scope_text(scope, url)


def _script_path(action):
    return os.path.join(ONIONCLAW_DIR, ALLOWED_ACTIONS[action]["script"])


def _installed():
    return os.path.exists(_script_path("check_tor"))


def _build_args(action, data):
    if action == "check_tor":
        return [PYTHON_BIN, _script_path(action)]
    if action == "renew":
        return [PYTHON_BIN, _script_path(action)]
    if action == "check_engines":
        return [PYTHON_BIN, _script_path(action), "--json"]
    if action == "search":
        query = data.get("query", "")
        max_results = str(min(int(data.get("max_results", 10)), 25))
        return [PYTHON_BIN, _script_path(action), "--query", query, "--max", max_results, "--json"]
    if action == "fetch":
        return [PYTHON_BIN, _script_path(action), "--url", data.get("url", ""), "--json"]
    if action == "pipeline":
        query = data.get("query", "")
        mode = data.get("mode", "corporate")
        if not re.fullmatch(r"[a-zA-Z0-9_-]{1,32}", mode):
            mode = "corporate"
        max_results = str(min(int(data.get("max_results", 10)), 25))
        return [PYTHON_BIN, _script_path(action), "--query", query, "--mode", mode, "--max", max_results, "--no-llm", "--format", "json"]
    raise ValueError("Unsupported action")


@app.route("/run", methods=["POST"])
def run():
    data = request.json or {}
    action = data.get("action")
    scope = data.get("scope") or {}

    if action not in ALLOWED_ACTIONS:
        return jsonify({"error": "Action is not allowed.", "exit_code": -1}), 403

    if not _installed():
        return jsonify({
            "error": "OnionClaw is not installed in this container. Build with ONIONCLAW_REPO or mount it at /opt/onionclaw.",
            "stdout": "",
            "stderr": "",
            "exit_code": -1,
        }), 503

    if action in {"search", "pipeline"}:
        error = _validate_scope_text(scope, data.get("query", ""))
    elif action == "fetch":
        error = _validate_fetch(scope, data.get("url", ""))
    elif action == "renew" and not scope.get("allow_identity_rotation", False):
        error = "Identity rotation requires allow_identity_rotation=true in the approved scope."
    else:
        error = _scope_error(scope)

    if error:
        return jsonify({"error": error, "stdout": "", "stderr": "", "exit_code": -1}), 403

    try:
        args = _build_args(action, data)
        result = subprocess.run(
            args,
            cwd=ONIONCLAW_DIR,
            capture_output=True,
            text=True,
            timeout=ALLOWED_ACTIONS[action]["timeout"],
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "status": "success",
            "action": action,
        })
    except subprocess.TimeoutExpired as exc:
        return jsonify({
            "error": f"Action timed out after {ALLOWED_ACTIONS[action]['timeout']} seconds",
            "stdout": exc.stdout or "",
            "stderr": exc.stderr or "",
            "exit_code": -1,
        }), 200
    except Exception as exc:
        return jsonify({"error": str(exc), "stdout": "", "stderr": "", "exit_code": -1}), 200


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "online",
        "installed": _installed(),
        "actions": list(ALLOWED_ACTIONS.keys()),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
