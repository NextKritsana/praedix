---
title: "database"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\database.py"
source_size_bytes: 881
source_modified: 2025-11-30T14:49:53
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# database

- Source: [database.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/database.py)

## Content

```py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load env vars if python-dotenv is available (optional)
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

# Database URL: fallback to local SQLite if unset or placeholder
DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./forenchain.db"
if DATABASE_URL.strip().startswith("..."):
    DATABASE_URL = "sqlite:///./forenchain.db"

# Create engine (handle SQLite thread check)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, future=True, connect_args=connect_args)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

# Declarative Base for models
Base = declarative_base()
```
