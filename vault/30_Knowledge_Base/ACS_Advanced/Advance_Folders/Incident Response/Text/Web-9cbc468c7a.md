---
title: "Web"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Tool and Result\\Web.bat"
source_size_bytes: 377
source_modified: 2025-12-04T22:12:33
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# Web

- Source: [Web.bat](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Tool%20and%20Result/Web.bat)

## Content

```bat
set "web=web"

if not exist "web" (
    mkdir "web"
    echo mkdir : web
)

set "webhistory_path=BrowsingHistoryView.exe"
set "webdownload_path=BrowserDownloadsView.exe"


set "output_webhistory=web\history.csv"
set "output_webdownload=web\download.csv"

.\BrowsingHistoryView.exe /scomma "web\history.csv"
.\BrowserDownloadsView.exe /scomma "web\download.csv"
```
