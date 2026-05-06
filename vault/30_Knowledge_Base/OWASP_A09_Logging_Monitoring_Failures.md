# A09:2021 – Security Logging and Monitoring Failures

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)

## Overview
Without logging and monitoring, breaches cannot be detected. Notable CWEs: CWE-778, CWE-117, CWE-223.

## Common Vulnerabilities
- Auditable events not logged (logins, failed logins)
- Logs only stored locally
- No alerting thresholds or response escalation
- Penetration testing does not trigger alerts

## How to Detect
- Perform brute force and check if target detects/blocks it
- Look for exposed log files: `dirb http://target` (search /logs, /debug)
- `nikto` to identify debug/log pages

## How to Prevent
- Log all login, access control, and input validation failures
- Use log management solutions (ELK Stack, Splunk)
- Establish incident response plan (NIST 800-61r2)

## Related CWEs
- CWE-117, CWE-223, CWE-532, CWE-778

---
*Source: OWASP Foundation — owasp.org/Top10*
