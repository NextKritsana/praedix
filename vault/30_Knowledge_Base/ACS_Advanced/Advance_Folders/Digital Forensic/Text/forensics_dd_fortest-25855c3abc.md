---
title: "forensics_dd_fortest"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\forensics_dd_fortest.py"
source_size_bytes: 4533
source_modified: 2025-11-25T17:08:46
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# forensics_dd_fortest

- Source: [forensics_dd_fortest.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/forensics_dd_fortest.py)

## Content

```py
# """
# forensics_dd.py (Mock Version for Windows/Integration Test)

# Modified to work without installing complex C++ Build Tools.
# If pytsk3 is missing, it returns simulated (mock) data.
# """
# from __future__ import annotations
# import hashlib
# import os
# from typing import List, Dict, Optional

# # --- PART 1: Safe Import ---
# try:
#     import pytsk3
#     HAS_PYTSK3 = True
# except ImportError:
#     HAS_PYTSK3 = False
#     print("[Warning] 'pytsk3' not found. Running in MOCK mode for Disk Forensics.")

# class DiskForensics:
#     """Class to perform basic operations on a raw `.dd` disk image."""

#     def __init__(self, image_path: str, sector_size: int = 512):
#         self.image_path = image_path
#         self.sector_size = sector_size
#         self.img = None

#     def open_image(self) -> None:
#         """Open the raw image."""
#         if not HAS_PYTSK3:
#             # Mock mode: Do nothing (just check if file exists)
#             if not os.path.exists(self.image_path):
#                 # Allow creating a fake file for testing if it doesn't exist
#                 with open(self.image_path, 'w') as f:
#                     f.write("MOCK DISK IMAGE")
#             return

#         # Real mode
#         if not os.path.exists(self.image_path):
#             raise FileNotFoundError(f"Image not found: {self.image_path}")
#         self.img = pytsk3.Img_Info(self.image_path)

#     def list_partitions(self) -> List[Dict]:
#         """Return a list of partitions."""
#         if not HAS_PYTSK3:
#             # --- MOCK DATA ---
#             # คืนค่าข้อมูลปลอมๆ เพื่อให้ Worker ทำงานต่อได้โดยไม่ Error
#             return [
#                 {
#                     'index': 0, 
#                     'start': 2048, 
#                     'length': 10000, 
#                     'start_byte': 1048576, 
#                     'description': 'Primary Partition (MOCK NTFS)'
#                 },
#                 {
#                     'index': 1, 
#                     'start': 12048, 
#                     'length': 5000, 
#                     'start_byte': 6168576, 
#                     'description': 'Linux Swap (MOCK)'
#                 }
#             ]

#         # Real Logic (from Davis)
#         if self.img is None:
#             self.open_image()
        
#         parts = []
#         try:
#             vol = pytsk3.Volume_Info(self.img)
#             for i, part in enumerate(vol):
#                 try:
#                     start = int(part.start)
#                     length = int(part.len)
#                 except:
#                     start = getattr(part, 'start', 0)
#                     length = getattr(part, 'len', 0)
#                 parts.append({
#                     'index': i,
#                     'start': start,
#                     'length': length,
#                     'start_byte': start * self.sector_size,
#                     'description': part.desc.decode('utf-8', errors='ignore') if hasattr(part, 'desc') else "Unknown"
#                 })
#         except Exception:
#              parts.append({'index': 0, 'description': 'Raw Filesystem'})
#         return parts

#     def list_files(self, partition_index: int = 0, path: str = '/') -> List[Dict]:
#         if not HAS_PYTSK3:
#             return [{'name': 'secret_password.txt', 'size': 123, 'type': 'File'}]
#         # (Real implementation omitted for brevity as we are mocking)
#         return []

#     def extract_file(self, partition_index: int, file_path: str, dest_path: str) -> None:
#         if not HAS_PYTSK3:
#             # Mock extract: just write a dummy file
#             with open(dest_path, 'w') as f:
#                 f.write("This is a mock extracted file.")
#             return
#         pass 

#     @staticmethod
#     def compute_hash(file_path: str, algo: str = 'sha256') -> str:
#         """Compute hash of a local file."""
#         h = hashlib.new(algo)
#         # Handle case where file might not exist in mock mode
#         if not os.path.exists(file_path):
#             return "0000000000000000000000000000000000000000000000000000000000000000"
            
#         with open(file_path, 'rb') as f:
#             for chunk in iter(lambda: f.read(8192), b''):
#                 h.update(chunk)
#         return h.hexdigest()
```
