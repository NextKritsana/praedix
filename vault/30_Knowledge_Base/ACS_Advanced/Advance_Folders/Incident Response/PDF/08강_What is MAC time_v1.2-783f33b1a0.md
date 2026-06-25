---
title: "08강_What is MAC time_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\08강_What is MAC time_v1.2.pdf"
source_size_bytes: 1633550
source_modified: 2025-11-12T12:18:34
imported_at: 2026-06-14T14:26:25
tags:
  - acs
  - acs-advanced
  - imported
---

# 08강_What is MAC time_v1.2

- Source: [08강_What is MAC time_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/08%EA%B0%95_What%20is%20MAC%20time_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

What is MAC Time?
• What is MAC Time?
• Linux MAC
• Window MAC
• Time Stomp
08
1

## Page 2

What is MAC Time? 01
What is MAC Time?
Attributes of files, directories, and file system metadata
Timetable based on that information
Different operating systems and filesystems can handle differently
Linux
windows
2

## Page 3

What is MAC Time? 01
The purpose and reason for collecting MAC Time
3
Track system access time
Understand the tools and techniques used
Trace the path of an attacker's activity
Files modified just before the problem occurred
If the attack was caused by malware
Understand how malicious code behaves and help you respond
Prove system penetration and subsequent activity
Claiming compensation for victimized organizations

## Page 4

Linux MAC 02
Modify
The last time the contents of a
file were changed
Add text to a document
Edit an image file
Track change history
Detect security issues with
pattern analysis
Access
The last time a file or directory
was accessed
Open File or Directory
Get Metadata
Look up user patterns
Unintentional access
Change
The last time the file's metadata
was changed
Size, owner, permissions, and
number of links in the file
File content edits
Tracking when metadata changes
Understanding the history of
changes
M A C
4

## Page 5

Ubuntu Linux
Linux MAC 02
5
Command : stat FILE
File Name : test1.txt
Permission : 664
UID : kusti / normal user
GID : kusti / general group
Access Time
Modify Time
Change Time
Birth
2024-01-01 01:37:07
Unix TimeStamp
Number of seconds measured from 00:00:00 UTC on
January 1, 1970
R W X R W X R W X
User Group Other
R : Read
W : Write
X : Execute
Read Permissions
Write Permissions
Execute permission
4
2
1

## Page 6

Linux MAC 02
PROCEDURE
01
STEP
03
STEP
05
STEP
02
STEP
04
STEP
Create File
Command : touch
Write File
Create Link
Command ln
Change Permission
Command : chmod
Move File
Command : mv
6

## Page 7

Create
Linux MAC 02
Create a file with the touch command and view it with the stat command
Time MAC
2024-02-01 08:42:40 Access
2024-02-01 08:42:40 Modify
2024-02-01 08:42:40 Change
7
MAC Time, Birth Time are the same

## Page 8

Move
Linux MAC 02
Time (Before) Time (After) MAC
2024-02-01 08:42:40 2024-02-01 08:42:40 Access
2024-02-01 08:42:40 2024-02-01 08:42:40 Modify
2024-02-01 08:42:40 2024-02-01 09:24:10 Change
8
Changing Change Time

## Page 9

Write
Linux MAC 02
Store ifconfig results in ACS_TEST as a redirect
Time (Before) Time (After) MAC
2024-02-01 08:42:40 2024-02-01 08:42:40 Access
2024-02-01 08:42:40 2024-02-01 09:33:19 Modify
2024-02-01 09:24:10 2024-02-01 09:33:19 Change
9
Modify, Change Time Changing

## Page 10

Read
Linux MAC 02
View the contents of the ACS_TEST file with the Cat command
Time (Before) Time (After) MAC
2024-02-01 08:42:40 2024-02-01 09:39:05 Access
2024-02-01 09:33:19 2024-02-01 09:33:19 Modify
2024-02-01 09:33:19 2024-02-01 09:33:19 Change
10
Change Access Time

## Page 11

Write
Linux MAC 02
Access, Modify, Change Time
Write Data via Vi
Time (Before) Time (After) MAC
2024-02-01 09:39:05 2024-02-01 09:51:09 Access
2024-02-01 09:33:19 2024-02-01 09:51:09 Modify
2024-02-01 09:33:19 2024-02-01 09:51:09 Change
11

## Page 12

Permission Change
Linux MAC 02
Time (Before) Time (After) MAC
2024-02-01 09:51:09 2024-02-01 09:51:09 Access
2024-02-01 09:51:09 2024-02-01 09:51:09 Modify
2024-02-01 09:51:09 2024-02-01 10:15:09 Change
12
Changing Change Time

## Page 13

Linux MAC 02
LINK
HARD LINK
Same inode as the original file
Available even if the original file is deleted
Symbolic LINK
A link pointing to the name of the source file
Unavailable if the original file is deleted
 Symbolic LINK if marked
ACS_LNK is a Symbolic LINK that points to ACS_TEST
Inode: Every file or directory has one inode, and inodes store information such as the owner of the file, permissions, and where the data is stored
13

## Page 14

LINK
Linux MAC 02
Time (Before) Time (After) MAC
2024-02-01 09:51:09 2024-02-01 09:51:09 Access
2024-02-01 09:51:09 2024-02-01 09:51:09 Modify
2024-02-01 10:15:09 2024-02-01 10:22:13 Change
14
Changing Change Time

## Page 15

What is MAC Time?
Windows ✓ M(Modified Time) : The last time the file content or attributes were
changed
✓ A(Accessed Time) : Last time the file was accessed
✓ C(Created Time) : Time the file was created
Window MAC 03
FAT32 NTFS
Filesystem dependent differences
15

## Page 16

Windows
You can check the MAC Time in the property value
Unlike Linux, C Time represents Create
Creation time : 2023 12/16 15:42:01
Change time : 2023 12/16 15:42:01
Accessed : 2024 01/01 1 min ago
Window MAC 03
Right click -> View Properties
File path : C:\Users\kkkgo\Desktop
16

## Page 17

Windows – MFT
.
Window MAC 03
Time information used by the NTFS file system
The last time the MFT record for that file or directory was changed
Metadata such as file name, size, permissions, owner information, etc.
Check the $Standard Information property and $File Name property
for time values
An important structure for storing metadata about a file or directory in an NTFS file system
Time values can be found in the $Standard Information attribute and the $File Name attribute
In Linux, inodes hold metadata information about files
More detailed information will be provided in a later lesson, Filesystem Logs
What is $MFT
Create Time, Modified Time are the same as property values
Access Time is an absolute value, not a relative value
MFT Modified Time added, not shown in Windows Properties
window
17

## Page 18

This is not commonly seen
Window MAC 03
18

## Page 19

Window MAC 03
Verifying the NTFS MFT Structure
Verify each property value
PROCEDURE
01
STEP
03
STEP
02
STEP
Create Volume
NTFS
FAT32
FAT32
Directory Entry
Root Directory
NTFS
, Create, Move, Write,
Copy, Rename
USE TOOLS
NTFS
Walker
https://dmitrybrant.com/ntfswalker
Download PATH
19

## Page 20

Window MAC 03
System Tools for Disk Management
Manage disk volumes on your system
Format a hard drive
Create, delete partitions
Select a high-capacity drive
Right click
Click Shrink Volume
20

## Page 21

Window MAC 03
1
2
3
4
5
Shrink by 100 MB
Select New Simple Volume
NTFS : 50MB
FAT32 : 49MB
Setting the volume
character
Create NTFS, FAT32 each
21

## Page 22

Window MAC 03
FAT32
Used before NTFS
Can only move files 4 GB or less
Works on all operating systems
NTFS
Emerged after Windows NT
Efficient file management
Provides fast file access
Offers a wide range of features
22
