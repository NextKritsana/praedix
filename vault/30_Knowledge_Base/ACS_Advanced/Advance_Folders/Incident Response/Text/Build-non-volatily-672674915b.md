---
title: "Build-non-volatily"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Tool and Result\\Build-non-volatily.bat"
source_size_bytes: 509
source_modified: 2025-12-04T21:54:10
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# Build-non-volatily

- Source: [Build-non-volatily.bat](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Tool%20and%20Result/Build-non-volatily.bat)

## Content

```bat
set "fh=forecopy"

if not exist "forecopy" (
    mkdir "forecopy"
    echo mkdir : forecopy
)

::ไฟล์ Cache.exe ยังไม่ได้ดาวโหลดมันจะคำรวนได้ยังไง
set "Thumb_Cache_path=Thumb Cache.exe"
set "output_fh=forecopy"

".\Thumb Cache.exe" -m "forecopy"
".\Thumb Cache.exe" -f C:\$Logfile "forecopy"
".\Thumb Cache.exe" -f C:\$Extend\$Logfile:$J "forecopy"
".\Thumb Cache.exe" -g "forecopy"
".\Thumb Cache.exe" -e "forecopy"
```
