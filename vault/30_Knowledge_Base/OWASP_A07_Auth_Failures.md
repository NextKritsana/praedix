# A07:2021 – Identification and Authentication Failures

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)

## Overview
Previously known as "Broken Authentication." Slid down from the second position. Notable CWEs: CWE-297 (Improper Validation of Certificate), CWE-287 (Improper Authentication), CWE-384 (Session Fixation).

## Description
Confirmation of the user's identity, authentication, and session management is critical to protect against authentication-related attacks.

### Common Vulnerabilities:
- Permits brute force or other automated attacks
- Permits default, weak, or well-known passwords (e.g., "Password1", "admin/admin")
- Uses weak or ineffective credential recovery processes (e.g., "knowledge-based answers")
- Uses plain text, encrypted, or weakly hashed passwords
- Has missing or ineffective multi-factor authentication (MFA)
- Exposes session identifier in the URL
- Reuses session identifier after successful login
- Does not correctly invalidate session IDs (during logout, idle period, or absolute timeouts)

## How to Detect (Pentest Approach)
- Test for default credentials on login pages
- Attempt brute force on login forms
- Check if account lockout is implemented
- Test password complexity requirements
- Check for session fixation vulnerabilities
- Test if sessions are invalidated after logout

### Tools to Use:
- `nmap --script http-default-accounts` — test default credentials
- `dirb` — discover login/admin pages
- Hydra or Medusa — brute force login forms (use responsibly)

### Common Default Credentials:
```
admin:admin
admin:password
root:root
root:toor
admin:123456
test:test
```

## How to Prevent
- Implement multi-factor authentication to prevent automated credential stuffing, brute force, and stolen credential reuse
- Do not ship or deploy with any default credentials
- Implement weak-password checks (e.g., against a list of the top 10,000 worst passwords)
- Align password length, complexity, and rotation policies with NIST 800-63b guidelines
- Limit or increasingly delay failed login attempts; log all failures and alert admins
- Use a server-side, secure, built-in session manager that generates a new random session ID with high entropy after login

## Related CWEs
- CWE-287: Improper Authentication
- CWE-297: Improper Validation of Certificate with Host Mismatch
- CWE-384: Session Fixation

---
*Source: OWASP Foundation — owasp.org/Top10*
