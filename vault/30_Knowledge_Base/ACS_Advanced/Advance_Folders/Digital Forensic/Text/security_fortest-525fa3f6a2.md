---
title: "security_fortest"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\backend-forenchain-main\\security_fortest.py"
source_size_bytes: 864
source_modified: 2025-11-25T17:08:02
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# security_fortest

- Source: [security_fortest.py](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/backend-forenchain-main/security_fortest.py)

## Content

```py
# # /security.py (ฉบับแก้ไขเพื่อทดสอบ)

# # ... (imports ด้านบนเหมือนเดิม) ...

# # แก้ฟังก์ชันนี้ฟังก์ชันเดียว
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     """
#     [TEST MODE]
#     ฟังก์ชันนี้ถูกแก้ชั่วคราวเพื่อ Bypass การตรวจสอบ Token
#     จะคืนค่า User ปลอมๆ กลับไปเสมอ เพื่อให้ทดสอบ API ส่วนอื่นได้
#     """
#     # สร้าง Object User ปลอมๆ (Mock User)
#     class MockUser:
#         id = "test_user_id_999"
#         username = "TestAdmin"
#         is_active = True

#     return MockUser()
```
