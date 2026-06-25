---
title: "10강_Windows_Forensic_Evidence of creation_(2)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\10강_Windows_Forensic_Evidence of creation_(2)_v1.2.pdf"
source_size_bytes: 503557
source_modified: 2025-10-02T12:32:40
imported_at: 2026-06-14T14:25:01
tags:
  - acs
  - acs-advanced
  - imported
---

# 10강_Windows_Forensic_Evidence of creation_(2)_v1.2

- Source: [10강_Windows_Forensic_Evidence of creation_(2)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/10%EA%B0%95_Windows_Forensic_Evidence%20of%20creation_%282%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Windows Forensic –
Creation Evidence (2)
• Extracting System Information from the Registry
• Tracking user activity in the registry
• Limitations of registry analysis
10
1

## Page 2

Extracting System Information from the Registry01
HKLM\SOFTWARE\Microsoft\Windows NT
\CurrentVersion
HKLM\SOFTWARE\Microsoft\Windows NT
\CurrentVersion\ProfileList
OS information SID information
2

## Page 3

01
Hardware configurationPC Name
HKLM/SYSTEM/ControlSet00X/Control/
ComputerName/(Active)ComputerName HKLM\HARDWARE\DESCRIPTION\System
3
Extracting System Information from the Registry

## Page 4

01
List of services and
driversTime Zone
HKLM/SYSTEM/ControlSet00X/Control/TimeZoneInformation
HKLM/SYSTEM/ControlSet00X or CurrentControlSet
4
Extracting System Information from the Registry

## Page 5

01
Wireless LAN
informationNetwork information
HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/NetworkCards
HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/ NetworkList/Profiles{GUID}
5
Extracting System Information from the Registry

## Page 6

Tracking user activity in the registry02
Application execution traces
UserAssist
Path HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count:
Executable execution history
{F4E57C4B-2036-45F0-A9AB-443BCFE33D9F}\Count:
Shortcut launch history
ROT13
Decryption
6

## Page 7

레지스트리의 사용자 활동 추적02
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer
\ComDlg32\OpenSavePidlMRU
OpenSavePidIMRU
MRU stands for "Most Recently Used," which
means most recently used items
The OpenSavePidMRU key stores a list of files that
a user has recently opened or saved through the
Open or Save File dialog box
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer
\ComDlg32\LastVisitedPidlMRU
LastVisitedPidIMRU
The LastVisitedPidMRU key records the path to
the last folder a user visited through the Open or
Save File dialog box
Gain insight into the folder locations users
frequently work in and the types of files stored in
those folders
Tracking user activity in the registry
User file browsing and usage behavior
7
Tracking user activity in the registry

## Page 8

레지스트리의 사용자 활동 추적02
Tracking user activity in the registry
HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/Winlogon
Last Logged In User Information
Winlogon
Stores settings related to the Windows logon process
Obtain information about user accounts that have accessed the
system, login times, authentication mechanisms used, etc.
HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Uninstall
List of installed programs
Uninstall
Stores a list of software installed on your system, including the
installation path, version information, and installation date for
each piece of software
Get information about software that was installed or uninstalled
at a specific point in time
HKCU/Software/Classes/Local Settings/Software/Microsoft/Windows
/Shell/MuiCache
Window titles of used programs
MuiCache
Stores the names and file paths of programs that the user has
runMUI is the Multilingual User Interface, used to manage
program names in a multilingual environment
HKCU/SOFTWARE/Microsoft/Windows/Applets/@@@/Recent File List
Traces of Programs Opened
Recent File list
Stores a list of documents or files that a user has recently
opened; works with the Recent Documents list in Windows
Explorer and provides quick access to files that a user has
recently worked on
Helps you understand a user's recent activity, files of interest, or
file access patterns at a particular time of day
8
Tracking user activity in the registry

## Page 9

02 레지스트리의 사용자 활동 추적
HKCU/Software/Microsoft/Windows/CurrentVersion/Explorer/TypedPat
hs
HKCU/SOFTWARE/Microsoft/Windows/CurrentVersion/Explorer/RecentDocs
Recently opened file traces
RecentDocs
Store a list of documents that users have recently opened
Understand the types and filenames of documents a user has recently
viewed
List of paths entered in the Explorer
address bar
TypedPaths
Stores paths that users have typed in the address bar of Windows Explorer
Identify paths to specific folders or files that the user was interested in or
considered important
HKCU/SOFTWARE/Microsoft/Windows/CurrentVersion/Explorer/RunMRU
Recent Run window search traces
RunMRU
Stores a list of commands entered and executed by users through the Run
dialog box on the Start menu
View traces of specific commands that users have performed on the system
or programs that they have run
HKCU/Software/Microsoft/Windows/CurrentVersion/Explorer/
ComDig32/OpenSavePidMRU
List of recently read or saved files
OpenSavePidMRU
A list of files that users have recently accessed using the Open or Save File
dialog box
Provide a list of documents, images, or other files that a user has recently
worked on, so you know what files the user has been interested in at any
given time
Tracking user activity in the registry
9
Tracking user activity in the registry

## Page 10

레지스트리의 사용자 활동 추적02
KCU/Software/Microsoft/Windows/CurrentVersion/Explorer/ComDig32
/LastVisitedPidMRU
HKCU/Software/Microsoft/Windows/CurrentVersion/Explorer/MenuOrder
/Favorites/Links
Favorites list
Favorites/Links
Stores a list of websites that you have added to your browser's
favorites (bookmarks)
By analyzing the favorites list, you can gain additional insight into
a user's online activity
Recently Accessed Folder Traces
LastVisitedPidMRU
Stores information about folders and files that users have
recently visited through the Open or Save File dialog box
Know the paths to files and folders that users have recently
worked on
HKCU/SOFTWARE/Microsoft/Internet Explorer/TypedURLs
HKCU/SOFTWARE/Microsoft/Windows/CurrentVersion/Applets/Regedit
Information about the last key accessed in
the Registry Editor
Regedit
Refers to Windows Registry Editor
This key provides information about the last time the Registry
Editor was accessed
Typed URL list
TypedURLs
Records the website addresses (URLs) that you type directly into
the address bar of your internet browser
From the list of URLs you type, investigators can learn about your
online activity, the websites you are interested in, or the online
information you access at certain times of day
Tracking user activity in the registry
10
Tracking user activity in the registry

## Page 11

레지스트리의 사용자 활동 추적02
Preservation
Evidence
Creation
Evidence
Windows
Forensic
Digital Forensics Courses and Methodologies on Windows Operating Systems
Creation Evidence Preservation Evidence
Data that Windows systems generate
and record themselves
Data that you created or
modified yourself
11
Tracking user activity in the registry

## Page 12

Limitations of registry analysis03
Creation
Evidence
Windows
Forensic
Registry
Data that Windows systems generate and record
themselves
About installing and
running software
Change
hardware
Change system settings
and configurations
User activity
12

## Page 13

Limitations of registry analysis03
Limitations of
registry analysis
▪ Problems with self-
organization ▪ Problems caused by non-
volatility
▪ Data is accumulated as an
Update instead of a Stack
Update
Self-
organizing x
13

## Page 14

Limitations of registry analysis03
Increased system load
Information overload
Reduced responsiveness
Increased analysis time
Increased
complexity
Performance
degradation
Over time, unused software registry keys,
temporary settings, experimental changes,
etc. remain and accumulate in the registry
The more voluminous the data within the
registry, the longer the time required for a
forensic analyst to find and analyze
relevant information
As the registry grows in size, it takes more
time for the system to load data at startup
As the registry grows in size and
complexity, the system's response time
slows down
14

## Page 15

Limitations of registry analysis03
Reliability of the
Registry
Manipulability
Possibility of
malware
interception
Can be created or modified by users or applications
They can be used for normal purposes, such as changing system
settings, adjusting user preferences, and installing software,
but they also leave room for exploitation
Malicious users or software can manipulate registry values to
interfere with the normal operation of the system or exploit
security vulnerabilities
15

## Page 16

Limitations of registry analysis03
Reliability of the
Registry
Manipulability Possible malware
infection
Representative examples of software management registry keys that run automatically at boot time
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
Manipulating registry information, which manages the execution traces
of software that runs automatically at bootup,
is a common tactic used by malware
The Windows registry contains several keys that specify which programs
or scripts should run automatically at system startup
When malware manipulates the registry, it can run continuously without
being easily recognized by users or administrators
16

## Page 17

Limitations of registry analysis03
Use of security software
Antivirus and anti-malware can prevent malware infections
and detect attempts to manipulate the registry
Regular system scans
Regular system scans can monitor registry changes and
identify suspicious or unnecessary entries
System and registry backups
By regularly backing up critical system and registry settings, you
can restore a previous state in the event of tampering / corruption
Manage user permissions
Minimize the permissions of user accounts to prevent
malware from making changes to your system
How to respond
17

## Page 18

Limitations of registry analysis03
Regular registry cleaning
Regularly cleaning unneeded registry entries using
tools such as registry cleaners can help prevent the
accumulation of unnecessary data and improve
system performance
Optimize your analytics tools
When performing registry analysis, you can optimize
your analysis tools to increase the efficiency of your
analysis by focusing on specific keywords or patterns
and performing analysis only on highly relevant data
Response strategy
18
