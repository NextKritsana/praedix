---
title: "15강_Other Collections_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\15강_Other Collections_v1.2.pdf"
source_size_bytes: 1652160
source_modified: 2025-11-12T12:34:46
imported_at: 2026-06-14T14:26:31
tags:
  - acs
  - acs-advanced
  - imported
---

# 15강_Other Collections_v1.2

- Source: [15강_Other Collections_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/15%EA%B0%95_Other%20Collections_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Other collections
• Timeline
• Task scheduling
• Data concealment
• WER
15
1

## Page 2

Timeline01
What is TimeLine?
A feature introduced in the Windows 10 operating system that allows
users to record and manage their activities over time
It provides a chronologically organized record of the various tasks and
application usage that a user has performed on their computer, and
helps users to find and continue previously performed tasks at any given
point in time
Activity tracking
 Logs actions that open or edit files, launch installed apps, and record web
browsing
Logs actions that run virtual machines or make changes to your desktop
Cross-device sharing
Share activity across devices for users signed in with a Microsoft
account, allowing them to continue work started on one device on
another
The account-specific path
The path varies slightly depending on the User account: for a local account, it exists
in L.{Local account Name} and for a Microsoft account, it is stored in {Microsoft
Identifier (CID)}
Users\<profile>\AppData\Local\ConnectedDevicesPlatform\
 L.<UserName>\ActivitiesCache.db
TimeLine
2

## Page 3

Timeline01
Related settings
Timeline
• Related settings can be found in multitasking
To check your account
• Open "Settings" from the Start menu and select
"Accounts
• Make sure your Microsoft account is properly linked
Windows Timeline settings
• In "Settings" go to "Privacy" and select "Activity History
• Make sure Windows Timeline is enabled
3

## Page 4

Timeline01
Window + Tab
Keyboard shortcuts
Here, users can see their activities organized over time
and find and resume previous work if needed
What can you do?
Tips
This is a feature that has been removed from Windows 11, so check in a pre-installed virtual machine
Timeline
4

## Page 5

Timeline01
Hover over the item you want to delete and right-click -> Delete to delete
the item
Delete function
Possibility of deletion
• An attacker could potentially delete certain activities from your timeline to cover their tracks or cover up an incident
• Because information in Windows Timeline is stored on the local device, users with administrative privileges or attackers can tamper with or
delete that data
• A user's activity must be evaluated using a combination of logs and traces beyond Timeline
Analytics notes
ActivitiesCache.db is extractable and stored in DB format in SQLite, so you
can see multiple tables when you check it through DB Browser for SQLite
Analyzable
Timeline
5

## Page 6

Timeline
Tables
Activity, ActivityOperation, Activity_PackageID, App settings, Asset, DataEncryptionKeys, MamualSequence,Metadata
table exists
Main Table
Activity
Application execution history and runtime representation
Activity Package ID
App-specific package names
Timeline01
6

## Page 7

Timeline01
Activity Table
Confirmed the existence of various columns: ID,
AppId, PackageIdHash, AppActivityID, etc.
Column
• Activity Status
• AppID
• Payload
• Activity Type
Column to check
Timeline
7

## Page 8

Timeline
App ID
Displays the application/application
package in the Activity_PackageId table
that created the activity record
Activity Status
1 Active
2 Updated
3 Delete
4 Ignore
Tips
Possibility of resetting the expiration
date if it is in an updated state
View information about the programs
you've run
Save in JSON format
Timeline01
8

## Page 9

Timeline
Decode
https://kacos2000.github.io/WindowsTimeline/WindowsTimeline.pdf
Payload description
• Payloads can be base64 decrypted to see plain text values
• View paths, versions, names, and more
• More information can be found at the link at the bottom of the PPT
Payload
Activity Type
5 Application, Application opens
6 Applications, Change Application Focus
10 Copy/paste
Timeline01
9

## Page 10

Timeline01
Work History ID
• Activity ID
• OperationOrdr
Activity ID Platform Package Name Expiration Time
afs_crossplatform
• Cloud sync enabled
x_exe_path
• Standalone programs
windows_win32
• Installed Programs
Package name Expiration time
• Time after 30 days
Activity_PackageID Table
Timeline
10

## Page 11

Timeline01
Windows Timeline Parser
This tool gives you visibility into tags, applications, display names, time values, activity status, and more.
Download PATH
https://github.com/kacos2000/WindowsTimeline/releases/tag/v.2.0.82.0
Display as Active, Deleted, etc. without numbers
Activity Status
Shows Duration, LastModified Time, Start Time, End
Time, etc. in yyyy-MM-dd format
Time value
Consolidate tables
The packaged hash value and values such as platform DeviceID are displayed on one screen, making it more convenient than viewing through
DB Browser
Timeline
11

## Page 12

Task scheduling02
Time
Month
Year
repeat
01 What is a task scheduler?
A system tool provided by the Windows operating system that gives users the ability
to schedule certain tasks or programs and set them to run automatically
02 Key features
Schedule tasks
• Users can schedule tasks based on specific times, dates, cycles, etc.
• Configurable tasks that perform repetitive tasks in the background or run autonomously
when certain events occur
Reliable task performance
• Windows Task Scheduler is stable and reliable for getting things done
• Manage tasks that run on system boot, and more, so your system always does what you
need it to do
Lots of management features
• You can set up and manage Task Scheduler through a graphical user interface (GUI), and
you can use commands to set up tasks through scripts or batch files
12

## Page 13

Task scheduling02
Incident perspective
Incident response collects task scheduler information for a variety of reasons and can gather information about attacker behavior and related
information
• Malicious actors exploit Task Scheduler to perform attacks such as
running malicious code or installing backdoors into the system
• Malicious tasks can be discovered by detecting changes to the Task
Scheduler, new tasks, etc.
• Collect the history of the Task Scheduler to track the intruder's
activity and see what tasks were run and when
• There are many types of malicious tasks, and scripts that run
periodically using the Task Scheduler have the potential to contain
malicious code
• Communicate with C2 servers, perform keylogging, etc.
Identify the attacker's behavior
• Information from the Task Scheduler is used to construct a
timeline of events
• By recording what tasks were scheduled and executed when in
the system, you can get a complete picture of the time flow
• In the event of a breach, Task Scheduler information can also
help with response and recovery efforts
• Used to block or modify tasks used in the intrusion to stabilize
the system
Organize timeline
Task Schedule EventLog
Task scheduling
13

## Page 14

Task scheduling02
Create a task schedule
Command
schtasks /create /tn "ACS_TASK_TEST" /tr c:\windows\system32\calc.exe /sc daily
• Schtasks: Commands used to manipulate the task scheduler in Windows
• Create: Option to create a new task
• /tn: Name the task as an abbreviation of TaskName
• /tr: Short for Test Run, specifying the path to the file to be executed
• /sc: Short for Schedule, used to set a schedule
• daily: daily
Command analysis
• /delete: Delete a task
• /F: Short for Force, meaning force run
• /change: Allows taskrun of task to be changed
• Add /query : /fo list to display registered tasks in a list
• /run: Run the task immediately
• /disable : Disable the task, /enable: Enable the task
Other options
Confirm task creation
C:\Windows\System32\Tasks
Task scheduling
14

## Page 15

• By default, TASKFIle is stored in XML format.
• The version and encoding are listed, and the date is the time the task scheduler was registered.
• Verify that the task scheduler's name is registered in the URI shown in the red box
• In the calnendartrigger shown in the green box, the value of StartBoundary is the date of registration and the value of enabled is True,
indicating that the task is registered and enabled, and the value of Daysinterval is set to 1 in SchedulebyDay to ensure that the task runs
every day.
• In the yellow boxed Action, see that the action is registered as a command and runs at C:\Windows\System32\calc.exe
Analytics
02 Task scheduling
15

## Page 16

Task scheduling02
create
To create a new task, you must use the Create option to create a new task
But what if we filter for the string Create?
Windows environment variables can be used to bypass this filtering
C:\Windows\System32\cmd.exe /C schtasks /F crea%OS:~-1,1%e /sc hour /mo3 /TN "[MALWARE_NAME]" /ST 12:00 /TR "[MALWARE FILE PATH]"
/mo3 means to set the task to every three hours, like /sc hour before it; /ST is an option to set it to start at 12:00; /sc is used for minutes and seconds rather than hours,
like second and minute
/mo can range from 1 to 23 and /sc can range from 1 to 1439 if it's a minute, and /F means to force the action to run
Obfuscation
Although the screen says MALWARE_NAME, the malware's name is actually a combination of numbers and capitalization, such as "a4k2n".
Command & Description
What if?
OS:~-1,1% represents T
Normally, on Windows NT and later computers, the result of the %OS%
environment variable is WINDOWS_NT
The %OS:~-1,1 gets the trailing alphanumeric character of the string
If you use the command crea%OS:~-1,1%e instead of create, the computer will
read it as create and execute the command
Crea%OS:~-1,1%e
Substitute %SYSTEMDRIVE:~0,1% for the C part of commands like
Schtask or ipconfig to run those commands
Security administrators need to be aware of this and be extra careful
with permission settings and security
In addition to these...
Task scheduling
16

## Page 17

Data concealment03
• A data hiding technique that works by
embedding information into media such as
images, video files, etc.
• The embedded information is usually beyond
human detection and nearly impossible to
detect
• When used maliciously, media files can
contain malicious code
Steganography
A special mechanism that allows you to
store additional data for each file
• Wasted space due to logical and physical size
differences
• Ram slack is unallocated space left in sectors
• Drive slack is Unallocated space left in a
cluster
• Volume slack is space left over after allocating
storage media into partitions
Slack space ADS
DATA
slack
ADS
17

## Page 18

Data concealment
File
Attribute
Main
Data Stream
Alternate
Data Stream
Alternate
Data Stream
NTFS
• Short for Alternate Data Streams, a feature used as part of the file system in Windows operating
systems
• The main file has basic data, and you can append additional streams (data streams) to it to use
• The additional data streams have characteristics that are not normally visible to the user
• The following attributes are stored after the data stream that stores attribute information in NTFS
• Malicious actors could potentially evade detection by storing malicious code in ADS while leaving safe
code in main files
ADS
<a href="https://www.flaticon.com/free-icons/ad"
title="Ad icons">Ad icons created by Freepik - Flaticon</a>
Data concealment03
18

## Page 19

Data concealment
Check ADS zones with the r option of the dir command
Read data from ADS area via More command
Add data named ADS_TEXT to aa.txt as ads
Data concealment03
19

## Page 20

Data concealment03
NTFS FAT32
This concept of ADS is typically applied in NTFS and
is supported in FAT32 filesystems by the X
ADS in FAT32
Moving an ADS-added file to a FAT32 filesystem deletes ADS
and does not restore ADS when moved back to NTFS
Delete ADS
Data concealment
20

## Page 21

WER04
Short for Windows Error Reporting, a feature of the Microsoft
Windows operating system that automatically detects and reports errors that occur in systems
and applications
This information allows Microsoft to identify and fix software bugs
This occurs when a program terminates abnormally or throws an exception, and when an error
is detected, a pop-up is displayed to inform the user that an error has occurred
WER
Possible errors due to malware or infiltration attempts
Collecting WER information can help you find traces of this malicious activity and determine if it has penetrated your system
Especially in the case of vulnerabilities, there is a possibility that WERs are left behind because they are not normal activity in Windows
WER information allows you to assess the stability of your system; recurring errors or issues with specific applications help you assess the current health of
your system
Incident perspective
21

## Page 22

WER04
PATH
%SystemDrive%ProgramData\Microsoft\Windows\WER\ReportArchive
Because it is in use on the system, it cannot be extracted in the
usual way and must be extracted using FTK Imager or a
specialized tool before analysis
Analysis methods
Enabling WER crash dumping can help you find exact traces of malware during
incident investigation
This is because malware is usually created without considering all environments
and often causes system-related errors, mainly due to incorrect operating system
version or incorrect platform, so you can determine whether it is malware
through the logs created when the error occurs
Tips
WER
22
