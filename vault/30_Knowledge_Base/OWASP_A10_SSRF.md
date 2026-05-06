# A10:2021 – Server-Side Request Forgery (SSRF)

> Source: [OWASP Top 10 (2021)](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/)

## Overview
New category added from the community survey (#1). SSRF flaws occur whenever a web application fetches a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination.

## Description
SSRF flaws occur when an attacker can make the server-side application make HTTP requests to an arbitrary domain of the attacker's choosing. The attacker can:
- Access internal services behind the firewall
- Scan internal ports
- Read local files via `file://` protocol
- Access cloud metadata services (e.g., AWS `http://169.254.169.254`)

## Common Vulnerabilities
- URL parameter fetching without validation: `?url=http://internal-server`
- PDF generators or image processors fetching external URLs
- Webhook configurations allowing arbitrary URLs
- Import from URL features

## How to Detect (Pentest Approach)
- Test URL parameters: `?url=http://127.0.0.1:22`
- Try accessing cloud metadata: `?url=http://169.254.169.254/latest/meta-data/`
- Test file protocol: `?url=file:///etc/passwd`
- Check for open redirect chains leading to SSRF

### Common SSRF Payloads:
```
http://127.0.0.1
http://localhost
http://169.254.169.254/latest/meta-data/  (AWS)
http://metadata.google.internal/  (GCP)
file:///etc/passwd
http://[::1]  (IPv6 localhost)
```

## How to Prevent
- Sanitize and validate all client-supplied input data
- Enforce URL schema, port, and destination with a positive allow list
- Disable HTTP redirections
- Do not send raw responses to clients
- Use network segmentation to limit SSRF impact

## Related CWEs
- CWE-918: Server-Side Request Forgery (SSRF)

---
*Source: OWASP Foundation — owasp.org/Top10*
