---
title: "08강_Disk_Forensic_(5)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\08강_Disk_Forensic_(5)_v1.2.pdf"
source_size_bytes: 535919
source_modified: 2025-10-02T12:26:07
imported_at: 2026-06-14T14:24:59
tags:
  - acs
  - acs-advanced
  - imported
---

# 08강_Disk_Forensic_(5)_v1.2

- Source: [08강_Disk_Forensic_(5)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/08%EA%B0%95_Disk_Forensic_%285%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Disk Forensic (5)
• What is MFT
• MFT Structure
• MFT Tools
08
1

## Page 2

What is MFT01
MFT
(Master File Table)
An integral part of the file system area
structure of Window's architecture,
the New Technology File System
(NTFS), which serves to store metadata
about all files and directories
Volume Boot Record
Master File Table
Data Area
NTFS Structure
2

## Page 3

MFT Structure02
Jump Boot Code
Unused
Unused
Start Cluster for $MFT
VBR Size = Cluster Size
Unused
Reserved
Sectors
Sec
Per
clus
Bytes per
SectorOEM ID
Media Unused
Total Sectors
Start Cluster for $MFTMirr
Unused Unused
Clus
Per
Index
Clus
Per
Entry
3

## Page 4

MFT Structure02
$MFT cluster start position = C0000 x ( SPC = 8 )
$MFTMirr cluster start position = 2 x ( SPC = 8 )
4

## Page 5

MFT Structure02
Volume Boot Record
MFT Entry 0
Data Area
NTFS Structure
MFT Entry 1
MFT Entry 2
…
…
MFT Entry 10
MFT Entry 11
…
…
MFT
Specially
reserved areas
MFT Cluster
Starting location
5

## Page 6

MFT Structure02
Entry Number Entry Name
MFT Entry 0 $MFT
MFT Entry 1 $MFTMirr
MFT Entry 2 $LogFile
MFT Entry 3 $Volume
MFT Entry 4 $AttrDef
Metadata about the $MFT itself
Ex) Location and size of the MFT
Mirror Image of $MFT
Copy and save the first few records in the MFT
Helps recover from MFT corruption
Transaction Log Files on a System
Maintain consistency of the NTFS file system
Contribute to data recovery after a system crash or
abnormal shutdown
Metadata on the volume
EX) Name of the volume, serial number, last mount
time, etc.
Contains information about the attribute definition
table, which contains definitions of all file and directory
attributes used in the NTFS file system
6

## Page 7

MFT Structure02
Entry Number Entry Name
MFT Entry 5 Root Directory
MFT Entry 6 $Bitmap
MFT Entry 7 $Boot
MFT Entry 8 $BadClus
MFT Entry 9 $Secure
Root directory of a file system
The top-level hierarchy of the file system
Cluster bitmap to track space allocation on NTFS
volumes
Shows how much disk space is in use or available
Information about the boot sector of a volume
Basic information and code needed to boot the system
Information about the list of bad clusters on a volume
Track physically damaged sectors on a disk
Manage security permissions for files and folders
Define access permissions for files and directories
7

## Page 8

MFT Structure02
Case mapping table used for case-insensitive
comparisons on the file system
Entry Number Entry Name
MFT Entry 10 $Upcase
MFT Entry 11 $Extend
MFT Entry 12
MFT Entry 13
MFT Entry 14
MFT Entry 15
…
A special-purpose directory that holds the extension
attributes of NTFS system files
Let’s Learn
about
$Extend
8

## Page 9

MFT Structure02
MFT Entry 24: $Quota
Manages per-user or per-group disk usage quota information.
Allows system administrators to monitor usage and set limits
MFT Entry 25: $ObjId
Provides a unique identifier for a file or directory. This does not
change when the file is moved within the volume and is primarily
used to track files in a distributed file system
MFT Entry 26: $Reparse
Stores information about reparse points. This supports the ability
to store additional data about a file or directory, or to redirect a
file to other location
MFT Entry 27: $ReMetadata
Stores transactional NTFS (TxNTFS) related metadata. This is used
to ensure the reliability and consistency of file system
transactions
9

