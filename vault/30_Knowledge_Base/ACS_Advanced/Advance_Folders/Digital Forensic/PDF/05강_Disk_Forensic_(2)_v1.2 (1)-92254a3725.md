---
title: "05강_Disk_Forensic_(2)_v1.2 (1)"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\05강_Disk_Forensic_(2)_v1.2 (1).pdf"
source_size_bytes: 531358
source_modified: 2025-10-18T19:34:45
imported_at: 2026-06-14T14:24:57
tags:
  - acs
  - acs-advanced
  - imported
---

# 05강_Disk_Forensic_(2)_v1.2 (1)

- Source: [05강_Disk_Forensic_(2)_v1.2 (1).pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/05%EA%B0%95_Disk_Forensic_%282%29_v1.2%20%281%29.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Disk Forensic (2)
• History of FAT - FAT 12 16 32
• Analyzing FAT32 clusters
• FAT32 Creation Deletion Repair Process
05
1

## Page 2

History of FAT - FAT 12 16 3201
FAT 32
SD Card
Floppy disk
ETC
USB
About FAT (File Allocation Table)
2

## Page 3

01
FAT
What is FAT?
3
History of FAT - FAT 12 16 32
Developer
Bill Gates | Microsoft
Early Development Goals
5.25-inch floppy disk drive
Structure
File Allocation Table
Advantages
Simple structure
Wide compatibility
Years
1976~1977 (Development)
Early 1980s (Public)
* 0, 1 cluster does not exist* 12,16,32, etc. based on FAT Table size

## Page 4

01
FAT 12
n = 12, 16, 32
12 = MBR + space for
index table
2n - 12
1980
12 bits
4084
32MB
FAT 16 VFAT FAT 32
1984 1995 1996
16 bits 32 bits
65524 429496729
6
2048MB 2TB
FAT 12 to 32 Comparative Analysis
4
History of FAT - FAT 12 16 32

## Page 5

Analyzing FAT32 clusters02
FAT32 Analysis
with FTK Imager
5

## Page 6

Analyzing FAT32 clusters02
Boot Sector
File Allocation Table #1
Root Directory
Data Area
FAT 32 Volume
File Allocation Table #2
FAT 32 Volume Structure
● Why is the File Allocation Table split in two?
Increase reliability and recoverability
Two tables store copies of the same information
Redundancy - protect data, improve reliability
Error recovery- error detection, data recovery
Data integrity - maintaining consistent data
FAT file systems are often used on removable storage media,
and because these media are more frequently removed and
moved between different systems, the file system structure is
more likely to become corrupted
* Root Directory
Represents the top level of the file and directory
structure; consists of 32 bytes
In FAT32, the root directory is not a fixed size, and
can grow as needed
One or more clusters can be used, forming a chain
of clusters
6

## Page 7

Analyzing FAT32 clusters02
52 52 61 41
72 72 41 61
F2 EF 03 00
10 15 00 00
00 00 00 00 00 00 00 00 00 00 00 00
00 00 55 AA
Lead Signature
Structure
signature
Free Cluster Count
Nest Free Cluster
Trail Signature
FSINFO (file System Information) Structure
Free Cluster Count :
Stores the total number of free clusters available on the volume
52 52 61 41 Lead Signature
Structure signature
Free Cluster Count
Nest Free Cluster
Trail Signature
Next Free Cluster :
Stores the number of the next free cluster the file system can store a file on
7

## Page 8

03
Check the
volume
information
Find
unallocated
area
Assign cluster
and write data
Find directory Create directory
entry
Update
directory entry
Construct a
chain of clusters
File creation process
within FAT32
8
FAT32 Creation Deletion Repair Process

## Page 9

03
Check volume
information Find the file Update
directory entry
Find directory Update FAT
The process of deleting
files within FAT32
9
FAT32 Creation Deletion Repair Process

## Page 10

FAT32 생성 삭제 복구 과정03
Check volume
information
FAT scan and
cluster chain
tracing
File integrity
check
Find deleted
directories
File data
recovery
File Recovery Process
within FAT32
10
FAT32 Creation Deletion Repair Process

## Page 11

FAT32 생성 삭제 복구 과정03
00 02  |  Bytes Per Sector (512)
08  |  Sector Per Cluster (8)
EA 0F  |  Reserved Sector Count
00  |  Hidden Sector
00 48 20 00  |  Total Sector
02  |  Root Dir Cluster
06  |  Boot Record Backup Sec
0B 08 00 00  |  FAT Size 32
Boot Sector Structure Accessing files
within FAT32
* Reserved Sector Count
Part of the BIOS Parameter Block (BPB) in
the boot sector that indicates the total
number of reserved sectors located at the
beginning of the file system
These reserved sectors are used to store
metadata for the file system
11
FAT32 Creation Deletion Repair Process

## Page 12

FAT32 생성 삭제 복구 과정03
Reserved Sector
Count FAT AREA
ROOT DIRECTORY Reserved Sector
Count FAT Size 32
DATA AREA Reserved Sector
Count FAT Size 32 x 2
00 02  |  Bytes Per Sector (512)
08  |  Sector Per Cluster (8)
EA 0F  |  Reserved Sector Count
00  |  Hidden Sector
00 48 20 00  |  Total Sector
02  |  Root Dir Cluster
06  |  Boot Record Backup Sec
0B 08 00 00  |  FAT Size 32
EA 0F FAT AREA
ROOT DIRECTORY EA 0F 0B 08 00 00
DATA AREA EA 0F ( 0B 08 00 00 ) x 2
Accessing files
within FAT32
FAT32 생성 삭제 복구 과정
12
FAT32 Creation Deletion Repair Process

## Page 13

FAT32 생성 삭제 복구 과정03
Directory Entry Structure
Accessing files
within FAT32
Directory Entry
A 32-byte structure that stores metadata about a file or directory
Each file or directory has one or more of these entries within
every directory, including the root directory
FAT32 생성 삭제 복구 과정
13
FAT32 Creation Deletion Repair Process

## Page 14

FAT32 생성 삭제 복구 과정03
Directory Entry Structure
Accessing files
within FAT32
File Name | 8bytes
Extension | 3bytes
File Attributes | 1bytes
Reserved | 1bytes
Create Time Tenth of Second | 1 bytes
Create Time | 2bytes
Create Date | 2bytes
Last Access Date | 2bytes
High 2 bytes of first cluster | 2bytes
Write Time | 2bytes
Write Date | 2bytes
Low 2 bytes of first cluster | 2bytes
File Size | 4bytes
Total 32 bytes
FAT32 생성 삭제 복구 과정
14
FAT32 Creation Deletion Repair Process

## Page 15

FAT32 생성 삭제 복구 과정03
{ DATA AREA (HIGH + LOW – Root
Directory)  x 8 }
Where the files are
located512
{ 8196 (0 + 5 – 2 )  x 8 }
Where the files are
located512
Accessing files
within FAT32
FAT32 생성 삭제 복구 과정
15
FAT32 Creation Deletion Repair Process

## Page 16

FAT32 생성 삭제 복구 과정03
HIGH LOW
High Cluster Number
Higher 16 bits of a 32-bit
cluster number
Low Cluster Number
Lower 16 bits of a 32-bit
cluster number
Accessing files
within FAT32
Start Cluster Number
FAT32 생성 삭제 복구 과정
16
FAT32 Creation Deletion Repair Process

## Page 17

FAT32 생성 삭제 복구 과정03
Accessing files
within FAT32
Real - Data Area
Structure
* Data Area
In a FAT32 file system, the Data Area is the
area that stores the actual data of files and
directories
Serves as data allocation and management,
fragmentation, data recovery, and available
space management
FAT32 생성 삭제 복구 과정
17
FAT32 Creation Deletion Repair Process

## Page 18

FAT32 생성 삭제 복구 과정03
4A 2C 02 00  |  FILE SIZE
File start location File size
Last address of the
file
Accessing files
within FAT32
FAT32 생성 삭제 복구 과정
18
FAT32 Creation Deletion Repair Process

## Page 19

FAT32 생성 삭제 복구 과정03
File Name 8bytes
FAT32 생성 삭제 복구 과정
19
FAT32 Creation Deletion Repair Process
*0x00: If the first byte of a directory entry is 0x00, this indicates that there are no more
valid entries at the current location. This indicates the end of the directory.
0x2E: This value indicates that the directory entry is a special entry that points to the
current directory (".") or a parent directory (".")
* A directory entry for a file that has not been deleted:
If the file or directory has not been deleted, the first byte of the directory entry
represents the first character of a valid filename. This can be a value between 0x01 and
0xFF, which corresponds to either a standard ASCII code or an extended character set.
Entries marked for deletion:
When a file is deleted, the first byte of the directory entry for that file is set to 0xE5. This
value indicates that the file or directory has been deleted, and its entry is no longer
considered a valid file by the file system.
