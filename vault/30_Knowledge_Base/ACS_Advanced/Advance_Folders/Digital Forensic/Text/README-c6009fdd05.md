---
title: "README"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\README.md"
source_size_bytes: 7173
source_modified: 2025-11-30T14:49:53
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# README

- Source: [README.md](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/README.md)

## Content

```md
# ForenChain Backend API

FastAPI backend for ForenChain, a digital forensics case management platform. The API lets investigators register, authenticate, manage cases, upload evidence, trigger analysis, and download case reports that include blockchain-backed integrity metadata.

---

## Quick Start

1. **Create a Python virtual environment** (optional but recommended).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the API**:
   ```bash
   uvicorn main:app --reload
   ```
4. The service listens on `http://127.0.0.1:8000` by default. Interactive docs are available at `/docs` (Swagger UI) and `/redoc`.

The app uses a local SQLAlchemy database (SQLite by default) and writes evidence files beneath `./storage/`.

---

## Authentication

The API uses bearer tokens. Obtain a token via `/api/auth/login` and attach it to protected requests using the `Authorization: Bearer <token>` header. Only the health check and authentication endpoints are public.

### Register
- **Endpoint:** `POST /api/auth/register`
- **Purpose:** Create a new user account.
- **Body:**
  ```json
  {
    "username": "forensic_analyst",
    "password": "VerySecure123!"
  }
  ```
- **Responses:**
  - `201 Created` with user info on success.
  - `400 Bad Request` if the username already exists.
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/auth/register \
       -H "Content-Type: application/json" \
       -d '{"username": "forensic_analyst", "password": "VerySecure123!"}'
  ```

### Login
- **Endpoint:** `POST /api/auth/login`
- **Purpose:** Authenticate and receive a JWT access token.
- **Body:**
  ```json
  {
    "username": "forensic_analyst",
    "password": "VerySecure123!"
  }
  ```
- **Responses:**
  - `200 OK` with `{ "access_token": "<jwt>", "token_type": "bearer" }`.
  - `401 Unauthorized` for invalid credentials.
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/auth/login \
       -H "Content-Type: application/json" \
       -d '{"username": "forensic_analyst", "password": "VerySecure123!"}'
  ```

---

## Case Management

### Create Case
- **Endpoint:** `POST /api/cases`
- **Auth:** Required.
- **Body:**
  ```json
  {
    "caseName": "Operation Nightfall",
    "description": "Dark web trafficking investigation"
  }
  ```
- **Responses:**
  - `201 Created` with the new case payload.
  - `401 Unauthorized` if the bearer token is missing or invalid.
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/cases \
       -H "Authorization: Bearer $TOKEN" \
       -H "Content-Type: application/json" \
       -d '{"caseName": "Operation Nightfall", "description": "Dark web trafficking investigation"}'
  ```

### List Cases
- **Endpoint:** `GET /api/cases`
- **Auth:** Required.
- **Purpose:** Retrieve all cases with summary information.
- **Response:** `200 OK` with an array of case objects.

### Case Detail
- **Endpoint:** `GET /api/cases/{caseId}`
- **Auth:** Required.
- **Purpose:** Retrieve detailed information for a specific case, including associated evidence records and analysis results.
- **Responses:**
  - `200 OK` with `CaseDetailResponse` payload.
  - `404 Not Found` if the case does not exist.

---

## Evidence & Analysis

### Upload Evidence File
- **Endpoint:** `POST /api/cases/{caseId}/upload`
- **Auth:** Required.
- **Purpose:** Upload evidence for a case. Stores the file, hashes it, records metadata, and schedules background analysis.
- **Request:** `multipart/form-data` with field `evidenceFile`.
  - Accepted extensions: `.pcap` or `.dd`.
- **Responses:**
  - `202 Accepted` with acknowledgment and evidence metadata.
  - `400 Bad Request` for unsupported file types.
  - `404 Not Found` if the case does not exist.
- **Example:**
  ```bash
  curl -X POST http://127.0.0.1:8000/api/cases/$CASE_ID/upload \
       -H "Authorization: Bearer $TOKEN" \
       -F "evidenceFile=@sample.pcap"
  ```
- **Notes:**
  - The server persists the file under `./storage/{caseId}/`.
  - SHA-256 hash is stored both in the database and the blockchain ledger via `blockchain.add_evidence_to_chain`.
  - `analysis_worker.run_analysis` executes asynchronously using FastAPI background tasks.
  - The case status transitions to `ANALYSIS_IN_PROGRESS` after upload.

---

## Reports

### Download Case Report
- **Endpoint:** `GET /api/cases/{caseId}/report`
- **Auth:** Required.
- **Purpose:** Download a comprehensive JSON report containing case data, evidence metadata, and analysis results.
- **Response:**
  - `200 OK` with `application/json` attachment (`ForenChain_Report_Case_{caseId}.json`).
  - `404 Not Found` if the case doesnt exist.

---

## Health Check

- **Endpoint:** `GET /healthz`
- **Purpose:** Simple readiness probe returning `{ "ok": true }`.
- **Auth:** Not required.

---

## Data Models

### Case Object
```json
{
  "id": "c1a2b3c4-d5e6-f7g8-h9i0-j1k2l3m4n5o6",
  "caseName": "Investigation of Malware XYZ",
  "description": "Analysis of a suspicious pcap file from the finance department.",
  "status": "ANALYSIS_IN_PROGRESS",
  "createdAt": "2025-10-17T14:30:00Z",
  "updatedAt": "2025-10-17T14:35:00Z"
}
```
- `status` can be `PENDING`, `ANALYSIS_IN_PROGRESS`, `COMPLETED`, or `FAILED`.

### Evidence Object
```json
{
  "id": "e1f2g3h4-i5j6-k7l8-m9n0-o1p2q3r4s5t6",
  "fileName": "evidence.pcap",
  "fileType": "pcap",
  "sha256Hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "blockchainTxHash": "0x123...abc",
  "uploadedAt": "2025-10-17T14:35:00Z"
}
```
- `fileType` values align with allowed uploads (`pcap`, `dd`).

### AnalysisResult Object
```json
{
  "id": "r1s2t3u4-v5w6-x7y8-z9a0-b1c2d3e4f5g6",
  "source": "VirusTotal_IP",
  "finding": "123.45.67.89",
  "result": {
    "malicious": 4,
    "suspicious": 1,
    "harmless": 78
  },
  "summary": "IP associated with C&C servers.",
  "timestamp": "2025-10-17T15:00:00Z"
}
```
- `source` denotes the analysis provider (e.g., `VirusTotal_IP`, `VirusTotal_File`).

---

## Project Structure

```
backend-forenchain/
├── storage/            # Evidence files (created at runtime)
├── analysis_worker.py  # Evidence analysis background task
├── blockchain.py       # Simulated blockchain integration
├── crud.py             # Database operations
├── database.py         # DB session setup
├── main.py             # FastAPI app entrypoint
├── models.py           # SQLAlchemy models
├── requirements.txt    # Python dependencies
├── schemas.py          # Pydantic schemas
├── security.py         # Auth helpers & JWT utilities
├── tasks.py            # Celery/worker placeholders (if any)
└── vt_client.py        # VirusTotal client (optional usage)
```

---

## Additional Notes

- Update the `SECRET_KEY` environment variable in production to secure JWTs.
- By default the application uses SQLite; configure `DATABASE_URL` in `database.py` or environment variables for other databases.
- Ensure the background analysis worker logic in `analysis_worker.py` and blockchain integration in `blockchain.py` meet your operational requirements before production deployment.
```
