---
title: "main"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\main.py"
source_size_bytes: 7093
source_modified: 2025-11-26T17:31:47
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# main

- Source: [main.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/main.py)

## Content

```py
# /main.py
from fastapi import (
    FastAPI, Depends, HTTPException, status, 
    File, UploadFile, BackgroundTasks,
    Response 
)
from fastapi.middleware.cors import CORSMiddleware # <--- Import ตัวนี้
from sqlalchemy.orm import Session, joinedload
from pathlib import Path
from typing import List
import hashlib, shutil

import schemas, crud, models, security, analysis_worker, blockchain
from database import SessionLocal, engine, DATABASE_URL

# สร้างตารางครั้งแรก
models.Base.metadata.create_all(bind=engine)

# 1. สร้าง App
app = FastAPI(title="ForenChain API")

# 2. ตั้งค่า CORS (ต้องอยู่หลังสร้าง app ทันที)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # อนุญาตทุกเว็บ (Frontend)
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุก Method (GET, POST, OPTIONS)
    allow_headers=["*"],  # อนุญาตทุก Header
)

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
    # print(body)
    user = crud.get_user_by_username(db, body.username)
    if not user or not security.verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = security.create_access_token({"sub": user.username})
    return schemas.Token(access_token=access_token)

# ---------- Phase 1: Cases ----------
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

# ---------- Phase 2: Upload & Analysis ----------
@app.post(
    "/api/cases/{caseId}/upload",
    response_model=schemas.EvidenceUploadResponse,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Evidence"]
)
def upload_evidence_file(
    caseId: str,
    background_tasks: BackgroundTasks,     # ย้ายมาตรงนี้ (Non-default argument)
    evidenceFile: UploadFile = File(...), # ย้ายมาตรงนี้ (Default argument)
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

    # 5) บันทึก hash ขึ้นเชน
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

    # 7) ให้ worker รันวิเคราะห์
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
    response_class=Response 
)
def get_case_report(
    caseId: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(security.get_current_user),
):
    """
    สร้างและดาวน์โหลดรายงานฉบับสมบูรณ์ (JSON) สำหรับเคส
    """
    # 1. ดึงข้อมูลเคสทั้งหมด
    db_case = crud.get_case_with_details(db=db, case_id=caseId)
    if not db_case:
        raise HTTPException(status_code=404, detail="Case not found") 

    # 2. แปลงข้อมูลจาก DB เป็น JSON String
    report_data = schemas.CaseDetailResponse.model_validate(db_case)
    report_json_string = report_data.model_dump_json(indent=2)

    # 3. สร้างชื่อไฟล์
    file_name = f"ForenChain_Report_Case_{caseId}.json"
    
    # 4. คืนค่าเป็นไฟล์ดาวน์โหลด
    return Response(
        content=report_json_string,
        media_type="application/json",
        headers={
            "Content-Disposition": f"attachment; filename={file_name}"
        }
    )
```
