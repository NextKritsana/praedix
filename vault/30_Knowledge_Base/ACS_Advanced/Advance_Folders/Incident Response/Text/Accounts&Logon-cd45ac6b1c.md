---
title: "Accounts&Logon"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Tool and Result\\Accounts&Logon.bat"
source_size_bytes: 540
source_modified: 2025-12-04T20:44:08
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# Accounts&Logon

- Source: [Accounts&Logon.bat](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Tool%20and%20Result/Accounts%26Logon.bat)

## Content

```bat
::process
set "PR_result=%Volatile_result%\Process"
if not exist "%PR_result%" (
mkdir "%PR_result%"
echo mkdir : PR_result
) 
::pslist
set "pslist_path=%tool_path%\pslist.exe"
set "output_pslist=%PR_result%\pslist.txt"
%pslist_path% > "%output_pslist%"
%pslist_path% -t >> "%output_pslist%"
::tasklist set "output_tasklist=%PR_result%\tasklist.txt"
tasklist > "%output_tasklist%"
::openedfilesview set "of_path=%tool_path%\openedfilesview.exe"
set "output_of=%PR_result%\openedfilesview.txt"
%of_path% /stext > "%output_of%"
```
