---
title: "09강_Windows_Forensic_생성증거_(1)_registry_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\09강_Windows_Forensic_생성증거_(1)_registry_v1.2.pdf"
source_size_bytes: 395983
source_modified: 2025-10-02T12:31:15
imported_at: 2026-06-14T14:25:00
tags:
  - acs
  - acs-advanced
  - imported
---

# 09강_Windows_Forensic_생성증거_(1)_registry_v1.2

- Source: [09강_Windows_Forensic_생성증거_(1)_registry_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/09%EA%B0%95_Windows_Forensic_%EC%83%9D%EC%84%B1%EC%A6%9D%EA%B1%B0_%281%29_registry_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Windows Forensic -
Generating Evidence (1)
• What is Registry
• Keys and values in the registry
• Registry Analysis Tool
09
1

## Page 2

2
01. current page topic What is Registry?01
Hierarchical structure of keys and values
A hierarchical structure of keys and values. This
structure is effective for categorizing, storing, and
retrieving information. Other keys can be nested
under a particular key, and each key can be assigned
one or more values.
Hive
A physical component of the registry. A file that
contains some or all of the data in the registry.
Five types.
Regedit
Registry editing tool provided by Windows.
View, modify, create, and delete keys and values directly.
Unique
Databases
A registry is a database that manages important
information such as software, hardware, system
information, and more.
Non-volatile
Registries are non-volatile, meaning that they retain
data even when power is turned off. They are non-
volatile because they keep data permanently, since
they manage critical information.
Data accumulation
Unused or unnecessary data continues to
accumulate. Can manifest as a decrease in system
performance.
Registry
Features

## Page 3

3
01. current page topic What is Registry01
Manage user profiles
Store information about a user's profile, including
information about the user's personal preferences,
environment variables, and installed programs.
Centralize settings information
Manage configuration information for operating
system hardware and software in one place for
centralized information management.
Hardware and software
Save system settings
Configuration information for your hardware,
settings for installed software, system environment
variables, and more.
Registry
Purpose
Manage operating system
configuration
The registry stores information about the boot
process, system services, hardware drivers, and
more, as it manages critical components of the
operating system. Manage your own state and
perform necessary actions.

## Page 4

4
01. current page topic What is Registry01
Windows Registry
Hive
HKEY_CLASSES_ROOT
File associations and Object Linking and Embedding (OLE)
information. Stores information about the association between a
file extension and the application used to open it.
HKEY_CURRENT_USER
Profile information for the currently logged in user. The user's
preferences, installed applications, personalization settings, and
more are stored in this hive.
HKEY_LOCAL_MACHINE
Settings that apply system-wide. Hardware settings, operating
system settings, settings for installed applications, and more are
stored in this hive.
HKEY_USERS
Contains all user profiles.
Each user account's HKCU hive is stored here.
HKEY_CURRENT_CONFIG
Current hardware profile information.
The hardware configuration information used when the system
boots is stored in this hive.

## Page 5

5
01. current page topic What is Registry01
Ease of data management
Improve system performance
Root and subkey tree structure
%systemroot%system32\config\
HKLM : system, software, security, sam
HKU : default, ntuser.dat(=sid)
Hive files as physical files

## Page 6

HKEY_CLASSES_ROOT
6
01. current page topic What is Registry01
File extension association keys
File associations
COM Object Properties
Configure a subkey of another root
without having a separate hive

## Page 7

HKEY_CURRENT_USER
7
01. current page topic What is Registry01
Profile information for the logged-in user

## Page 8

HKEY_LOCAL_MACHINE
8
01. current page topic What is Registry01
Store your system's hardware, software,
system settings, and other data

## Page 9

HKEY_USERS
9
01. current page topic What is Registry01
Stores information about all user
profiles loaded in the system.
DEFAULT
S-1-5-18: SystemProfile
S-1-5-20: NetworkServices SID
S-1-5-19: LocalService SID
S-1-5-21 : User SID
1001 User permission, 1000 UserPrivileged user,
500 Administrator
What is SID?
A security identifier (SID) is a unique identifier used
to identify users, user groups, and other security
entities in the Microsoft Windows operating system.
SIDs are used extensively in security-related tasks
and in access control lists (ACLs), which are unique
values that the system generates for each user
account or group. SIDs consist of a series of numbers
and have the following format.
S-1-5-21-3623811015-3361044348-30300820-1013
S: Prefix that represents the SID
1: Version number of the SID
5: A unique identifier for the organization that
issued the SID. A 5 typically indicates the Windows
Security Authority.
The remaining digits are used to uniquely identify a
specific domain and user.

## Page 10

HKEY_CURRENT_CONFIG
10
01. current page topic What is Registry01
Hardware profile information used
when the system starts.

## Page 11

Registry keys Registry values
Keys and values in the registry02
11
Structural units of the Registry
Concepts that correspond
to folders
Root Key and Sub Key
Master Key and Derived Key
The actual data stored
within the key
Concepts that
correspond to files
Value - Date Type - Data

## Page 12

Keys and values in the regis
try
02
12
Root Key
Derived Key Master Key
Key Value Data Type Data
Sub Key
Regedit
(Registry Editor)
Keys and values in the registry

## Page 13

13
01. current page topic Keys and values in the regis
try
02
Registry File Data Type
REG_NONE No type
REG_SZ String value
REG_EXPAND_SZ A string value that can be expanded. Can include environment
variables.
REG_BINARY Binary values (arbitrary data)
reg_dword/reg_dword_little_indian DWORD value (32-bit) integer
(0 to 4,294,967,295 [232 - 1]) (Little endian)
reg_dword_big_indian DWORD value (32-bit) integer
(0 to 4,294,967,295 [232 - 1]) (Big endian)
Keys and values in the registry

## Page 14

14
01. current page topic Keys and values in the regis
try
02
Registry File Data Type
REG_LINK Symbolic links (Unicode)
REG_MULTI_SZ Multi-string values (arrays of unique strings)
reg_resource_list Resource List
(used for enumerating and configuring plug-and-play hardware)
reg_full_resource_descriptor Resource Descriptors
(used for enumerating and configuring Plug & Play hardware)
reg_resource_requirements_list Resource Requirements List
(used to enumerate and configure Plug & Play hardware)
reg_qword/reg_qword_little_indian QWORD value (64-bit integer), Bit/Little endian or undefined
Keys and values in the registry

## Page 15

15
01. current page topic Keys and values in the regis
try
02
When creating a registry key
Derived Key
Master Key
Permission
Denied
S
B
D
Q
M
E
When backing up registry
values
Open Regedit
(Registry Editor)
Top-left corner of Regedit
File - Export
Select a range
(All or selected branch)
Save to a location
of your choice
When creating a registry key
When creating registry values
When backing up registry values
Keys and values in the registry

## Page 16

16
01. current page topic Registry Analysis Tool03
First
 Second
Using the Registry Analysis Tool

## Page 17

17
01. current page topic Registry Analysis Tool03
RECmd
Made by Eric Zimmerman
Source: Ericzimmerman.github.io
Registry Explorer
Command Interface GUI
Search query support
Show a tree structure of key and value details
Track and display the history of changes
to keys and values
Recover deleted keys and values
RECmd.exe
-f "path to the hive"
--(option to save)"path to save"
-(options you want to save)f "filename you want"
-(search options you want) "filters you want
