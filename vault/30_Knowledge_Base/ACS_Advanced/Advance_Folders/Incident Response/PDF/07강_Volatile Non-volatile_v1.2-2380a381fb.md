---
title: "07강_Volatile Non-volatile_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\07강_Volatile Non-volatile_v1.2.pdf"
source_size_bytes: 693110
source_modified: 2025-11-12T12:18:07
imported_at: 2026-06-14T14:26:24
tags:
  - acs
  - acs-advanced
  - imported
---

# 07강_Volatile Non-volatile_v1.2

- Source: [07강_Volatile Non-volatile_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/07%EA%B0%95_Volatile%20Non-volatile_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Online and Offline
• Online and Offline
• Volatile data
• Non-volatile data
• Simple hands-on
07
1

## Page 2

Online and Offline01
WHY?Why do you need it?
• cyber security incidents have the potential to cause significant harm to
organizations or individuals
• Respond quickly to minimize damage and prevent further losses
• Quickly isolate and protect data or systems accessed by intruders
• Effective response maintains business continuity
• Recover systems and data quickly
• Identify and track intruders
When to do this?
• Detect intrusions through system logs, monitoring tools, security solutions,
and more
• When you detect unusual activity on your system, such as unauthorized
access or file changes, suspicious traffic, etc.
• When you are notified of a security issue externally
2

## Page 3

Online and Offline01
If online, collect and utilize as much as you can while the system is powered on
While online, the computer's state is constantly changing, making it difficult to use as legal evidence
later on
From an incident response perspective, the goal is to quickly remediate the cyber security incident to
minimize damage and cost
Use automated tools when the target environment is clear
Rapid response
Damage increases over time
Quick response prevents further
damage
Preserves a lot of information
Shut down
Shut down power to prevent spread
This may result in volatile data loss
Business continuity impact
Data retention
Consider ways to preserve volatile data without power interruption
Create a memory dump to preserve critical information
Online collection
3

## Page 4

Online and Offline01
온라인일 경우, 시스템 전원이 켜져 있는 상태에서 수집할 수 있는 최대한 수집하고 활용
온라인상태에서는 컴퓨터의 상태가 계속해서 변하기 때문에 추후 법적 증거로는 사용이 어려움
침해사고대응 입장에서는 해당 침해사고를 빠르게 수습하여 피해와 비용을 최소화 하는 것이 목표
대상 환경이 명확한 경우, 자동화된 도구를 사용
Offline collectionAccurate analytics
Analyzing with Deleted Data
Analyze your entire data
When you need more accurate analysis than a quick response
Data retention
Selective collection if possible, and imaging if the entire disk needs to be analyzed
Software when ingestion is a priority, and hardware tools when imaging is required
Software-based tools are used when curated collection is a priority, usually in incident response,
where speed is often prioritized over integrity, so they aim to collect quickly without using write
protection tools
Hardware-based tools read and write data at a constant rate and are often used for imaging
large storage media
4

## Page 5

Volatile data02
Volatile data
Data that exists and is stored only while a system or program is running
Characterized by being lost when the power is turned off or the system is rebooted, usually stored in system
memory (RAM)
Program execution data Program execution data refers to data created and used when a specific program is running
It is created as the program is loaded into memory (RAM) and includes the program's code,
variables, stack, heap, etc.
Various information and data are dynamically generated and stored in memory as the program
runs
P.C
 S&H
Reg
 IR
Program Code
• The instructions in a program, and the
order in which they are executed, are
stored in memory
• This is the part of the program that defines
the actual behavior of the program. The
instructions to be executed by the CPU are
located here
Stack&Heap
• The stack is an area of memory used when
a program calls functions or creates local
variables
• The heap is a dynamically allocated memory
space used to store data
Register
• CPU registers store temporary data that
programs use while running
• Data can be accessed at very high speeds,
making them critical to a program's
performance
From the IR perspective
• Analyzing program execution data can help
you understand how malicious code
behaves on your system
• This gives you the knowledge to prevent or
respond to future intrusions 5

## Page 6

Volatile data02
OS info
2
Process
Data
3
System Stat
info
4
What is Operating System Data?
• While the operating system is running, various data used by the
operating system is stored in RAM
• Information created, managed, and stored by a computer's
operating system, including the system's state, configuration,
user experience, logs, and events
Types of operating system data
• Registry files are databases that store important configuration
information in the Windows operating system
• configuration file is a settings file used in various operating
systems to define the behavior of systems and applications
• Operating system data includes file system data, user data,
system health and performance data, and network data
Operating system data
6

## Page 7

Volatile data02
OS info
2
Process
Data
3
System Stat
info
42
What Is Process Data?
• Data generated by a program or task that you run
• For example, a document you're writing in a word processor, a
web page opened in a web browser, etc.
Data about processes highlights
• Process list: process name, PID, and PPID
• Process status: status information, such as running, waiting, or
shutting down
• Process resources: CPU usage and memory usage
• User process data also includes network activity, time
information, process execution path and command line, and
user interaction data
User process data
7

## Page 8

Volatile data02
OS info
2
Process
Data
3
System Stat
info
4
What Is System Health Information?
• Data and information about the current state of a computer
system or software
• Helps monitor the normal operation and performance of the
system and helps identify and resolve problems
Types of system health information
• Operating system information: Information about the type and
version of the operating system currently installed on your
system
• Hardware information: Information about the architecture of
the hardware being used
• Operating time information: Current time
• Network connection information: current network interface
information
System status information
2
8

## Page 9

Volatile data02
https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf
01
04
02
03
Using scripts and built-in functions
Minimize the potential for data
corruption
Minimize traces
Checking the time and whether
something is working
Useful for future timeline creation
Collection logs
Improving the accuracy of ingest logs
Improving the accuracy of your
timeline
Account for differences in each
artifact
Duplicate check
Volatile Sensitivity
Use NIST SP 800-86
OOV
Network connection
information
Logon sessions
Physical Memory
Process information
Open File
About network
settings
System time
9

## Page 10

Volatile data02
https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf
• Volatile data generated during execution
• Analyze the state, code, and data of processes
and threads
• Can analyze malware in memory
Physical Memory
Know your network environment and
network structure
What ports are open
What services are running
About network settings
• Created during the process of logging in
and starting a session
• Identify and track the activity of specific
users
• Identify when a specific user accesses and
logs in
Logon sessions
• Identify which processes are currently
running and the files they are using
• Includes file handle information
Open File
• How your system is connected to the network
• Collected for security, auditing, and monitoring
purposes
• Current network connection and socket
information
Network connection
information
• Determining maliciousness
• Utilized resources to perform malicious
behavior
• Executed by which user
Process information
Based on this information, you can analyze attack patterns by identifying the time of occurrence of cyber security
incidents, the order in which events occurred, and the duration of activity
Identify and correlate events and visualize system event flow
Timeline
10

## Page 11

Volatile data02
Arp -a
Netstat -ano
ARP
Determine the IP addresses and corresponding MAC addresses of
devices currently connected to your network
Identifies each device on the network
Detects activity that deviates from normal network behavior
Netstat -ano
Identify malicious activity
Detect malicious traffic
Identify the early stages of an attack
See which protocols and ports are being used
Be suspicious of unexpected connections between computers
11

## Page 12

Volatile data02
Route
Routing information can help detect suspicious network connections or
routes
Suspicious if routing information is different from normal network flow
Suspicious for external connections or special network configurations
such as VPNs
Route Print
12

## Page 13

Volatile data02
Get-Process, PS
CMDlets in Powershell
Get-Process, PS
tasklist
Tasklist
Use from the command line
What you can learn
Identify malicious software or malicious processes with process
information
Suspect malware when suspicious patterns are drawn
Analytics can detect differences from normal processes
13

## Page 14

Volatile data02
Non-volatile data
Data that persists even after a system or device restarts or loses power
This data is stored in memory, storage devices, disks, etc. and is typically persistent information
Program execution data
Hard disks are primarily used to store non-volatile data
Depending on the file system, files, folders, configuration files, etc. are stored permanently
SSDs, like hard disks, are used to store non-volatile data
EVT
Log
Net
Log
Conf
 IR
Event log
• Event Logs from the Operating System
• System, security, application, etc.
• Records of system status and user activity
Network Log
• Logs related to network activity
• Connection logs
• Remote connection logs
Configuration file
• Files that contain settings and
configurations for your system
• preferences, etc.
From the IR perspective
• Analyze deleted and hidden files
• But very time consuming
• Most often used in incident response for
write protection X
14

## Page 15

Volatile data02
https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf
01
04
02
03
Should we analyze all that information?
Possible damage to the system due to lack of speed
Considerable time required for imaging
Efficient
Non-volatile data has the potential to play an
important role in future submissions as legal
evidence
Add non-volatile data collection scripts to live
data collection scripts for efficiency
Role
Curate data collected, indiscriminate data collection
has the potential to access confidential corporate
information and critical system files
select
Consider corporate policies, legal constraints,
and require informed consent from
managers
Requires careful planning and procedures to
conduct ethically and legally
Checklist
15

## Page 16

Non-volatile data03
Tool name
Forecopy_handy.exe
Download path
https://code.google.com/archive/p/proneer/downloads
01 Prefetch
forecopy_handy.exe –p
02 Registry
forecopy_handy.exe –g
03 Eventlog
forecopy_handy.exe –e
04 MFT
forecopy_handy.exe –m
05 File
forecopy_handy.exe –f PATH
06 Directory
forecopy_handy.exe –d PATH
Collect non-volatile data
16
Collection lists

## Page 17

Non-volatile data03
Forecopy_handy.exe can collect $LOGFILE by using the -f option and entering
SYSTEMDRIVE%$LOGFILE
mft can be collected with the -m option
Registry hive files can be collected with the -g option
Forecopy_handy
forecopy_handy.exe -f %SystemDrive%\$Logfile .
forecopy_handy.exe –g .
forecopy_handy.exe –m .
17

## Page 18

Create a batch script04
CREATE A BATCH SCRIPT
01
STEP
04
STEP02
STEP
03
STEP
Collecting Network
Information
Arp
Netstat
Route
MFT collection
Collecting a registry hive
SYSTEM
SAM
Collect process
information
Task list
Get-Process
18

## Page 19

Create a batch script
Create a batch script04
@echo off
echo start at %DATE%_%TIME% > log.txt
echo OS=%OS% > Computer_info.txt
ipconfig >> Computer_info.txt
::create directory
mkdir vol
mkdir vol\network
mkdir vol\process
mkdir nonvol
Remove unnecessary
alarms
@echo off
Current date and time
values
%DATE%_%TIME
Redirect
>, >>
Create a directory
mkdir
Ip Information
ipconfig
Comment
::
19

## Page 20

Create a batch script
Create a batch script04
::vol
echo start networkpart at %DATE%%TIME% >> log.txt
arp -a > vol\network\arp.txt
netstat -ano > vol\network\netstat.txt
route print > vol\network\route.txt
echo start processpart at %DATE%%TIME% >> log.txt
powershell.exe -command ps > vol\process\ps.txt
tasklist > vol\process\tasklist
Arp table
Network info
Route table
Process list
Collection items and commands
arp –a
netstat –ano
route –print
Get-process (ps)
tasklist
20

## Page 21

Create a batch script04
::nonvol
echo start reg at %DATE%_%TIME% >> log.txt
forecopy_handy -g .\nonvol\
echo start mft at %DATE%_%TIME% >> log.txt
forecopy_handy -m .\nonvol\
echo end program at %DATE%_%TIME% >> log.txt
Collection Behavior
Create a timelog before running the ingest command for each artifact
Collect artifacts for each command
21

## Page 22

Output
Create a batch script04
Output
• MFT
• Registry Hive
• Arp result
• Netstat result
• Route result
• Ipconfig result
• Computer info result
• Process list result
• Time Log
.
22