## Page 10

MFT Structure02
MFT Entry 28: $Repair
Can contain information used for file system repair operations.
Supports NTFS's self-repair feature
MFT Entry 30: $TxfLog
Manages transactional NTFS related log files. This log is used to
maintain consistency of NTFS transactions
MFT Entry 33: $TxfLog.blf
The real name of the transactional NTFS log file. This file is used for
transaction logging and contains transaction information on the
system
*MFT Entry : $UsnJrnl
The $UsnJrnl manages information in the Update Sequence Number
Journal, which tracks changes to the file system
It records all changes that have occurred to the file system so
that system restores, file recovery, backup software, etc. can
quickly identify and process changed files
Unofficial
Unofficial
Unofficial
* $UsnJrnl
10

## Page 11

MFT Structure02
If you have attribute numbers that are not formally
documented
Internal or experimental use: Some attribute numbers may be used
internally or for experimental purposes by Microsoft
These attributes do not appear in published documentation and may
only be used in certain versions of Windows or under certain
circumstances
System extensions: NTFS has evolved over time and new features have
been added
Some attribute numbers may have been introduced to support these
new features or extensions, and may not yet be officially documented
Out of use or hidden features: There may be attribute numbers that
were used in the past but have been discontinued in later versions, or
that are reserved for hidden features. These properties might be
related to features that the average user or developer doesn't need
access to
A detailed descriptions of attributes such as "Deleted", "Txf", and
"Tops" are difficult to find in published NTFS documentation
"Txf" may be related to Transactional NTFS, which is the ability to
support transactions at the file system level
Not much is known about "Tops" and "Deleted" officially, and it is
possibly attributes used for specific internal purposes or experimental
features
Unofficial
Unofficial
Unofficial
* $UsnJrnl
11

## Page 12

MFT Structure02
MFT Entry Header (48byte)
MFT Entry Structure
Fixup
Attributes
End Marker
Unused Space
12

## Page 13

MFT Structure02
MFT Entry Header
Offset Description Information
00 ~ 03 Signature Fixed the signature word 'FILE' in MFT Entry
04 ~ 05 Offset to fixup array Offset to Fixup array
06 ~ 07 Number of entries in fixup
array Entry number in the Fixup array
08 ~ 0F $Logfile Sequence Number Log file sequence number
10 ~ 11 Sequence Number Sequence number of the MFT Entry
12 ~ 13 Link count Number of links to that file/directory
13

## Page 14

MFT Structure02
MFT Entry Header
Offset Description Information
14 ~ 15 Offset to first attribute The offset to the first property
16 ~ 17 Flags (in-use and directory) Status of Entry
18 ~ 1B Used size of MFT Entry Used Size of MFT Entry
1C ~ 1F Allocated size of MFT Entry Size assigned to MFT Entry
20 ~ 27 File reference to base record File references for base records
28 ~ 29 Next attribute ID Next property ID
2A ~ 2B Align to 4-byte boundary Align data to a 4bytes boundary
2C ~ 2F This MFT Entry's number Number of the MFT Entry
14

## Page 15

MFT Structure02
속성 ID Attribute Description
0 x 10 $STANDARD_INFORMATION Standard information about the file, e.g. file creation time, modification
time, owner information, access rights, etc.
0 x 20 $ATTRIBUTE_LIST Where split attributes are stored when attributes provides a file or
directory need to be spread across multiple MFT entries
0 x 30 $FILE_NAME File name
0 x 40 $VOLUME_VERSION Version information for volumes
0 x 40 $OBJECT_ID Unique identifier for a file or directory
0 x 50 $SECURITY_DESCRIPTOR About file or directory security
0 x 60 $VOLUME_NAME Name of the volume
0 x 70 $VOLUME_INFORMATION Information about the volume
Attributes
15

