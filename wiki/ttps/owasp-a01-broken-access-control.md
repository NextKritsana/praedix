# A01:2021 – Broken Access Control

**Summary**: Failures that allow users to act outside of their intended permissions, leading to unauthorized information disclosure or data modification.

**Severity**: High
**CVE**: N/A
**CVSS Score**: 8.1 (Estimated average)
**Affected systems**: Web application authorization modules, APIs
**Sources**: OWASP_A01_Broken_Access_Control.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification, or destruction of all data. (source: OWASP_A01_Broken_Access_Control.md)

### Common Vulnerabilities:
- Violation of the principle of least privilege or deny by default
- Bypassing access control checks by modifying the URL (parameter tampering or force browsing)
- Permitting viewing or editing someone else's account (Insecure Direct Object References - IDOR)
- Accessing API with missing access controls for POST, PUT and DELETE
- Elevation of privilege (acting as admin when logged in as a user)
- Metadata manipulation (replaying or tampering with JWT tokens, cookies, or hidden fields)
- CORS misconfiguration allows API access from unauthorized/untrusted origins

## Attack Vector and Conditions
Attackers typically manipulate parameters, headers, or URL structures to bypass authorization logic. This often requires an authenticated session, though some failures allow unauthenticated access to restricted pages.

### Example Attack Scenarios
- **IDOR**: `https://example.com/app/accountInfo?acct=notmyacct` (source: OWASP_A01_Broken_Access_Control.md, line 43)
- **Force Browsing**: Accessing `admin_getappInfo` without admin rights.

## Detection Indicators
- Multiple 403 Forbidden errors followed by a 200 OK for a restricted resource
- Unauthorized access logged in application logs (if logging is implemented)
- Unexpected changes to data records by unauthorized users

## Remediation Steps
- Deny by default except for public resources
- Implement access control mechanisms once and re-use throughout the application
- Model access controls should enforce record ownership
- Disable web server directory listing
- Log access control failures and alert admins

## Tools used
- [[dirb]] — discover hidden admin pages
- [[nikto]] — scan for misconfigurations
- [[sqlmap]] — test for IDOR via SQL injection

## Related pages
- [[owasp-top-10]]
- [[owasp-a03-injection]]
- [[owasp-a07-auth-failures]]
