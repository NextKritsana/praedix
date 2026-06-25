---
title: "04강_Disk_Forensic_(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\04강_Disk_Forensic_(1)_v1.2.pdf"
source_size_bytes: 1017634
source_modified: 2025-09-24T16:21:47
imported_at: 2026-06-14T14:24:56
tags:
  - acs
  - acs-advanced
  - imported
---

# 04강_Disk_Forensic_(1)_v1.2

- Source: [04강_Disk_Forensic_(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/04%EA%B0%95_Disk_Forensic_%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Disk Forensic (1)
• The boot process of a Windows system
• MBR
• GPT
• MBR Partition Analysis
04
1

## Page 2

The boot process of a Windows system01
Demo text info Demo text info Demo text info
Power ON
When the firmware is BIOS
ntoskrnl.exe = Windows NT kernel
One of the core parts of an operating system, also known as the kernel
hal.dll = Hardware Abstraction Layer Dynamic Link Library
The Dynamic Link Library, which is part of the Hardware Abstraction Layer
(HAL)
2

## Page 3

01
Demo text info Demo text info
.efi = Extensible Firmware Interface
Firmware interface standards used during the computer boot process
3
The boot process of a Windows system
Power ON
When the firmware is BIOS

## Page 4

01
Acting as a bootloader for Windows on systems that
use a traditional BIOS boot mechanism
On BIOS systems, locates and loads bootmgr in the
first sector of the master boot record (MBR) or
startupable partition
Then responsible for selecting from the operating
systems you have installed or loading the default
operating system
Location in the root directory of the system drive
Windows acts as a bootloader on systems that use
the Unified Extensible Firmware Interface (UEFI) boot
mechanism
UEFI systems load and run the bootmgfw.efi file
directly, which is located within the EFI system
partition (ESP). Because UEFI firmware is file system
aware, it can locate and run EFI executables (.efi)
directly from an ESP formatted in FAT32
Located under the EFI\Microsoft\Boot\ directory within
the EFI system partition (=EXP)
bootmgr is a traditional executable binary file,
bootmgfw.efi is an EFI executable that can be run by UEFI firmware
bootmgr bootmgfw.efi
4
The boot process of a Windows system

## Page 5

윈도우 시스템의 부팅 과정01
winload.efi is actually the bootloader that loads the
Windows operating system kernel
It is called by bootmgfw.efi, and it initializes the system's
hardware, loads the Windows kernel into memory, and
prepares the operating system for the startup process
winload.efi loads the hardware abstraction layer (HAL),
system registry settings, drivers, and more to set up the
environment for the operating system to function normally
This process occurs before Windows' login screen appears
Located within the EFI system partition, but the exact path
can vary depending on the version and configuration of
Windows installed
\Located in the \Windows\System32\ directory
Boot Manager in Windows
Responsible for initializing and managing the system's boot
process at the beginning of the boot process
Loaded directly by the UEFI firmware, provides a user
interface for selecting between installed operating systems
or loading the default operating system
Displays a list of bootable operating systems and runs the
OS's loader (winload.efi) to load the operating system of the
user's choice
Provides access to advanced boot options and
troubleshooting tools
Located in the \EFI\Microsoft\Boot\ directory within the EFI
System Partition (ESP).
Bootmgfw.efi acts as the boot manager, which initializes the boot process and provides a selection interface between operating
systems. On the other hand, winload.efi acts as the bootloader, which actually loads the selected Windows operating system
Bootmgfw.efi is loaded directly by the UEFI firmware at a very early stage of the boot process. winload.efi is loaded by bootmgfw.efi at
the next stage, which starts the actual operating system's kernel
winload.efi bootmgfw.efi
5
The boot process of a Windows system

## Page 6

MBR02
MBR
(Master Boot Record)
Boot Code
Partition Table
Signature
446
64
2
512
Partition Table Entry #1
Partition Table Entry #2
Partition Table Entry #3
Partition Table Entry #4
MBR Structure
6

## Page 7

MBR02
Partition Table Entry
Boot Indicator1
16
Starting CHS address
Partition Type
Total Sectors
Ending CHS address
Starting LBA address
3
1
3
4
4
MBR
Partition Table Entry
Structure
Partition Table Entry
A data structure used to record partition information on a
storage device, such as a hard disk or SSD
CHS = Cylinder-Head-Sector
A way to represent where data is stored on your hard drive
LBA = Logical Block Addressing
How to specify the location of a data block on computer storage
7

## Page 8

MBR
Partition Table
Partition Table Entry #1
Partition Table Entry #2
Partition Table Entry #3
Partition Table Entry #4
Primary Extended Partition
About
Partition Table
Entry#4
8
Primary Extended Partition
Special kind of partition that creates space to create additional
logical partitions
1. Used to create logical partitions
2. MBR's 4 partition limit bypass
3. Booting partition X
02

## Page 9

MBR02
EBR
(Extended Boot Record)
Unused Data
Partition Table
Signature
446
64
2
512
Used Partition Entry #1
Used Partition Entry #2
Unused Partition Entry #3
Unused Partition Entry # 4
EBR Structure
9
EBR = Extended Boot Record
Data structure for managing logical partitions within a Primary Extended
Partition, primarily in the MBR partition table
Storing information such as the start location and size of logical partitions,
Organizes a chain with links between logical partitions

## Page 10

MBR02
MBR
Partition
EBR Location EBR
Partition
EBR Location EBR
Partition
EBR Location
How to navigate the data
structures involved in
managing logical partitions
(feat. chained)
10

## Page 11

GPT03
GPT
(GUID Partition Table)
Protective MBR
GPT Header
Partition Table
512
bytes
92
bytes
Maximum
128
Partition Table Entry #1
Partition Table Entry #2
…
Partition Table Entry #128
GPT Structure
GPT: A standard that defines the partitioning structure of hard drives
Alternative to MBR designed to support larger storage devices and more
partitions larger storage devices and more partitions
11

## Page 12

GPT03
GPT
(GUID Partition Table)
128
9.4ZB
The end of the disk
Late 1990s
(U)EFI
MBR
(Master Boot Record)
4
2TB
X
Early 1980s
BIOS
Primary
partition
Disk capacity
Partition
backup
Announce
Firmware
MBR | GPT
Compare
12

## Page 13

GPT03
GPT
(GUID Partition Table)
Protective MBR0
34-
2047
Las
t
Primary GPT Header
Primary GPT Partition Entries
Data Partitions
Secondary GPT Partition Entries and Header
1
2-33
GPT Structure
13
GPT
Identify partitions with a unique identifier
(GUID) for each partition
Ensures uniqueness of partitions
Increases compatibility between systems
Supports 2^64 logical block addresses
Storage devices up to 9.4 ZB (zettabytes; 1
ZB = 10^21 bytes) in theory
Stores copies of the header and partition
table at the front and back of the disk,
respectively
The default partitioning method for booting
on EFI systems, but some operating
systems also support the use of GPT drives
in legacy BIOS mode

## Page 14

GPT03
GPT Partition Table Header
1 2 3
4 5 6
7 8
9
10
10
11
12 13 14 15
1
2
3
4
5
6
8byte Signature('EFI PART' 0x45 46 49 20 50 41 52 54)
4byte Revision number of header (0x00 01 00 00)
4byte Header size (0x00 00 00 5C)
4byte CRC32 of Header
4byte Reserved
8byte Current LBA
GPT Partition Table
Header Structure
LBA = Logical Block Addressing
A method for locating of data block on a computer storage device
Revision Number
A number that typically represents a version of software or hardware
14

## Page 15

GPT03
7
8
9
8byte Backup LBA
8byte First usable LBA for partitions
8byte Last usable LBA
16byte Disk GUID in mixed endian10
GPT Partition Table
Header Structure
GPT Partition Table Header
1 2 3
4 5 6
7 8
9
10
10
11
12 13 14 15
15
Disk GUID
Used to uniquely identify storage devices
Managed by GTP partitions recognize that they belong to a
storage device by referencing its Disk GUID

## Page 16

GPT03
11
12
13
14
15
8byte Starting LBA of array of partition entries
4byte Number of partition entries in array
4byte Size of a single partition entry
4byte CRC32 of partition entries array
Reserved
GPT Partition Table Header
1 2 3
4 5 6
7 8
9
10
10
11
12 13 14 15
GPT Partition Table
Header Structure
16

## Page 17

GPT03
GPT Partition Entry ( 128 byte)
16byte Unique partition GUID
8byte First LBA
8byte Last LBA
8byte Attribute flags
72byte Partition name
16byte Partition type GUID
Bootable partition (1)
Read Only (2)
Hidden Partition (3)
This partition is unused  (4)
Integrity Protection (5)
System Partition (0)
GPT Partition Table
Entry Structure
17

## Page 18

MBR Partition Analysis04
01
STEP
FTK Imager
File – Create Disk Image
 02
Select
Physical Drive
Logical Drive
03 Select drives
Image dump with FTK Image
18
STEP STEP

## Page 19

06
05
MBR Partition Analysis04
04
STEP STEP STEP
Three choices for features Select Image Type Add Image File
Image dump with FTK Image
19

## Page 20

09
08
MBR Partition Analysis04
07
STEP STEP STEP
Evidence Item Information Image Destination Folde
& Image File name Creating Image
Image dump with FTK Image
20

## Page 21

13
12
MBR Partition Analysis04
11
STEP STEP STEP
Dumped image files File - Add Evidence Item Select Image File
21
Image dump with FTK Image

## Page 22

MBR Partition Analysis04
MBR
(Master Boot Record)
Boot Code
Partition Table
Signature
446
byte
Boot Code Structure
22

## Page 23

MBR Partition Analysis04
MBR
(Master Boot Record)
Boot Code
Partition Table
Signature
16 x 4
64
Partition Table Entry #1
Partition Table Entry #2
Partition Table Entry #3
Partition Table Entry #4
Partition Table Structure
23

## Page 24

MBR Partition Analysis04
Partition Table Entry #1
0x 00 02 03 00 07 8E 0C 02 80 00 00 00 00 A0 00 00
Partition Table Entry
Boot Indicator
16
Starting CHS address
Partition Type
Total Sectors
Ending CHS address
Starting LBA address
1
3
1
3
4
4
0x 00 = Non-bootable partition
0x 02 03 00 = Startup location of that partition
0x 07 =  Advanced Unix, exFAT, OS/2 HPFS, Windows NT NTFS
0x 8E 0C 02 = End location of the partition
0x 80 00 00 00 = Start position of the partition
0x 00 A0 00 00 =  Total size
Partition Table Entry Structure
24

## Page 25

03
02
MBR Partition Analysis04
01
STEP STEP STEP
Offset Menu
- Go to Offset
Move the partition start
sector position by
Arrival of the
first partition entry
* 0x 80 00 00 00 = Startup location of that partition
25
Hands-on

## Page 26

06
05
MBR Partition Analysis04
04
STEP STEP STEP
Offset Menu
- Go to Offset
Move by Total Sector from
previous position Second partition entry arrives
* 0x 00 A0 00 00 = Total Sector
26
Hands-on

## Page 27

MBR Partition Analysis04
Partition Table Entry #1
Partition Table Entry #2
Partition Table Entry #3
Partition Table Entry #4
80, 128, 65536
A080, 41088,
21037056
14080, 82048,
42008576
1E080, 123008,
62980096
A000, 40960,
20971520
A000, 40960,
20971520
A000, 40960,
20971520
21000, 135168 ,
69206016
Partition Table Entry HEX, DEC, DEC*512 HEX, DEC, DEC*512 Starting LBA address &
Total Sector
27
Hands-on

## Page 28

MBR Partition Analysis04
*Partition Table Entry #2*
*Partition Table Entry #3*
28
Hands-on

## Page 29

MBR Partition Analysis04
*Partition Table Entry #3*
*Partition Table Entry #4*
29
Hands-on

## Page 30

MBR Partition Analysis04
80, 128, 65536, 62980096, 63045632
A080, 41088, 21037056, 62980096,
84017152
HEX, DEV, DEV*512, EBR start position,
DEV*512 +EBR start position
Hands-on
*Partition Table Entry #4*
EBR Partition Table
Get a starting location
30

## Page 31

MBR Partition Analysis04
EBR | Used Partition Entry #1 EBR | Used Partition Entry #2
31
