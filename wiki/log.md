# Wiki Operations Log

All changes to the wiki are recorded here for transparency and continuity.

| Date | Source / Action | Severity | Agent | Changes |
| :--- | :--- | :--- | :--- | :--- |
| 2026-05-02 | Ingest: Copy Fail Clipping | Critical | Gemini-CLI | Initialized wiki, created CVE-2026-31431, LPE-Linux-Kernel-Crypto. |
| 2026-05-02 | Migration: OWASP Top 10 | Info | Gemini-CLI | Migrated and refactored 10 OWASP files from vault to wiki/ttps. |
| 2026-05-03 | Architecture snapshot | Info | Codex | Added project-architecture page covering hybrid Postgres/Obsidian memory, stream_type/workflow_status, and OnionClaw isolated runtime plan. |
| 2026-05-04 | Research workflow update | Info | Codex | Made OnionClaw dark web / OSINT optional in Vulnerability Research, rebuilt API/frontend, verified OnionClaw online, and identified next web app DAST tools to add. |
| 2026-05-05 | CLI terminal client | Info | Codex | Added `praedix_cli.py` and `praedix.cmd` so Praedix scans can be started and monitored from PowerShell with banner, status panel, progress, and report preview. |
| 2026-05-05 | Editable CLI banner | Info | Codex | Added `assets/banner.txt` and CLI `--banner` / `--no-banner` options so the terminal header can be hand-drawn without editing Python code. |
| 2026-05-05 | ASCII image converter | Info | Codex | Installed `github.com/TheZoraiz/ascii-image-converter` with Go and added project wrappers `ascii-image-converter.cmd` and `make-banner.cmd` for converting images into CLI banner text. |
| 2026-05-05 | CLI polish and scan test | Info | Codex | Fixed UTF-16/ANSI banner handling, verified colored MJ ASCII banner output, completed a CLI scan of `scanme.nmap.org`, and changed final CLI output to show only completion plus report filename unless `--report-preview` is used. |
| 2026-05-05 | Target validation guard | Info | Codex | Added CLI/API validation that blocks unknown single-label targets like `porn`, allows `dvwa`/`localhost`, force-recreated the API container, and cleaned orphaned validation scan records. |
