---
title: "07강_Disk_Forensic_(4)_v1.2 (1)"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\07강_Disk_Forensic_(4)_v1.2 (1).pdf"
source_size_bytes: 711029
source_modified: 2025-10-18T19:34:58
imported_at: 2026-06-14T14:24:59
tags:
  - acs
  - acs-advanced
  - imported
---

# 07강_Disk_Forensic_(4)_v1.2 (1)

- Source: [07강_Disk_Forensic_(4)_v1.2 (1).pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/07%EA%B0%95_Disk_Forensic_%284%29_v1.2%20%281%29.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Disk Forensic (4)
• Features of NTFS
• Structure of NTFS
• Create and Delete NTFS
• NTFS Tools
07
1

## Page 2

Features of NTFS01
* USN Journal = Update Sequence Number Journal
* VSS = Volume Shadow Copy
* EFS = Encrypting File System
New Technology File System
Features of NTFS
EFS
High-
volume
support
Dynamic
Beds Cluster
assignment
QuotasVSS
Files
Compress
Sparse
File
ADS
USN
Journal
* ASD = Alternate Data Streams
* Sparse = sparse files
2

## Page 3

Features of NTFS01
New Technology File System
The need for a better
filesystem for servers than FAT
Enhanced security features
Transactions and Unicode
support
Managing disk quotas
* Transaction: something that bundles a
series of actions into one unit
3
Features of NTFS

## Page 4

Features of NTFS01
FAT32
(File Allocation Table)
NTFS
(New Technology File System)
16 EB 4 GB
Granular permission
control over files and
folders and file encryption
Fully compatible with
Windows OS only
Transaction-based
logging features
Own advanced security
features X
Compatible with most
operating systems
Feature X
Simplicity of structure easily restored
Security
Durability
and recovery
Maximum size
of a single file
Compatibility
4

## Page 5

Structure of NTFS02
Volume Boot Record
Master File Table
Data Area
NTFS Structure
Boot information, located in the first
sector of the disk and written at the
beginning of the volume
A centralized database that holds
information about all files and
directories
Areas that store physical file data and
directory data, holding large amounts
of real data
5

## Page 6

Structure of NTFS02
NTFS
Volume Boot Record
= Boot Sector
The area at the very beginning of an NTFS formatted partition
Contains initial information and code needed to load the operating system when the system boots up
Indicates that NTFS is a more complex, higher performance file system compared to the FAT file system
6

## Page 7

Structure of NTFS02
OFFSET Size Field Name
00 ~ 02 3 Jump Instruction
03 ~ 0A 8 OEM ID
0B ~ 23 25 BPB
24 ~ 53 48 Extended BPB
54 ~ 1FD 426 Bootstrap code
1FD~ 1FF 2 End of sector marker
(Signature)
7

## Page 8

Structure of NTFS02
Jump Boot
Code
Unused
Unused
Start Cluster for $MFT
VBR Size = Cluster Size
Unused
Reserved
Sectors
Sec
Per
Clus
Bytes per
SectorOEM ID
Medi
a Unused
Total Sectors
Start Cluster for $MFTMirr
Unused Unused
Clus
Per
Index
Clus
Per
Entry
8

## Page 9

Create and Delete NTFS03
Setting the In-Use Flag
Set bit to 1
Reading the root directory
Finding dir1 using an index
Assigning MFT Entry
Read the location of the MFT
Create a new index entry
NTFS
Create
File
Discover free clusters
File Contents,
Create $DATA Property
Determine the location of the file
Initialize the
$STANDARD_INFORMATION,MFT
Entry Property
Find an MFT Entry
Log each step to $Log File
9

## Page 10

Create and Delete NTFS03
영구 삭제
Waiting for reuse state
Change MFT Entry
(name, size, modification
date, etc... )
Recycle
bin
Remove Filename from
INDEX
Set the corresponding
position of $Bitmap to 0
Reading the root directory
Finding dir1 using an index
Read the location of the MFT
Unassigning an MFT Entry
Remove IN-Use Flag
Save those steps to $LogFile
Find the location of File1
First MFT Entry
10

## Page 11

Create and Delete NTFS03
Deleted files
When a file is deleted, the 'In-Use' flag in
the Master File Table (MFT) entry for that
file is set to 0x0000, indicating that it is
unused
However, most of the other information in
the MFT entry remains intact, such as the
file's name, creation time, modification
time, etc.
Delete the file name from the MFT entry in
the directory that was pointing to the file
It is possible to trace back the MFT entry of
the parent directory from the MFT entry of
the deleted file
Important information to determine which
directory the file belonged to
Manage a list of all files in a single
directoryUpdating the index every time
a file is added or deleted in a directory
If the name of the file is not in DOS
format, that is, not in 8.3 format, two
index entries are created
One for the original file name and one
for the name created for DOS
compatibility
The index entry contains the
$FILE_NAME attribute, which contains
information such as the file's name,
creation time, modification time, etc.
Index file
N
S
F
T
11

## Page 12

NTFS Tools04
NTFS TOOL
NTFS Walker
Download Link : dmirtybrant.com/ntfswalker
12

## Page 13

NTFS Tools04
What it looks
like when you
run NTFS
Walker
*Requires administrator
privileges to run
Select disk to scan
1.Physical Media
2.Logical Drives
What it looks
like when you
select a disk to
scan
*Only NTFS can be
selected
Select Partition
13

## Page 14

NTFS Tools04
MFT Entry
Number
File Name
Size
Date
Created
Date
Modified
Attributes
A number that uniquely
identifies a file or folder
The name of the file or folder
File Size
Displayed in bytes
Date and time the file or folder
was created
The date and time the file or
folder was last modified
Additional property information
about a file or folder
14

## Page 15

NTFS Tools04
File Information Preview Hex Data
Restored appearance 15

## Page 16

NTFS Tools04
Sequence
Number
Hard Link
Count
Record Size
Record
Allocated Size
Basic
Information
The sequence number of the Master File Table (MFT)
record to which the file belongs
Incremented each time the file is deleted and its MFT
record is reused
The number of hard links to a file or directory
References to the same file content in different
locations within the file system
The actual size of the MFT record
The amount of space used to store the file's metadata
Total size allocated to MFT records
Maximum space a record can occupy
16

## Page 17

NTFS Tools04
Flags
Mex version
Version
Number
Class ID
Standard
Information
The file's attribute flags, which include information
such as whether the file is a hidden file, a system file,
encrypted, etc.
Maximum version number you can set for file
versioning
The current version number of the file. Used for
versioning files
The class identifier associated with the file, which
contains information about the file belonging to
a specific program or application
Why Attribute type 0x10?

"0x10" is a number expressed in hexadecimal, a unique
number that identifies the attribute type
NTFS identifies each file attribute with a unique type
number"0x10" is the "Standard Information" attribute, which
contains basic metadata information about the file
Create Time: The date and time the file was created
Modified Time: The date and time the file was last modified
MFT Changed Time: The date and time the file's MFT record was last changed,
updated when the file's metadata changes as well as changes to the file itself
Last Access Time: The date and time the file was last accessed
Time-Related0
17

## Page 18

NTFS Tools04
Parent directory
ref
Allocated size
Actual size
Reparse
File
Name
References the MFT record number of the parent
directory where the file is located, allowing the
file system to track the path to the file
The size of the total space allocated to the file
Can be larger than the actual size of the file,
determined by the cluster size of the file system
The actual size of a file
The amount of data the file actually uses
Whether a file has reparse points
Reanalysis points are used to specify additional
data or special behavior for a file or folder
Name
namespace
Name
Indicates the namespace to which the file name belongsNTFS
supports several types of namespaces (e.g., POSIX, Win32,
DOS) to provide compatibility in different environments
The actual name of the file or folder
Reasons for duplicate time information
NTFS redundantly records time information in "Attribute Type 0x10 - Standard Information" and
"Attribute Type 0x30 - File Name" because of a design strategy to maintain data integrity and
accessibility in the file system
To improve the performance of file browsing and searching by making it easier to reference time
information even when files are renamed or moved.
NTFS uses this redundant storage approach to maximize the efficiency and reliability of the system
18

## Page 19

NTFS Tools04
Type
Length
ID
Data runs
Data
The sequence number of the Master File Table
(MFT) record to which the file belongs
Incremented each time the file is deleted and its
MFT record is reused
Number of hard links to a file or directory
References to the same file content in different
locations within the file system
The actual size of the MFT record
The amount of space used to store the file's metadata
Total size allocated to MFT records
Maximum space a record can occupy
Attribute type 0x80 - What is Data
Attributes play a key role in managing the body data of a file in
the NTFS file system
An important mechanism for storing a file's contents on disk and
enabling access to and management of the actual data in the file
This attribute allows NTFS to provide advanced file system
capabilities, supporting a variety of data management features
such as encrypting, compressing, and handling sparse files
19
