# A10:2021 – Server-Side Request Forgery (SSRF)

**Summary**: Vulnerabilities that occur when a web application fetches a remote resource without validating the user-supplied URL, allowing an attacker to coerce the application to send crafted requests.

**Severity**: High
**CVE**: N/A
**CVSS Score**: 8.3 (Estimated average)
**Affected systems**: Web applications with URL-fetching features, Cloud metadata services
**Sources**: OWASP_A10_SSRF.md
**Last updated**: 2026-05-02

---

## Vulnerability Description
SSRF flaws allow an attacker to make the server-side application send HTTP requests to an arbitrary domain. This can be used to access internal services behind a firewall, scan internal ports, or access cloud metadata. (source: OWASP_A10_SSRF.md)

### Common Vulnerabilities:
- URL parameter fetching without validation (e.g., `?url=http://internal`)
- PDF generators or image processors fetching external URLs
- Webhook configurations allowing arbitrary destination URLs
- Import-from-URL features

## Attack Vector and Conditions
Attackers provide internal or restricted URLs (e.g., `127.0.0.1`, `169.254.169.254`) as input to features that fetch remote resources. The server, trusting its own internal network, fetches the resource and often returns the content to the attacker.

### Common Payloads
- **AWS Metadata**: `http://169.254.169.254/latest/meta-data/` (source: OWASP_A10_SSRF.md, line 23)
- **Local File**: `file:///etc/passwd`
- **Internal Service**: `http://127.0.0.1:22`

## Detection Indicators
- Application takes a long time to respond when a non-existent internal IP is provided (timeout)
- Response content includes internal service banners or cloud metadata
- Unusual outbound traffic from the application server to internal network ranges

## Remediation Steps
- Sanitize and validate all client-supplied input data
- Enforce a positive allow-list for URL schemas, ports, and destinations
- Disable HTTP redirections in the library used for fetching
- Use network segmentation to limit the application's access to internal services

## Tools used
- Manual testing with Burp Suite (repeater/intruder)
- [[nikto]] — can identify some SSRF-prone parameters

## Related pages
- [[owasp-top-10]]
- [[owasp-a03-injection]]
- [[owasp-a01-broken-access-control]]
