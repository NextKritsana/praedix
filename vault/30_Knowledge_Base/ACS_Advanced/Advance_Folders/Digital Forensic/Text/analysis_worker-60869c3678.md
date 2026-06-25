---
title: "analysis_worker"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\analysis_worker.py"
source_size_bytes: 7401
source_modified: 2025-11-23T15:00:44
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# analysis_worker

- Source: [analysis_worker.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/analysis_worker.py)

## Content

```py
# /analysis_worker.py (ฉบับสมบูรณ์ - คัดลอกทับทั้งไฟล์)
import pyshark
import subprocess
import hashlib
import json
from pathlib import Path
from datetime import datetime
from scapy.all import rdpcap, DNS, DNSQR
# Worker ต้องเชื่อมต่อ DB เอง (เพราะรันใน Background)
import crud
import blockchain
import schemas
from database import SessionLocal # <--- (Worker ต้อง Import SessionLocal เอง)
import vt_client

# --- Helper Functions (สำหรับ Worker) ---

def get_db_session():
    """
    (นี่คือฟังก์ชันที่ขาดไป)
    สร้าง DB Session ใหม่สำหรับ Background Worker
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def calculate_sha256(file_path):
    """(ฟังก์ชันช่วย) คำนวณ SHA-256 ของไฟล์"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# --- Main Analysis Functions ---

def extract_iocs_from_pcap(file_path: str) -> list[dict]:
    """
    (ส่วนที่ 1) ดึง Network IOCs (Domains) โดยใช้ Scapy (Sync)
    """
    print(f"[Worker] Extracting IOCs from {file_path}...")
    iocs = []
    domains = set()
    try:
        # อ่านไฟล์ .pcap ด้วย scapy
        packets = rdpcap(file_path) 
        
        # วนลูปดูทีละ packet
        for pkt in packets:
            # ถ้า packet นี้มี Layer DNS และเป็นคำถาม (Query Record)
            if pkt.haslayer(DNSQR):
                try:
                    # ดึงชื่อ domain ที่ถาม (qname)
                    qname = pkt[DNSQR].qname.decode('utf-8').rstrip('.')
                    domains.add(qname)
                except Exception as e:
                    print(f"[Worker Info] Scapy DNS decode error: {e}")

        # แปลง set เป็น list of dicts
        for domain in domains:
            iocs.append({
                "source": "PCAP_DNS",
                "finding": domain,
                "result": {},
                "summary": "DNS query detected for this domain."
            })
            
    except Exception as e:
        print(f"[Worker Error] Scapy DNS failed: {e}")
        
    return iocs

def extract_http_files(file_path: str, output_dir: Path) -> list[dict]:
    """(ส่วนที่ 2) ดึงไฟล์ที่ถูกถ่ายโอนผ่าน HTTP (ตาม Blueprint)"""
    print(f"[Worker] Extracting HTTP objects from {file_path}...")
    file_iocs = []
    
    try:
        http_export_dir = output_dir / "http_extracted"
        http_export_dir.mkdir(exist_ok=True)
        command = [
            "tshark", "-r", file_path, 
            "--export-objects", f"http,{str(http_export_dir)}"
        ]
        subprocess.run(command, check=True, capture_output=True)

        for extracted_file in http_export_dir.glob("*"):
            file_hash = calculate_sha256(extracted_file)
            file_iocs.append({
                "source": "PCAP_HTTP_File",
                "finding": extracted_file.name,
                "result": {"sha256": file_hash},
                "summary": f"File extracted from HTTP stream (Hash: {file_hash[:10]}...)"
            })
            
    except subprocess.CalledProcessError as e:
        print(f"[Worker Error] TShark export-objects failed: {e.stderr.decode()}")
    except Exception as e:
        print(f"[Worker Error] HTTP extraction failed: {e}")
        
    return file_iocs


# --- Main Worker Entrypoint ---

def run_analysis(db_url: str, evidence_id: str, case_id: str, file_path: str, file_type: str):
    """
    ฟังก์ชันหลักที่ BackgroundTasks เรียกใช้
    """
    print(f"[Worker START] Processing evidence: {evidence_id} (Case: {case_id})")
    
    # (นี่คือบรรทัดที่ 9 (เดิม) ที่ Error - ตอนนี้มันจะหา get_db_session เจอแล้ว)
    db = next(get_db_session()) 
    
    try:
        # Step 1: Analyze file (Phase 3)
        all_analysis_results = []
        if file_type == "pcap":
            all_analysis_results.extend(extract_iocs_from_pcap(file_path))
            pcap_path_obj = Path(file_path)
            all_analysis_results.extend(extract_http_files(file_path, pcap_path_obj.parent))
        
        elif file_type == "dd":
            print(f"[Worker] Disk Dump analysis (.dd) is not implemented yet.")
            pass

        # === [PHASE 4: VIRUSTOTAL INTEGRATION] ===
        print(f"[Worker] Starting VirusTotal enrichment for {len(all_analysis_results)} items...")
        
        enriched_results = []
        for item in all_analysis_results:
            vt_result_data = {}
            vt_summary = " (VT scan skipped or N/A)"
            
            try:
                if item["source"] == "PCAP_HTTP_File":
                    file_hash = item["result"].get("sha256")
                    if file_hash:
                        vt_result_data, vt_summary = vt_client.scan_hash(file_hash)
                
                elif item["source"] == "PCAP_DNS":
                    domain = item["finding"]
                    vt_result_data, vt_summary = vt_client.scan_domain(domain)
                
            except Exception as e:
                print(f"[Worker Error] VT scan failed for {item['finding']}: {e}")
                vt_summary = " (VT scan failed)"

            item["result"].update(vt_result_data) 
            item["summary"] += vt_summary 
            enriched_results.append(item)
        # === [END OF PHASE 4] ===


        # Step 2: Save ENRICHED results to DB
        for result_data in enriched_results:
            crud.create_analysis_result(
                db=db, 
                case_id=case_id, 
                result=schemas.AnalysisResultBase(**result_data)
            )
        
        # Step 3: Chain of Custody - Part 2 (Report Hash)
        report_file_path = Path(file_path).parent / "analysis_report.json"
        with open(report_file_path, "w") as f:
            json.dump(
                {"timestamp": datetime.utcnow().isoformat(), "results": enriched_results}, 
                f,
                default=str
            )
        
        report_hash = calculate_sha256(report_file_path)
        evidence_record = crud.get_evidence(db=db, evidence_id=evidence_id)
        if evidence_record:
            blockchain.add_report_to_chain(
                evidence_hash=evidence_record.sha256Hash,
                report_hash=report_hash
            )

        # Step 4: อัปเดตสถานะ Case เป็น COMPLETED
        crud.update_case_status(db=db, case_id=case_id, status=schemas.CaseStatus.COMPLETED)
        
        print(f"[Worker FINISH] Processing complete for: {evidence_id}")

    except Exception as e:
        print(f"[Worker FAILED] Error processing {evidence_id}: {e}")
        crud.update_case_status(db=db, case_id=case_id, status=schemas.CaseStatus.FAILED)
    
    finally:
        db.close() # (สำคัญมาก)
```
