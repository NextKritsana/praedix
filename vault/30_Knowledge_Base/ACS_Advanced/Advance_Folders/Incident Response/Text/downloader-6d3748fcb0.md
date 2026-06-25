---
title: "downloader"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Lab\\Lecture 26 Down drop\\downloader.ps1"
source_size_bytes: 575
source_modified: 2025-12-07T14:43:43
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# downloader

- Source: [downloader.ps1](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Lab/Lecture%2026%20Down%20drop/downloader.ps1)

## Content

```ps1
$url = "https://drive.usercontent.google.com/u/0/uc?id=1Wa7c8BES4CzQcJTemDde9oZEMx79ycq3&export=download"
$dest = "$env:USERPROFILE\Downloads\a.txt"

# บังคับใช้ TLS 1.2 (สำคัญมาก)
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# สั่งดาวน์โหลด
try {
    Write-Host "Downloading..."
    Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
    Write-Host "Download Success!" -ForegroundColor Green
}
catch {
    Write-Host "Failed: $_" -ForegroundColor Red
}
```
