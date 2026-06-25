---
title: "blockchain"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-backend-main\\blockchain.py"
source_size_bytes: 5284
source_modified: 2025-11-30T16:15:39
imported_at: 2026-06-14T14:25:25
tags:
  - acs
  - acs-advanced
  - imported
---

# blockchain

- Source: [blockchain.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-backend-main/blockchain.py)

## Content

```py
# /blockchain.py
import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# --- Config ---
RPC_URL = os.getenv("SEPOLIA_RPC_URL")
PRIVATE_KEY = os.getenv("BLOCKCHAIN_PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("SMART_CONTRACT_ADDRESS")

# --- ABI ---
CONTRACT_ABI = json.loads("""
[
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
        print(f"[Blockchain] Connected. Block: {w3.eth.block_number}")
    else:
        print("[Blockchain Error] Could not connect to RPC.")
else:
    print("[Blockchain Warning] Missing configuration in .env")

def _send_transaction(func_call):
    """ฟังก์ชันช่วยสำหรับส่ง Transaction"""
    if not w3 or not w3.is_connected():
        return "0x_blockchain_not_connected"

    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        
        # 1. ดึง Nonce และ Chain ID
        nonce = w3.eth.get_transaction_count(account.address)
        chain_id = w3.eth.chain_id  # <--- (สำคัญ) ดึง Chain ID อัตโนมัติ

        # 2. สร้าง Transaction
        tx_data = func_call.build_transaction({
            'chainId': chain_id,
            'gas': 3000000,       
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce,
        })

        # 3. เซ็น Transaction
        signed_tx = w3.eth.account.sign_transaction(tx_data, private_key=PRIVATE_KEY)

        # 4. ส่ง Transaction (แก้จุดที่พังตรงนี้!)
        print("[Blockchain] Sending transaction...")
        
        # ตรวจสอบเวอร์ชันและเลือกใช้คำสั่งที่ถูกต้อง
        if hasattr(signed_tx, 'raw_transaction'):
            # สำหรับ Web3.py v6+ (แบบใหม่)
            raw_tx = signed_tx.raw_transaction
        else:
            # สำหรับ Web3.py v5 (แบบเก่า)
            raw_tx = signed_tx.rawTransaction

        tx_hash = w3.eth.send_raw_transaction(raw_tx)
        
        # 5. รอผลลัพธ์
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
        return f"0x_error_{str(e)[:50]}"

# --- Public Functions ---

def add_evidence_to_chain(evidence_hash: str, case_id: str, file_name: str) -> str:
    try:
        if not w3: return "mock_tx_no_connection"
        
        # แปลง Address เป็น Checksum
        checksum_address = w3.to_checksum_address(CONTRACT_ADDRESS)
        contract = w3.eth.contract(address=checksum_address, abi=CONTRACT_ABI)
        
        # แปลง Hash เป็น Bytes32
        if evidence_hash.startswith("0x"):
            evidence_bytes = w3.to_bytes(hexstr=evidence_hash)
        else:
            evidence_bytes = w3.to_bytes(hexstr="0x" + evidence_hash)
        
        func = contract.functions.addEvidence(evidence_bytes, case_id, file_name)
        return _send_transaction(func)
        
    except Exception as e:
        print(f"[Blockchain Error] addEvidence failed: {e}")
        return f"0x_error_{str(e)[:50]}"

def add_report_to_chain(evidence_hash: str, report_hash: str) -> str:
    try:
        if not w3: return "mock_tx_no_connection"

        checksum_address = w3.to_checksum_address(CONTRACT_ADDRESS)
        contract = w3.eth.contract(address=checksum_address, abi=CONTRACT_ABI)

        if evidence_hash.startswith("0x"):
            e_bytes = w3.to_bytes(hexstr=evidence_hash)
        else:
            e_bytes = w3.to_bytes(hexstr="0x" + evidence_hash)

        if report_hash.startswith("0x"):
            r_bytes = w3.to_bytes(hexstr=report_hash)
        else:
            r_bytes = w3.to_bytes(hexstr="0x" + report_hash)

        func = contract.functions.addReport(e_bytes, r_bytes)
        return _send_transaction(func)

    except Exception as e:
        print(f"[Blockchain Error] addReport failed: {e}")
        return f"0x_error_{str(e)[:50]}"
```
