#!/usr/bin/env python3
"""Praedix terminal client.

This CLI talks to the existing Praedix API. It does not run scanners directly.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


DEFAULT_API = "http://localhost:5000"
FINAL_STATUSES = {"done", "error"}
DEFAULT_BANNER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "banner.txt")
ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
ALLOWED_SINGLE_LABEL_TARGETS = {
    item.strip().lower()
    for item in os.getenv("PRAEDIX_ALLOWED_SINGLE_LABEL_TARGETS", "dvwa,localhost").split(",")
    if item.strip()
}


class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"


def color(text: str, code: str, enabled: bool = True) -> str:
    if not enabled:
        return text
    return f"{code}{text}{C.RESET}"


def terminal_width() -> int:
    return max(72, min(shutil.get_terminal_size((100, 24)).columns, 120))


def line(width: int, left: str = "+", fill: str = "-", right: str = "+") -> str:
    return left + (fill * (width - 2)) + right


def box(title: str, rows: list[tuple[str, str]], colors: bool = True) -> str:
    width = terminal_width()
    out = [color(line(width), C.CYAN, colors)]
    if title:
        label = f" {title} "
        out.append(color("|", C.CYAN, colors) + color(label.ljust(width - 2), C.GREEN, colors) + color("|", C.CYAN, colors))
        out.append(color("|" + ("-" * (width - 2)) + "|", C.CYAN, colors))
    for key, value in rows:
        prefix = f" {key}: "
        raw = prefix + str(value)
        if len(raw) > width - 3:
            raw = raw[: width - 6] + "..."
        out.append(color("|", C.CYAN, colors) + raw.ljust(width - 2) + color("|", C.CYAN, colors))
    out.append(color(line(width), C.CYAN, colors))
    return "\n".join(out)


def read_banner_file(path: str | None) -> str | None:
    if not path:
        return None
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError:
        return None
    if raw.startswith(b"\xff\xfe"):
        content = raw.decode("utf-16", errors="replace").rstrip()
    elif raw.startswith(b"\xfe\xff"):
        content = raw.decode("utf-16-be", errors="replace").rstrip()
    elif raw.startswith(b"\xef\xbb\xbf"):
        content = raw.decode("utf-8-sig", errors="replace").rstrip()
    else:
        content = raw.decode("utf-8", errors="replace").rstrip()
    return content or None


def banner(colors: bool = True, banner_path: str | None = DEFAULT_BANNER) -> str:
    custom = read_banner_file(banner_path or os.environ.get("PRAEDIX_BANNER"))
    if custom:
        if "\033[" in custom:
            return custom if colors else ANSI_RE.sub("", custom)
        return color(custom, C.CYAN, colors)
    art = r"""
   ____                      _ _
  |  _ \ _ __ __ _  ___  __| (_)_  __
  | |_) | '__/ _` |/ _ \/ _` | \ \/ /
  |  __/| | | (_| |  __/ (_| | |>  <
  |_|   |_|  \__,_|\___|\__,_|_/_/\_\
"""
    subtitle = "AI Security Firm - Terminal Audit Console"
    return color(art.rstrip(), C.CYAN, colors) + "\n" + color(subtitle.center(48), C.GREEN, colors)


def normalize_api(api: str) -> str:
    return api.rstrip("/")


def normalize_target(raw: str) -> tuple[str, str]:
    raw = raw.strip()
    if not raw:
        raise ValueError("Target is empty")
    parsed = urllib.parse.urlparse(raw if "://" in raw else f"//{raw}")
    target = parsed.hostname or raw
    if not target:
        raise ValueError("Could not parse target")
    return raw, target


def is_ip_address(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def validate_target_name(target: str) -> None:
    lowered = target.lower()
    if lowered in ALLOWED_SINGLE_LABEL_TARGETS or is_ip_address(target):
        return
    if "." in target:
        return
    allowed = ", ".join(sorted(ALLOWED_SINGLE_LABEL_TARGETS))
    raise ValueError(
        f"Unknown single-label target '{target}'. Use a full domain such as 'example.{target}' "
        f"or an allowed local alias ({allowed})."
    )


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def request_json(method: str, url: str, body: dict[str, Any] | None = None, timeout: int = 30) -> dict[str, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = response.read().decode("utf-8")
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8", errors="replace")
        try:
            detail = json.loads(payload).get("error", payload)
        except json.JSONDecodeError:
            detail = payload
        raise RuntimeError(f"{exc.code} {exc.reason}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Cannot reach Praedix API at {url}: {exc.reason}") from exc


def status_label(value: Any, colors: bool = True) -> str:
    text = str(value)
    if text == "online" or value is True:
        return color(text, C.GREEN, colors)
    if text == "offline" or value is False:
        return color(text, C.RED, colors)
    return text


def print_status(api: str, colors: bool = True, banner_path: str | None = DEFAULT_BANNER) -> int:
    status = request_json("GET", f"{api}/api/status")
    print(banner(colors, banner_path))
    print()
    print(
        box(
            "System Status",
            [
                ("API", status_label(status.get("status"), colors)),
                ("Scanner", status_label(status.get("scanner"), colors)),
                ("Database", status_label(status.get("database"), colors)),
                ("OnionClaw", status_label(status.get("onionclaw"), colors)),
                ("OnionClaw installed", status_label(status.get("onionclaw_installed"), colors)),
                ("AI model", status.get("model", "-")),
                ("Total scans", status.get("total_scans", 0)),
                ("Active scans", status.get("active_scans", 0)),
            ],
            colors,
        )
    )
    return 0


def build_scan_body(args: argparse.Namespace, target: str) -> dict[str, Any]:
    body: dict[str, Any] = {"target": target, "stream_type": args.stream}
    if args.stream == "research":
        keywords = parse_csv(args.keywords) or [target]
        scope = {
            "enable_dark_web": bool(args.dark_web),
            "client": args.client or target,
            "allowed_keywords": keywords,
            "blocked_keywords": parse_csv(args.blocked),
            "allow_onion_fetch": bool(args.allow_onion_fetch),
            "allow_identity_rotation": bool(args.allow_identity_rotation),
            "approved": bool(args.dark_web),
            "approved_by": args.approved_by or "",
            "notes": "Started from Praedix CLI",
        }
        body["research_scope"] = scope
    return body


def validate_args(args: argparse.Namespace) -> None:
    if args.dark_web and args.stream != "research":
        raise ValueError("--dark-web can only be used with --stream research")
    if args.dark_web and not args.approved_by:
        raise ValueError("--dark-web requires --approved-by")


def progress_bar(current: int, maximum: int, width: int = 34, colors: bool = True) -> str:
    maximum = max(1, maximum)
    current = max(0, min(current, maximum))
    filled = int(width * (current / maximum))
    bar = "#" * filled + "-" * (width - filled)
    pct = int(100 * (current / maximum))
    return color(f"[{bar}] {pct:3d}%", C.MAGENTA, colors)


def step_summary(step: dict[str, Any]) -> str:
    command = step.get("command") or step.get("tool") or "step"
    status = step.get("status", "completed")
    exit_code = step.get("exit_code")
    suffix = f" exit={exit_code}" if exit_code is not None else ""
    return f"{command} ({status}{suffix})"


def print_new_steps(scan: dict[str, Any], printed_count: int, verbose: bool, colors: bool) -> int:
    steps = scan.get("steps") or []
    for idx, step in enumerate(steps[printed_count:], start=printed_count + 1):
        print(color(f"[*] Step {idx}: ", C.BLUE, colors) + step_summary(step))
        if verbose:
            output = step.get("output") or step.get("stdout") or step.get("error")
            if output:
                preview = str(output).strip()
                if len(preview) > 700:
                    preview = preview[:700] + "\n..."
                for line_text in preview.splitlines()[:18]:
                    print(color("    | ", C.DIM, colors) + line_text)
    return len(steps)


def poll_scan(api: str, scan_id: str, verbose: bool, colors: bool, report_preview: bool = False) -> int:
    printed_steps = 0
    last_status = None
    while True:
        scan = request_json("GET", f"{api}/api/scan/{scan_id}", timeout=30)
        printed_steps = print_new_steps(scan, printed_steps, verbose, colors)
        current = int(scan.get("current_step") or 0)
        maximum = int(scan.get("max_steps") or 1)
        status = scan.get("status", "unknown")
        workflow = scan.get("workflow_status", "queued")
        if status == "done":
            current = maximum
        if (status, workflow, current) != last_status:
            print(f"{progress_bar(current, maximum, colors=colors)}  {status} / {workflow}")
            last_status = (status, workflow, current)
        if status in FINAL_STATUSES:
            print()
            if status == "done":
                print(color("[+] Scan complete", C.GREEN, colors))
            else:
                print(color("[!] Scan ended with error", C.RED, colors))
            report_file = scan.get("report_file")
            if report_file:
                print(f"Report file: {report_file}")
            report = scan.get("report")
            if report and report_preview:
                print()
                print(color("Report preview:", C.CYAN, colors))
                preview = str(report).strip()
                if len(preview) > 1400:
                    preview = preview[:1400] + "\n..."
                print(preview)
            return 0 if status == "done" else 1
        time.sleep(2)


def run_scan(args: argparse.Namespace, api: str, colors: bool) -> int:
    original, target = normalize_target(args.url)
    validate_target_name(target)
    body = build_scan_body(args, target)
    print(banner(colors, args.banner))
    print()
    print(color("WARNING: Use only on authorized targets.", C.YELLOW, colors))
    print()
    print(
        box(
            "Scan Configuration",
            [
                ("Input", original),
                ("Target sent to API", target),
                ("API", api),
                ("Stream", args.stream),
                ("Dark web / OSINT", "enabled" if args.dark_web else "disabled"),
                ("Verbose", "yes" if args.verbose else "no"),
            ],
            colors,
        )
    )
    print()
    response = request_json("POST", f"{api}/api/scan", body=body, timeout=30)
    scan_id = response.get("scan_id")
    if not scan_id:
        raise RuntimeError(f"Unexpected API response: {response}")
    print(color(f"[+] Scan started: {scan_id}", C.GREEN, colors))
    if args.no_poll:
        print(f"Open in web UI or poll API: {api}/api/scan/{scan_id}")
        return 0
    return poll_scan(api, scan_id, args.verbose, colors, args.report_preview)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="praedix",
        description="Praedix CLI - start and monitor security scans from the terminal.",
    )
    parser.add_argument("-u", "--url", help="Target domain, IP, Docker service, or URL.")
    parser.add_argument("--api", default=DEFAULT_API, help=f"Praedix API base URL. Default: {DEFAULT_API}")
    parser.add_argument("--stream", choices=["local_vm", "research"], default="local_vm", help="Workflow stream.")
    parser.add_argument("--status", action="store_true", help="Show Praedix service status and exit.")
    parser.add_argument("--dark-web", action="store_true", help="Enable OnionClaw dark web / OSINT research.")
    parser.add_argument("--client", help="Client or engagement name for research scans.")
    parser.add_argument("--keywords", help="Allowed research keywords, comma separated.")
    parser.add_argument("--blocked", help="Blocked research keywords, comma separated.")
    parser.add_argument("--approved-by", help="Person who approved dark web / OSINT scope.")
    parser.add_argument("--allow-onion-fetch", action="store_true", help="Allow OnionClaw to fetch .onion pages.")
    parser.add_argument("--allow-identity-rotation", action="store_true", help="Allow Tor identity rotation.")
    parser.add_argument("--no-poll", action="store_true", help="Start scan only; do not wait for results.")
    parser.add_argument("--report-preview", action="store_true", help="Print a short final report preview after completion.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print tool output previews while scanning.")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors.")
    parser.add_argument("--banner", default=DEFAULT_BANNER, help="Path to custom ASCII/ANSI banner text.")
    parser.add_argument("--no-banner", action="store_true", help="Use the built-in Praedix text banner.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    colors = not args.no_color
    api = normalize_api(args.api)
    if args.no_banner:
        args.banner = None
    try:
        validate_args(args)
        if args.status:
            return print_status(api, colors, args.banner)
        if not args.url:
            parser.error("the following argument is required unless --status is used: -u/--url")
        return run_scan(args, api, colors)
    except (RuntimeError, ValueError) as exc:
        print(color(f"[!] {exc}", C.RED, colors), file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print(color("\n[!] Interrupted", C.YELLOW, colors), file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
