# Security Intelligence Wiki
A knowledge base maintained by AI (Gemini / Claude Code).
Based on Andrej Karpathy's LLM Wiki pattern — adapted for offensive security research and pentest operations.

## Purpose
This wiki is a structured, interlinked knowledge base for cybersecurity knowledge, vulnerability research, pentest findings, and client intelligence. Gemini maintains the wiki. The human (Lead Pentester / Knowledge Manager) curates sources, asks questions, and approves all sensitive entries.

---

## Folder structure

```
raw/                  -- source documents (immutable -- never modify these)
  cve/                -- CVE reports, NVD exports, vendor advisories
  scan-outputs/       -- raw tool output (nmap, burp, hackingtool logs)
  client-briefs/      -- engagement scope documents, rules of engagement
  research/           -- OnionClaw exports, threat intel feeds, papers

wiki/                 -- markdown pages maintained by AI
  index.md            -- table of contents for the entire wiki
  log.md              -- append-only record of all operations
  ttps/               -- Tactics, Techniques, Procedures per category
  vulns/              -- vulnerability concept pages
  tools/              -- tool usage notes and findings
  clients/            -- per-client engagement summaries (anonymized)
  advisories/         -- drafted client notifications and disclosures
```

---

## Ingest workflow

When the user adds a new source to `raw/` and asks you to ingest it:

1. Read the full source document
2. Identify: vulnerability class, affected systems, severity, CVE ID (if any), recommended fix
3. Discuss key takeaways with the user **before writing anything**
4. Create or update a page in the appropriate `wiki/` subfolder
5. Create or update concept pages for each vulnerability class or TTP involved
6. Add wiki-links `[[page-name]]` to connect related findings, tools, and CVEs
7. Update `wiki/index.md` with new pages and one-line descriptions
8. Append an entry to `wiki/log.md` with: date, source name, severity tag, what changed

A single engagement or CVE report may touch 5–15 wiki pages. That is normal.

---

## Page format

Every wiki page must follow this structure:

```markdown
# Page Title

**Summary**: One to two sentences describing this vulnerability, TTP, or finding.

**Severity**: Critical / High / Medium / Low / Informational
**CVE**: CVE-YYYY-XXXXX (if applicable)
**CVSS Score**: X.X
**Affected systems**: e.g. Apache 2.4.x, Windows Server 2019
**Sources**: List of raw files this page draws from
**Last updated**: YYYY-MM-DD

---

Main content goes here. Use clear headings and short paragraphs.

Include:
- Vulnerability description and root cause
- Attack vector and conditions required
- Proof-of-concept notes (local/VM test only — never production)
- Detection indicators (log patterns, IOCs)
- Remediation steps with references
- Link to related TTPs using [[wiki-links]] throughout

## Tools used
- [[tool-name]] — what it found / how it was used

## Related pages
- [[related-vuln]]
- [[related-ttp]]
- [[related-cve]]

## Citation rules
- Every technical claim must reference its source file
- Use format: `(source: filename, section/line)` after the claim
- If two sources conflict, explicitly note the contradiction
- If a claim has no source, mark it: `[NEEDS VERIFICATION]`
- Never include client names in plain text — use client codes (e.g. CLIENT-001)
```

---

## Stream A — Vulnerability research (OnionClaw)

When the user ingests an OnionClaw export or threat intel feed:

1. Parse for: host, port, service, banner, known CVE matches
2. Cross-reference against `wiki/vulns/` for existing pages on the same CVE or vulnerability class
3. Score severity using CVSS v3.1
4. If finding is a potential zero-day (no CVE assigned):
   - Create a draft page in `wiki/advisories/` marked `[DRAFT — NOT DISCLOSED]`
   - Do **not** publish or share until human review is complete
   - Follow responsible disclosure workflow (see below)
5. Create or update the relevant `wiki/vulns/` page
6. Update `wiki/index.md` and `wiki/log.md`

### Responsible disclosure checklist (zero-day)
Before any client notification or public disclosure, confirm:
- [ ] Human lead has verified the finding manually
- [ ] Affected vendor / system owner has been notified privately
- [ ] Minimum 90-day remediation window has been offered
- [ ] Written authorization exists if the system is a client's asset
- [ ] Advisory draft reviewed and approved by human lead

---

## Stream B — Local VM testing (hackingtool)

When the user pastes scan output or tool logs from a local/VM test:

