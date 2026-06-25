---
title: "15강_Dead_Live_Forensic_(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\15강_Dead_Live_Forensic_(1)_v1.2.pdf"
source_size_bytes: 583731
source_modified: 2025-10-18T19:35:28
imported_at: 2026-06-14T14:25:06
tags:
  - acs
  - acs-advanced
  - imported
---

# 15강_Dead_Live_Forensic_(1)_v1.2

- Source: [15강_Dead_Live_Forensic_(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/15%EA%B0%95_Dead_Live_Forensic_%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Dead, Live Forensic (1)
• Definition of Live Forensic
• Definition of Dead Forensic
• A Comparative Analysis of Dead and Live Forensics
• Situations where Live Foresic is required
• When you need dead forensics
15
1

## Page 2

Definition of Live Forensic01
Incidents Dispatch Collecting evidence
Live Forensic Procedures
2

## Page 3

Definition of Live Forensic01
Principles of
justification
Principles of
ReproductionPrinciples of agility
Continuity of
procedure Principles of integrity
Power On Power Off
Basic principles of digital forensics 3
Live Forensic Procedures

## Page 4

Definition of Live Forensic01
Live Forensic
Volatile data
After filling
Non-volatile
 data
Storage
 Imaging
Precision
analytics
Procedure for performing Live Forensics
Volatile data is information that disappears when the system
is powered off or restarted, such as the contents of random
access memory (RAM).
Non-volatile data, on the other hand, is information that is
preserved when the power is turned off, such as data on a hard
drive.
The main reason to perform live forensics in the field is to
proactively capture volatile data that may disappear when the
system is powered off.
Collecting volatile data should be prioritized in the live forensic
process. This is because much volatile data can be permanently
lost once the system is powered off. Once the volatile data has
been captured, the collection of non-volatile data can proceed,
and imaging of the storage media can be used for subsequent
detailed analysis.
In summary, live forensics is a delicate endeavor that requires a
systematic approach to ensure that potential evidence is
captured in a way that is essential to investigations and legal
proceedings and maintains its integrity and usefulness.
4

## Page 5

Definition of Live Forensic01
Memory Dump
OS and system information
Network connection information
Network Interface Information
Network packet information
Autorun items
Clipboard, Task Scheduler, and event log information
Process information
Live Forensic's guidelines
for volatile data
 collection lists for Live Forensics
Version of the operating system, installed patches,
service packs, hardware information, etc.
The current state of the system, running
processes, network connections, and much
more.
Network connection information for
 associated with the currently open port
About network interface settings
Programs that run automatically at
 when the system boots
What users copied, Task Scheduler contains
 scheduled tasks, event logs
What processes are running and
 details about them
Network packets are the contents of
communications between the system and
 outside of the system.
5

## Page 6

Definition of Live Forensic01
Live Forensic
 Considerations
The first must be collected using an open and validated CLI tool
Collecting active data can potentially compromise evidence on the system and should be done using CLI tools.
What are CLI tools?
CLI tools have a smaller impact on the system than GUI tools and are easier to automate.
Also, CLI tools typically use fewer system resources than GUP tools and can collect volatile data more quickly.
The second is to use a variety of tools rather than relying on a single tool.
As you learn more about digital forensics, you'll realize that there are situations that are invisible with this tool
but visible when using other tools.
For example, a corrupted image file might look fine when viewed in HXD, but be broken and invisible when
viewed through FTK Imager.
For this reason, using multiple dogs can increase the completeness of the data.Of course, excessive duplicate
collection can be a poison.
The third reason we chose standalone as a consideration is that there is a chance that the system's native tools
or libraries could be compromised or tampered with.
Why knowing your operating system is more important than you might think.
It's also important to use the right tools for the right version of the operating system.
Fourth, if a trojan or malware is installed on the system, it is important to cross-validate against physical
memory to verify if there is any hidden data.
Finally, you can use the interpreter natively supported by your operating system.
We'll talk about collecting for live forensics later, but for Windows, collecting with batch scripts or native
Windows tools can prevent evidence from being destroyed by using a different interpreter.
6

## Page 7

Definition of Live Forensic01
ver: Short for "version," the version of the operating
system you're currently running.
useraccount get name,sid: Get the name and
security identifier (SID) of all user accounts using the
WMIC tool
whoami: The currently logged in user's
Return account name
hostname: The hostname of the current system,
i.e., the name of the computer.
wmic os get
Caption,Version,LastBootupTime:
Use the Windows Management Instrumentation Command-
line (WMIC) tool to get information about the operating system
wmic logicaldisk get
caption,description,filesystem
Use the WMIC tool to get information about all drives
connected to your system
Live Forensic commands
7

## Page 8

Definition of Live Forensic01
wmic process list brief
View process information using the Windows Management Instrumentation
Command-line (WMIC) tool. It provides similar information to the tasklist, but
additionally includes the following information.
HandleCount: The number of handles that the process is opening.
A handle is a reference to a system resource.
ThreadCount: The number of threads the process has.
Threads are individual streams of instructions executed within a process.
Priority: The priority of the process. When distributing CPU time, processes
with higher priorities receive more time.
ExecutablePath: The full path to the executable file that runs the process.
tasklist
Shows a list of all processes currently running on the system.
By default, it provides the following information.
Image Name: Name of the executable file that runs the process.
PID (Process ID): The process ID, which is a unique identifier used by
the operating system to manage processes.
Session Name: Name of the session the process is running in.
Session#: The number of the session in which the process is running.
Mem Usage: The amount of memory used by the process.
8
Live Forensic commands

## Page 9

Definition of Live Forensic01
wmic startup get caption,command
Gets a list of programs that run at system startup using the Windows
Management Instrumentation Command-line (WMIC) tool.
"caption" is the name of the program and "command" is the command
used to run the program.
This can help you understand which programs run automatically when
the system boots. This information can be used to find the cause of
system performance issues or to detect malicious programs.
wevtutil qe System /c:N /rd:true /f:text
Query the N most recent entries in the system event log in text format
using the Windows Event Utility (Wevtutil) tool.
"/c:1" specifies the number of events to view, "/rd:true" specifies to view
the most recent events first, and "/f:text" specifies the output format as
text.
You can see the most recent events that have occurred on your system.
You can also analyze as many event logs as you need, even though you
wrote N.
9
Live Forensic commands

## Page 10

Definition of Live Forensic01
The ipconfig /all command provides configuration information
about a network interface card (NIC). This information is useful for
diagnosing network problems or verifying network settings.
Host name: Indicates the name of the current system. Used to identify the
system on the network.
Primary DNS Suffix: The primary DNS suffix is used to create the system's
full domain name; without this information, the system would only have
a hostname.
Node Type: This indicates which method the system uses for name
resolution; "Mixed" means the system uses both broadcast and WINS.
Enable IP Routing, Enable WINS Proxy: These indicate whether the system
uses IP routing or the WINS proxy feature.
Wireless LAN Adapter Local Area Connection* 1, * 2: These indicate the
wireless network adapter.
Media Status: This indicates the current network connection status,
"Media Disconnected" means that it is not currently connected to the
network.
"Description" indicates the type of network adapter and "Physical
Address" indicates the MAC address of the
 network adapter
10
Live Forensic commands

## Page 11

Definition of Live Forensic01
Ethernet Adapter Vmware Network Adapter VMnet1, VMnet8: These
represent Vmware virtual network adapters. They are used by virtual
machines to communicate with the host system.
Wireless LAN Adapter wlan0: This represents the primary wireless
network adapter.
IPv4 address: Indicates the IP address assigned to you when you
connected to the network.
Subnet mask: determines which part of the network represents the local
network.
Default gateway: Indicates the path the system uses to connect to the
external network.
Ethernet adapter Bluetooth network connection: this indicates a
Bluetooth network adapter Used to communicate with Bluetooth devices
11
Live Forensic commands

## Page 12

Definition of Live Forensic01
netstat -ano is a command to display network statistics.
netstat stands for "network statistics" and is a useful tool that
provides information about your network, including network
connections, routing tables, interface statistics, and more.
The -ano option has the following meanings
-a: Show all (active) connections and listening ports
-n: Display addresses and port numbers as numbers
 By default, netstat attempts to display the host name,
communication protocol name, and network service name.
-o: Display the process ID of the process that owns the connection
The netstat -ano command can provide the following information
Protocol: Information about the protocol of network packets.
Local Address: IP address and port number of the current system.
Foreign Address: The IP address and port number of the connected
external system.
State: Indicates the status of the current connection.
For example, LISTENING indicates that the system is currently
waiting for a connection, ESTABLISHED indicates a successful
connection, and so on.
Process ID (PID): The ID of the process that owns the connection.
This is useful for determining which process is using a particular
connection.
12
Live Forensic commands

## Page 13

Definition of Dead Forensic02
Source: KITRI BoB Project
Once the volatile data has been collected, the next
step is to collect the non-volatile data and image
the storage media, collect and store evidence, and
transport it.
While it is obviously preferable to collect data on-
site, it is often difficult to seize the target's device
unless the person has already been proven guilty.
From a company's point of view, the loss of the
device could result in immediate business loss.
This makes it natural to collect volatile data and
record information on each device and image the
storage media.
13
Understanding dead forensics

## Page 14

Definition of Dead Forensic02
Dead Forensic
Hibernation
Obtaining keys, session values
Snapshots
Analyze non-volatile data
Image
virtualization
Dead forensics is a digital forensics approach that is performed
when a system is turned off, or "dead".
In this approach, it is important to analyze non-volatile data, that is, data
that remains when the power is turned off. Non-volatile data includes file
systems and data stored on storage media such as hard drives, SSDs, and
flash drives, as well as system logs, application logs, and more. Analyzing
non-volatile data in Dead Forensic has the following benefits.
Reliable analysis through image virtualization: You can create an exact
replica (image) of a storage medium while preserving the original data.
This image can be mounted in a virtual environment to analyze data
without tampering with the original system.
Hibernation file analysis: Hibernation is the ability to record the state of a
system on a storage medium so that it can be quickly recovered later.
Hibernation files (e.g., hiberfil.sys) contain the contents of system
memory, so by analyzing them, you can recover and analyze portions of
volatile data.
Obtaining keys and session values: Dead forensic analysis can be used to
extract sensitive security-related data such as encryption keys used on a
system, user session information, authentication tokens, and more. This
can provide important clues in a security breach case.
Point-in-time analysis with snapshots: Snapshots record the entire system
state at a specific point in time. By analyzing these snapshots, you can
determine the state of the system at the time of the incident, the
presence of files, user activity, and more.
14
Understanding dead forensics

## Page 15

Comparative Analysis of Dead and Live Forensics03
Live Forensic Dead Forensic
Collected dataPurpose Procedure
Risks Limitations
Commonalities
| |Collect, preserve digital evidence,
analyzed, and used as legal
evidence as legal evidence.
System information, user
activity, files, network activity,
etc. Collect a variety of data
Follow elaborate procedures to
minimize the trail of evidence and
strive to maintain the integrity of
the evidence
Live forensics can affect your system, and there
is a risk of accidentally destroying evidence.
Dead forensics, on the other hand, analyzes
replicated data, so there is less risk of
destroying original data.
Imaging virtualization in Dead Forensic
depends on the existence of hibernation
15

## Page 16

04
Malware infection
When a computer is infected with
malware, volatile information such as
running processes, network
connections, and data stored in
memory can be used to analyze the
malware's behavior and determine
what damage was done.
Insider threats
To detect employee activity that seeks
to leak information inside your
organization, you need to collect
volatile data.
Track your activity through running
programs, web browsing history,
clipboard contents, network
connections, and more, and prevent
sensitive information from being
compromised
Real-time cyberattacks
When a cyberattack on your
organization is in progress, you need
to collect volatile data to monitor
attacker behavior in real time.
Network connectivity, running
processes, system logs, and more can
help you understand the path and
method of the attack and respond
immediately.
Situations where Live Forensics is required
16
Situations where Live Forensics is required

## Page 17

04
Situations where Live Forensics is required
Accessing encrypted data
Windows BitLocker
As digital devices become more secure, live forensics is becoming
increasingly important.
Especially when users have encryption on their devices, it
becomes impossible to obtain sensitive data without breaking it.
Digital devices such as PCs, smartphones, and tablets are
typically encrypted with varying levels of encryption by the user.
For example, there may be encryption for user accounts, and if
you have a Pro version of Windows, you can encrypt the entire
disk with a feature called Bitlocker. Cell phones are similar, with
Apple's iPhones making sure that no one but the owner knows
the password you set, Android, after a certain version, makes it
impossible to access data without knowing the password. This is
where Live Forensic comes into play.
It allows you to collect data while it is still unencrypted, with the
cooperation of the subject of the investigation .In principle, this
can yield more information than collecting data through dead
forensics, allowing for a more complete analysis.
17
Situations where Live
Forensics is required
Situations where Live Forensics is required

## Page 18

04
Situations where Live Forensics is required
Value as evidence
Example of what the scene looks like during Live Forensics
Evidence
Investigato
rs Inductees
Who
should be
surveyed
Live forensics is a method that enables the real-time collection and
analysis of digital evidence, Essential for preserving and analyzing
evidence that can easily disappear or change, especially volatile data that
only exists when the system is up and running.
A key part of digital forensics, it plays a critical role in criminal
investigations. Live forensic procedures vary depending on the laws and
policies of each country or organization. Typically, these investigations
are conducted on-site, and sometimes remotely. The presence of the
subject of the investigation may vary depending on the circumstances,
but the destruction or manipulation of evidence during the investigation
is strictly prohibited. Live Forensic courses allow for selective evidence
collection to the extent permitted by law.
This means seizing only a limited range of evidence through a warrant
under certain circumstances. Because selective seizures tend to rely on
investigator judgment, it is important to involve digital forensic experts
and the subject of the investigation or his or her legal representative to
ensure impartiality and maintain the integrity of the evidence.
Evidence collected and analyzed through Live Forensic has legal value and
can be used as evidence in court. Such evidence can provide crucial
information in solving a case and, as a result, facilitate a quick and
effective criminal investigation. As such, Live Forensic is an important part
of digital forensics, contributing to the accuracy and reliability of
investigations through the rapid acquisition and analysis of evidence.
18
Situations where Live
Forensics is required
Situations where Live Forensics is required

## Page 19

When you need dead forensics
Revisit and drill down
Leverage additional
analytics tools
Overcoming the limitations
of Live Forensic
Ensure reproducibility
Dead Forensics is used when information
gathered through Live Forensics needs to be
revisited or further analyzed. Because the data
collected by Live Forensic is often limited or
incomplete, after shutting down the system and
creating a clone more in-depth analysis can be
performed after shutting down the system and
creating a clone.
In Dead Forensic, you can perform more
precise analysis of specific areas. For
example, it can be used to analyze file
system metadata, deleted files, space
allocation information on a disk, and
more. These analyses provide more in-
depth information and can provide
important insights for criminal
investigations.
In Live Forensics, you need to take
limited actions to avoid disrupting the
operation of the system, but in Dead
Forensics there are no such restrictions
Dead Forensic helps ensure
reproducibility, one of the fundamental
principles of digital forensics. By
following precise procedures to ensure
that the analysis process and results can
be reproduced, and by targeting non-
volatile data or copies of data that do
not change, the reliability of the analysis
results can be increased.
04
19
Situations where Live
Forensics is required
Situations where Live Forensics is required
