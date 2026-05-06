# A05:2021 – Security Misconfiguration

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

## Overview
90% of applications were tested for some form of misconfiguration, with an average incidence rate of 4.5%. With more shifts into highly configurable software, it's not surprising to see this category move up. Notable CWEs: CWE-16 (Configuration) and CWE-611 (XML External Entity - XXE).

## Description
The application might be vulnerable if:
- Missing appropriate security hardening or improperly configured permissions on cloud services
- Unnecessary features are enabled or installed (ports, services, pages, accounts, privileges)
- Default accounts and their passwords are still enabled and unchanged
- Error handling reveals stack traces or overly informative error messages
- Latest security features are disabled or not configured securely
- Software is out of date or vulnerable

### Common Vulnerabilities:
- Default credentials (admin/admin, root/toor)
- Unnecessary services running (FTP, Telnet, SSH on unexpected ports)
- Directory listing enabled
- Verbose error messages exposing stack traces
- Missing security headers
- Unnecessary HTTP methods enabled (PUT, DELETE, TRACE)
- Outdated server software with known CVEs

## How to Detect (Pentest Approach)
- Scan for open ports and services: `nmap -sV -F <target>`
- Check for default pages: `dirb http://<target>`
- Test for directory listing
- Check HTTP response headers for security headers
- Test for TRACE/TRACK methods: `curl -X TRACE <target>`
- Look for server version disclosure in headers

### Tools to Use:
- `nmap -sV` — service version detection
- `nikto` — comprehensive web misconfiguration scanner
- `dirb` — directory brute-forcing
- `nmap --script http-methods` — check allowed HTTP methods
- `nmap --script http-headers` — check security headers

### Security Headers to Check:
```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=31536000
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
```

## How to Prevent
- A repeatable hardening process for fast, easy deployment of properly locked-down environments
- A minimal platform without unnecessary features, components, documentation, and samples
- Review and update configurations as part of the patch management process
- A segmented application architecture with segmentation, containerization, or cloud security groups
- Sending security directives to clients (Security Headers)
- An automated process to verify the effectiveness of configurations in all environments

## Related CWEs
- CWE-2: Environmental Security Flaws
- CWE-11: ASP.NET Misconfiguration
- CWE-16: Configuration
- CWE-611: Improper Restriction of XML External Entity Reference (XXE)

---
*Source: OWASP Foundation — owasp.org/Top10*
