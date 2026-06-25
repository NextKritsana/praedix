---
title: "crud"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\crud.py"
source_size_bytes: 4674
source_modified: 2025-11-30T14:49:53
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# crud

- Source: [crud.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/crud.py)

## Content

```py
# /crud.py (COMPLETE FIXED VERSION)
from sqlalchemy.orm import Session
import models, schemas
import uuid
from datetime import datetime
from sqlalchemy.orm import joinedload

# --- User Functions ---
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, hashed_password: str):
    user = models.User(
        id=str(uuid.uuid4()),
        username=username,
        hashed_password=hashed_password,
        is_active=True,
        createdAt=datetime.utcnow(),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# --- Case Functions ---
def get_case(db: Session, case_id: str):
    return db.query(models.Case).filter(models.Case.id == case_id).first()

def get_cases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Case).offset(skip).limit(limit).all()

def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.Case(
        id=str(uuid.uuid4()),
        caseName=case.caseName,
        description=case.description,
        status=schemas.CaseStatus.PENDING,
        createdAt=datetime.utcnow(),
        updatedAt=datetime.utcnow()
    )
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case

def update_case_status(db: Session, case_id: str, status: schemas.CaseStatus):
    db_case = get_case(db, case_id)
    if db_case:
        db_case.status = status
        db_case.updatedAt = datetime.utcnow()
        db.commit()
        db.refresh(db_case)
    return db_case

def get_case_with_details(db: Session, case_id: str):
    return db.query(models.Case).options(
        joinedload(models.Case.evidence),
        joinedload(models.Case.analysisResults)
    ).filter(models.Case.id == case_id).first()

# --- Evidence Functions ---
def get_evidence(db: Session, evidence_id: str):
    """ดึงข้อมูล Evidence ชิ้นเดียว"""
    return db.query(models.Evidence).filter(models.Evidence.id == evidence_id).first()

def create_evidence_record(
    db: Session, 
    case_id: str, 
    file_name: str, 
    file_type: str, 
    sha256_hash: str, 
    tx_hash: str
):
    db_evidence = models.Evidence(
        id=str(uuid.uuid4()),
        fileName=file_name,
        fileType=file_type,
        sha256Hash=sha256_hash,
        blockchainTxHash=tx_hash,
        uploadedAt=datetime.utcnow(),
        case_id=case_id
    )
    db.add(db_evidence)
    db.commit()
    db.refresh(db_evidence)
    return db_evidence

# --- Analysis Result Functions ---
def create_analysis_result(
    db: Session, 
    case_id: str,  # Uses case_id to match your model
    source: str,
    finding: str,
    result_data: dict,
    summary: str,
    analysis_type: str = "VIRUSTOTAL"
):
    """Save analysis results to database"""
    try:
        print(f"💾 Saving analysis result for case {case_id}")
        print(f"   Source: {source}, Finding: {finding}")
        print(f"   Result: {result_data}")
        
        analysis_result = models.AnalysisResult(
            id=str(uuid.uuid4()),
            case_id=case_id,
            source=source,
            finding=finding,
            result=result_data,
            summary=summary,
            analysis_type=analysis_type,
            timestamp=datetime.utcnow()
        )
        db.add(analysis_result)
        db.commit()
        db.refresh(analysis_result)
        
        print(f"✅ Analysis result saved with ID: {analysis_result.id}")
        return analysis_result
        
    except Exception as e:
        print(f"❌ Error saving analysis result: {e}")
        db.rollback()
        raise

def get_analysis_results_by_case_id(db: Session, case_id: str):
    """
    Get all analysis results for a case (direct relationship - matches your model)
    """
    try:
        print(f"🔍 CRUD: Getting analyses for case {case_id}")
        results = db.query(models.AnalysisResult)\
            .filter(models.AnalysisResult.case_id == case_id)\
            .all()
        print(f"✅ CRUD: Found {len(results)} analysis results")
        return results
    except Exception as e:
        print(f"❌ CRUD Error in get_analysis_results_by_case_id: {e}")
        return []  # Return empty list instead of crashing

# --- Debug/Utility Functions ---
def get_all_analysis_results(db: Session):
    """Get all analysis results for debugging"""
    return db.query(models.AnalysisResult).all()

def get_evidence_by_case_id(db: Session, case_id: str):
    """Get all evidence for a case"""
    return db.query(models.Evidence).filter(models.Evidence.case_id == case_id).all()
```
