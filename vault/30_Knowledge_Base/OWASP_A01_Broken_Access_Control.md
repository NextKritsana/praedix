# A01:2021 – Broken Access Control

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)

## Overview
Moving up from the fifth position, 94% of applications were tested for some form of broken access control with the average incidence rate of 3.81%, and has the most occurrences in the contributed dataset with over 318k. Notable CWEs included are CWE-200 (Exposure of Sensitive Information), CWE-201 (Insertion of Sensitive Information Into Sent Data), and CWE-352 (Cross-Site Request Forgery).

## Description
Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification, or destruction of all data.

### Common Vulnerabilities:
- Violation of the principle of least privilege or deny by default
- Bypassing access control checks by modifying the URL (parameter tampering or force browsing)
- Permitting viewing or editing someone else's account (Insecure Direct Object References - IDOR)
- Accessing API with missing access controls for POST, PUT and DELETE
- Elevation of privilege (acting as admin when logged in as a user)
- Metadata manipulation (replaying or tampering with JWT tokens, cookies, or hidden fields)
- CORS misconfiguration allows API access from unauthorized/untrusted origins
- Force browsing to authenticated pages as an unauthenticated user

## How to Detect (Pentest Approach)
- Try accessing admin pages/APIs without authentication
- Modify URL parameters (e.g., `?user_id=2` to `?user_id=1`)
- Test HTTP methods: change GET to PUT/DELETE
- Check for missing authorization headers
- Test JWT token manipulation
- Check CORS headers with: `curl -H "Origin: http://evil.com" -v <target>`

### Tools to Use:
- `dirb` or `dirsearch` — discover hidden admin pages
- `nikto` — scan for misconfigurations
- `sqlmap` — test for IDOR via SQL injection
- Burp Suite (manual) — intercept and modify requests

## How to Prevent
- Except for public resources, deny by default
- Implement access control mechanisms once and re-use throughout the application
- Model access controls should enforce record ownership
- Disable web server directory listing and ensure file metadata (.git) are not present
- Log access control failures, alert admins when appropriate
- Rate limit API and controller access
- Stateful session identifiers should be invalidated on the server after logout
- Stateless JWT tokens should be short-lived

## Example Attack Scenarios

### Scenario 1: IDOR
```
https://example.com/app/accountInfo?acct=notmyacct
```
An attacker modifies the `acct` parameter to access any user's account.

### Scenario 2: Force Browsing
```
https://example.com/app/getappInfo
https://example.com/app/admin_getappInfo  ← requires admin rights
```
If an unauthenticated user can access either page, it's a flaw.

## Related CWEs
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
- CWE-201: Insertion of Sensitive Information Into Sent Data
- CWE-352: Cross-Site Request Forgery

---
*Source: OWASP Foundation — owasp.org/Top10*
