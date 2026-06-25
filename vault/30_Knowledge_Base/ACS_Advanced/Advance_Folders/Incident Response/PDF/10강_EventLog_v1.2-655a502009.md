---
title: "10강_EventLog_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\10강_EventLog_v1.2.pdf"
source_size_bytes: 1533794
source_modified: 2025-11-12T12:21:35
imported_at: 2026-06-14T14:26:27
tags:
  - acs
  - acs-advanced
  - imported
---

# 10강_EventLog_v1.2

- Source: [10강_EventLog_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/10%EA%B0%95_EventLog_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

What is event log?
• What is event log?
• EventLog more
• Message Analysis
10
1

## Page 2

What is event log? 01
• The feature that records various event
activities that occur on a computer system
• Record incidents, warnings, errors, and
more from the operating system and
applications or services
What is event log?
• Beginning with Windows NT
• Size limit X since Windows Vista
• The size limit is removed, but a
default size exists
ADD TEXT
• Malware execution starts when a breach occurs
• Behavior of the malware
• Power Shell Execution Commands
What you'll see
• Record almost everything you do on your
computer
• Run executables
• Remote access, add accounts
• Commands typed and double-clicked
In addition
2

## Page 3

Major Logs
EventLog란?01
Security
What is a Security Log?
Log security-related events
Monitor the security of your system and identify security
issues
Very closely related to judicial precedent
Detect failed login
When a login fails, the event is logged in the Security log
If the frequency of failures is high, it is suspected to be an
early sign of a judicial precedent
Account lockout events
Multiple failed login attempts as mentioned in the first point
may result in an account lockout
Permission escalation attempt detection log
Events when an intruder attempts to escalate permissions,
and when it fails
Security policy change log
When security policy changes, events about those changes
Firewall off, allow for files with certain extensionsOpen port
Application
What is an Application Log?
Mainly records events that occur in applications
Applications include not only executable files, but also office
programs, Chrome, security software, etc.
When an unregistered application runs
When an intruder attempts to run a malicious application,
the event is considered suspicious activity and may be
suspicious
Analyze patterns to detect intrusive behavior
Applications running at unusual times
When certain events occur repeatedly
Detect unauthorized application modifications
application files through event logs
If an application is being modified without permission, it
could be part of an intrusion.
What is event log?
3

## Page 4

Major Logs
EventLog란?01
System
What Is the System Log?
A log that records system-level events and error messages in
the Windows operating system
It primarily tracks basic operational and status information
of the system and monitors the normal operation of the
system
Detecting malicious services or processes
If an intruder starts a malicious service or runs a malicious
process, the activity is logged in the System event log
This allows you to detect and block malicious activities
Detect system resource overuse
If malware or intruders overuse system resources to perform
an attack, the event is logged in the System log
Setup
What Is a Setup Log?
A log that records information related to system installation
and setup in the Windows operating system
Primarily tracks activity related to changing the system's
configuration, installing or removing software, installing
drivers, updating Windows, etc.
Malicious software distribution and installation
Can reveal traces of malicious software that has penetrated
your system
Missing security updates
Recognize that a security vulnerability is likely to be
exploited
Lack of defenses against the latest attack vectors if critical
patches are not updated
What is event log?
4

## Page 5

Forwarded Events
What are Forwarded Events?
Normal users don't accumulate these logs
Store events collected from remote computers
When is it useful?
Forwarded Events can be used to manage accumulated
events from a centralized server for easier and more
convenient monitoring
Major Logs
EventLog란?01
So far, all of your event log analysis has been suspicion, not confirmation
One circumstance can lead to a misjudgment if it's the whole picture
When can we confirm that a judicial precedent has occurred?
You've been informed by a credible organization that a judicial precedent
of such severity has occurred that it is visible from the outside
Security personnel analyze other artifacts along with event logs to put the
pieces together and determine that a judicial precedent has occurred
Caveats
What is event log?
5

## Page 6

EventLog란?01
Event Viewer
Print Event ID, User, and Computer Information
Details allows you to print more detailed information
What is event log?
6

## Page 7

EventLog란?01
Admin
Operational
Analytic
Debug
Troubleshooting information for
administrators and users
Logs used for analysis and diagnostics
Logs of issues that users can't handle
Used by developers to troubleshoot
program
Type
Powershell
• Recently, malware has been using fileless attacks using PowerShell rather than creating
executables such as .exe files
• PowerShell event logs record script execution, errors and exceptions, permissions issues, and
other action events
• If a malicious script is executed using PowerShell, the PowerShell event log records information
related to the executed script
PATH
C:\Windows\System32\winevt\Logs
What is event log?
7

## Page 8

EventLog란?01
Window event Viewer
Microsoft-Windows-PowerShell%4Operational.evtx
Analyze
Verify that the Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force command ran on 2024/1/15 12:02:01
Verify that Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force exists in the Powershell event log with event ID 4104 when it occurred
Event ID
An event identifier (event ID) is a number that uniquely identifies a specific event that occurred in the Windows event log, each event is assigned a unique event ID
4104 is the event ID and the description says Execute a Remote Command
What is event log?
8

## Page 9

EventLog란?01
File
The save path for event log files
%System Root%\system32\winevt\Logs\Application.evtx
RestrictGuestAccess
Whether to restrict guest access
AutoBackupLogFiles
Whether to automatically back up log files
MaxSize
Maximum size of event log files
20 MB by default
Registry PATH
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Application
What is event log?
9

## Page 10

EVTX Structure
File Header
Chunk Header
Record 1
Record 2
Record N
Chunk Header
Record 1
Record 2
Record N
Chunk Header
Record 1
Record 2
Record N
evtx
Chunk 1
Chunk 2
Chunk N
Event log 란01
Used to store Windows event logs
Structured format containing a variety of information
Basically organized into a File Header and several Chunks
Located at the beginning of the file
Contains metadata such as file format, version, and event log attributes
Size : 4096 Byte
A logical division of a file
Contains information of records belonging to the chunk
Chunk Header Size : 512Byte
Chunk Size : 65536 Byte
A Chunk contains one or more Records
Contains the actual event data that occurred in the event log
Information describing the type, attributes, content, etc. of the
event, etc.
What is event log?
10

## Page 11

EventLog more 02
https://learn.microsoft.com/ko-kr/defender-for-identity/deploy/configure-windows-event-collection
Secpol.msc
Abbreviations for Security Policy
Commands to open "Security Policy" or "Local Security Policy", a tool used to configure local security policies in Windows
operating systems
Manage system security settings, configure user accounts and permissions, password policies, network security settings,
and more
Security Policy
For advanced users and system administrators
Account lockout policies, password complexity rules, and User
Account Control (UAC) settings
[Local Policies] -> [Security Settings] -> [Audit Policy]
Select both successful and failed event audit
security settings
Shows both successful and unsuccessful
results for this event
11

## Page 12

이벤트로그 more 02
https://learn.microsoft.com/ko-kr/defender-for-identity/deploy/configure-windows-event-collection
Local Policies -> Security Settings -> Advanced
Audit Policy Configuration
Enabling this policy will add 3 Event IDs
Check your audit policy
Check both Success and Failure
Check
Account logon
Events that occur when a new service or driver for a
service is installed or uninstalled
DS Access
"Directory Service Access", indicating access to a directory service used primarily in a
network environment
Related to Microsoft Active Directory, a directory service widely used in corporate
environments
For more information, see Chapter 4
EventLog more
12

## Page 13

[Computer Configuration] -> [Administrative Templates] -> [Windows Components]
-> [Event Logging Service]
이벤트로그 more 02
gpedit.msc
Abbreviation for Group Policy Editor
A powerful tool for managing various policy and configuration settings on your system. It allows you to edit and change
Group Policy on your local computer
Used to adjust the behavior of the system and manage the policies that apply to users
Included in business and professional editions such as Windows Professional, Enterprise, or Education editions
You can set size limits for the event log and define a maximum size to store events that occurred over a period of time
You can also set the frequency at which event logs are automatically backed up and apply policies to generate alerts
when certain events occur
EventLog more
13

## Page 14

이벤트로그 more 02
Strengthen the event log
Setting the event log size to small can save storage space
But cannot store large amounts of logs
Larger size allows more events to be stored
But takes up a lot of disk space
4GB Application, Security, System
Why?
1GB
Backup
These log files can be a big indicator for creating an incident
timeline
Larger size than other logs because of the accumulation of various
data
Includes powershell and other logs at the discretion of the security
officer
ETC Logs
Storing on a non-system volume
Exposes event logs to possible deletion
Things to consider
Therefore, choosing the right size depends on the capacity
and security needs of your system
EventLog more
14

## Page 15

이벤트로그 more 02
Malware propagates through remote desktops
When a remote user opens a file infected with malware or visit s a or visit
a website, the malware propagates to the host system
Desktop connections put credentials at risk of being
stolen
Spyware, such as keyloggers, can be used to steal a user's cre dentials
could be stolen
Excessive desktop connections can slow down your
system
Especially problematic if you have limited bandwidth
Remote desktop is a technology that allows the desktop environment of one computer to be accessed and used remotely from another computer
This technology allows users to use their computer from anywhere with an internet connection as if it were right in front of them
Remote Desktop related event ID
EventLog more
15
event Event ID
Remote Desktop Services: Session Logon Successfully21
Remote Desktop Services: Receive Shell Startup Notification 22
Remote Desktop Services: Session Logoff Successful 23
Remote Desktop Services: Session Disconnected 24
Remote Desktop Services won't accept logon because installation
is in progress 34
Remote Desktop session disconnected 39
Remote Desktop disconnected 40

## Page 16

이벤트로그 more 02
Malware propagates through remote desktops
When a remote user opens a file infected with malware or visit s a or visit a website,
the malware propagates to the host system
Desktop connections put credentials at risk of being stolen
Spyware, such as keyloggers, can be used to steal a user's cre dentials could be
stolen
Excessive desktop connections can slow down your system
Especially problematic if you have limited bandwidth
Remote desktop is a technology that allows the desktop environment of one computer to be accessed and used remotely from another computer
This technology allows users to use their computer from anywhere with an internet connection as if it were right in front of them
User Account, Application Install related event ID
EventLog more
16
event Event ID
Failed User Account login 4625
Account login with Explicit Credentails 4624
Logon 4648
Logoff 4634
Installing a New MSI File 1022
Installing a new MSI file 1033
Application successfully installed 11707

## Page 17

이벤트로그 more 02
https://microsoft-message-analyzer.en.lo4d.com/windows
Features
Users can use this tool to precisely analyze data based on specific event types, time ranges, sources, and more
Use conditional statements to narrow your analysis and see selected event logs at a glance
About Tool
Originally a tool for analyzing and debugging network traffic, formerly a free program provided by Microsoft
Powerful tool that can be used to analyze event logs as well as network traffic
Microsoft Message Analyzer
EventLog more
17

## Page 18

kusti
kusti
kusti
kusti
Message Analyzer 03
kusti
kusti
kusti
Extraction method
Extract winevt using forecopy_handy.exe, which we
used in the volatile and non-volatile data lesson
command
Command : forecopy_handy.exe –e [PATH]
18

## Page 19

Message Analyzer 03
All event logs can be imported and analyzed, but select a few for efficiency
Selected by security and analytics staff based on judicial precedent type
Select Open -> Select the event log file collected using forecopy_handy in advance
SYSTEM, APPLICATION, SECURITY, etc.
Message Analyzer
19

## Page 20

Microsoft Message Analyzer
Filter
Data
Message Analyzer 03 Message Analyzer
20
