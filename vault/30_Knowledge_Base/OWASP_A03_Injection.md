# A03:2021 – Injection

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A03_2021-Injection/)

## Overview
94% of the applications were tested for some form of injection with a max incidence rate of 19%, an average incidence rate of 3%, and 274k occurrences. Notable CWEs: CWE-79 (Cross-site Scripting), CWE-89 (SQL Injection), CWE-73 (External Control of File Name or Path).

## Description
An application is vulnerable to injection when:
- User-supplied data is not validated, filtered, or sanitized
- Dynamic queries or non-parameterized calls are used directly in the interpreter
- Hostile data is used within ORM search parameters
- Hostile data is directly used or concatenated in SQL queries, commands, or stored procedures

### Types of Injection:
- **SQL Injection** — manipulate database queries
- **NoSQL Injection** — target MongoDB, CouchDB, etc.
- **OS Command Injection** — execute system commands
- **LDAP Injection** — manipulate directory queries
- **XSS (Cross-Site Scripting)** — inject client-side scripts
- **ORM Injection** — exploit object-relational mapping
- **Expression Language (EL) Injection**
- **OGNL Injection**

## How to Detect (Pentest Approach)
- Test all input fields with SQL injection payloads: `' OR 1=1--`
- Test URL parameters: `?id=1' UNION SELECT null,null--`
- Test for XSS: `<script>alert('XSS')</script>`
- Test for command injection: `; ls -la` or `| cat /etc/passwd`
- Check for error messages exposing database info

### Tools to Use:
- `sqlmap -u "http://target/page?id=1" --dbs` — automated SQL injection
- `nikto` — web vulnerability scanner
- `nmap --script http-sql-injection` — basic SQL injection detection

### Common SQL Injection Payloads:
```
' OR '1'='1
' UNION SELECT null,null,null--
'; DROP TABLE users;--
' AND 1=1--
' AND 1=2--
```

### Common XSS Payloads:
```html
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg/onload=alert('XSS')>
javascript:alert('XSS')
```

## How to Prevent
- Use a safe API with parameterized interface or ORM tools
- Use positive server-side input validation
- Escape special characters using interpreter-specific escape syntax
- Use LIMIT and other SQL controls to prevent mass disclosure in case of SQL injection
- Automated testing of all parameters, headers, URL, cookies, JSON, SOAP, and XML data inputs

## Example Attack Scenarios

### Scenario 1: SQL Injection
```
String query = "SELECT * FROM accounts WHERE custID='" + request.getParameter("id") + "'";
```
Attacker sends: `' UNION SELECT SLEEP(10);--`

### Scenario 2: HQL Injection
```java
Query HQLQuery = session.createQuery("FROM accounts WHERE custID='" + request.getParameter("id") + "'");
```

## Related CWEs
- CWE-79: Cross-site Scripting (XSS)
- CWE-89: SQL Injection
- CWE-73: External Control of File Name or Path

---
*Source: OWASP Foundation — owasp.org/Top10*
