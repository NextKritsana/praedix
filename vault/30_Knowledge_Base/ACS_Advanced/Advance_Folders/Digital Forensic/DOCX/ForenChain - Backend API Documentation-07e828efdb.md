---
title: "ForenChain - Backend API Documentation"
type: "acs-advance-docx"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\ForenChain - Backend API Documentation.docx"
source_size_bytes: 6187603
source_modified: 2025-10-25T19:58:04
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# ForenChain - Backend API Documentation

- Source: [ForenChain - Backend API Documentation.docx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/ForenChain%20-%20Backend%20API%20Documentation.docx)

ForenChain - Backend API Documentation

Version: 1.0.0

Base URL: /api

1. Introduction

This document provides a detailed specification for the ForenChain REST API. This API is the primary interface between the frontend application and the backend server. All communication is over HTTPS and all data is sent and received as JSON.

2. Authentication

All endpoints are protected and require an authentication token.

Authentication Type: Bearer Token (JWT)

Header: Authorization: Bearer <your_jwt_token>

(Note: The authentication endpoints (/api/auth/login, /api/auth/register) are not detailed in this document but will be required for obtaining a token.)

3. Data Models

Case Object

{
  "id": "c1a2b3c4-d5e6-f7g8-h9i0-j1k2l3m4n5o6",
  "caseName": "Investigation of Malware XYZ",
  "description": "Analysis of a suspicious pcap file from the finance department.",
  "status": "ANALYSIS_IN_PROGRESS", // PENDING, ANALYSIS_IN_PROGRESS, COMPLETED, FAILED
  "createdAt": "2025-10-17T14:30:00Z",
  "updatedAt": "2025-10-17T14:35:00Z"
}

Evidence Object

{
  "id": "e1f2g3h4-i5j6-k7l8-m9n0-o1p2q3r4s5t6",
  "fileName": "evidence.pcap",
  "fileType": "pcap", // pcap, dd
  "sha256Hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "blockchainTxHash": "0x123...abc",
  "uploadedAt": "2025-10-17T14:35:00Z"
}

AnalysisResult Object

{
  "id": "r1s2t3u4-v5w6-x7y8-z9a0-b1c2d3e4f5g6",
  "source": "VirusTotal_IP", // VirusTotal_IP, VirusTotal_File, etc.
  "finding": "123.45.67.89",
  "result": {
    "malicious": 4,
    "suspicious": 1,
    "harmless": 78
  },
  "summary": "IP associated with C&C servers.",
  "timestamp": "2025-10-17T15:00:00Z"
}

4. Endpoints

Cases

POST /cases

Create a new investigation case.

Request Body: application/json
{
  "caseName": "Investigation of Malware XYZ",
  "description": "Analysis of a suspicious pcap file."
}

Success Response (201 Created):

Returns the full Case Object that was created.

{
  "id": "c1a2b3c4-d5e6-f7g8-h9i0-j1k2l3m4n5o6",
  "caseName": "Investigation of Malware XYZ",
  "description": "Analysis of a suspicious pcap file.",
  "status": "PENDING",
  "createdAt": "2025-10-17T14:30:00Z",
  "updatedAt": "2025-10-17T14:30:00Z"
}

Error Response (400 Bad Request):

If caseName is missing or invalid.

GET /cases

Retrieve a list of all investigation cases for the authenticated user.

Success Response (200 OK):

Returns an array of Case Objects.

[
  {
    "id": "c1a2b3c4-d5e6-f7g8-h9i0-j1k2l3m4n5o6",
    "caseName": "Investigation of Malware XYZ",
    "status": "COMPLETED",
    "createdAt": "2025-10-17T14:30:00Z"
  },
  {
    "id": "z9y8x7w6-v5u4-t3s2-r1q0-p9o8n7m6l5k4",
    "caseName": "Suspicious Disk Image",
    "status": "ANALYSIS_IN_PROGRESS",
    "createdAt": "2025-10-18T10:00:00Z"
  }
]

GET /cases/{caseId}

Retrieve the full details of a single investigation case.

URL Parameters:

caseId (string, required): The ID of the case to retrieve.

Success Response (200 OK):

Returns a detailed object containing the case info, an array of its evidence files, and an array of analysis results.

{
  "id": "c1a2b3c4-d5e6-f7g8-h9i0-j1k2l3m4n5o6",
  "caseName": "Investigation of Malware XYZ",
  "description": "Analysis of a suspicious pcap file.",
  "status": "COMPLETED",
  "createdAt": "2025-10-17T14:30:00Z",
  "updatedAt": "2025-10-17T15:10:00Z",
  "evidence": [
    {
      "id": "e1f2g3h4-i5j6-k7l8-m9n0-o1p2q3r4s5t6",
      "fileName": "evidence.pcap",
      "fileType": "pcap",
      "sha256Hash": "e3b0c442...",
      "blockchainTxHash": "0x123...abc",
      "uploadedAt": "2025-10-17T14:35:00Z"
    }
  ],
  "analysisResults": [
    {
      "id": "r1s2t3u4-v5w6-x7y8-z9a0-b1c2d3e4f5g6",
      "source": "VirusTotal_IP",
      "finding": "123.45.67.89",
      "summary": "IP associated with C&C servers.",
      "timestamp": "2025-10-17T15:00:00Z"
    }
  ]
}

Error Response (404 Not Found):

If a case with the specified caseId does not exist.

Evidence

POST /cases/{caseId}/upload

Upload an evidence file (.pcap or .dd) to a specific case. This triggers the asynchronous analysis process.

URL Parameters:

caseId (string, required): The ID of the case to which the file will be added.

Request Body: multipart/form-data

key: evidenceFile

value: The .pcap or .dd file to upload.

Success Response (202 Accepted):

The server has accepted the file and has started the analysis process in the background. The response contains the details of the newly created evidence record.

{
  "message": "File accepted and analysis has started.",
  "evidence": {
    "id": "e1f2g3h4-i5j6-k7l8-m9n0-o1p2q3r4s5t6",
    "fileName": "evidence.pcap",
    "fileType": "pcap",
    "sha256Hash": "e3b0c442...",
    "blockchainTxHash": "0x123...abc",
    "uploadedAt": "2025-10-17T14:35:00Z"
  }
}

Error Response (400 Bad Request):

If no file is provided, or the file type is unsupported.

Error Response (404 Not Found):

If the specified caseId does not exist.
