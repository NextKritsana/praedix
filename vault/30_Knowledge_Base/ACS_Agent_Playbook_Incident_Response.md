# ACS Agent Playbook: Incident Response

> Purpose: Help Praedix reason about incident response evidence and choose collection-oriented checks without overclaiming compromise.

## How to Detect
- For internet-facing incident triage, begin with `nmap -F {target}` to identify exposed services that could explain intrusion paths.
- Follow with `nmap -sV -p <ports> {target}` on open ports to capture service versions.
- Use `curl -I` and `curl -s` for exposed web services to identify server banners, suspicious redirects, login portals, admin panels, and exposed files.
- Use `dig {target} ANY` for DNS context, especially MX, TXT, SPF, DMARC, DKIM, and suspicious subdomain clues.
- Use `whois {target}` for ownership and registrar context when investigating domain exposure.
- Use `sslscan {target}` to identify weak TLS posture that may support incident timeline or exposure analysis.
- Use `traceroute {target}` only for network path context, not as compromise evidence.

## Common
- Distinguish exposure from compromise. Open services, weak headers, and old versions are leads, not proof of breach.
- Incident response needs timeline, affected assets, initial access vector, persistence, lateral movement, exfiltration evidence, and containment status.
- If logs are not available to Praedix, mark host compromise as inconclusive and recommend log collection.
- Treat tool output as external visibility only. It cannot prove process execution, registry persistence, memory artifacts, or file system tampering.
- For Windows IR, useful evidence classes include Event Logs, Sysmon, PowerShell logs, Prefetch, Amcache, ShimCache, SRUM, browser history, scheduled tasks, services, and registry run keys.
- For memory IR, useful evidence classes include process tree, network connections, loaded DLLs, injected code, handles, and command history.
- Do not claim malware execution, credential theft, or data exfiltration without direct forensic evidence.

## Payloads
This playbook does not use exploit payloads. Use investigation questions instead:
```text
What ports are externally reachable?
What service versions are exposed?
Are admin interfaces public?
Are DNS mail controls configured?
Are weak TLS protocols or ciphers present?
Are web headers missing security controls?
What logs or forensic artifacts are needed next?
```

## Tools to Use
- `nmap -F {target}`: identify exposed services quickly.
- `nmap -sV -p <ports> {target}`: collect version evidence.
- `nmap --script vuln -p <ports> {target}`: vulnerability leads only; verify before reporting.
- `dig {target} ANY`: DNS and mail control context.
- `whois {target}`: ownership and registrar context.
- `curl -I http://{target}`: web headers, cookies, redirects.
- `curl -s http://{target}`: exposed content and portal clues.
- `sslscan {target}`: TLS evidence.
- `traceroute {target}`: route context.
