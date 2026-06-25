---
title: "06강_Disk_Forensic_(3)_v1.2 (1)"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\06강_Disk_Forensic_(3)_v1.2 (1).pdf"
source_size_bytes: 544920
source_modified: 2025-10-18T19:34:55
imported_at: 2026-06-14T14:24:57
tags:
  - acs
  - acs-advanced
  - imported
---

# 06강_Disk_Forensic_(3)_v1.2 (1)

- Source: [06강_Disk_Forensic_(3)_v1.2 (1).pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/06%EA%B0%95_Disk_Forensic_%283%29_v1.2%20%281%29.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Disk Forensic (3)
• FAT32 compared to exFAT
• Analyzing exFAT file system structure
• Analyzing the exFAT creation deletion recovery process
06
1

## Page 2

FAT32 compared to exFAT01
About exFAT
(Extended File Allocation Table)
FAT64 Large storage
devices
Support for
Unicode
Single file
size limit X MS Patents
2

## Page 3

FAT32와 exFAT의 비교01
About exFAT
(Extended File Allocation Table)
Variable Sector Size
(512 to 4096)
Maximum cluster size
Subdirectory size VBR with 9 sectors in
size
Increased number of
subdirectory files
(up to 2796202)
OEM parameter sectors
Original Equipment Manufacturer
May include technical parameters that are
adjusted during the manufacturing process
to optimize the performance of a particular
part or product
OEM parameter sectors
FAT32 compared to exFAT
3

## Page 4

FAT32와 exFAT의 비교01
exFAT
(Extended File Allocation Table)
File size limit
Volume size limit
FAT32
(File Allocation Table)
Compatibility
File allocation tables
Comparison items
FAT32 compared to exFAT
4

## Page 5

exFAT 파일 시스템 구조 분석02
exFAT exFAT Structure
The structure of the file system, the size of the cluster, the
location of the FAT table, etc.
Backup Main Boot Region
Track where files and directories are located on a drive
Where the actual data is stored
Main Boot Region
Backup Boot Region
FAT Region
Data Region
* Region
Meaning of physical or logical regions on storage media
Each region is an area allocated to store a specific type
of data or perform a specific function
nIn the context of a file system, a "Region" is a space in
the structure of a drive or storage medium that is
reserved for a specific purpose
Analyzing exFAT file system structure
5

## Page 6

exFAT 파일 시스템 구조 분석02
Sector 0 = Boot Sector
Sector 1~ 8 = Extended Boot Sector
Sector 9 = OEM Parameter Record Sector
Sector 10 = Reserved Sector
Volume Boot Record
Sector 11 = Checksum Sector
About Volume Boot Record &BPB
Jump Instruction
OEM Name
BPB
Boot Code
Volume Label
Volume GUID
Reserved Sectors
Boot Sector Signature
* BPB
An important data structure located at the beginning of a
file system that provides the information needed to
properly read and understand a bootable storage device;
contains details about how the file system is organized;
found regardless of the type of file system
6
Analyzing exFAT file system structure

## Page 7

02
Sector 0, VBR - Boot Sector
EB 76 90 Jump Command to Boot Code
45 58 46 41 54 20 20 20 File System Name
BIOS Parameter Block
Boot Program (Boot Code)
55 AA End of Sector Marker
* Why Extended BPB exists
BPBs contain basic information about a file system,
As file systems develops over time, there is a need to store
additional information
In exFAT, the Extended BPB contains information such as the
globally unique identifier (GUID) of the file system, the size of
the allocation unit, checksums, etc
The Extended BPB exists for additional information that does
not fit in the primary BPB
Bytes per Sector, Sectors per Cluster, Number of FATs
Reserved Sectors, FAT Size, Total Sectors, Root Directory Sectors
Volume Serial Number, File System Revision, Volume Flags,
Bytes per Cluster, Number of Clusters, First Cluster of the Root Directory
Extended BPB
7
Analyzing exFAT file system structure

## Page 8

exFAT 파일 시스템 구조 분석02
Address Range Size Field Name
0 x 40 ~ 47 8 Partition Offset
0 x 48 ~ 4F 8 Volume Length
0 x 50 ~ 53 4 FAT Offset
0 x 54 ~ 57 4 FAT Length
0 x 58 ~ 5B 4 Cluster Heap Offset
0 x 5C ~ 5F 4 Cluster Count
0 x 60 ~ 63 4 Root Directory First Cluster
0 x 64 ~ 67 4 Volume Serial Number
0 x 68 ~ 69 2 File System Revision
0 x 6A ~ 6B 2 Volume Flags
0 x 6C 1 Bytes Per Sector
0 x 6D 1 Sectors Per Cluster
0 x 6E 1 Number of FATs
0 x 6F 1 Drive Select
0 x 70 1 Percent in Use
0 x 71 ~ 77 7 Reserved
Sector 0,
VBR - Boot Sector
BIOS Parameter Block
8
Analyzing exFAT file system structure

## Page 9

FAT
exFAT 파일 시스템 구조 분석02
Backup Volume Boot Record
In 12~ 23 Sector
Backup Boot Region
FAT Region
In 0x 50 ~ 0x 53
FAT #1 FAT #2
4bytes
FAT Offset
Why 2 FATs?
1. Backup in case of corruption and errors
2. 2. Allows for comparative analysis
9
Analyzing exFAT file system structure

## Page 10

exFAT 파일 시스템 구조 분석02
Within the DATA Region of the file system
Consists of a set of clusters that actually store data
Cluster Heap
* Key functions and features of Cluster Heap
Storing Data
Cluster management
Efficient use of space
File System Integrity
Data Region
Cluster Heap
Cluster
Cluster
Cluster
Cluster
Cluster
Cluster * Cluster = The basic unit for storing data in a file system
* Heap = A region of memory where programs are dynamically
allocated memory while running.
exFAT 파일 시스템 구조 분석
10
Analyzing exFAT file system structure

## Page 11

exFAT 파일 시스템 구조 분석02
Use a total of 10 Directory Entries, including the most basic
directory for the entire file system
Root Directory
9
7
5
3
1 2
4
6
8
Root
Directory
Volume Label Directory Entry
Allocation Bitmap Directory Entry
Supported by Windows CE Version only
Up-Case Directory Entry
Volume GUID Directory Entry
TexFAT Padding Directory Entry
Supported by Windows CE Version only
Windows CE Access Control Table Directory Entry
File Directory Entry
Stream Extension Directory Entry
File Name Extension Directory Entry
* Directory Entry : Size - 32bytes, has Type Code
exFAT 파일 시스템 구조 분석
11
Analyzing exFAT file system structure

## Page 12

exFAT 파일 시스템 구조 분석02
Entry
Type
Volume Label
Char
Cnt Volume Label
Reserved
DATA Region Directory Entry
Volume Label Directory Entry
• Entry Type: A field that identifies the type of entry
• * Char Cnt: Character Count The number of characters
contained in the volume label
• * Volume Label Length: Field indicating the length of the
volume label
• * Volume Label: Character data of the actual volume label
• * Reserved: Space reserved for system use
Typically, only one Volume Label Directory Entry exists per file system
Who Am I ?
A special type of directory entry that contains
important information within an exFAT file system
This entry is used to store the name of the volume,
and is primarily used to make the file system
identifiable to users
exFAT 파일 시스템 구조 분석
12
Analyzing exFAT file system structure

## Page 13

exFAT 파일 시스템 구조 분석02
Entry
Type
Reserved
Bitmap
Flags Reserved
Data LengthFires Cluster
Who Am I ?
Track the allocation status of clusters in
the DATA Region of a file system
Used to point to a bitmap that indicates
whether each cluster is busy or not
Entry Type: A field that identifies the type of entry. Allocation Bitmap
Directory Entry is assigned a specific value
Bitmap Size: Indicates the size of the bitmap. This means the total
number of bytes occupied by the bitmap
First Cluster: The number of the first cluster where the bitmap data starts
Reserved: The space reserved for system use
exFAT 파일 시스템 구조 분석
DATA Region Directory Entry
Allocation Bitmap Directory Entry
13
Analyzing exFAT file system structure

## Page 14

exFAT 파일 시스템 구조 분석02
Entry
Type
Reserved 2
Reserved 1 Reserved 2
Data Length
Table Checksum
First Cluster
Who Am I ?
Unify the case of file names to make
them to make them comparable
Required when the file system
handles file names in a case-
insensitive case-insensitive way of
handling filenames
Entry Type: This field identifies that the entry is an Up-Case Table Directory Entry
Table Checksum: The checksum of the Up-Case table, which is used to verify the integrity of the table
Reserved1: Reserved field, typically set to 0
Table Length: The length of the Up-Case table in bytes
Reserved2: More reserved fields, typically set to 0
First Cluster: The location of the first cluster where the Up-Case table data starts
Reserved3: Additional reserved fields
exFAT 파일 시스템 구조 분석
DATA Region Directory Entry
Up-Case Table Directory Entry
14
Analyzing exFAT file system structure

## Page 15

02
Entry
Type
Volume GUID
2nd
Cnt Volume GUID
Reserved
Set
Checksum
General
Primary flags
Who Am I ?
Used to store a unique volume
identifier, which is important in the
management and maintenance of file
systems
*GUID = Globally Unique Identifier
Has a unique value
Entry Type: This field identifies that the entry is a Volume GUID Directory Entry
Volume GUID: A unique identifier that is 16 bytes long. This value is used to uniquely identify the volume
Reserved: The space reserved for use by the system. This space is typically filled with 0
Volume Serial Number: The volume serial number, which can be used to further identify the volume
DATA Region Directory Entry
Volume GUID Directory Entry
exFAT 파일 시스템 구조 분석
15
Analyzing exFAT file system structure

## Page 16

exFAT 파일 시스템 구조 분석02
Entry
Type
Last Accessed Time
2^nd
Cnt Created Time
Reserved
Set
Checksum
Creat
e
10ms
File
Attributes Reserved Last Modified Time
Last
mod
Creat
e
TZ
Last
mod
TZ
Last
Acc
TZ
Who Am I ?
Stores information about files
Contains metadata about a file, such as the file's name,
size, timestamp, attributes, and information about where
the file data is stored
Entry Type: This field identifies that the entry is a File Directory Entry. It is assigned a
specific value to indicate that it is an entry for a file
Secondary Count: Indicates the number of Secondary Directory Entries associated
with this file
Set Checksum: The checksum of the entry set, including all Secondary Directory
Entries associated with the File Directory Entry
File Attributes: Fields that represent the attributes of the file, including information
such as whether the file is read-only or hidden
Reserved1: The space reserved for system use
Create Timestamp: Information about when the file was created
Last Modified Timestamp: Information about when the file was last modified
Last Accessed Timestamp: Information about when the file was last accessed
* Create 10ms – Creation 10 Milliseconds
* Last mod – Last Modified
* Create TZ – Creation Time Zone(Time zone)
* Last mod TZ – Last Modified Time Zone
* Last Acc TZ – Last Access Time Zone
DATA Region Directory Entry
File Directory Entry
exFAT 파일 시스템 구조 분석
16
Analyzing exFAT file system structure

## Page 17

exFAT 파일 시스템 구조 분석02
Entry
Type
Reserved3
Gen
2^nd
Flags
Reserved
Reser
ved1
Name
Len
Reserved
2 Valid Data Length
First Cluster
Name
Hash
Who Am I ?
Associated with the File Directory Entry
and provides additional information
about the data stream of the file
Contains metadata about the actual
data content of the file
Entry Type: This field identifies that the entry is a Stream Extension
General Secondary Flags: Contains flags for additional data
Reserved1: Not used, typically set to 0
Name Length: Indicates the length of the associated file name (the name is stored in the File
Directory Entry)Name Hash: A hash value of the file name, used for quick search and integrity
checking
Reserved2: Unused, usually set to 0
Valid Data Length: Indicates the actual data length of the file. This value can be different
from the logical size of the file
Reserved3: Not used, typically set to 0
First Cluster: The number of the first cluster where the file data is stored
Data Length: Indicates the total length (size) of the file data in bytes
DATA Region Directory Entry
Stream Extension Entry
exFAT 파일 시스템 구조 분석
17
Analyzing exFAT file system structure

## Page 18

exFAT 파일 시스템 구조 분석02
Who Am I ?
Used to store file names
Used in conjunction with a File Directory Entry to allow
the full name of the file to be stored
Because exFAT supports long file names, if the file name
exceeds the length that can be stored in a File Directory
Entry, one or more File Name Extension Entries are used
Entry Type: A field that identifies the entry as a File Name Extension Entry
General Secondary Flags: Stores additional flags associated with the file name
File Name Characters: Stores the string portion of the file name. The characters
are typically encoded in UTF-16 format
Reserved: Space reserved for system use, usually unused
DATA Region Directory Entry
File Name Extension Entry
exFAT 파일 시스템 구조 분석
18
Analyzing exFAT file system structure

## Page 19

exFAT 파일 시스템 구조 분석02
Entry
Type
Reserved
Reserved
DATA Region Directory Entry
Windows CE Access Control Table Directory Entry
Who Am I ?
Information that can only be found in detailed internal documentation about the design and implementation of the file system
An Access Control Table (ACT) is used to define access permissions to a file or directory; the exact structure is not confirmed
*Windows CE, made to work efficiently even on resource-constrained devices
 CE = Compact Edition
exFAT 파일 시스템 구조 분석
19
Analyzing exFAT file system structure

## Page 20

exFAT 파일 시스템 구조 분석02
Approach
The FAT AREA
* Information you can get from FAT AREA
File and Directory allocation information
Free and used space on the file system
The allocation status of a cluster
Checking the integrity of the file system
Trace the size and path of a file
exFAT 파일 시스템 구조 분석
20
Analyzing exFAT file system structure

## Page 21

Approach DATA Region Cluster Heap Offset
exFAT 파일 시스템 구조 분석02
Cluster Heap
In 0x 58 ~ 0x 5B
42ytes
In VBR
exFAT 파일 시스템 구조 분석
21
Analyzing exFAT file system structure

## Page 22

exFAT 파일 시스템 구조 분석02
Approach DATA Region Up-Case Table
CHS
1638
4
2
1024
2
512
UP-Case
Table
891289
6
+ =
BPS SPC
*CHS = Cluster Heap Sector
*BPS = Bytes Per Sector
*SPC = Sectors Per Cluster
exFAT 파일 시스템 구조 분석
22
Analyzing exFAT file system structure

## Page 23

exFAT 파일 시스템 구조 분석02
Approach DATA Region Directory Entry
SPC
CHS
1638
4
2 x 2
2048
2
512
UP-Case
Table
891289
6
+ =
BPS
Reason for multiplying by 2: Minimum size of Directory Entry
= twice the sector size
exFAT 파일 시스템 구조 분석
23
Analyzing exFAT file system structure

## Page 24

Analyzing the exFAT creation deletion recovery process03
Explore
available
clusters
Save Data Update
directory entries
Create a new
directory entry
Update
Allocation
Bitmap
Creating exFAT My Test.txt file’s
creation process
24

## Page 25

exFAT 생성 삭제 복구 과정 분석03
Browse
Directory Entry
Update
Allocation
Bitmap
Maintain
integrity
Delete Directory
Entry Release clusters
Deleting the Test.txt file
within an exFAT creation
25
Analyzing the exFAT creation deletion recovery process

## Page 26

exFAT 생성 삭제 복구 과정 분석03
Find deleted
directory entries
Restore the
Directory Entry
Restore file
accessibility
Check the
Allocation
Bitmap
Update
Allocation
Bitmap
Recovery process of Test.txt file
within exFAT creation
File recovery is only possible if the data in the deleted file has not been overwritten
26
Analyzing the exFAT creation deletion recovery process
