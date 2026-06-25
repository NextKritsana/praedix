---
title: "main"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\main.py"
source_size_bytes: 16332
source_modified: 2025-11-30T18:40:35
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# main

- Source: [main.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/main.py)

## Content

```py
from fastapi import (
    FastAPI, Depends, HTTPException, status, 
    File, UploadFile, BackgroundTasks,
    Response, Request  # <--- 1. เพิ่มตัวนี้
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload
from pathlib import Path
from typing import List
import hashlib, shutil

import schemas, crud, models, security, analysis_worker, blockchain
from database import SessionLocal, engine, DATABASE_URL

# สร้างตารางครั้งแรก
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ForenChain API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default port
        "http://127.0.0.1:5173",  # Vite alternative
        "http://localhost:3000",  # Create React App default
        "http://127.0.0.1:3000",  # Create React App alternative
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods including OPTIONS
    allow_headers=["*"],  # Allow all headers
    expose_headers=["*"], # Expose all headers to browser
)

@app.middleware("http")
async def debug_cors(request: Request, call_next):
    response = await call_next(request)
    print(f"🔧 CORS Debug: {request.method} {request.url}")
    print(f"   Origin: {request.headers.get('origin')}")
    print(f"   Response Headers: {dict(response.headers)}")
    return response

STORAGE_DIR = Path("./storage")
STORAGE_DIR.mkdir(exist_ok=True)

# --- DB dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

STORAGE_DIR = Path("./storage")
STORAGE_DIR.mkdir(exist_ok=True)

# --- DB dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Auth Endpoints ----------
@app.post("/api/auth/register", response_model=schemas.UserPublic, tags=["Auth"], status_code=status.HTTP_201_CREATED)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user_in.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = security.get_password_hash(user_in.password)
    user = crud.create_user(db, username=user_in.username, hashed_password=hashed)
    return user

@app.post("/api/auth/login", response_model=schemas.Token, tags=["Auth"])
def login(body: schemas.AuthLoginRequest, db: Session = Depends(get_db)):
    print(body)
    user = crud.get_user_by_username(db, body.username)
    if not user or not security.verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = security.create_access_token({"sub": user.username})
    return schemas.Token(access_token=access_token)

# ---------- Phase 1 ----------
@app.post("/api/cases", response_model=schemas.Case, status_code=status.HTTP_201_CREATED, tags=["Cases"])
def create_new_case(
    case: schemas.CaseCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    return crud.create_case(db=db, case=case)

@app.get("/api/cases", response_model=List[schemas.Case], tags=["Cases"])
def get_all_cases(
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    return crud.get_cases(db=db)

@app.get("/api/cases/{caseId}", response_model=schemas.CaseDetailResponse, tags=["Cases"])
def get_case_details(
    caseId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    db_case = crud.get_case_with_details(db=db, case_id=caseId)
    if not db_case:
        raise HTTPException(status_code=404, detail="Case not found")
    return db_case

@app.get("/api/cases/{caseId}/analyses", response_model=List[schemas.AnalysisResult], tags=["Cases"])
def get_case_analyses(
    caseId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    Get detailed analysis results for a specific case
    """
    try:
        print(f"🔍 Getting analyses for case: {caseId}")
        
        # Check if case exists
        db_case = crud.get_case(db, caseId)
        if not db_case:
            print(f"❌ Case not found: {caseId}")
            raise HTTPException(status_code=404, detail="Case not found")
        
        # Get analysis results from database
        print(f"📊 Fetching analysis results for case: {caseId}")
        analyses = crud.get_analysis_results_by_case_id(db, caseId)
        print(f"✅ Found {len(analyses)} analysis results")
        
        return analyses
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error in get_case_analyses: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
# ---------- Phase 2 ----------
@app.post(
    "/api/cases/{caseId}/upload",
    response_model=schemas.EvidenceUploadResponse,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Evidence"]
)
def upload_evidence_file(
    caseId: str,
    background_tasks: BackgroundTasks,
    evidenceFile: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    # 1) ตรวจ case
    db_case = crud.get_case(db, caseId)
    if not db_case:
        raise HTTPException(404, "Case not found")

    # 2) ตรวจสกุลไฟล์
    ext = Path(evidenceFile.filename).suffix.lower()
    if ext not in [".pcap", ".dd"]:
        raise HTTPException(400, "Unsupported file type. Only .pcap or .dd are allowed.")
    file_type = ext.lstrip(".")

    # 3) บันทึกไฟล์
    case_dir = STORAGE_DIR / caseId
    case_dir.mkdir(parents=True, exist_ok=True)
    file_path = case_dir / evidenceFile.filename
    try:
        with file_path.open("wb") as buf:
            shutil.copyfileobj(evidenceFile.file, buf)
    finally:
        evidenceFile.file.close()

    # 4) คำนวณ SHA-256
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    file_hash = h.hexdigest()

    # 5) (จำลอง) บันทึก hash ขึ้นเชน
    tx_hash = blockchain.add_evidence_to_chain(
        evidence_hash=file_hash, case_id=caseId, file_name=evidenceFile.filename
    )

    # 6) ลง DB
    ev = crud.create_evidence_record(
        db=db,
        case_id=caseId,
        file_name=evidenceFile.filename,
        file_type=file_type,
        sha256_hash=file_hash,
        tx_hash=tx_hash,
    )

    # In upload_evidence_file - fix error handling
    # 6A) Trigger VirusTotal analysis immediately
    try:
        print(f"🔄 Starting VirusTotal for hash: {file_hash}")
        from vt_client import scan_hash
        
        vt_result = scan_hash(file_hash)
        print(f"✅ VirusTotal response type: {type(vt_result)}")
        print(f"✅ VirusTotal response: {vt_result}")
        
        # Check if we got a proper dict response
        if isinstance(vt_result, dict) and 'result' in vt_result:
            print(f"📊 Saving analysis to database...")
            analysis_record = crud.create_analysis_result(
                db=db,
                case_id=caseId,
                source=vt_result.get("source", "VirusTotal_File"),
                finding=vt_result.get("finding", file_hash),
                result_data=vt_result.get("result", {}),
                summary=vt_result.get("summary", "VirusTotal analysis completed"),
                analysis_type="VIRUSTOTAL_FILE_SCAN"
            )
            print(f"✅ Analysis saved with ID: {analysis_record.id}")
        else:
            print(f"❌ Invalid VirusTotal response format: {vt_result}")
            
    except Exception as vt_error:
        print(f"❌ VirusTotal analysis failed: {vt_error}")
    # 7) ให้ worker รันวิเคราะห์อื่นๆ
    background_tasks.add_task(
        analysis_worker.run_analysis,
        db_url=DATABASE_URL,
        evidence_id=ev.id,
        case_id=caseId,
        file_path=str(file_path),
        file_type=file_type,
    )

    # 8) อัปเดตสถานะ
    crud.update_case_status(db, caseId, schemas.CaseStatus.ANALYSIS_IN_PROGRESS)

    return schemas.EvidenceUploadResponse(
        message="File accepted and analysis has started.",
        evidence=schemas.Evidence.model_validate(ev)
    )

@app.get("/healthz")
def healthz():
    return {"ok": True}

# ---------- Phase 6: Report Generation ----------
@app.get(
    "/api/cases/{caseId}/report",
    tags=["Report"],
    # เราจะคืนค่าเป็นไฟล์ JSON โดยตรง
    response_class=Response 
)
def get_case_report(
    caseId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    สร้างและดาวน์โหลดรายงานฉบับสมบูรณ์ (JSON) สำหรับเคส
    รวมถึงข้อมูลหลักฐานและผลการวิเคราะห์ทั้งหมด
    """
    
    # 1. ดึงข้อมูลเคสทั้งหมด (เหมือนที่ /api/cases/{caseId} ทำ)
    db_case = crud.get_case_with_details(db=db, case_id=caseId)
    if not db_case:
        raise HTTPException(status_code=404, detail="Case not found") 

    # 2. แปลงข้อมูลจาก DB เป็น Pydantic Model (เพื่อให้แน่ใจว่าตรงสเปก)
    # (เราใช้ Model เดียวกับที่ส่งให้ Frontend ดูรายละเอียด)
    report_data = schemas.CaseDetailResponse.model_validate(db_case)
    
    # 3. แปลง Pydantic Model เป็น JSON String ที่จัดรูปแบบสวยงาม
    # (ใช้ model_dump_json สำหรับ Pydantic v2)
    report_json_string = report_data.model_dump_json(indent=2)

    # 4. สร้างชื่อไฟล์สำหรับดาวน์โหลด
    file_name = f"ForenChain_Report_Case_{caseId}.json"
    
    # 5. คืนค่าเป็น Response แบบไฟล์ดาวน์โหลด
    return Response(
        content=report_json_string,
        media_type="application/json",
        headers={
            # Header นี้คือสิ่งที่ "บังคับ" ให้เบราว์เซอร์ดาวน์โหลด แทนที่จะแสดงผล
            "Content-Disposition": f"attachment; filename={file_name}"
        }
    )

# ---------- Phase 7: VirusTotal Analysis Endpoints ----------
@app.post("/api/analyze/hash", tags=["VirusTotal"])
def analyze_hash(
    analysis_request: dict,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    Analyze a file hash with VirusTotal
    Expected request: {"file_hash": "abc123..."}
    """
    file_hash = analysis_request.get("file_hash")
    if not file_hash:
        raise HTTPException(status_code=400, detail="File hash is required")
    
    try:
        # Import and use your vt_client
        from vt_client import scan_hash
        result = scan_hash(file_hash)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"VirusTotal analysis failed: {str(e)}")

@app.post("/api/analyze/domain", tags=["VirusTotal"])
def analyze_domain(
    analysis_request: dict,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    Analyze a domain with VirusTotal
    Expected request: {"domain": "example.com"}
    """
    domain = analysis_request.get("domain")
    if not domain:
        raise HTTPException(status_code=400, detail="Domain is required")
    
    try:
        from vt_client import scan_domain
        result = scan_domain(domain)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"VirusTotal analysis failed: {str(e)}")

@app.post("/api/analyze/ip", tags=["VirusTotal"])
def analyze_ip(
    analysis_request: dict,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    Analyze an IP address with VirusTotal
    Expected request: {"ip_address": "8.8.8.8"}
    """
    ip_address = analysis_request.get("ip_address")
    if not ip_address:
        raise HTTPException(status_code=400, detail="IP address is required")
    
    try:
        from vt_client import scan_ip
        result = scan_ip(ip_address)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"VirusTotal analysis failed: {str(e)}")
    
    # ---------- Debug Endpoints ----------
@app.get("/debug/analysis", tags=["Debug"])
def debug_analysis(db: Session = Depends(get_db)):
    """Debug endpoint to check all analysis results"""
    results = crud.get_all_analysis_results(db)
    return {
        "total_analysis_results": len(results),
        "results": [
            {
                "id": r.id,
                "case_id": r.case_id,
                "source": r.source,
                "finding": r.finding,
                "result": r.result,
                "summary": r.summary
            }
            for r in results
        ]
    }

@app.get("/api/evidence/{evidenceId}/status", response_model=dict, tags=["Evidence"])
def get_evidence_status(
    evidenceId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    Get the status of evidence analysis
    """
    try:
        # Get evidence from database
        evidence = crud.get_evidence(db, evidenceId)
        if not evidence:
            raise HTTPException(status_code=404, detail="Evidence not found")
        
        # Get associated analysis results
        analyses = db.query(models.AnalysisResult)\
            .filter(models.AnalysisResult.case_id == evidence.case_id)\
            .all()
        
        # Determine status based on analysis results
        status = "COMPLETED" if len(analyses) > 0 else "ANALYSIS_IN_PROGRESS"
        
        return {
            "evidenceId": evidenceId,
            "status": status,
            "analysisCount": len(analyses),
            "caseId": evidence.case_id
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting evidence status: {str(e)}")
    
# ---------- Delete Case Endpoint ----------
@app.delete("/api/cases/{caseId}", tags=["Cases"])
def delete_case_endpoint(
    caseId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    Delete a case and all associated evidence and analysis results
    """
    try:
        print(f"🗑️ Deleting case: {caseId}")
        
        # Check if case exists
        db_case = crud.get_case(db, caseId)
        if not db_case:
            raise HTTPException(status_code=404, detail="Case not found")
        
        case_name = db_case.caseName
        
        # Delete associated files from storage
        case_dir = STORAGE_DIR / caseId
        if case_dir.exists():
            import shutil
            shutil.rmtree(case_dir)
            print(f"📁 Deleted case directory: {case_dir}")
        
        # Delete from database (cascade should handle evidence and analysis results)
        db.delete(db_case)
        db.commit()
        
        print(f"✅ Case deleted successfully: {caseId}")
        return {
            "message": f"Case '{case_name}' deleted successfully",
            "deleted_case_id": caseId
        }
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print(f"❌ Error deleting case: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to delete case: {str(e)}")
```
