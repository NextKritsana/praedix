---
title: "11강_Executable Files_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\11강_Executable Files_v1.2.pdf"
source_size_bytes: 1223399
source_modified: 2025-11-12T12:22:21
imported_at: 2026-06-14T14:26:28
tags:
  - acs
  - acs-advanced
  - imported
---

# 11강_Executable Files_v1.2

- Source: [11강_Executable Files_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/11%EA%B0%95_Executable%20Files_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Executable file
• AppcompatCache
• Clean Hive
• UserAssist
• What is Prefetch?
• Analyzing Prefetch
11
1

## Page 2

01. 현재 페이지 주제
AppcompatCache 01
AppcompatCache
shimcache
• AppCompatCache is an important file used by Microsoft Windows operating system,
primarily created for compatibility control and troubleshooting of applications
• The file stores important information to maintain the compatibility of applications running
on Windows, and it primarily helps to manage the compatibility of applications running on
Windows
Features
• Stores path, size, last modified time, etc. of executable files
• Serves a similar role to Prefetch, but unlike Prefetch, it is limited in number X
• When malware is executed, it is written to the corresponding artifact because most of the
time there are compatibility issues
Features
• Recently, we've seen a lot of fileless attacks, so if something called an
""executable files" is not created, it exists
Caution
2

## Page 3

01. 현재 페이지 주제
AppcompatCache 01
Registry PATH
HKLM\SYSTEM\CurrentControlSet\Control\SessionManager\AppCompatCache
SYSTEM\ControlSet00x\Control\SessionManager\AppCompatCache
PATH
If the CurrentControlSet does not exist, in most cases the information can be found in one of the ControlSet00x
ControlSet00x represents a copy of the system configuration, and reflects the system configuration selected when the user boots up
AppcompatCache
3

## Page 4

01. 현재 페이지 주제
AppcompatCache 01
ShimCache Header
Field Name Size
Signature 4byte
CRC32 4byte
Entry len 4byte
Path len 2byte
Path ?? Byte
Last Modified 8byte
Data len 1byte
Data n Byte
Null Padding 3byte
AppcompatCache
4

## Page 5

01. 현재 페이지 주제
AppcompatCache 01
AppcompatCache Parser
• In Incident Response, where speed is of the essence, analyzing the registry using the previous methods can take a
significant amount of time for even the most skilled person
• We use a tool called AppcomaptCache Parser to analyze the registry
• It is used in CLI form and takes a SYSTEM file as an argument
https://github.com/EricZimmerman/AppCompatCacheParse
https://f001.backblazeb2.com/file/EricZimmermanTools/AppCompatCacheParser.zip
AppcompatCache
5

## Page 6

01. 현재 페이지 주제
1
 2
 3
AppcompatCache 01
Extract System
Part of the sequence of tasks to extract system files using FTK Imager
Later...
Later on, you can use a tool called Forecopy handy to extract the registry hive file from the cli, but for this lecture,
we'll use FTK for ease of use and quicker understanding.
AppcompatCache
6

## Page 7

01. 현재 페이지 주제
AppcompatCache 01
Select the partition with the largest capacity
Think of root as the C drive
AppcompatCache
7

## Page 8

01. 현재 페이지 주제
AppcompatCache 01
SYSTEM path : C:\Windows\System32\config
SYSTEM.LOG1 and SYSTEM.LOG2
are the log files that record
configuration information
System.Log?
AppcompatCache
8

## Page 9

01. 현재 페이지 주제
Clean Hive 02
1
2
3
.
OPEN cancel
Clean Hive
• Currently, the extracted SYSTEM file may be in the Clean state, but most users prefer to use the Clean state
• The Clean Hive feature stores SYSTEM caches in .Log1 and .Log2, such as configuration information that remains
when the system is not shut down normally, and combines them together to create a complete SYSTEM registry
hive
9

## Page 10

01. 현재 페이지 주제
Clean Hive 02
4
5
6
7
.
Selection flow
A warning window will appear stating that Dirty Hive has been detected -> Select Yes -> Select OK
-> Select SYSTEM.LOG1 and SYSTEM.LOG2 -> Open them
open cancel
Clean Hive
10

## Page 11

01. 현재 페이지 주제
8
9
11
12
.
Clean Hive 02
Selection flow
This completes the Clean Hive and saves the file in a place that is easily accessible to analysts
Clean Hive
11

## Page 12

01. 현재 페이지 주제
Clean Hive 02
kusti
Using Commands
Give the f option to AppcompatCacheParser.exe, enter the PATH of Clean Hive, and enter -csv to output in csv format
Finally, select a location to save and run it to create a CSV file like the bottom right
Clean Hive
12

## Page 13

01. 현재 페이지 주제
Clean Hive 02
Result Exam
Check the PATH value
We see that the program named compattelrunner.exe was launched on October 28, 2023 at 08:35 from the path
C:\Windows\system32\
Clean Hive
13

## Page 14

01. 현재 페이지 주제
UserAssist 03
UserAssist
• Stores the path, size, and last modified time of an executable file
• The main purpose is to improve the user experience by keeping track of
which applications or files the user has launched
• HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
Explorer\UserAssist
PATH
14

## Page 15

01. 현재 페이지 주제
UserAssist 03
Executable Files : { 5E6AB780-7743-11CF-A12B-00AA00 4AE837 }\Count
Shortcuts : { 75048700-EF1F-11D0-9888-006097DEACF9 }\Count
Executable Files : {CEBFF5CD-ACE2-4F4F-9178-9926F41 749EA }\Count
Shortcuts : {F4E57C4B-2036-45F0-A9AB-443BCFE33D9F }\Count
Due to UAC since Windows 7, when a normal user writes a file or registry to a specific path, virtualization occurs,
and the data written through virtualization is stored in UsrClass.dat instead of NTUSER.DAT
Major Subkey
UserAssist
15
