---
title: "11강_Windows_Forensic_생성증거_(3)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\11강_Windows_Forensic_생성증거_(3)_v1.2.pdf"
source_size_bytes: 1350631
source_modified: 2025-10-11T21:46:16
imported_at: 2026-06-14T14:25:01
tags:
  - acs
  - acs-advanced
  - imported
---

# 11강_Windows_Forensic_생성증거_(3)_v1.2

- Source: [11강_Windows_Forensic_생성증거_(3)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/11%EA%B0%95_Windows_Forensic_%EC%83%9D%EC%84%B1%EC%A6%9D%EA%B1%B0_%283%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Windows Forensic -
Creation Evidence (3)
• Amcache
• Shimcache
11
1

## Page 2

Amcache01
Row
information
RecentFileCache.bcf
Compatibility artifacts used by Windows 7
Used to temporarily store the program path
when a process is created
Disadvantages of resetting every time
ProgramDataUpdater is performed
Path: %SystemDrive%\Windows\AppCompat\Programs
2

## Page 3

Amcache01
Path: C:\Windows\appcompat\Programs\AmCache.hve
Row
information
Execution
path
Initial
Execution time
Timeline
Delete
Time information
Execution
Information
Amcache
Store information about the application's execution path, first run time, uninstall time, etc.
Storing application
execution information
In combination with prefetch files, you can
organize the entire timeline of your program
3

## Page 4

Amcache01
Source: Amcache Analytics (brunch.co.kr)
Windows8 Windows11
4

## Page 5

Amcache01
Windows8 Windows11
File
Storing information about specific files
This information can include the file's name, path, hash value, creation time, and
modification time, which can be used to identify and verify files that have been
executed on the system
Generic
As the name implies, it stores information that is used for a variety of purposes.
It can contain a variety of data that doesn't fall into a specific classification, which
can provide a variety of hints during forensic analysis
Orphan
Stores information about files or programs that are no longer referenced by the
system
Contains information about files that existed on the system in the past but have
been deleted or moved
Can be useful for tracking the previous existence of a file
Programs
 Stores detailed information about programs installed on your system
This can include the program's name, installation path, version information,
installation date, and more, providing important data about what programs users
have installed and when they installed them
Device Census
Used to collect usage and configuration statistics for devices
Includes your system's hardware configuration, performance data, usage statistics, etc.
Used to understand your system's hardware health and usage patterns at any given time
DriverPackageExtended
Inventory
Mare
 Used to track activity associated with executables
Can provide additional data about the activity of executable files and can be used
to further analyze events related to the execution of an application.
Stores extended information about driver packages installed on your system
Information such as the driver's name, manufacturer, version, and installation date
Helps you track the installation and update history of drivers and diagnose potential driver-
related issues
Contains a list of applications and hardware installed on your system
Stores details such as each application's file path, executable file hash, installation time, etc.
Monitor software and hardware changes within your system, and help you understand usage
and deployment patterns of your software
5

## Page 6

Amcache01
What is the Program Compatibility Assistant (PCA)?
PCA
is a part of Microsoft Windows that provides
 features designed to address compatibility issues that
users may encounter when running legacy applications
on newer versions of Windows
How PCA works
1. Version checking
2. Detect and resolve issues
3. User notifications
4. Compatibility database
Forensic perspective
Provides critical information to understand
application usage patterns of users and
reconstruct the timeline of software that has
been executed on the system
PCA roles
Scans executed programs for possible compatibility issues, notifies
the user if there are any, and attempts to resolve the issue by
applying known compatibility solutions
Relationship between Amcahce and PCA
When PCA runs a program, it can leverage information in the executable provided by Amcache to perform compatibility checks
Metadata in executable files stored in Amcache may be used by PCA to determine the version of a program or to verify digital signatures
PCA may also refer to data stored in Amcache when applying compatibility patches for certain programs or suggesting recommended actions to users
The primary reason PCAs are mentioned is that data in Amcache can be directly relevant to resolving compatibility issues
Amcache provides the information needed for PCA to work effectively, and PCA uses the information it gets from Amcache to manage issues related
to running software on your system 6

## Page 7

Amcache01
File
FileStores information about a specific file
This information can include the file's name, path,
hash value, creation time, and modification time,
which can be used to identify and verify files that
have been executed on the system
Windows8
Value Description Data types Roles
0 Product name UNICODE string Full name of the product
1 Company name UNICODE string The name of the company that created
the file
2 File version number only UNICODE string Version number of the product
3 Language code (1033 for en-US) Deward Language codes for products
4 SwitchBack Context Cue words Contextual information about SwitchBack
5 File version UNICODE string Version information for files
6 File size (bytes) Deward File size information
7 PE Header Fields - SizeOfImage Deward Total size of the executable image
8 Hash of PE header (unknown algorithm) UNICODE string Hash value for PE headers
9 PE Header Fields - Checksum Deward Checksum of the PE header
a Unknown Cue words Unknown
b Unknown Cue words Unknown
c File description UNICODE string File description
d Unknown, possibly major & minor OS
versions Deward Operating system version
f Linker (compile-time) timestamp DWORD - Unix Time The linker's compile timestamp
10 Unknown Deward Unknown
11 Last modified timestamp File time Timestamp of the file's last modification
12 Generated timestamp File time File creation timestamp
15 The full path to the file UNICODE string The file's storage path
16 Unknown Deward Unknown
17 Last modified timestamp 2 File time Second modification timestamp
100 Program ID UNICODE string Program identifier
101 SHA1 hash of the file UNICODE string SHA1 hash of the file
7

## Page 8

Amcache01
1985
1995
2001
2009
2012
2015
2021
https://learn.microsoft.com
8

## Page 9

Amcache01
https://learn.microsoft.com
9

## Page 10

Amcache01
Win11 21H2
X
Win11 22H2
O
New
 Artifact
10

## Page 11

Amcache01
Path/Application|Time Year-Month-Date
Hour:Minute:Second.Milliseconds
Runtime | Execution Status | Executable File Path | Description of File | Software Vendor | File Version | ProgramId | Exit Code Value
11

## Page 12

Amcache01
Amcache.hve from a Digital Forensics
Perspective
You can see the application's execution path, first execution time, and even
estimate the deletion time
When combined with the subsequent analysis of the Prefetch and
Iconcache.db files, a complete timeline of the application can be constructed
In addition, amcache files record traces of anti-forensic programs, portable
programs, and external storage devices, which are important artifacts from a
digital forensics perspective
12

## Page 13

Amcache01
13

## Page 14

Amcache01
Prefetch
Icon Cache
A maximum limit of 128 prefetch files, deleting old
prefetch files if exceeded
The icon image of the application is recorded in the form of a BMP file, allowing
you to check information about the installation, copying, and viewing behavior of
the application
However, it does not provide information about the application's execution time
Problems with existing methods for viewing trace information
Amcache
Application-related information is written to the amcache file only
on the first run, and not after the second run
14

## Page 15

Amcache01
Experimental results from the paper above
Different installation and execution paths and different program names, even for the same program.
File reference keys are newly generated and related information is accumulated and recorded in the
amcache file
However, if you delete and reinstall the same program from the same folder or run the same
executable file twice, the file reference key is not newly generated and related information is not
recorded in the amcache file
15

## Page 16

Amcache01
Conclusion
Amcache claims that digital forensics investigators can use prefetch and icon cache analysis to
determine when a computer user first installed an application, how many times it was run, when it
was last run, and even how many times it was uninstalled and reinstalled, providing a complete
timeline of individual applications, as well as traces of anti-forensic programs, portable programs,
registry cleaners, and external storage devices
16

## Page 17

Amcache01
AmcacheParser
Made by Eric Zimmerman
Https://github.com/EricZimmerman/AmcacheParser
AmcacheParser.exe -f Amcache.hve --csv C:\Users\UserName\Downloads\AmcacheParser
Structure for storing information about Plug and
Play devices in Windows that stores information
about the device
Files associated with the driver
Shortcuts
File unlinking items
17

## Page 18

Amcache01
AmcacheParser
csv
YYYYMMddhhmmss_
 Amacache_Title.csv
DeviceContainers DevicePnps
Provides centralized information about a device's identity
and status
Manage critical information about devices, including each
device's unique identifier, last modified time, classification,
user-friendly name, connected status, Connected, make,
model, name, number, major classification, and current
status
Components that manage device recognition and configuration
through the Plug and Play system
Provides information needed to manage, troubleshoot, and
maintain devices and drivers, including the device's identifier,
when settings were changed, category, globally unique identifier,
description, driver identifier, package name, driver version,
hardware identifier, installation file, installation status,
manufacturer information, model, parent device identifier,
problem code, driver provider, service, driver stack identifier, and
more
18

## Page 19

Amcache01
AmcacheParser
csv
YYYYMMddhhmmss_
 Amacache_Title.csv
DriveBinaries DriverPackages
Stores information about the installed driver binary files
Each file is distinguished by a unique identifier (KeyName)
Contains details about the driver, including creation and
modification times, name, whether it is included by default,
execution mode, signature status, checksum, manufacturer,
identifier, and package name
Driver packages are responsible for information
Each package manages an identifier (KeyName) and information
such as when it was last modified, date created or modified,
device class, storage path, embeddedness, hardware identifier,
inf file location, provider and submission information, and system
file name and version
19

## Page 20

Amcache01
AmcacheParser
Shortcuts , UnassociatedFileEntries
csv
YYYYMMddhhmmss_
 Amacache_Title.csv
Information about the shortcut (.lnk) files on your system.
Includes the unique identifier of the shortcut, its actual name, and the last
modification time of the registry key, useful for analyzing application usage
patterns and digital forensics investigations
Information for files with no open with program specified
Detailed metadata, including the name of the application that created the
file, the last time the file metadata was changed, the SHA1 hash used to
verify file integrity, whether it is an operating system component, the full file
path, file name and extension, file association date, product name, file size
and version, path hash, file binary type, whether it is an executable file,
version information for executable files, USN for file change history, file
language, and file description
Important for file management, security scanning, and system auditing of
your system
20

## Page 21

Shimcache02
SDB
Shim Data Base
 Application Compatibility Database
About Shimcache
Also known as ppCompatCache, short for Application Compatibility Cache
One of the internal mechanisms of the Windows operating system used by the
operating system to evaluate and manage the compatibility of installed
applications
Shimcache

Application Compatibility Cache
Compatibility
infrastructure
Compatibility
issues
Matching
TAG
File Properties
Compatibility infrastructure uses databases to diagnose and resolve
compatibility issues in applications, accessible through programming
interfaces, and contains information about components such as executables
Compatibility issues are resolved for individual applications at runtime
There is a “matching” process that uses database lookups to determine
which resolution to apply to an application, and the attributes and location
of files are important in this matching process
TAGs are unique identifiers assigned to each item and attribute in the
database, associated with a TAG type that indicates the format of the data.
A TAGID refers to a specific database entry, while a TAGREF refers to an
entry that can be used across multiple databases
File attributes refer to the metadata of a file and are used by the system to
correctly identify and match files to database entries
21

## Page 22

Shimcache02
Why two paths
This is because Windows maintains multiple “Control Sets” to manage
different states of the system
About Shimcache
Also known as ppCompatCache, short for Application Compatibility Cache
One of the internal mechanisms of the Windows operating system used by
the operating system to evaluate and manage the compatibility of installed
applications
Shimcache
HKLM\SYSTEM\CurrentControlSet\Control\SessionManager\AppCompatCache
HKLM\SYSTEM\ControlSet00x\Control\SessionManager\AppCompatCache

executable file's
Path Size
Last Execution Time Last Modified Time
ShimCache records the executable file name, file path, and
date and time of last modification
Entries can be analyzed to identify whether the executable
has been run on the system or not
In addition to the local drive, executable files on removable
media and UNC paths are also stored in ShimCache
ShimCache entries are written to the hard drive when the
system is rebooted or shut down
Complicates anti-forensics (data deletion of registry entries)
Therefore, analyzing ShimCache can provide valuable
information, especially during malware incident analysis
22

## Page 23

Shimcache02
23

## Page 24

Shimcache02
Introduces information about applications that can be obtained through Shimcache files by analyzing the structure of
Shimcache, and shows how to detect traces of execution of anti-forensic tools, such as complete deletion, by
improving existing commercial tools
Introduction
The function for resolving compatibility issues caused by different versions of the operating system when running an
application is the BasepCheckBadApp function, which is an internal function of kernel32.dll
When this function is called, the application compatibility database is consulted to deal with program -specific
compatibility issues
The contents of the SDB are consulted, and its cache data is dereferenced for faster troubleshooting, and the
reference is to Shimcache
In other words, think of it as cache data =Shimcache to quickly load the application's compatibility database
Shimcache explained in the paper
https://github.com/leeseungaaa/shimdetector 24

## Page 25

Shimcache02
ShimCache File Structure
Header Size 52Bytes
25

## Page 26

Shimcache02
Signature
CRC 32
Entry Length
Path Length
26

## Page 27

Shimcache02
Path Length
0d0e ~
Path Value
27

## Page 28

Shimcache02
C9+1 ~
LastModified time
C9+8 CA ~ D1
28

## Page 29

Shimcache02
29

## Page 30

Shimcache02
AppCompatCacheParser
Made by Eric Zimmerman
Source: https://github.com/EricZimmerman/AppCompatCacheParser
ControlSet, CacheEntryPosition, Path,
LastModifiedTimeUTC, Executed, Duplicate,
SourceFile
Launch Screen
Download - git
30