1. Parse tool output into structured findings (host, port, vuln, severity)
2. Map each finding to OWASP Top 10 category where applicable
3. Cross-reference `wiki/vulns/` for existing knowledge on the same class
4. Create a new page in `wiki/clients/CLIENT-XXX/` for this test session
5. Generate a pre-deploy checklist: findings sorted by severity with fix guidance
6. Update the relevant `wiki/tools/` page with any new usage notes

### Scope guard
Before processing any scan output, confirm with the user:
- Target is `localhost`, `127.0.0.1`, or a private IP inside a VM (`10.x`, `192.168.x`, `172.16-31.x`)
- If target IP is outside this range: **stop and ask for written authorization first**

---

## Question answering

When the user asks a technical or research question:

1. Read `wiki/index.md` first to find relevant pages
2. Read those pages and synthesize an answer
3. Cite specific wiki pages and source files in your response
4. Reference CVE IDs, CVSS scores, and tool names where applicable
5. If the answer is not in the wiki, say so clearly — do not hallucinate CVE details
6. If the answer adds new knowledge, offer to save it as a new wiki page

Good answers should be filed back into the wiki so knowledge compounds over time.

---

## Client advisory drafting

When the user asks to draft a client notification:

1. Read the relevant `wiki/clients/CLIENT-XXX/` and `wiki/advisories/` pages
2. Draft in plain language — assume the client is non-technical unless told otherwise
3. Structure: Executive Summary → Affected Systems → Risk → Recommended Actions → Timeline
4. Never include raw exploit code or proof-of-concept payloads in client-facing documents
5. Mark draft as `[AWAITING HUMAN APPROVAL]` until the lead signs off
6. After approval, move to `wiki/advisories/sent/` and log in `wiki/log.md`

---

## Lint / audit

When the user asks to lint or audit the wiki:

- Check for contradictions between findings or CVE interpretations
- Find orphan pages (no inbound links from other pages)
- Identify vulnerability classes mentioned but missing dedicated pages
- Flag CVEs where NVD severity differs from internal assessment — note the gap
- Check all pages follow the page format above
- Report findings as a numbered list with suggested fixes

---

## Paperclip agent integration

When Paperclip agents write to this wiki:

- Agent must include its agent ID in `wiki/log.md` entries: `[AGENT: project-manager-01]`
- Agents may **create and update** pages but may **not approve** advisories or disclosures
- All advisory pages created by agents carry `[AWAITING HUMAN APPROVAL]` until a human removes it
- Agents must never write to `raw/` or `wiki/advisories/sent/`

---

## Rules

- Never modify anything in `raw/`
- Always update `wiki/index.md` and `wiki/log.md` after any change
- Keep page names lowercase with hyphens: `sql-injection.md`, `client-001-session-01.md`
- Write in clear, plain language — avoid jargon without definition
- Never store real client names, employee names, or PII in plain text — use client codes
- Scope guard applies at all times: only process scan output from authorized targets
- When uncertain about a finding's severity or scope, ask the human before writing
- AI provides informational intelligence only — human lead makes all final decisions

---

## Current Praedix Implementation Snapshot (2026-05-03)

Read `wiki/project-architecture.md` before making architectural changes.

Current application shape:

- `frontend/` is a React + Vite dashboard.
- `api/` is a Flask API that orchestrates AI scans.
- `api/db.py` is the Postgres persistence layer.
- `tools/hackingtool_wrapper.py` exposes local scanner tools.
- `tools/onionclaw_wrapper.py` exposes a gated OnionClaw/Tor research runtime.
- `praedix_cli.py` and `praedix.cmd` expose a PowerShell-friendly terminal client.
- `vault/` remains the Obsidian-style knowledge base and report archive.
- `wiki/` is the maintained security intelligence wiki.

Postgres is now intended to be the structured source of truth for:

- `targets`
- `scans`
- `tool_runs`
- `reports`
- `findings`
- `target_memory`

Obsidian/Markdown remains the human-readable memory for:

- OWASP knowledge
- research notes
- client-facing reports
- wiki pages
- human-curated summaries

The scan workflow now includes:

- `stream_type`: `local_vm` or `research`
- `workflow_status`: current stage such as `local_scan`, `recon_and_triage`, `pre_deploy_report`, or `awaiting_human_review`
- `research_scope`: approved keyword/scope settings for Stream A
- `scope_approved`: boolean gate for sensitive research

OnionClaw must stay isolated and gated:

