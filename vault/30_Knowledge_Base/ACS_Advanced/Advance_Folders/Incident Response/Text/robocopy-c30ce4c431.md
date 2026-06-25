---
title: "robocopy"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Tool and Result\\robocopy.bat"
source_size_bytes: 461
source_modified: 2025-12-04T22:53:32
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# robocopy

- Source: [robocopy.bat](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Tool%20and%20Result/robocopy.bat)

## Content

```bat
set "robo=robocopy"

if not exist "robocopy" (
    mkdir "robocopy"
    echo mkdir : robocopy
)

if not exist "robocopy\appcache" (
    mkdir "robocopy\appcache"
    echo mkdir : appcache
)

robocopy /MIR "C:\Windows\apppatch" "robocopy\appcache"

if not exist "robocopy\thumbcache" (
    mkdir "robocopy\thumbcache"
    echo mkdir : thumbcache
)

robocopy /MIR "C:\Users\acer\AppData\Local\Microsoft\Windows\Explorer" "robocopy\thumbcache"
```
