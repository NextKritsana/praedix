# A08:2021 – Software and Data Integrity Failures

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/)

## Overview
A new category for 2021. Focuses on making assumptions related to software updates, critical data, and CI/CD pipelines without verifying integrity. CWE-502 (Deserialization of Untrusted Data) is a notable CWE.

## Description
Software and data integrity failures relate to code and infrastructure that does not protect against integrity violations. Examples include:
- Applications that rely on plugins, libraries, or modules from untrusted sources, repositories, and CDNs
- An insecure CI/CD pipeline that introduces the potential for unauthorized access, malicious code, or system compromise
- Auto-update functionality that downloads and applies updates without sufficient integrity verification
- Insecure deserialization where objects or data are encoded/serialized in a way that an attacker can see and modify

### Common Vulnerabilities:
- Using libraries from untrusted CDNs without integrity checks (Subresource Integrity - SRI)
- Insecure deserialization leading to remote code execution
- CI/CD pipeline without proper access controls or code signing
- Auto-updates without digital signatures

## How to Detect (Pentest Approach)
- Check if external scripts/libraries use Subresource Integrity (SRI) hashes
- Look for deserialization endpoints
- Check for unsigned software update mechanisms
- Review CI/CD pipeline configurations for security

### Tools to Use:
- `nikto` — identify potential deserialization vulnerabilities
- Manual source code review for `serialize()`/`deserialize()` calls
- Check `<script>` tags for SRI attributes in page source

## How to Prevent
- Use digital signatures or similar mechanisms to verify the software or data is from the expected source
- Ensure libraries and dependencies are consuming trusted repositories
- Use a software supply chain security tool like OWASP Dependency Check or OWASP CycloneDX
- Ensure there is a review process for code and configuration changes
- Ensure your CI/CD pipeline has proper segregation, configuration, and access control
- Do not send unsigned or unencrypted serialized data to untrusted clients

## Related CWEs
- CWE-345: Insufficient Verification of Data Authenticity
- CWE-353: Missing Support for Integrity Check
- CWE-426: Untrusted Search Path
- CWE-502: Deserialization of Untrusted Data

---
*Source: OWASP Foundation — owasp.org/Top10*
