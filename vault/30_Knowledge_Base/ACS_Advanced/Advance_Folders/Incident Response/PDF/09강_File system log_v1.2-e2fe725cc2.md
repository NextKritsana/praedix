---
title: "09강_File system log_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\09강_File system log_v1.2.pdf"
source_size_bytes: 2206034
source_modified: 2025-11-12T12:19:05
imported_at: 2026-06-14T14:26:26
tags:
  - acs
  - acs-advanced
  - imported
---

# 09강_File system log_v1.2

- Source: [09강_File system log_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/09%EA%B0%95_File%20system%20log_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

What is file system log?
• What is file system log?
• $MFT
• $LogFile
• $J
• Others
09
1

## Page 2

What is file system log? 01
• Logging activity on files and directories
• Maintain reliability and consistency
• Prevent data loss
Actions
• Changes to the file system
• Access history
• File creation and deletion
• Changing permissions
Record types
Purpose of file system logs
2

## Page 3

파일시스템 로그란?01
OS Information
New Technology File System
Features
Logs for file IO, transactions,
modifications, etc.
Cautions
Performed directly by the operating system X
Logs recorded by the filesystem
1
2
3
MFT
$LogFile
$UsnJrnl$J
What is file system log?
3

## Page 4

$MFT 02
PATH
Tool PATH MFT?
Tool
Storing metadata for files and directories
Maintain and repair file system consistency
What is $MFT?
[Root]\$MFT
Extract using FTK Imager
$MFT PATH
MFT Viewer in GUI
What is MFT Explorer
https://f001.backblazeb2.com/
file/EricZimmermanTools/MFTE
xplorer.zip
Download PATH
4

## Page 5

$MFT 02
MFT Explorer Launch Screen
https://f001.backblazeb2.com/file/EricZimmermanTools/MFTExplorer.zip
$MFT
5

## Page 6

$MFT 02
MFT Explorer Launch Screen
File system structure
MAC Time, MetaData
Sub-files
Hex, Overview, Details
For deleted files, there is a chance that no metadata remains
Time values should not be trusted absolutely
$MFT
6

## Page 7

$MFT 02
Delete the Delete.png file
Check with NTFS Walker
Notice that the name is gone but still has
the time value from Delete.png above
$MFT
7

## Page 8

$MFT 02
Until the file system reuses the area, there is a chance that the data is still there
In this case, you can carve the malware, analyze it, and add the analysis results to your security solution
$MFT
8
Create a file
Set the portion marked 0 to 1
1 is area of the disk that is in use
0 is unused space
Shows the area the disk is using
Deleting files
Deallocate it from the Bitmap
Set the deallocated portion back to 0
The deallocated area will initialize the
existing data X

## Page 9

$LogFile 03
$LogFile
01
04
02
03
What is $LogFile?
Create DIR/FILE
Delete DIR/FILE
Chang DIR/FILE
Information
• Chkdisk /F /L:[Size]
Log Size up
9
Record all tranche operations in Record units
Use for recovery in case of sudden file loss
during a job
Explained on the next page
Transaction

## Page 10

$LogFile 03
What is a transaction?
f_job1
s_job1
f_job2
s_job2
f_job3
s_job3
X
$LogFile
10
Meaning data for the current work in progress
Start offset of redo data
Refers to the data for the current ongoing task
Start offset for undo data
Data changes complete
Separate the order
of each task record
• Transaction tasks on a record-by-record basis
• Used for recovery in case of file loss
• Record before and after information of MFT
Entry number and changed attributes,
location, and values
• Analyzes MAC Time
Logfile

## Page 11

$LogFile 03
https://sites.google.com/site/forensicnote/ntfs-log-tracker
Download PATH
NTFS_Log_Tracker_CMD.exe -h
command
-l : $LogFile Path
-u : $UsnJrnl:$J Path
-s : Source Files Folder Path for UsnJrnl Record Carving
-a : UsnJrnl's Carving Alignment(1~8) (Default : 8)
-m : $MFT Path (Optional)
-b : Suspicious Behavior Detection (Optional)
Source Parameters
-o : Output File Path (Output Format : SQLite DB)
-c : CSV Output (Optional)
Output Parameters
$LogFile
11

## Page 12

$LogFile 03
NTFS_Log_Tracker_CMD.exe -l ./$LogFile -o . -c
command
Why?
See important data such as EventTime, Event, Detail, Create Time, Modified Time, Access Time, MFT_Modified Time, etc.
By analyzing and interpreting the extracted information, you can track changes to the file system and determine attacker behavior
$LogFile
12

## Page 13

$J 04
Change log files provided by the NTFS file system
Applications detect whether a file has changed
Enabled starting with Windows 7
$UsnJrnl$J
• Four 8-byte pieces of information
• Maximum size of log data
• The size of the area to allocate when new
data
• FileTime of $UsnJrnl
• The minimum value of currently stored
record
• Actual changelog records are stored
• Sparse Area filled with zeros
• Continuous variable-sized records
• The preceding Sparse Area keeps the size of the log data
stored in the $J property constant
Root\Extend
PATH
13

## Page 14

$J 04
http://msdn.microsoft.com/en-us/library/aa365722.aspx
typedef struct {
DWORD RecordLength;
WORD MajorVersion;
WORD MinorVersion;
DWORDLONG FileReferenceNumber;
DWORDLONG ParentFileReferenceNumber;
USN Usn;
LARGE_INTEGER TimeStamp;
DWORD Reason;
DWORD SourceInfo;
DWORD SecurityId;
DWORD FileAttributes;
WORD FileNameLength;
WORD FileNameOffset;
WCHAR FileName[1];
} USN_RECORD_V2,*PUSN_RECORD_V2;
USN_RECORD_V2
Structure
1 : File or directory has been overwritten
2 : File or directory has been extended
4 : File or directory has been truncated
100 : File or directory created for the first time
200 : File or directory was deleted
800 : Access to a file or directory has changed
DWORD : 4byte
WORD : 2byte
DWORDLONG : 8byte
LARGE_INTEGER : 8byte
WCHAR : N byte
Inforamtion
• ParentFileReferenceNumber exists because if you use only FileReferenceNumber, you
might not get the path to the file if it is deleted
• FileAttributes indicates the attribute information of the changed target
• Reason is a flag used to determin the reasons for changes that have accumulated in a
journal record since the file or directory was opened
• Also called Reason Flag, when a file or directory is closed, a final USN record is
created using the USN_REASON_CLOSE flag set
$J
14

## Page 15

$J 04
fsutil usn readjournal c: > c:\J_Info.txt
command
$J
15

## Page 16

Others 05
N T F S  L O G  T r a c k e r
Comprehensively analyze information from $MFT, $LogFile, and $UsnJrnl
Save the result as SQL DB
In the interface, after specifying the paths of $LogFile, $J, and $MFT, click
Parse
S a v e  D B
IMG
 IMG DB Browser
for SQLite
D o w n l o a d  P A T H
https://sites.google.com/site/forensicnote/ntfs-log-tracker
16

## Page 17

기타 05
Filter : File Creation
SELECT * FROM LogFile WHERE CreateTime <= '2019-12-07 18:48:042'
Select Browse Data and apply a filter named File Creation to the Event item
Intuitively review information about specific event types
Example
“SELECT * FROM table_name WHERE event = something_event“
Extract data specific to a particular event for more information
Useful for analysts to investigate and track details about a specific event type
SQL Query
Others
17

## Page 18

기타 05
Keeping the creation time unchanged when a file is
created with the same name in the same path within
a short period of time
OS
NTFS, FAT32 file systems
Caveats
As a technique in antiforensics, it should be
considered when analyzing exploit X
Should be fully considered when analyzing
Registry PATH
\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
Tunneling
Others
18

## Page 19

기타 05
MaximumTunnel
EntryAgeInSeconds MaximumTunnel
Entries
Default value : 15
If a file is deleted within 15 seconds and a file with the
same name is created, inherit the file's creation time
Info
Default value : 1
If the corresponding value is 0, enable the
feature X
Always give new attributes to created files
Info
Others
19

## Page 20

기타 05
Tunneling labs
echo test > tuntest.log
$item = get-item .\tuntest.log
cat tuntest.log
Write-Host $item .CreationTime
Remove-Item .\tuntest.log
Start-Sleep -Seconds 2
echo Change! > tuntest.log
$item = get-item .\tuntest.log
cat tuntest.log
Write-Host $item .CreationTime
Remove-Item .\tuntest.log
Tunneling lab code
Others
20
Create a tuntest.log file with the name test in it
Print the Creation Time
Delete the tuntest.log file
Create a tuntest.log file with the text Change!
Print the Creation Time
Delete the tuntest.log file
Wait 2 seconds
Tunneling time: 3 sec
