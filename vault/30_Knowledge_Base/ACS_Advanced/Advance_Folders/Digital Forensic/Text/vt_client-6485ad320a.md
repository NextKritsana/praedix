---
title: "vt_client"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\vt_client.py"
source_size_bytes: 2792
source_modified: 2025-11-23T15:00:44
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# vt_client

- Source: [vt_client.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/vt_client.py)

## Content

```py
# /vt_client.py (ไฟล์ใหม่)
import requests
import os
import time
from dotenv import load_dotenv

# โหลด .env เพื่อดึง API Key
load_dotenv()

VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
VT_API_URL = "https://www.virustotal.com/api/v3"

# จัดการ Rate Limit (4 requests/นาที)
LAST_CALL_TIME = 0

def _wait_for_rate_limit():
    global LAST_CALL_TIME
    elapsed = time.time() - LAST_CALL_TIME
    if elapsed < 16: # (รอ 16 วินาที)
        wait_time = 16 - elapsed
        print(f"[VT Client] Rate limit: Waiting {wait_time:.2f} seconds...")
        time.sleep(wait_time)
    LAST_CALL_TIME = time.time()

def _parse_vt_response(attributes: dict) -> tuple[dict, str]:
    stats = attributes.get("last_analysis_stats", {})
    malicious = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)
    
    summary = f"VT Scan: {malicious} malicious, {suspicious} suspicious."
    
    result_data = {
        "malicious": malicious,
        "suspicious": suspicious,
        "harmless": stats.get("harmless", 0),
        "undetected": stats.get("undetected", 0)
    }
    return result_data, summary

def scan_hash(file_hash: str) -> tuple[dict, str]:
    if not VT_API_KEY:
        print("[VT Error] VIRUSTOTAL_API_KEY not set. Skipping.")
        return {"error": "VT_API_KEY not set"}, "VirusTotal API key is missing."
    
    _wait_for_rate_limit()
    print(f"[VT Client] Scanning Hash: {file_hash[:10]}...")
    url = f"{VT_API_URL}/files/{file_hash}"
    headers = {"x-apikey": VT_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return {}, "Hash not found in VirusTotal."
        response.raise_for_status()
        data = response.json().get("data", {}).get("attributes", {})
        return _parse_vt_response(data)
    except requests.RequestException as e:
        print(f"[VT Error] Hash scan failed: {e}")
        return {"error": str(e)}, "VT API request failed."

def scan_domain(domain: str) -> tuple[dict, str]:
    if not VT_API_KEY:
        print("[VT Error] VIRUSTOTAL_API_KEY not set. Skipping.")
        return {"error": "VT_API_KEY not set"}, "VirusTotal API key is missing."

    _wait_for_rate_limit()
    print(f"[VT Client] Scanning Domain: {domain}...")
    url = f"{VT_API_URL}/domains/{domain}"
    headers = {"x-apikey": VT_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get("data", {}).get("attributes", {})
        return _parse_vt_response(data)
    except requests.RequestException as e:
        print(f"[VT Error] Domain scan failed: {e}")
        return {"error": str(e)}, "VT API request failed."
```
