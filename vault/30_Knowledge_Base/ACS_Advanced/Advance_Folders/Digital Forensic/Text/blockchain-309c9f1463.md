---
title: "blockchain"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\blockchain.py"
source_size_bytes: 7275
source_modified: 2025-11-26T20:08:06
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# blockchain

- Source: [blockchain.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/blockchain.py)

## Content

```py
# /blockchain.py
import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# --- Config (ใช้ตัวแปรเดิมจาก .env ของคุณ) ---
RPC_URL = os.getenv("SEPOLIA_RPC_URL")
PRIVATE_KEY = os.getenv("BLOCKCHAIN_PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("SMART_CONTRACT_ADDRESS") # Address ที่เพื่อนส่งมา

# --- ABI (คัดลอกมาจากไฟล์ DraftIntegration ของเพื่อน) ---
CONTRACT_ABI = json.loads("""
[
    {
        "type": "error",
        "name": "EvidenceAlreadyExists",
        "inputs": []
    },
    {
        "type": "error",
        "name": "EvidenceNotFound",
        "inputs": []
    },
    {
        "type": "error",
        "name": "InvalidHash",
        "inputs": []
    },
    {
        "type": "error",
        "name": "NotAuthorized",
        "inputs": []
    },
    {
        "type": "error",
        "name": "ReportAlreadySet",
        "inputs": []
    },
    {
        "type": "error",
        "name": "ZeroAddress",
        "inputs": []
    },
    {
        "type": "event",
        "name": "EvidenceAdded",
        "inputs": [
            { "name": "evidenceHash", "type": "bytes32", "indexed": true },
            { "name": "caseId", "type": "string", "indexed": false },
            { "name": "fileName", "type": "string", "indexed": false },
            { "name": "uploader", "type": "address", "indexed": true },
            { "name": "timestamp", "type": "uint256", "indexed": false }
        ],
        "anonymous": false
    },
    {
        "type": "event",
        "name": "ReportAdded",
        "inputs": [
            { "name": "evidenceHash", "type": "bytes32", "indexed": true },
            { "name": "reportHash", "type": "bytes32", "indexed": false },
            { "name": "uploader", "type": "address", "indexed": true },
            { "name": "timestamp", "type": "uint256", "indexed": false }
        ],
        "anonymous": false
    },
    {
        "type": "function",
        "name": "addEvidence",
        "inputs": [
            { "name": "_evidenceHash", "type": "bytes32", "internalType": "bytes32" },
            { "name": "_caseId", "type": "string", "internalType": "string" },
            { "name": "_fileName", "type": "string", "internalType": "string" }
        ],
        "outputs": [],
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "name": "addReport",
        "inputs": [
            { "name": "_evidenceHash", "type": "bytes32", "internalType": "bytes32" },
            { "name": "_reportHash", "type": "bytes32", "internalType": "bytes32" }
        ],
        "outputs": [],
        "stateMutability": "nonpayable"
    }
]
""")

# --- Setup Web3 ---
w3 = None
if RPC_URL and PRIVATE_KEY and CONTRACT_ADDRESS:
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if w3.is_connected():
        print(f"[Blockchain] Connected to Sepolia. Current Block: {w3.eth.block_number}")
    else:
        print("[Blockchain Error] Could not connect to Sepolia RPC.")
else:
    print("[Blockchain Warning] Missing configuration in .env")

def _send_transaction(func_call):
    """ฟังก์ชันช่วยสำหรับส่ง Transaction"""
    if not w3 or not w3.is_connected():
        return "0x_blockchain_not_connected"

    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        
        # สร้าง Transaction
        nonce = w3.eth.get_transaction_count(account.address)
        chain_id = w3.eth.chain_id
        # สร้าง tx พื้นฐาน
        tx_data = func_call.build_transaction({
            'chainId': chain_id, # Chain ID ของ Ganache
            'gas': 3000000,  # เพิ่ม Gas Limit ให้พอ       
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce,
        })

        # เซ็น Transaction
        signed_tx = w3.eth.account.sign_transaction(tx_data, private_key=PRIVATE_KEY)

        # ส่ง Transaction
        print("[Blockchain] Sending transaction...")
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        # รอการยืนยัน (Wait for receipt)
        print(f"[Blockchain] Waiting for receipt... Tx: {tx_hash.hex()}")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        if tx_receipt.status == 1:
            print(f"[Blockchain] Confirmed! Block: {tx_receipt.blockNumber}")
            return tx_hash.hex()
        else:
            print("[Blockchain Error] Transaction failed (Reverted).")
            return "0x_tx_failed"

    except Exception as e:
        print(f"[Blockchain Error] Transaction Exception: {e}")
        return f"0x_error_{str(e)[:20]}"

# --- Public Functions (ที่ Backend เรียกใช้) ---

def add_evidence_to_chain(evidence_hash: str, case_id: str, file_name: str) -> str:
    """
    เรียก Smart Contract: addEvidence(_evidenceHash, _caseId, _fileName)
    """
    try:
        if not w3: return "mock_tx_no_connection"
        
        # [แก้ไข 1] แปลง Address เป็น Checksum อัตโนมัติ
        checksum_address = Web3.to_checksum_address(CONTRACT_ADDRESS)
        contract = w3.eth.contract(address=checksum_address, abi=CONTRACT_ABI)
        
        # [สำคัญ] แปลง Hash String เป็น Bytes32 ตามที่ Contract ต้องการ
        if evidence_hash.startswith("0x"):
            evidence_bytes = w3.to_bytes(hexstr=evidence_hash)
        else:
            evidence_bytes = w3.to_bytes(hexstr="0x" + evidence_hash)
        
        # เรียกฟังก์ชัน addEvidence ตาม ABI ใหม่
        func = contract.functions.addEvidence(evidence_bytes, case_id, file_name)
        
        return _send_transaction(func)
        
    except Exception as e:
        print(f"[Blockchain Error] addEvidence failed: {e}")
        return "0x_error_add_evidence"

def add_report_to_chain(evidence_hash: str, report_hash: str) -> str:
    """
    เรียก Smart Contract: addReport(_evidenceHash, _reportHash)
    """
    try:
        if not w3: return "mock_tx_no_connection"

        # [แก้ไข 2] แปลง Address เป็น Checksum อัตโนมัติ
        checksum_address = Web3.to_checksum_address(CONTRACT_ADDRESS)
        contract = w3.eth.contract(address=checksum_address, abi=CONTRACT_ABI)

        # [สำคัญ] แปลง Hash ทั้งคู่เป็น Bytes32
        if evidence_hash.startswith("0x"):
            e_bytes = w3.to_bytes(hexstr=evidence_hash)
        else:
            e_bytes = w3.to_bytes(hexstr="0x" + evidence_hash)

        if report_hash.startswith("0x"):
            r_bytes = w3.to_bytes(hexstr=report_hash)
        else:
            r_bytes = w3.to_bytes(hexstr="0x" + report_hash)

        # เรียกฟังก์ชัน addReport ตาม ABI ใหม่
        func = contract.functions.addReport(e_bytes, r_bytes)

        return _send_transaction(func)

    except Exception as e:
        print(f"[Blockchain Error] addReport failed: {e}")
        return "0x_error_add_report"
```
