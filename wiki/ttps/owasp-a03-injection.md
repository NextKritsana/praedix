# A03:2021 – Injection

**Summary**: Vulnerabilities that occur when an application sends untrusted data to an interpreter as part of a command or query, leading to unauthorized data access or command execution.

**Severity**: Critical
**CVE**: N/A
**CVSS Score**: 9.8 (Estimated average for RCE/SQLi)
**Affected systems**: Databases (SQL/NoSQL), OS Shells, LDAP directories, Web Browsers (XSS)
**Sources**: OWASP_A03_Injection.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Injection occurs when user-supplied data is not validated, filtered, or sanitized before being used in dynamic queries or commands. This allows attackers to manipulate the intended logic of the interpreter. (source: OWASP_A03_Injection.md)

### Types of Injection:
- **SQL Injection**: manipulate database queries
- **OS Command Injection**: execute system commands
- **XSS (Cross-Site Scripting)**: inject client-side scripts
- **NoSQL, LDAP, and ORM Injection**

## Attack Vector and Conditions
Attackers supply specially crafted input (payloads) via URL parameters, form fields, or headers. If the application concatenates this input directly into a query or command string, the injection is successful.

### Common Payloads
- **SQLi**: `' OR '1'='1` (source: OWASP_A03_Injection.md, line 31)
- **XSS**: `<script>alert('XSS')</script>` (source: OWASP_A03_Injection.md, line 38)
- **Command Injection**: `; ls -la`

## Detection Indicators
- Unexpected database errors or stack traces
- Application behavior changes based on input (e.g., returning more records than expected)
- JavaScript execution in the browser when viewing user-supplied content

## Remediation Steps
- Use parameterized interfaces (Prepared Statements) or ORMs
- Implement positive server-side input validation (allow-listing)
- Escape special characters using interpreter-specific syntax
- Use LIMIT in SQL queries to prevent mass data disclosure

## Tools used
- [[sqlmap]] — automated SQL injection testing
- [[nikto]] — web vulnerability scanner
- [[nmap]] — `http-sql-injection` script

## Related pages
- [[owasp-top-10]]
- [[owasp-a01-broken-access-control]]
- [[owasp-a10-ssrf]]
