# ACS Agent Playbook: Digital Forensics

> Purpose: Help Praedix produce evidence-aware forensic recommendations from external scan results and known forensic artifact classes.

## How to Detect
- Use external scan results to identify where forensic collection should focus, not to prove host-level events.
- Start with `nmap -F {target}` and version checks to identify exposed attack surfaces.
- Use `curl -I`, `curl -s`, `nikto`, and `dirb` to identify exposed web artifacts such as backups, indexes, admin panels, logs, and misconfigured directories.
- Use `dig` and `whois` to capture domain and infrastructure context for case notes.
- For TLS-enabled services, use `sslscan` to capture certificate dates and TLS posture.
- If a web exposure suggests leaked files, verify the exact URL, HTTP status, file name, and response evidence before reporting.

## Common
- Digital forensics depends on chain of custody, acquisition method, timestamps, hashes, source media, and reproducible analysis.
- External scan output can guide collection but cannot replace disk, memory, log, or network packet evidence.
- Important Windows artifact classes: Registry hives, Event Logs, Prefetch, Amcache, ShimCache, SRUM, Jump Lists, LNK files, browser artifacts, scheduled tasks, services, PowerShell logs, and Sysmon logs.
- Important Linux artifact classes: auth logs, syslog, bash history, cron, systemd units, SSH keys, web logs, process lists, package logs, and persistence locations.
- Important media artifact classes: image metadata, file headers, EXIF, container metadata, timestamps, hash comparison, and tamper indicators.
- Do not claim timestamp manipulation, file deletion, persistence, or user activity without artifact evidence.

## Payloads
No exploit payloads are used for digital forensics. Use evidence prompts:
```text
What artifact proves the event?
What timestamp source supports it?
What hash identifies the file?
What collection method preserved integrity?
What alternative explanation exists?
What evidence is missing?
```

## Tools to Use
- `nmap -F {target}`: identify likely collection priority from exposed services.
- `nmap -sV -p <ports> {target}`: document service versions for timeline context.
- `curl -I http://{target}`: headers, status codes, last-modified clues.
- `curl -s http://{target}`: exposed page or file evidence.
- `dirb http://{target} -r`: identify exposed directories and files.
- `nikto -h {target} -maxtime 120`: web exposure leads.
- `dig {target} ANY`: DNS context.
- `whois {target}`: domain registration context.
- `sslscan {target}`: certificate and TLS evidence.
