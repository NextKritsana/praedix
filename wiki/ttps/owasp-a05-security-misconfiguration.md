# A05:2021 – Security Misconfiguration

**Summary**: Vulnerabilities arising from insecure default configurations, incomplete configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages.

**Severity**: Medium
**CVE**: N/A
**CVSS Score**: 6.5 (Estimated average)
**Affected systems**: Web servers, Application servers, Cloud platforms, CMS
**Sources**: OWASP_A05_Security_Misconfiguration.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Security misconfiguration can happen at any level of an application stack, including the network, platform, web server, application server, database, frameworks, and custom code. (source: OWASP_A05_Security_Misconfiguration.md)

### Common Vulnerabilities:
- Default credentials (e.g., admin/admin)
- Unnecessary features/services enabled (ports, pages, accounts)
- Directory listing enabled on the server
- Verbose error messages exposing stack traces
- Missing or misconfigured security headers (X-Frame-Options, CSP, etc.)

## Attack Vector and Conditions
Attackers often use automated scanners to find default pages, unpatched flaws, and common misconfigurations. Publicly accessible cloud storage or management interfaces are frequent targets.

## Detection Indicators
- Presence of default welcome pages or management consoles
- Server version disclosure in HTTP response headers
- Stack traces appearing in application error pages

## Remediation Steps
- Implement a repeatable hardening process for environments
- Maintain a minimal platform by removing unnecessary features and components
- Review and update configurations as part of the patch management process
- Use automated processes to verify configuration effectiveness

## Tools used
- [[nmap]] — `sV` for version detection and `http-methods` to check allowed methods
- [[nikto]] — comprehensive web misconfiguration scanner
- [[dirb]] — directory brute-forcing for default pages

## Related pages
- [[owasp-top-10]]
- [[owasp-a04-insecure-design]]
- [[owasp-a06-vulnerable-and-outdated-components]]
