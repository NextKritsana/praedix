# A09:2021 – Security Logging and Monitoring Failures

**Summary**: Failures to log, monitor, and alert on security-critical events, which prevents the detection and timely response to active breaches.

**Severity**: Medium
**CVE**: N/A
**CVSS Score**: N/A (Impact-dependent)
**Affected systems**: Logging infrastructure, SIEM, Incident response systems
**Sources**: OWASP_A09_Logging_Monitoring_Failures.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
Security logging and monitoring failures occur when auditable events (logins, failed attempts, high-value transactions) are not recorded, or when logs are not monitored for suspicious activity. Without effective logging, breaches can go undetected for long periods. (source: OWASP_A09_Logging_Monitoring_Failures.md)

### Common Vulnerabilities:
- Auditable events not logged (e.g., failed login attempts)
- Logs stored only locally (at risk of deletion by attackers)
- No alerting thresholds or response escalation procedures
- Penetration testing or active attacks do not trigger any alerts

## Attack Vector and Conditions
Attackers benefit from the absence of logging by remaining undetected as they perform reconnaissance, lateral movement, and data exfiltration. They may also attempt to clear local logs to hide their tracks.

## Detection Indicators
- Performing a simulated attack (e.g., brute force) does not appear in monitoring dashboards
- Log files are missing entries for critical security events
- Publicly exposed log or debug files containing sensitive info

## Remediation Steps
- Log all authentication, access control, and input validation failures
- Ensure logs are generated in a format that can be easily consumed by log management solutions
- Use centralized log management (e.g., ELK Stack, Splunk)
- Establish an incident response and recovery plan (e.g., NIST 800-61r2)

## Tools used
- [[dirb]] — discover exposed log or debug files (e.g., `/logs`, `/debug`)
- [[nikto]] — identify debug/log pages

## Related pages
- [[owasp-top-10]]
- [[owasp-a04-insecure-design]]
- [[owasp-a01-broken-access-control]]
