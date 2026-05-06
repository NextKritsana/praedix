# A04:2021 – Insecure Design

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A04_2021-Insecure_Design/)

## Overview
A new category for 2021. Insecure design is a broad category representing different weaknesses expressed as "missing or ineffective control design." This is not the source for all other Top 10 risk categories. There is a difference between insecure design and insecure implementation.

## Description
Insecure design focuses on risks related to design and architectural flaws. It calls for more use of threat modeling, secure design patterns, and reference architectures. An insecure design cannot be fixed by a perfect implementation; by definition, the needed security controls were never created to defend against specific attacks.

### Common Vulnerabilities:
- No rate limiting on sensitive operations (login, password reset)
- Business logic flaws (e.g., buying items at negative prices)
- Missing anti-automation controls
- Lack of tenant isolation in multi-tenant systems
- Overly informative error messages
- Missing security questions or weak recovery mechanisms
- Trust boundaries not properly defined

## How to Detect (Pentest Approach)
- Test for missing rate limiting on login pages
- Test business logic: can you order negative quantities?
- Check if password reset tokens are predictable
- Test for missing CAPTCHA on forms
- Check if error messages reveal internal system info

### Tools to Use:
- `nikto` — find design-level misconfigurations
- Manual testing with Burp Suite for business logic flaws
- `nmap` — identify unnecessary exposed services

## How to Prevent
- Establish and use a secure development lifecycle with AppSec professionals
- Use threat modeling for critical authentication, access control, business logic, and key flows
- Write unit and integration tests to validate all critical flows
- Segregate tier layers on the system and network layers
- Limit resource consumption by user or service

## Related CWEs
- CWE-209: Generation of Error Message Containing Sensitive Information
- CWE-256: Plaintext Storage of a Password
- CWE-501: Trust Boundary Violation
- CWE-522: Insufficiently Protected Credentials

---
*Source: OWASP Foundation — owasp.org/Top10*
