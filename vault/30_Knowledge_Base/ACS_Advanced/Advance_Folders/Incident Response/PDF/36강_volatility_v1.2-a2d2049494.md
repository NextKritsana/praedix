---
title: "36강_volatility_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\36강_volatility_v1.2.pdf"
source_size_bytes: 1035399
source_modified: 2025-11-12T13:31:14
imported_at: 2026-06-14T14:26:56
tags:
  - acs
  - acs-advanced
  - imported
---

# 36강_volatility_v1.2

- Source: [36강_volatility_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/36%EA%B0%95_volatility_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

volatility
• What is a memory dump?
• volatility2
• volatility3
36
1

## Page 2

What is a memory dome?01
What is memory?
Computer memory is the space where a computer temporarily stores and processes data
Storage space that a computer's central processing unit can access quickly, holding data and instructions that the
computer needs while it performs tasks
RAM is readable and writable, and is a volatile memory that loses all stored information when the power is turned off
What information is stored
Memory stores the instructions of the running programme
The values of variables used during execution are stored in memory, and variables are various data types such
as numbers, strings, and objects
Memory stores a variety of information about the system, including information about the currently running
process, network status, hardware status, etc.
Storage, including the stack and heap areas that programs use to store and manage data
Incident Response Perspective
• Because memory dumps capture the state of a computer's memory at a point in time, they contain real-time system information,
including currently running processes, network connections, and loaded modules
• Can reveal what an attacker has been doing on the system and what state it is currently in
• By analysing memory dumps, it is possible to detect malicious code that is not stored on disk but only operates in memory
• Information gained from analysis can be used to build a defence system to prevent similar attacks in the future, or to respond quickly
when an attack occurs
What is a memory dome?
2

## Page 3

Create a memory dump
Memory dump using the FTK Imager tool
Run FTK Imager
Press File and click Capture Memory
Set where to store that memory in the destination path
Start memory dump when Capture Memory is selected
How?
Caveats
Depending on the computer you're using, it can potentially take up a significant amount of space
What is a memory dome?01 What is a memory dome?
3

## Page 4

Check the memory dump
A little more! Understanding
This captured memory stores the value of the
reference when you clicked Capture Memory
Analysing the memory dump file can reveal what
was happening at the time
The dump was taken from a computer with 16GB of
RAM, which has about 19 gigabytes of storage
Description.
• A memory capture is easier to understand if you think of it as taking a single photo
• In the photo, the passerby, water, birds, etc. are no longer moving and are still
 This is also true of the memory capture
• No processes are moving, and processes that are running are stuck where they are
What is a memory dome?01 What is a memory dome?
4

## Page 5

Smaller memory files
vmem is an abbreviation for Virtual Memory File
Created by VMware Workstation when a running virtual machine is paused
Virtual memory files can be used primarily for debugging, analysis,
forensics, etc.
Depends on the size of the virtual memory granted to the virtual machine
when it was created
In the case of the virtual machine shown in the PPT, it has a size of about 2
gigabytes
1/9th of the memory files dumped from the local host
.vmem
Extracted vmem
What is a memory dome?01 What is a memory dome?
5

## Page 6

Volatility2
Memory file analyzer
• Volatility 2 can analyse memory dumps created by various operating systems
including Windows, Linux, Mac and Linux
• Supports plugins to extract information such as network connections, running
processes, loaded drivers, open files, registry keys, and more
• Open source project, allowing users to modify the code or add new plugins as
needed
• Memory dumps can be used to find traces of malicious code, track user
behaviour, investigate the health of a system, and more
• In the course, we will use standalone, which means that the programme can be
analysed on its own without the need for a separate course
What is volatility2
https://www.volatilityfoundation.org/26
Windows XP
Windows Vista
Windows 7
Windows 8
Basic support
Linux (Ubuntu, Debian)
Mac
Requires a separate
symbol
http://downloads.volatilityfoundation.org/releases/2.6/volatility_2.6_win64_standalone.zip
Download PATH
What is a memory dome?01 What is a memory dome?
6

## Page 7

Volatility3
Memory file analyzer
• As python2 reaches the end of its life, development of volatility2 is stopped and volatility3 is
developed using python3
• Volatility 3 focuses on ease of use
• Volatility 3 can be cloned via Git and used immediately without a complex installation
process
• For Windows operating systems, profiles are created completely automatically, making it
easy to change profiles
• For Linux, Volatility now interprets the Linux kernel's table of symbols to find the meaning of
values in memory
• Volatility analyses the kernel's symbol table and saves it in its own special format, the ISF file
format, which can be used to analyse Linux memory dumps
What is volatility3
Windows, Linux, MAC
Windows 10 analyzable
Supported OS
https://github.com/volatilityfoundation/volatility3/archive/refs/tags/v2.4.1.zip
Download PATH
Volatility Foundation
Volatility3
https://isf-server.techanarchy.net/
ISF Table
What is a memory dome?01
7

## Page 8

volatility202
Dump is a term in computer science that generally refers to the bulk extraction or copying of data
A process dump, or partial memory dump, allows you to analyze what happened in that part of the memory.
Dumping a file lets you see its contents
Dump function
Collect process information, registry information, handles, and more
Information
See which ports are open and what network connection information is available
Identify the attacker's entry path
Network information
volatility2
8

## Page 9

https://www.volatilityfoundation.org/26
volatility_2.6_win64_standalone.exe with the -f option to select memory files to analyze, using the imageinfo plugin
This plugin allows you to retrieve basic information about the selected memory dump. You can check the operating system version, localtime, KDBG info, Profile info, etc.
imageinfo
• The KDBG provides the information necessary for the kernel debugger
to analyse and debug kernel modules
• KDBG contains identifying information about the kernel, such as the
kernel version, build number, compilation date, etc.
• Knowing the kernel version information allows you to check
compatibility with an application or driver
• Information about the debugging client to which the debugger is
connected, including the debugging session ID, debugging mode, etc.
• The KDBG contains information about the current debugging session
• The system's global KDBG also contains information about the current
debugging session
• Information about debugger extensions, which are used to assist in the
debugging process or provide additional functionality
About the kernel
Volatility_2.6_win64_standalone.exe -f [memory_file] imageinfo
Command
volatility202 volatility2
9

## Page 10

Print all running processes in chronological order
If a malicious process was running, you can find traces of it in Pslist's output
and see when it started
Double Linked List format for browsing
pslist
If the difference between the start and end times is less than a second, the process is suspicious
Malware often renames processes similarly to disguise itself as a legitimate process, so check the name carefully as well
pslist Noteworthy
Double Linked List
A linear data structure where each node has two references, one pointing to the next node and the
other to the previous node
The data part contains the actual data stored in the list, and the link part contains references to the
next and previous nodes
The pslist plugin tends to rely on this Double Linked List traversal and therefore fails to detect DKOMs
DKOM
Short for Direct Kernel Object Manipulation, the act of modifying kernel objects
directly
DKOM can be used to hide processes, hide device drivers, escalate thread
privileges, escalate process privileges, etc
Can see hidden processes
Verify processes with different verification techniques
Check against Pslist to see which processes are hidden
psxview
volatility202 volatility2
10

## Page 11

• Roles structured by PID and PPID
• Except for the first process created, all processes are created by cloning the
parent process and a hierarchical tree is created, where each process has
information about the child processes and the parent process
• It is easy to see the relationship between parent and child processes, and it is
easy to see which processes created which other processes
• The behaviour of a particular process can be traced through the tree
• Quickly detect processes that behave differently from commonly known
processes
pstree
Commands
• Volatility_2.6_win64_standalone.exe -f [memory_file] --profile=[PROFILE] pslist
• Volatility_2.6_win64_standalone.exe -f [memory_file] --profile=[PROFILE] psxview
• Volatility_2.6_win64_standalone.exe -f [memory_file] --profile=[PROFILE] pstree
volatility202 volatility2
11

## Page 12

• vol -f [memory_file] --profile=[PROFILE] memdump -p [PID] -D [PATH]
• vol -f [memory_file] --profile=[PROFILE] dumpfiles -Q [OFFSET] -D [PATH]
https://lifars.com/wp-content/uploads/2020/07/Windows-Memory-Forensics-Technical-Guide-Part-3.pdf
Dump files and data
mumdump
Extract executable files only
procdump
Commands
volatility202 volatility2
12

## Page 13

• vol -f [memory_file] --profile=[PROFILE] filescan
• vol -f [memory_file] --profile=[PROFILE] dumpfiles -Q [OFFSET] -D [PATH]
Extractable files
Pool tag scanning
method
filescan
File Dump
filedump
Commands
How to scan physical or virtual memory on a Windows system to find memory blocks with a specific pool tag
The 'Pool Tag' method is one of the methods used by the Windows operating system for memory management
It provides an identifier to help track and debug memory allocation requests
Each block of memory allocated from a memory pool is tagged with a 4-byte string called a 'pool tag', which helps to identify what that memory is used for
Pool tag scanning
volatility202 volatility2
13

## Page 14

You can see the command via vol.exe -h
Netscan
• Extract network connections, listening ports, network-related processes, etc.
running on Windows operating systems
Cmdline
• Used to extract a process's command line arguments from a memory dump
• You can determine which arguments a process was started with, which can
be useful for malware analysis, system anomaly analysis, etc.
Console, cmdscan
• View commands entered using cmd
• See what users have done with cmd
Other plugins
Yara Support
YARA stands for "Yet Another Recursive Acronym" and can be used to identify malware patterns using text-based rules to identify malicious code patterns
Identify specific patterns or behaviors of malware in memory dumps
YARA rules can be used to perform malware detection and analysis, which can improve the security of your system
volatility202
14

## Page 15

OS.[Command]
volatility303 volatility3
15

## Page 16

https://github.com/volatilityfoundation/volatility3/blob/develop/doc/source/vol-cli.rst
Similar role to symbols in Volatility2
Use the --save-config option to create a config.json file and
view it to see that it contains information such as OS Version,
KDBG, System time, etc.
config.json
Why?
The reason for doing this is that it saves time in the end
After analysing it once, we don't need to do it anymore, but since the plugin starts scanning with Scanning memory_layer using bytesScanner every time you use it, you
can skip it if you specify the config.json file with the -c option
Of course, you can use a shorter command without the -c option
Why?
• vol --save-config config.json -f [memory_file] windows.info
volatility303 volatility3
16

## Page 17

volatility2 volatility3
vol.exe -f [MEMORY FILE] --profile=[PROFILE] pslist vol.exe -c [CONFIG FILE] -f [MEMORY FILE] windows.pslist.PsList
vol.exe -f [MEMORY FILE] --profile=[PROFILE] psscan vol.exe -c [CONFIG FILE] -f [MEMORY FILE] windows.psscan.Psscan
vol.exe -f [MEMORY FILE] --profile=[PROFILE]
dumpfiles -Q <offset> -D [PATH]
vol.exe -c [CONFIG FILE] -f [MEMORY FILE]
windows.dumpfiles.DumpFiles --physaddr <offset> -D [PATH]
https://newtonpaul.com/malware-analysis-memory-forensics-with-volatility-3/
Tips
python2 is rarely used, python3 is mostly used
However, volatility3 allows you to analyze windows10, but when analyzing windows 7, you may want to use volatility2, which has more features
Depending on the type of OS and what you're collecting, you'll need to consider which tools and versions to use
Command differences
For Volatility3, notice that the -profile option used by volatility2 is gone
Instead, use the -c option to specify the configfile, which speeds up the operation
volatility303 volatility3
17

## Page 18

volatility3-2.4.1\build\lib\volatility3\framework\plugins\windows
PATH
 install
volatility303 volatility3
18

## Page 19

volatility303
Modifying plugins
Using help in Volatility3, you can see that there is no plugin called hashdump in the list of available plugins
Hashdump is a command that is mainly used to extract SAM files
I noticed that it was provided by default in Volatility2, and was also visible in the list of available plugins, but not in volatility3
volatility3-2.4.1\build\lib\volatility3\framework\plugins\windows
Plugin PATH
 Install
•Using pip in powershell, first install the modules named
pycryptodeme and volatility3 using powershell
•PyCryptodome is a powerful cryptographic library used in
Python
•PyCryptodome is a replacement for the old PyCrypto
libraryPyCrypto is no longer being developed, and
PyCryptodome is an improved version that inherits the
functionality of PyCrypto
•hashdump.py requires this module to be imported to use it
19

## Page 20

volatility303
Hashdump.py
Open hashdump.py and you can see the syntax that is calling crypto without the
crypto module
Crypto
If you open hashdump.py, you can see that you are calling crypto without the crypto module
Add crypto and sys to the import and use the sys.module['Crypto'] = crypto command on line 9 to change crypto
starting with a capital C to crypto starting with a lowercase c
After modification
Confirm Add Hashdump
Injection
volatility3
20
