# A02:2021 – Cryptographic Failures

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

## Overview
Previously known as "Sensitive Data Exposure" (a broad symptom rather than a root cause), the focus is on failures related to cryptography. This often leads to exposure of sensitive data. Notable CWEs include CWE-259 (Use of Hard-coded Password), CWE-327 (Broken or Risky Crypto Algorithm), and CWE-331 (Insufficient Entropy).

## Description
The first thing to determine is the protection needs of data in transit and at rest. Passwords, credit card numbers, health records, personal information, and business secrets require extra protection.

### Common Vulnerabilities:
- Data transmitted in clear text (HTTP, SMTP, FTP)
- Old or weak cryptographic algorithms or protocols (MD5, SHA1, DES)
- Default crypto keys in use, weak keys generated, or improper key management
- Encryption not enforced (missing HTTP security headers or directives)
- Server certificate not properly validated (chain of trust)
- Passwords stored using simple hashing instead of adaptive salted hashing (bcrypt, scrypt, Argon2)
- Deprecated hash functions like MD5 or SHA1 used
- Initialization vectors ignored, reused, or not generated sufficiently secure

## How to Detect (Pentest Approach)
- Check if the site uses HTTPS everywhere (`nmap --script ssl-enum-ciphers -p 443 <target>`)
- Look for HTTP to HTTPS redirect failures
- Check for weak TLS/SSL versions (TLS 1.0, 1.1, SSLv3)
- Scan for weak cipher suites
- Check response headers for `Strict-Transport-Security`, `Content-Security-Policy`
- Look for sensitive data in URLs, logs, or error messages

### Tools to Use:
- `nmap --script ssl-enum-ciphers` — check SSL/TLS configuration
- `nikto` — identify weak crypto configurations
- `sslscan` or `testssl.sh` — detailed TLS analysis

## How to Prevent
- Classify data processed, stored, or transmitted and identify sensitive data
- Don't store sensitive data unnecessarily; discard it as soon as possible
- Encrypt all sensitive data at rest
- Ensure up-to-date and strong standard algorithms, protocols, and keys
- Encrypt all data in transit with secure protocols such as TLS with forward secrecy (FS) ciphers
- Disable caching for responses containing sensitive data
- Store passwords using strong adaptive and salted hashing functions (Argon2, scrypt, bcrypt, PBKDF2)
- Verify independently the effectiveness of configuration and settings

## Example Attack Scenarios

### Scenario 1: Weak Password Storage
A site stores passwords using simple unsalted hashes. An attacker retrieves the password database and uses rainbow tables to crack all passwords.

### Scenario 2: Missing TLS
A site doesn't enforce HTTPS. An attacker on a public Wi-Fi network downgrades connections from HTTPS to HTTP, intercepts requests, and steals session cookies.

## Related CWEs
- CWE-259: Use of Hard-coded Password
- CWE-327: Use of a Broken or Risky Cryptographic Algorithm
- CWE-331: Insufficient Entropy

---
*Source: OWASP Foundation — owasp.org/Top10*