## Page 16

MFT Structure02
Attributes
속성 ID Attribute Description
0 x 80 $DATA Actual file data
0 x 90 $INDEX_ROOT About directory indexes
0 x A0 $INDEX_ALLOCATION Additional index information that cannot be stored in properties
0 x B0 $BITMAP Store BITMAPs used to track MFT entries or index assignments
0 x C0 $SYMBOLIC_LINK Symbolic link
0 x C0 $REPARSE_POINT Reparse Branch
0 x D0 $EA_INFORMATION About Extended Attributes (EA)
0 x E0 $EA Actual extended attribute data
0 x 0100 $LOGGED_UTILITY_STREAM Logged utility stream information for a file
16

## Page 17

MFT Structure02
Attributes ID
What is an Attribute Identifier What are the cases of identical
property ID
The ID is used to distinguish the type of
attribute
The system uses this identifier to locate
and interpret the corresponding
attribute within the MFT entry
A hexadecimal code indicating the type
of a particular attribute
Because of the NTFS design, some
attributes are logically related or
perform similar functions
However, in general, each attribute
owns a unique ID
17

## Page 18

MFT Structure02
Resident Properties Non-Resident
Properties
If the data for that property is stored
directly inside the MFT entry, and the
amount of data is small and can fit
completely within the space of the MFT
entry
The file's metadata is stored directly in
the MFT entry.Provides fast access speed
Often used to store small files or basic
information about a file (such as file
name, creation time, etc.)
Used when the data for that property
exceeds the size of the MFT entry and
must be stored elsewhere on disk The
data is too large to fit in the MFT entry
The data is stored across a cluster on disk
The MFT entry stores a "data run" that
points to the location of this data
Requires more disk read operations to
access the data
Used to store the actual content of large
files
18

## Page 19

MFT Structure02
Resident Properties Non-Resident
Properties
19

## Page 20

VCN
Virtual Cluster Number
LCN
Logical Cluster Number
Sparse
MFT Structure02
A file format designed to save disk
space
The file does not physically allocate
any part of the disk for actual data
Used to save space on database and
backup systems
LCN is a value that represents the
physical cluster location on disk
LCN is used to determine how the file
system is using physical disk space
Specifically used to find data about the
Non-Resident attribute
A value that indicates the relative location
of a cluster within the data stream of a
file or directory
VCNs are used when referencing or
accessing data inside a file, independent
of the actual location on disk
20

## Page 21

Sparse VCN
MFT Structure02
Sparse LCN
Data run
A contiguous section on disk where the actual
data in a file is stored
Provides a mapping between the virtual cluster
number (VCN) where data starts inside the file
and the logical cluster number (LCN) of the
disk where that data is actually stored
Stored in the $DATA attribute within the file's
MFT entry and is used by the file system to
read and write file data
Used when very little data is actually used
compared to the total file size
Sparse LCN is a logical cluster number used
to indicate space that is actually
unallocated data, that is, filled with '0’
Because Sparse files do not allocate disk
space for areas with no data, the LCNs for
these areas do not actually exist or are
undefined
Sparse A virtual cluster number that
represents an virtual area within a file
where no data exists
When the file system reads these areas, it
doesn't actually read data from disk, but
instead provides data filled with '0’
Certain parts of a file are actually empty,
but make it look like there is data to
programs working with the file
21

## Page 22

Run List
MFT Structure02
In the NTFS file system, a 'Run List' is
a data structure that represents how
the actual data blocks of a file or
directory are distributed on disk
Each 'Run' represents an area on disk
where data is stored contiguously,
and the 'Run List' is a list of all these
'Runs' in order
Run List
In a sparse file, the run list only
represents the area where data is
actually stored
Empty space or areas within the file
that are filled with "0" are not included
in the run list
As a result, the run list for a sparse file
can be relatively short, and the actual
disk space usage is small relative to the
size of the file.
Sparse Files and Run Lists
22

