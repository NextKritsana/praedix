# A06:2021 – Vulnerable and Outdated Components

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

## Overview
Previously titled "Using Components with Known Vulnerabilities." This category moves up from #9 in 2017. It is a known issue that is difficult to test and assess risk. It is the only category without any mapped CWEs.

## Description
You are likely vulnerable if:
- You do not know the versions of all components you use (both client-side and server-side)
- The software is vulnerable, unsupported, or out of date (OS, web/app server, DBMS, APIs, libraries)
- You do not scan for vulnerabilities regularly
- You do not fix or upgrade the underlying platform, frameworks, and dependencies in a timely fashion
- Software developers do not test the compatibility of updated, upgraded, or patched libraries
- You do not secure the components' configurations (see A05:2021-Security Misconfiguration)

## How to Detect (Pentest Approach)
- Identify software versions: `nmap -sV <target>`
- Check web server headers for version info
- Search for known CVEs against detected versions
- Check for outdated JavaScript libraries in web page source

### Tools to Use:
- `nmap -sV` — detect service and version numbers
- `nikto` — identifies outdated server software
- `nmap --script vulners` — check for known CVEs
- `whois` — domain and hosting information

### Example Version Detection:
```bash
nmap -sV -p 80,443,22 scanme.nmap.org
# Output reveals: Apache 2.4.49 → check CVE-2021-41773
```

## How to Prevent
- Remove unused dependencies, unnecessary features, components, files, and documentation
- Continuously inventory the versions of both client-side and server-side components using tools like OWASP Dependency-Check, retire.js
- Monitor sources like NVD, CVE for vulnerabilities in components
- Only obtain components from official sources over secure links
- Monitor for libraries and components that are unmaintained or do not create security patches

## Related CVE Examples
- CVE-2021-44228 (Log4Shell) — Apache Log4j remote code execution
- CVE-2021-41773 — Apache HTTP Server path traversal
- CVE-2017-5638 — Apache Struts 2 remote code execution

---
*Source: OWASP Foundation — owasp.org/Top10*
