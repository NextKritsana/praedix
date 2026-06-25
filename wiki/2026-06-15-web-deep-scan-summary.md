# Praedix Work Summary - 2026-06-15

## Scope

This note summarizes the recent Praedix updates around the Obsidian knowledge base, MITRE playbooks, scanner tooling, and the new Web App Deep Scan profile.

## Knowledge Base Updates

- Imported ACS PDF/course material into the Obsidian vault under `vault/30_Knowledge_Base/ACS_Advanced`.
- Imported the remaining ACS advanced folders:
  - Digital Forensic
  - Incident Response
  - Malware DevAnalysis
  - Real-world System Exploitation
  - Real-world Web Exploitation
- Added reusable import scripts:
  - `tools/import_acs_pdfs_to_obsidian.py`
  - `tools/import_acs_advance_folders_to_obsidian.py`
- Added agent playbooks at the root of `vault/30_Knowledge_Base` so the current knowledge loader can see them:
  - `ACS_Agent_Playbook_Web_Exploitation.md`
  - `ACS_Agent_Playbook_Incident_Response.md`
  - `ACS_Agent_Playbook_Malware_Analysis.md`
  - `ACS_Agent_Playbook_Digital_Forensics.md`
  - `ACS_Agent_Playbook_System_Exploitation.md`
- Added MITRE guidance notes:
  - `MITRE_ATLAS_AI_Security_Playbook.md`
  - `MITRE_ATTACK_Enterprise_Playbook.md`

## Scanner Tooling Updates

- Added modern web reconnaissance and DAST tools to the scanner image:
  - `nuclei`
  - `httpx`
  - `katana`
  - `ffuf`
  - `subfinder`
- Updated `tools/hackingtool_wrapper.py` so the scanner API allowlist accepts those tools.
- Added per-tool timeouts so long-running tools do not block indefinitely.
- Used Kali packages for `nuclei`, `httpx-toolkit`, `ffuf`, and `subfinder`.
- Installed `katana` through Go with a build timeout.
- Moved Flask installation for the scanner wrapper to pip to avoid a Kali mirror failure during Docker build.

## Web App Deep Scan Profile

- Added scan profile support in the API:
  - `standard`
  - `web_deep`
- `web_deep` increases the scan budget from 15 to 24 AI/tool steps.
- The agent prompt now tells the AI to use the modern web stack during deep web scans:
  - `subfinder` for public-domain subdomain discovery
  - `httpx` for live web service probing and tech detection
  - `katana` for crawling
  - `ffuf` for controlled content discovery
  - `nuclei` for rate-limited template-based vulnerability checks
- The prompt also tells the AI to avoid shell pipes, redirects, and chained commands because the scanner runs one executable command at a time.
- Final reports are instructed to map findings to OWASP Top 10 and relevant MITRE ATT&CK techniques when evidence supports it.

## Persistence and API Changes

- Added `scan_profile` to scan creation and validation.
- Added `scan_profile` to database schema/migration.
- Added `scan_profile` to DB formatting so scan status responses include the selected profile.
- Fixed migration ordering so existing databases add the column before creating the profile index.

## UI and CLI Changes

- Added a Scan profile selector to the New Scan page.
- Added profile display badges to scan progress.
- Added profile visibility to active scans on the Dashboard.
- Added a Modern Web Recon category to the Tools page.
- Added CLI support:
  - `--profile standard`
  - `--profile web_deep`

Example:

```powershell
python praedix_cli.py -u dvwa --profile web_deep
```

## Runtime Verification

- Python syntax checks passed for API, DB, scanner wrapper, and CLI.
- Frontend production build passed with `npm run build`.
- Docker services were rebuilt and restarted.
- `scan-runner`, `api`, and `frontend` containers were recreated as needed.
- `/api/status` reported:
  - API online
  - scanner online
  - database online
  - OnionClaw online
- Confirmed scanner API allowlist includes:
  - `nuclei`
  - `httpx`
  - `katana`
  - `ffuf`
  - `subfinder`
- Confirmed tool execution through `/api/tool/run`:
  - `nuclei -version`
  - `httpx -version`
  - `katana -version`
  - `ffuf -V`
  - `subfinder -version`

## Current Status

The system can now run the new Web App Deep Scan profile from the web UI or CLI. The profile gives the AI more tool coverage for real web application reconnaissance and vulnerability discovery than the previous standard scan path.

The web UI is available at:

```text
http://localhost:3000/scan
```

## Notes

- The in-app browser verification step could not be completed because the browser plugin failed while setting up its internal assets.
- Verification was completed through frontend build checks, Docker container status, API health checks, and direct scanner API tool execution.
