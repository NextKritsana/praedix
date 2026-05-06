# A08:2021 – Software and Data Integrity Failures

**Summary**: Failures related to code and infrastructure that do not protect against integrity violations, such as using untrusted plugins or insecure CI/CD pipelines.

**Severity**: High
**CVE**: CVE-2021-44228 (Log4j), CWE-502
**CVSS Score**: 8.8 (Estimated average)
**Affected systems**: CI/CD pipelines, Update mechanisms, Deserialization modules
**Sources**: OWASP_A08_Software_Data_Integrity.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
This category focuses on making assumptions about software updates, critical data, and CI/CD pipelines without verifying their integrity. It includes vulnerabilities like insecure deserialization. (source: OWASP_A08_Software_Data_Integrity.md)

### Common Vulnerabilities:
- Relying on plugins or libraries from untrusted CDNs without integrity checks (SRI)
- Insecure CI/CD pipelines allowing unauthorized code injection
- Auto-update functionality without sufficient integrity verification (digital signatures)
- Insecure deserialization allowing modification of objects or remote code execution

## Attack Vector and Conditions
Attackers may compromise a supply chain (e.g., a popular library) to distribute malicious code or exploit deserialization endpoints to execute arbitrary code on the server.

## Detection Indicators
- Unexpected code changes in the production environment
- Use of external scripts without `integrity` attributes (SRI) in HTML
- Application crashes or unusual behavior when processing serialized data

## Remediation Steps
- Use digital signatures to verify software and data sources
- Use trusted repositories for libraries and dependencies
- Implement software supply chain security tools (e.g., OWASP Dependency Check)
- Ensure CI/CD pipelines have proper access controls and review processes
- Avoid sending unsigned or unencrypted serialized data to untrusted clients

## Tools used
- [[nikto]] — identify potential deserialization vulnerabilities
- Manual source code review for `serialize()` and `deserialize()` calls

## Related pages
- [[owasp-top-10]]
- [[owasp-a06-vulnerable-and-outdated-components]]
- [[owasp-a03-injection]]
