---
title: "14강_Process_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\14강_Process_v1.2.pdf"
source_size_bytes: 530388
source_modified: 2025-11-12T12:27:19
imported_at: 2026-06-14T14:26:30
tags:
  - acs
  - acs-advanced
  - imported
---

# 14강_Process_v1.2

- Source: [14강_Process_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/14%EA%B0%95_Process_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Processes
• What Is a Process?
• Normal Processes
• Abnormal processes
14
1

## Page 2

What Is a Process?01
What it does
Code and data allocated in memory
Running status information
All the information you need to manage system resources
PCB
The data structure of an operating system kernel
In an operating system, processes are represented by
PCBs
Each time a process is created, it creates its own PCB
Independence
Processes are allocated independent memory space
No direct access to other processes' memory
Prevents alteration and corruption of other processes'
data
Process
Key concepts in the
system
2

## Page 3

What Is a Process?01
Variables
Initialized data
Data
Code that Contains Actual Commands
Save compiled programs at runtime
Code
Dynamically allocated memory is stored
Possibility of size changes during
program execution
Heap
Calling Functions
Local Variables
Temporary data
Stack
3

## Page 4

What Is a Process?01
Feature
Run
Ready
Prepare for a
delay
Wait
Delay
waitingCreate
Exit
Delay status
4

## Page 5

What Is a Process?01
Running a Process
A process's code runs on the CPU
Program counter increments as the CPU
executes each instruction
Entering the wait state when the allotted time
is exhausted
Exits when allocated tasks are completed
Errors, explicit termination, and resource
reclaim also enter the exit state
Goes to lazy ready when overtaken by a
priority process
Create a process
A user or application requests a new task
Operating system detects the execution
event and registers it with the kernel
Assigns a PCB to manage the process
Stores state, register values, scheduling
information, etc.
Goes to ready state when enough memory is
allocated
Transition to delayed ready state when
memory allocation fails
Process Preparation
Waiting to receive CPU allocation
Determined by scheduling algorithm to be
allocated
Typically uses a round-robin scheduling technique
If CPU is allocated, switch to execute state
Switch to lazy ready if it loses that memory
Process Waiting
Request to process input/output, when
requesting resources that are not immediately
available
Transition to Ready when input/output
completes
Can be placed in lazy wait for free space reasons
Run
Ready
Prepare for a
delay
Wait
Delay
waitingCreate
Exit
Round Robin Scheduling Technique: A CPU scheduling algorithm that allocates CPUs in time quantum/slice in order, without prioritizing processes
Program counter: One of the registers inside the processor that holds the address of the next instruction to be executed, called the instruction pointer
This is needed to speed up the execution of tasks and keep track of the current execution point
5

## Page 6

What Is a Process?01
1
2
A state that a process goes through very briefly
when it exits
Reclaim all resources
Deleting an allocated PCB
3
EXIT
DELAY
WAITING
PREPARE
FOR A
DELAY
Spawned processes not receiving memory right away
Switching from ready or running state when memory is about to be lost
Hold the process to free up memory space
Switching to Ready when it receives memory again
Entering lazy wait state when memory space is lost
When the input/output the process is waiting for is
complete
Transition to wait if memory is freed
6

## Page 7

What Is a Process?01
WHY
Follow-up actions
Isolate or stop the process
Determine if the process was used in the intrusion
Respond accordingly
Post-recovery
Repair and remediate systems damaged in an accident
Recover corrupted files or settings
Minimize changes caused by a breach
Incident tracking
Know exactly what happened when the incident
occurred
Detailed record of process behavior at the time
Essential for future analysis and response strategy
Map the sequence of events
Analyze and respond
Correlate which process it came from
Understand the attacker's behavioral path
Synthesize information to analyze attack patterns and
scenarios
Develop strategies to prevent and respond to similar
incidents
7

## Page 8

What Is a Process?01
01
02
03
04
2. Rootkit
Infiltrates a computer system and is undetectable by the user or
system administrator
Designed to gain unauthorized access and control
Infiltrate the operating system's kernel or core system processes
Gain top-level privileges to access all functions and resources of the
system
Alter system files or processes for stealth and system manipulation
1. What is a malicious process?
Software with malicious intent
Damage and steal information from systems or users
Possess high concealment and intrusion technology
Mainly use technologies such as rootkits and Trojans to
infiltrate and conceal themselves
3. Trojan horse
A type of malware that is downloaded disguised as a legitimate
program
Tricks users into downloading or executing it
Using email attachments, social media links, download sites, etc.
Communicate with an external server on the infected system to carry
out malicious commands
Download additional malicious software
4. Caveats
Some malware deletes itself after execution
Removes itself from the infected system, making detection
and response more difficult
Malicious processes loaded into memory can be extracted and
analyzed
8

## Page 9

Explorer.exe PID : 9916
Parent Process
Typora.exe
POWERPNT.EXE
Notepad++.exe
Procexp.exe
Powershell.exe
Child Processes
Normal Processes02
9

## Page 10

Normal process?
Normal Processes02
Normal
Process
Expected Behavior
Performing expected behaviors
within the system
Execute tasks in an expected
manner
Execution Entity
User
System
Why?
Abnormal behavior can be identified
Compare to normal processes
Roles
Keeping your completion system stable
Provide a variety of features
Abnormal processes
Exists in an inappropriate location and performs unintended actions
Runs with inappropriate privileges and uses too many of your computer's
resources
10

## Page 11

Normal Processes02
Most viewed processes
SYSTEM
Processes that play a key role in the operating system
Manage access to hardware and other system resources, run the core services of the operating system, and maintain
overall system stability and performance
System
Process
Child Process
Interrupt
Smss :
Memory Compression :
Shows system resources used for all hardware interrupts that occur on a PC
Short for System Manger SubSystem, the first system process created after the kernel is created
Responsible for configuring the environment to create a session in Windows, check the Boot
Execute registry to run it
A process, new since Windows 10, that reduces the size of data before it is written to RAM
Computers can store more files than usual in physical memory
Computer speeds up because fewer page files are needed and fewer tasks are called separately
System.exe
In the past, a backdoor named "System.exe" was found in the
Autorun list registration, attackers could use that backdoor to remotely perform malicious activities such as mouse control, file
management, screen capture, keylogging, etc.
"System" processes typically do not have the extension, users notice this difference when reviewing process lists
11

## Page 12

Normal Processes02
Most viewed processes
What we do
System, User Interface: Manage the interaction between users and the system and manage system resources.
Win32 Console Operations: Supports and controls the functionality of Win32 console programs.
System Resource Management: Manages system resources and is responsible for allocating and releasing them
System stability and security: manages communication between subsystems and processes
Glupteba
The Glupteba malware, which emerged in 2020, was found to disguise itself as a legitimate process at C:\Windowsss\csrss.exe and lurk in the
system
Coin Miner malware that mines XMR (Monero) coins by downloading various additional modules to perform various functions
Uses TrustedInstaller's privileges to gain system privileges via UAC Bypass
csrss.exe
Processes that control Windows' graphics system and operate in user mode
When the process is stopped, the Windows operating system stops working, located in C:\Windows\System32
csrss.exe
Process
12

## Page 13

Normal Processes02
Most viewed processes
What we do
Boot and initialize the system: Initialize and start required services and resources
System Periodic Scan and Repair: Checks the consistency of the file system at boot time and repairs errors if necessary
Manage system processes: Manage system resources, responsible for allocating and releasing resources
Service.exe
In the past, malware created to mine cryptocurrencies with the name service.exe rather than services.exe was discovered
The malware is characterized by high CPU and graphics card usage, slowing down Windows, etc.
wininit.exe
Run an uninstaller that carries out the instructions stored in the WinInit.ini file
Program can take necessary actions even while the computer is booting, located at C:\Windows\system32\wininit.exe
wininit.exe
Process
Services.exe
Service Control Administrator as a Child Process of Wininit.exe, required by the system, not the user
Performs tasks such as starting, stopping, and restarting services running in the background of the system, located in 'C:\Windows\System32'
13

## Page 14

Normal Processes02
Most viewed processes
What we do
Manage user logon and logoff: Manage the process when a user logs in or out of the system
Security authentication: Verify user login information and manage access rights for users after applying policies
Desktop initialization: Initialize new work environments and prepare users' desktops for new work
winlogon.exe
Manage the process of when users sign in or sign off the system
This process always runs in the background in Windows and is responsible for some important system functions
winlogon.exe
Process
All of the processes described so far are Windows default processes that cannot be accessed or modified directly by the user
They directly affect the stability and security of the system, so arbitrarily terminating or deleting them will cause serious
problems with the system
Located in "C:\Windows\System32" by default
Caveats
14

## Page 15

Normal Processes02
PATH
C:\Windows
1
svchost
Short for "Service Host“
Responsible for grouping multiple system services and running them within
one process
Svchost loads a dll file and runs it
Runs in multiple instances, each hosting a specific group of services
Typically located in the Windows system folder, C:\Windows\System32
2
conhost
Introduced in Windows 7; in earlier versions of
Windows, the csrss. process fulfills this role
Works when running a console, such as cmd.exe,
PowerShell, etc.
Responsible for rendering graphics in the console
window
3
svchost
Responsible for hosting
system services
Roles
Manage the user interface
conhost
Responsible for running
the console application
Criticality
Not required to run
Windows
Explorer.exe
A program that is an important part of the
Windows operating system and is needed to
manage the user interface
Manages key components of the Windows
environment, such as the taskbar, start menu,
desktop icons, etc.
Not essential to running Windows and can usually
be stopped and restarted from the Task Manager
without negatively impacting the system
15

## Page 16

Normal Processes02
You can actually kill the process from Task Manager
When you terminate, the desktop off
Explorer.exe off
You can rerun the process from Task Manager
When executed, the desktop on
Explorer.exe on
16

## Page 17

Process Explorer
Normal Processes02
Process Explorer
Tool Name
View process information
Search for running processes
Monitor resource usage
Manage processes
Information available
https://learn.microsoft.com/ko-kr/sysinternals/downloads/process-explorer
Download Path
Part of the Sysinternals Suite
Tool Info
Handles and DLLs used by processes
Tracking system resource usage
Tree structure of each process's parent-
child relationships
Resolving IP addresses with network-
related information
Details
17

## Page 18

Normal Processes02
PPID : Parent Process ID
PID : Process ID
Command
wmic process get ProcessID,ParentProcessID,Caption
Explorer.exe PID : 9916
Parent Process
Typora.exe
POWERPNT.EXE
Notepad++.exe
Procexp.exe
Powershell.exe
Child Processes
18

## Page 19

Abnormal processes03
Notepad runs powershell.exe
This is not normal behavior, so suspect
Abnormal processes
Processes running in an unexpected location: System files are typically located in C:\Windows\System32; suspicious when
running outside of this location
Suspicious processes in a parent-child relationship: Suspicious when a process is running behind a process that you did not run
yourself
Processes that use excessive system resources: Suspicious when they use too much CPU, memory, network bandwidth, etc.
compared to normal operations
Run under explorer
Run conhost.exe under powershell
Normal Powershell
19

## Page 20

Abnormal processes03
OFFICE16
OFFlCE16
Little L, Big i
svchsot
20
