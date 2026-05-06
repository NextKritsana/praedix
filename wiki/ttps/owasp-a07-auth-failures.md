# A07:2021 – Identification and Authentication Failures

**Summary**: Vulnerabilities related to the confirmation of a user's identity, authentication, and session management.

**Severity**: High
**CVE**: N/A
**CVSS Score**: 7.5 (Estimated average)
**Affected systems**: Authentication modules, Session management, MFA systems
**Sources**: OWASP_A07_Auth_Failures.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Previously known as "Broken Authentication," this category involves flaws that allow attackers to compromise passwords, keys, or session tokens, or to assume other users' identities. (source: OWASP_A07_Auth_Failures.md)

### Common Vulnerabilities:
- Permitting brute force or automated credential stuffing attacks
- Allowing default, weak, or well-known passwords
- Ineffective credential recovery processes
- Missing or ineffective multi-factor authentication (MFA)
- Session identifiers exposed in URLs or not invalidated correctly

## Attack Vector and Conditions
Attackers use automated tools to perform brute force or credential stuffing (using lists of leaked credentials). They may also attempt to fixate sessions or predict session IDs if entropy is low.

## Detection Indicators
- High volume of failed login attempts in logs
- Multiple accounts accessed from a single IP address
- Users reporting unauthorized changes to their accounts

## Remediation Steps
- Implement multi-factor authentication (MFA)
- Do not deploy with default credentials
- Implement weak-password checks and align with NIST 800-63b guidelines
- Limit failed login attempts and implement delays
- Use a secure, server-side session manager that generates high-entropy session IDs

## Tools used
- [[nmap]] — `http-default-accounts` script to test default credentials
- [[dirb]] — discover login and admin pages
- Hydra — brute force login forms (source: OWASP_A07_Auth_Failures.md, line 31)

## Related pages
- [[owasp-top-10]]
- [[owasp-a01-broken-access-control]]
- [[owasp-a02-cryptographic-failures]]
