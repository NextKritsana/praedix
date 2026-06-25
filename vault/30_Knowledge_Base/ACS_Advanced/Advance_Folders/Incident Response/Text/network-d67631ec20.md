---
title: "network"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\Tool and Result\\network.bat"
source_size_bytes: 511
source_modified: 2025-12-03T22:10:01
imported_at: 2026-06-14T14:27:16
tags:
  - acs
  - acs-advanced
  - imported
---

# network

- Source: [network.bat](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/Tool%20and%20Result/network.bat)

## Content

```bat
::network
set "result_folder=%output_path%"
set "Volatile_result=%result_folder%\Volatile_result"
set "Net_result=%Volatile_result%\Network"

if not exist "%Net_result%" (
  mkdir "%Net_result%"
  echo mkdir : Net_result
)

:: arp
set "output_arp=%Net_result%\arp.txt"
arp -a -v > "%output_arp%"

::route
set "output_route=%Net_result%\route.txt"
route PRINT -4 > "%output_route%"

::netstat
set "output_netstat=%Net_result%\netstat.txt"
netstat -nao | findstr LISTENING > "%output_netstat%"
```