## Page 23

MFT Structure02
12 34 56
01 23 45
Cluster Run
Header Data
Len Size Offset Size Len Size Offset Size
Real
Address
2byte 1byte 0 x 34 0 x 56
1byte 0byte 0 x 45 X
0 x 56
X
Run List Structure
23

## Page 24

MFT Structure02
Fixup Array
Located in the last 2 bytes of each sector, an
important mechanism for maintaining data integrity
Checks the integrity of the data by verifying that the
above values match the values in the Fixup Array
Sector 1 Sector 2
Fixup
Signature
Fixup
Signature
Fixup
Signature
Fixup
Array
Fixup
Signature
Fixup
Array
24

## Page 25

MFT Structure02
Updating a file
record as
"deleted"
How data is
stored based on
file size
Processing
Fixup Arrays
Add metadata
(Attributes) to
the Test.txt file
Update the
index
Changes in MFT
when generating a
Test.txt File
The reason for the 900 bytes
standard
To allow MFT records to efficiently utilize
the space left by the Resident and non-
Resident attributes
25

## Page 26

MFT Structure02
Updating a file
record as
"deleted"
Reclaiming disk
space where
the file was
stored
Update
$BITMAP
File,$LogFile
The index of
the directory
where the file is
located is
updated
Deleted files are
not
immediately
deleted
Changes in MFT
when deleting
Test.txt File
26

## Page 27

MFT Tools03
MFTECmd running
MFTECmd
Made by Eric Zimmerman
Recommended commands : .\MFTECmd.exe -f "C:\`$MFT"
--csv "C:\Users\Users\Documents"
--csvf "MFT_$(Get-Date -Format 'yyyyMMdd_HHmm').csv"
Download Link : Https://github.com/EricZimmerman/MFTECmd
27

## Page 28

MFT Tools03
C:\Users\Users\Documents\MFT_yyyymmdd_hhmm
28

## Page 29

MFT Tools03
Field Description
Entry Number The index number of the MFT entry. Each file and directory has a unique index number
Sequence Number The sequence number of the MFT entry. It is incremented when a file or directory is
created, deleted, or recreated
InUse Indicates whether the MFT item is currently in use
FileSize The size of the file
Reparse, Target Reparse point and target information. Reparse points are used to specify user-defined
behavior
Parent, Path, FileName,
Extension The parent directory, path, file name, and extension information for the file or directory
ReferenceCount The number of items that reference this MFT item
IsDirectory Indicates whether the item is a directory
HasAds Whether the file has an alternate data stream (ADS)
C:\Users\Users\Documents\MFT_yyyymmdd_hhmm
29

## Page 30

MFT Tools03
Field Description
ISAds Whether the item is an alternate data stream
Parent Entry Number,
Parent Sequence Number The MFT entry number and serial number of the parent directory
SI<FN, uSecZeros, Copied,
SiFlags, Name Type
Various file attribute information, such as consistency between the standard information
and file name attributes, the number of microsecond values set to 0 in the timestamp,
whether the file was copied, flags in the standard information attribute, and the type of
file name
created0x10, Created0x30,
LastModified0x10,
LastModified0x30,
LastRecordChange0x10,
LastRecordChange0x30,
LastAccess0x10,
LastAccess0x30
The time attributes of creation, last modification, last record change, and last access.
0x10 and 0x30 represent specific flags used in NTFS time attributes
Update Sequence Number,
Logfile Sequence Number,
Security Id, Object Id, File
Droid, Logged Util Stream,
ZoneId Contents
A value that increments when a file or directory changes, a value that identifies a specific
transaction within an NTFS log file, a value that references the security settings of a file,
a value that uniquely identifies and tracks a file, stream information that stores the
metadata of a file, and information that indicates from which area a file was
downloaded
C:\Users\Users\Documents\MFT_yyyymmdd_hhmm
30
