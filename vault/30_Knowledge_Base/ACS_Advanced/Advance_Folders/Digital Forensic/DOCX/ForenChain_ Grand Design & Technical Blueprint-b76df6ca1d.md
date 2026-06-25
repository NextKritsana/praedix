---
title: "ForenChain_ Grand Design & Technical Blueprint"
type: "acs-advance-docx"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\ForenChain_ Grand Design & Technical Blueprint.docx"
source_size_bytes: 6190527
source_modified: 2025-10-25T19:58:15
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# ForenChain_ Grand Design & Technical Blueprint

- Source: [ForenChain_ Grand Design & Technical Blueprint.docx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/ForenChain_%20Grand%20Design%20%26%20Technical%20Blueprint.docx)

ForenChain: Grand Design & Technical Blueprint

1. Vision & Document Purpose

This document serves as the single source of truth for the technical architecture of the ForenChain project. Its purpose is to provide a clear guide for each team (Frontend, Backend, Blockchain) on what to build, how the components will interact, and where their responsibilities lie. This will minimize miscommunication and ensure seamless integration.

2. High-Level System Architecture

The ForenChain platform consists of four main components: Frontend (Web Application), Backend (Server & Analysis), Blockchain (Smart Contract), and External Services (VirusTotal API).

Main Data Flow:

The User interacts with the Frontend.

The Frontend communicates with the Backend via a REST API.

The Backend orchestrates the entire process:

Saves evidence files and metadata to Storage & Database.

Calls the Blockchain Smart Contract to log a hash (proof of integrity).

Runs the Forensic Analysis Modules (.pcap & .dd).

Calls the VirusTotal API for further analysis.

Saves the analysis results to the Database.

The Frontend retrieves the results from the Backend to display to the user.

3. Component Details & Tasks per Team

A. Frontend (Team: Waezul, Ni'am)

This team's primary responsibility is to build an intuitive and responsive user interface.

What to Build:

Login/Authentication Page: An interface for users to sign in.

Main Dashboard: A page that lists all "Investigation Cases" created by the user. Each case will display its status (e.g., "Analysis Complete," "Analyzing").

Case Detail Page: A page to view the details of a single case. Here, the user will:

Upload evidence files (.pcap or .dd).

View a list of uploaded evidence.

See a summary of the analysis results.

Analysis Report Page: A page that displays detailed analysis results, including:

Information from the Blockchain (evidence hash, timestamp).

VirusTotal scan results (e.g., a list of malicious IPs, infected files).

A button to download the report in PDF format.

Technology: React.js or Vue.js.

Interaction: Communicates only with the Backend API. The frontend must not interact directly with the database or the blockchain.

B. Blockchain (Team: Alwi, 'T')

This team's primary responsibility is to create the immutable Chain of Custody system.

Function of the Blockchain:

It is NOT for storing evidence files. The file sizes are too large and it would be prohibitively expensive.

It is ONLY for storing the "digital fingerprint" (SHA-256 hash) of the evidence files and the resulting analysis reports. This serves as mathematical proof that a file has not been altered since it was recorded.

What to Build:

Smart Contract (ChainOfCustody.sol): A smart contract on the Ethereum network (Sepolia Testnet) with the following core functions:

function addEvidence(bytes32 _evidenceHash, string calldata _caseId, string calldata _fileName): This function will be called by the backend when a file is first uploaded. It will record the file's hash, case ID, filename, the uploader's address, and a timestamp.

function addReport(bytes32 _evidenceHash, bytes32 _reportHash): Called by the backend after the analysis is complete. It adds the hash of the report file to the existing evidence record.

function getEvidenceDetails(bytes32 _evidenceHash) public view returns (...): A function to verify and retrieve the record details for a given hash.

Interaction Scripts: Scripts (likely in Python using web3.py) that the backend will use to interact with the Smart Contract.

C. Forensics & Backend (Team: Davis, Kritsana, Cao Nguyen Gia Khanh)

This is the engine of the entire application. This team is responsible for all server-side logic, analysis, and integrations.

What to Build:

REST API Server (Python - Flask/FastAPI): This is the bridge between the Frontend and all backend logic. The required API endpoints are:

POST /api/cases: Creates a new investigation case entry in the database.

POST /api/cases/{caseId}/upload: Receives an evidence file upload. This will be a complex endpoint that:
a. Accepts the file.
b. Saves the file to a storage system (e.g., a folder on the server).
c. Calculates the SHA-256 hash of the file.
d. Calls the addEvidence function on the Smart Contract.
e. Initiates the analysis process (see point 2) asynchronously (in the background).

GET /api/cases: Retrieves a list of all cases.

GET /api/cases/{caseId}: Retrieves the complete details of a case, including analysis results from the database.

Forensic Analysis Modules (Python): Two main modules that will run in the background.

PCAP Analysis Module (assigned to Kritsana):
a. Use the scapy library to read the .pcap file.
b. Extract files transferred over protocols (e.g., HTTP).
c. Extract unique IP addresses from conversations. (optional)
d. Send each extracted file and IP to the VirusTotal API. (IP = Optional)
e. Save the results to the database.

Disk Dump Analysis Module (assigned to Davis):
a. Use a safe environment (like a Docker container) to mount the .dd file. (looks hard)
b. Iterate through the files within the disk image.
c. Calculate the SHA-256 hash of each file.
d. Send the file hashes to the VirusTotal API.
e. Save the results to the database.

Core Logic & Integration (assigned to Cao Nguyen Gia Khanh):

Design the database schema (PostgreSQL/MongoDB).

Manage the logic to link cases, evidence, and analysis results.

Build wrappers to interact with the Blockchain scripts and the VirusTotal API.

4. Integrated Workflow (Example)

Waezul/Ni'am: Creates the UI where a user can create a new case: "XYZ Malware Investigation".

Frontend calls POST /api/cases. Cao: The logic in the backend creates a new entry in the Cases table in the database.

Frontend allows the user to upload evidence.pcap to the case, calling POST /api/cases/{caseId}/upload.

Backend (Cao/Davis/Kritsana):

Receives and stores evidence.pcap.

Calculates its hash: e3b0c442...

Calls the script from Alwi/'T' to record this hash on the Blockchain.

Starts the PCAP Analysis Module belonging to Kritsana.

PCAP Analysis Module (Kritsana):

Finds a file malware.exe and an IP 123.45.67.89 within the pcap.

Sends malware.exe and 123.45.67.89 to VirusTotal.

VirusTotal responds: the file is malicious, and the IP is linked to a C&C server.

Saves these findings to the Results table in the database.

ALSO Disk Analysis

Frontend (Waezul/Ni'am): Periodically calls GET /api/cases/{caseId}. Once the status changes to "Complete," the UI will display the results, showing that malware.exe was found and the IP 123.45.67.89 is malicious. The user can click to verify the evidence hash on the Blockchain.

This document should be the primary reference. If there are any doubts or potential overlaps, the teams should refer back to the architecture and division of tasks described here.
