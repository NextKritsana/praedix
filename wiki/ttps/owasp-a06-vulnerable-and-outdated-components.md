# A06:2021 – Vulnerable and Outdated Components

**Summary**: Risks associated with using software components (libraries, frameworks, and modules) that are unsupported, out of date, or have known vulnerabilities.

**Severity**: High
**CVE**: CVE-2021-44228, CVE-2021-41773, [[CVE-2026-31431]]
**CVSS Score**: 9.8 (Typical for critical RCE in components)
**Affected systems**: Operating Systems, Web Servers, DBMS, APIs, Libraries
**Sources**: OWASP_A06_Vulnerable_Outdated_Components.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Applications are vulnerable when they use components that are outdated or have known security flaws. This includes the OS, web/app server, database, and all libraries/frameworks used. (source: OWASP_A06_Vulnerable_Outdated_Components.md)

### Notable Examples:
- **Log4Shell (CVE-2021-44228)**: Remote code execution in Apache Log4j
- **Apache Path Traversal (CVE-2021-41773)**: Flaw in Apache HTTP Server 2.4.49
- **Copy Fail ([[CVE-2026-31431]])**: Linux Kernel Local Privilege Escalation

## Attack Vector and Conditions
Attackers identify vulnerable components through version banners, fingerprinting, or metadata. They then use publicly available exploits (Proof-of-Concepts) to target the known flaw.

## Detection Indicators
- Version strings in HTTP headers or service banners
- Known vulnerable library files found in application directories
- Automated scanners flagging outdated versions

## Remediation Steps
- Maintain a continuous inventory of all components and their versions
- Remove unused dependencies and unnecessary features
- Monitor sources like NVD and CVE for new vulnerabilities
- Patch or upgrade components in a timely fashion
- Only obtain components from official, secure sources

## Tools used
- [[nmap]] — `sV` and `vulners` scripts to detect services and known CVEs
- [[nikto]] — identifies outdated server software
- OWASP Dependency-Check (noted in source)

## Related pages
- [[owasp-top-10]]
- [[CVE-2026-31431]]
- [[owasp-a05-security-misconfiguration]]
- [[owasp-a08-software-and-data-integrity-failures]]
