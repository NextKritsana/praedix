---
title: "schemas"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\schemas.py"
source_size_bytes: 2854
source_modified: 2025-11-23T15:00:44
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# schemas

- Source: [schemas.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/schemas.py)

## Content

```py
# /schemas.py (ฉบับแก้ไขที่ถูกต้อง)
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum
import uuid

# --- Auth/User Schemas ---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    id: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AuthLoginRequest(BaseModel):
    username: str
    password: str

# --- Enums (ค่าคงที่) ---
class CaseStatus(str, Enum):
    PENDING = "PENDING"
    ANALYSIS_IN_PROGRESS = "ANALYSIS_IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

# --- AnalysisResult Models ---
class AnalysisResultBase(BaseModel):
    source: str
    finding: str
    result: dict  # สำหรับเก็บ JSON object เช่น {"malicious": 4, "suspicious": 1}
    summary: str

class AnalysisResult(AnalysisResultBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Pydantic v2 config
    model_config = ConfigDict(from_attributes=True)

# --- Evidence Models ---
class EvidenceBase(BaseModel):
    fileName: str
    fileType: str  # pcap, dd

class Evidence(EvidenceBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    sha256Hash: str | None = None
    blockchainTxHash: str | None = None
    uploadedAt: datetime = Field(default_factory=datetime.utcnow)
    
    # Pydantic v2 config
    model_config = ConfigDict(from_attributes=True)

# Alias/outbound representation used by endpoints
class EvidenceOut(Evidence):
    pass

# --- Case Models ---
class CaseBase(BaseModel):
    caseName: str
    description: str | None = None

class CaseCreate(CaseBase):
    # ใช้สำหรับรับ Input ตอน POST /cases
    pass

class Case(CaseBase):
    # ใช้สำหรับ Response (ส่งข้อมูลกลับไป)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    status: CaseStatus = CaseStatus.PENDING
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)
    
    # Pydantic v2 config
    model_config = ConfigDict(from_attributes=True)

# --- Model สำหรับ GET /cases/{caseId} (แบบละเอียด) ---
class CaseDetailResponse(Case):
    evidence: list[Evidence] = []
    analysisResults: list[AnalysisResult] = []

# --- Model สำหรับ POST /cases/{caseId}/upload (Response)  ---
class EvidenceUploadResponse(BaseModel):
    message: str
    evidence: Evidence # (ใช้ Evidence model ที่เราสร้างไว้แล้ว)
```
