# A02:2021 – Cryptographic Failures

**Summary**: Failures related to cryptography (or lack thereof) which often lead to the exposure of sensitive data in transit or at rest.

**Severity**: High
**CVE**: N/A
**CVSS Score**: 7.5 (Estimated average)
**Affected systems**: Data storage, communication protocols (HTTPS, SMTP, FTP)
**Sources**: OWASP_A02_Cryptographic_Failures.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Previously known as "Sensitive Data Exposure," this category focuses on root causes related to cryptography. It involves failures to protect data in transit and at rest, such as passwords, credit card numbers, and personal information. (source: OWASP_A02_Cryptographic_Failures.md)

### Common Vulnerabilities:
- Data transmitted in clear text (HTTP, SMTP, FTP)
- Old or weak cryptographic algorithms (MD5, SHA1, DES)
- Default or weak crypto keys and improper key management
- Missing HTTP security headers (e.g., HSTS)
- Passwords stored using simple hashing instead of adaptive salted hashing (bcrypt, Argon2)

## Attack Vector and Conditions
Attackers may perform man-in-the-middle (MITM) attacks to intercept clear-text data or exploit weak encryption to decrypt sensitive information. Retrieval of password databases can lead to offline cracking if weak hashing is used.

## Detection Indicators
- Use of non-secure protocols (HTTP)
- Warnings about weak cipher suites or expired certificates
- Sensitive data found in clear-text in database backups or logs

## Remediation Steps
- Classify data and encrypt sensitive data at rest
- Encrypt all data in transit with secure protocols like TLS with forward secrecy
- Discard sensitive data as soon as it is no longer needed
- Use strong adaptive and salted hashing functions for passwords (Argon2, bcrypt)
- Disable caching for responses containing sensitive data

## Tools used
- [[nmap]] — `ssl-enum-ciphers` to check SSL/TLS configuration
- [[nikto]] — identify weak crypto configurations
- [[sslscan]] — detailed TLS analysis

## Related pages
- [[owasp-top-10]]
- [[owasp-a05-security-misconfiguration]]
- [[owasp-a07-auth-failures]]
