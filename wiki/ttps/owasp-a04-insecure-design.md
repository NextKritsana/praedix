# A04:2021 – Insecure Design

**Summary**: Risks related to design and architectural flaws, where security controls were never created to defend against specific attacks.

**Severity**: High
**CVE**: N/A
**CVSS Score**: 7.3 (Estimated average)
**Affected systems**: Application architecture, business logic modules
**Sources**: OWASP_A04_Insecure_Design.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Insecure design focuses on risks related to design and architectural flaws. It differs from insecure implementation; an insecure design cannot be fixed by a perfect implementation because the necessary security controls were never designed in the first place. (source: OWASP_A04_Insecure_Design.md)

### Common Vulnerabilities:
- No rate limiting on sensitive operations (login, password reset)
- Business logic flaws (e.g., purchasing items at negative prices)
- Missing anti-automation controls (e.g., CAPTCHA)
- Lack of tenant isolation in multi-tenant systems
- Overly informative error messages revealing internal system details

## Attack Vector and Conditions
Attackers exploit flaws in the application's logic or architecture. These attacks often don't involve technical exploits like injection but rather misuse the application's intended features in unintended ways.

## Detection Indicators
- Ability to perform repetitive actions (brute force) without being blocked
- Successful transactions with illogical data (negative quantities, prices)
- Predictable patterns in security tokens or session IDs

## Remediation Steps
- Establish and use a secure development lifecycle (SDLC)
- Use threat modeling for critical authentication, access control, and business logic flows
- Write unit and integration tests to validate all critical flows
- Segregate system and network layers
- Limit resource consumption by user or service

## Tools used
- [[nikto]] — find design-level misconfigurations
- Burp Suite (manual) — testing for business logic flaws
- [[nmap]] — identify unnecessarily exposed services

## Related pages
- [[owasp-top-10]]
- [[owasp-a05-security-misconfiguration]]
- [[owasp-a09-logging-monitoring-failures]]