- OnionClaw is optional. Only run it when the user explicitly enables dark web / OSINT search.
- Do not allow arbitrary shell command execution for OnionClaw.
- Require human-approved scope before research actions.
- Require `allow_onion_fetch=true` before fetching `.onion` URLs.
- Require `allow_identity_rotation=true` before Tor identity rotation.
- Keep client notification/advisory output behind human approval.

CLI usage:

```powershell
.\praedix.cmd --status
.\praedix.cmd -u dvwa
.\praedix.cmd -u scanme.nmap.org -v
.\praedix.cmd -u scanme.nmap.org -v --report-preview
.\praedix.cmd -u ginandjuice.shop --stream research
.\praedix.cmd -u ginandjuice.shop --stream research --dark-web --keywords "ginandjuice.shop,Gin and Juice" --approved-by acer
```

The CLI talks to the Flask API and polls `/api/scan/<scan_id>`. It normalizes full URLs to hostnames before starting scans. By default, completed scans print only `[+] Scan complete` and `Report file: ...`; use `--report-preview` when the user explicitly wants the report text in the terminal.

Target validation is enforced in both `praedix_cli.py` and `api/app.py`:

- Unknown single-label targets are rejected.
- Default allowed single-label aliases are `dvwa` and `localhost`.
- This prevents inputs like `porn` from being treated as the `.porn` TLD and drifting into registry infrastructure scans.
- Public targets must be full hostnames such as `example.com`; local Docker aliases can be added through `PRAEDIX_ALLOWED_SINGLE_LABEL_TARGETS`.

The default editable terminal banner is `assets/banner.txt`; users can draw their own ASCII/ANSI art there, pass `--banner path\to\file.txt`, or generate it from an image with `make-banner.cmd`. `praedix_cli.py` supports UTF-8 and UTF-16 banner files because PowerShell `>` redirection can write UTF-16. ANSI color banner files are supported; `--no-color` strips ANSI codes.

ASCII image tooling:

```powershell
.\ascii-image-converter.cmd -h
.\ascii-image-converter.cmd "C:\path\to\image.jpg" -W 90 --complex
.\make-banner.cmd "C:\path\to\image.jpg" 90
```

The installed binary is at `C:\Users\acer\go\bin\ascii-image-converter.exe`; the project wrappers avoid requiring a PATH update. The current `assets/banner.txt` was generated from the user's local `C:\Users\acer\Downloads\MJ-m1.png`.

Next recommended scanner expansion for web app audits:

- Add `nuclei`, `katana`, `ffuf` or `feroxbuster`, `httpx`, `subfinder`, `arjun`, `dalfox`, `whatweb`, and `testssl.sh`.
- Keep the scanner allowlist strict.
- Avoid risky hackingtool categories such as DDoS, phishing, RAT, payload generation, wireless attacks, and post-exploitation.

Last verified:

```powershell
python -m py_compile api\app.py api\db.py tools\onionclaw_wrapper.py
npm.cmd run build
docker compose config
```

As of 2026-05-04, API/frontend were rebuilt and recreated after the optional OnionClaw UI/API update. `GET /api/status` returned database/scanner/OnionClaw online and `onionclaw_installed=true`.

As of 2026-05-05, the CLI was added and verified with:

```powershell
python -m py_compile praedix_cli.py
.\praedix.cmd --help
.\praedix.cmd --status
.\ascii-image-converter.cmd -h
```

The status output used the editable `assets/banner.txt` banner successfully, and the ASCII image converter wrapper printed help successfully.

Also on 2026-05-05:

- User generated a colored ASCII banner from `C:\Users\acer\Downloads\MJ-m1.png` at width 80.
- Fixed CLI banner decoding after PowerShell created a UTF-16 `assets/banner.txt`.
- Added ANSI stripping for `--no-color`.
- User ran a real CLI scan against `scanme.nmap.org`; it completed and produced `2026-05-04_18-43-49_scanme.nmap.org.md`.
- Changed CLI default so completed scans do not print long report previews; `--report-preview` is now opt-in.
- Added target validation after the user tested `porn` and the scanner followed WHOIS/DNS into `.porn` registry infrastructure.
- Force-recreated the API container so backend validation took effect.
- Marked two validation test scans (`1776aebe`, `5e6908cc`) as `error / aborted_by_api_restart` because API recreate orphaned their scan threads. `GET /api/status` then showed `active_scans: 0`.

Resume with:

```powershell
docker compose up -d
```
