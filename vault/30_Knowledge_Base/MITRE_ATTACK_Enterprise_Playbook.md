# MITRE ATT&CK Enterprise Playbook

> Source: MITRE ATT&CK official site. Use this as a defensive mapping framework for adversary behavior, external exposure, evidence collection, and report classification.

## How to Detect
- Start by mapping observed behavior to ATT&CK tactics, then choose tools. Do not start from a technique name and assume compromise.
- Current Enterprise matrix tactics include Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Stealth, Defense Impairment, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, and Impact.
- Use `nmap -F {target}` for external discovery of reachable services that may support Reconnaissance, Initial Access, Discovery, or Command and Control exposure analysis.
- Use `nmap -sV -p <ports> {target}` to collect service-version evidence for Exploit Public-Facing Application, External Remote Services, Valid Accounts exposure, and exposed admin surfaces.
- Use `curl -I` and `curl -s` to inspect web headers, redirects, cookies, login portals, exposed files, admin panels, API docs, and suspicious content.
- Use `nikto`, `dirb`, and `nmap --script http-headers,http-methods,http-enum` to identify public-facing web exposure, directory listings, unsafe methods, and exposed application paths.
- Use `dig {target} ANY` and `whois {target}` for Reconnaissance context such as DNS, WHOIS, certificates, mail controls, ownership, and domain infrastructure.
- Use `sslscan {target}` for TLS evidence that may support exposure findings, weak configuration, or certificate-based infrastructure analysis.
- Use OnionClaw OSINT only when scope-approved to collect dark web or open-source leads for credential exposure, sale listings, exposed infrastructure, or victim-related mentions. Treat OSINT as leads until verified.
- For host-level ATT&CK tactics such as Persistence, Privilege Escalation, Credential Access, Lateral Movement, Collection, Exfiltration, and Impact, external scans alone are insufficient. Require endpoint logs, EDR, SIEM, cloud logs, memory, disk artifacts, authentication logs, or packet captures before claiming compromise.

## Common
- MITRE ATT&CK is a knowledge base of adversary tactics and techniques based on real-world observations. Use it to classify behavior and improve coverage, not as proof by itself.
- Separate external exposure from confirmed adversary behavior. A vulnerable service is an Initial Access risk, not proof that Initial Access occurred.
- Evidence levels should be explicit: lead, exposure, suspected behavior, confirmed behavior, confirmed impact.
- Tactic mapping is not severity. Severity depends on exploitability, asset criticality, exposure, authentication, compensating controls, and observed impact.
- Do not report Persistence, Lateral Movement, Exfiltration, or Impact from `nmap`, `curl`, `nikto`, or `dirb` alone.
- ATT&CK technique names should be used as report labels only when evidence matches the technique behavior.
- For pre-deploy or local VM testing, use ATT&CK as an attacker-behavior lens to prioritize fixes, but keep findings grounded in OWASP and tool evidence.
- For incident response, use ATT&CK to organize hypotheses and evidence requests: what logs prove execution, what artifacts prove persistence, what network records prove C2, and what data proves exfiltration.
- For cloud or identity exposure, look for valid accounts, external remote services, public admin portals, weak MFA posture, exposed keys, and overly broad permissions. Praedix may need manual/cloud-log evidence beyond scanner output.
- For Stealth and Defense Impairment, require evidence of log deletion, sensor tampering, security tool modification, impairing defenses, hiding artifacts, or evasion behavior. External recon cannot prove these alone.
- For Credential Access, do not test or harvest credentials. Report exposed credential artifacts only when discovered in authorized sources and redact secrets.
- For Command and Control, external indicators include suspicious domains, ports, TLS certificates, beacons in logs, unusual protocols, or known malware infrastructure. A listening port alone is not C2.

## Payloads
Use safe validation prompts and evidence questions, not offensive payloads.

ATT&CK evidence questions:
```text
What tactic best describes the observed behavior?
What exact tool output supports this mapping?
Is this exposure, suspected behavior, or confirmed behavior?
What additional evidence is required to confirm the technique?
What logs or artifacts would prove or disprove this hypothesis?
What compensating controls reduce exploitability?
```

Safe external validation checks:
```text
Confirm open ports and service versions.
Confirm web headers and exposed paths.
Confirm TLS configuration and certificate metadata.
Confirm DNS, WHOIS, and public infrastructure context.
Confirm whether an exposed service requires authentication.
Confirm whether a suspected vulnerable version is actually reachable.
```

