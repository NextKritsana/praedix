---
title: "security"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\security.py"
source_size_bytes: 2563
source_modified: 2025-11-30T15:08:01
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# security

- Source: [security.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/security.py)

## Content

```py
# /security.py
import os
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from sqlalchemy.orm import Session
from database import SessionLocal
import crud

# OAuth2 - expects "Authorization: Bearer <token>"
# [แก้ไขจุดที่ 1] เพิ่ม auto_error=False เพื่อให้เข้าผ่าน Chrome ได้โดยไม่โดนบล็อกทันที
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)

# Password hashing (use pbkdf2_sha256 to avoid bcrypt backend issues on Windows)
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# JWT settings
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# [แก้ไขจุดที่ 2] เปลี่ยนฟังก์ชันนี้ให้เป็น Bypass Mode
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    [BYPASS MODE] 
    ฟังก์ชันนี้ถูกแก้เพื่อข้ามการตรวจ Token ชั่วคราว 
    เพื่อให้ทดสอบ Create Case ใน Postman และโหลด Report ใน Chrome ได้
    โดยไม่ต้อง Login จริง
    """
    # สร้าง User จำลอง (Mock User) ส่งกลับไปเลย ไม่ว่าจะส่ง Token อะไรมาก็ตาม
    class MockUser:
        id = "user_id_999"
        username = "TestAdmin"
        is_active = True

    return MockUser()
```