Do not perform:
```text
Credential guessing
Phishing
Payload deployment
Persistence creation
Privilege escalation
Lateral movement
Data exfiltration
Denial-of-service
Malware execution
Security tool tampering
```

## Tools to Use
- `nmap -F {target}`: external service discovery for Reconnaissance, Discovery, Initial Access exposure, and attack-surface overview.
- `nmap -sV -p <ports> {target}`: service version evidence for vulnerability and exposure mapping.
- `nmap --script vuln -p <ports> {target}`: vulnerability leads only; verify before reporting.
- `nmap --script http-headers,http-methods,http-enum {target}`: web method, header, and path enumeration.
- `curl -I http://{target}` and `curl -I https://{target}`: headers, redirects, cookies, server clues, security controls.
- `curl -s http://{target}`: visible content, forms, scripts, links, comments, exposed API clues.
- `nikto -h {target} -maxtime 120`: web server misconfiguration and known issue leads.
- `dirb http://{target} -r`: exposed directories and files.
- `wafw00f http://{target}`: WAF or filtering context.
- `sslscan {target}`: TLS protocols, ciphers, and certificate evidence.
- `dig {target} ANY`: DNS context for Reconnaissance and infrastructure mapping.
- `whois {target}`: ownership and registrar context.
- `traceroute {target}`: network path context, not compromise evidence.
- OnionClaw OSINT with explicit approval: leads for exposed credentials, leaked infrastructure references, sale mentions, threat actor chatter, and dark web exposure. Do not claim breach without direct evidence.

## MITRE ATT&CK Mapping Guide
- Reconnaissance: DNS, WHOIS, victim-owned websites, public repositories, certificates, scan databases, open websites, and public AI services.
- Resource Development: acquired domains, VPS, web services, serverless infrastructure, accounts, tools, exploits, certificates, and staged capabilities.
- Initial Access: exploit public-facing application, external remote services, phishing, trusted relationships, supply chain compromise, valid accounts, drive-by compromise, and removable media.
- Execution: command and scripting interpreters, user execution, scheduled tasks, services, WMI, software deployment tools, container administration, serverless execution, and exploitation for client execution.
- Persistence: account manipulation, scheduled tasks, services, startup items, web shells, valid accounts, cloud persistence, container persistence, and boot/logon mechanisms.
- Privilege Escalation: exploitation for privilege escalation, hijack execution flow, abuse elevation control, vulnerable drivers, setuid/setgid, sudo/sudo caching, and misconfigured permissions.
- Stealth: hiding artifacts, masquerading, obfuscated files, hidden users, hidden windows, process injection, proxy execution, and evasion-oriented behavior.
- Defense Impairment: disabling or modifying security tools, impairing defenses, log deletion, indicator removal, tampering with sensors, and weakening monitoring.
- Credential Access: brute force, credential dumping, OS credential stores, browser credential stores, cloud credentials, secrets in files, unsecured credentials, keylogging, and phishing-derived credentials.
- Discovery: system information, network services, accounts, groups, processes, software, cloud resources, containers, permissions, domain trust, and network topology.
- Lateral Movement: remote services, remote desktop, SMB/Windows admin shares, SSH, pass-the-hash, internal spearphishing, replication, and software deployment.
- Collection: local data, network shares, cloud storage, email, browser session data, screen capture, audio capture, clipboard data, and archive collection.
- Command and Control: application-layer protocols, web services, encrypted channels, proxies, domain fronting, ingress tool transfer, fallback channels, and non-standard ports.
- Exfiltration: exfiltration over web service, cloud storage, C2 channel, alternative protocol, removable media, scheduled transfer, encrypted/compressed data, and traffic shaping.
- Impact: data destruction, encryption, account access removal, resource hijacking, service stop, defacement, disk wipe, firmware corruption, financial theft, and denial-of-service.

## Reporting Rules
- Always include the ATT&CK tactic, candidate technique, evidence, confidence, and what would be needed to confirm.
- Use "maps to" rather than "is" unless behavior is confirmed.
- If only scanner output exists, report "exposure related to Initial Access" rather than "Initial Access occurred."
- For each high-risk mapping, add a defensive recommendation: patch, close exposure, enforce MFA, rotate secrets, improve logging, restrict admin interfaces, strengthen EDR/SIEM coverage, add rate limits, or segment networks.
