---
title: "16_Dead_Live_Forensic_(2)_v1.5"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\16_Dead_Live_Forensic_(2)_v1.5.pdf"
source_size_bytes: 837552
source_modified: 2025-10-18T19:35:33
imported_at: 2026-06-14T14:25:07
tags:
  - acs
  - acs-advanced
  - imported
---

# 16_Dead_Live_Forensic_(2)_v1.5

- Source: [16_Dead_Live_Forensic_(2)_v1.5.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/16_Dead_Live_Forensic_%282%29_v1.5.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Dead, Live Forensic (2)
• The evidence collection process in Live Forensic
• The Evidence Gathering Process in Dead Forensics
• Imaging
• Hibernation
16
1

## Page 2

The evidence collection process in Live Forensic01
D F  I n v e s t i g a t o r
P e r s p e c t i v e
Collect and analyze digital evidence
Volatile data
T h e  C E R T
p e r s p e c t i v e
Minimize damage
Initial Response
Collection x Analysis and Response o
Active data
Digital
Forensic
Computer
Emergency
Response
2

## Page 3

The evidence collection
process in Live Forensic01
Source: SP 800-86, Guide to Integrating Forensic Techniques into Incident Response | CSRC (nist.gov) 3
The evidence collection process in Live Forensic

## Page 4

01
Network connectivity information
 All networks the system is currently connected to, including connection
status, ports, and protocols in use.
Login sessions
Who is currently logged into the system, when they logged in,
where they logged in, etc.
In-memory information
 Currently running processes, open files, network
connections, etc.
Running processes
 Process name, PID, resources being used,
time the process started, etc.
Open file
 information includes file name, location,
time opened, program opened, etc.
Network configuration
 IP address, MAC address, subnet mask,
default gateway, DNS server, etc.
Operating System Time
 The current time set on the system
Volatile data
4
The evidence collection process in Live Forensic

## Page 5

01
Power Off
Power
Saving
5
The evidence collection process in Live Forensic

## Page 6

01
Secure Boot
What UEFI does, loading only signed software at boot time
to prevent unauthorized code execution
Measured Boot
Validate system integrity by measuring system configuration
during the boot process and storing it in the TPM
Root of Trust
Load hardware-level trusted code and configuration
during the initial boot phase of the system
Read-Only File System
Make critical parts of your system read-only to
prevent unauthorized changes to

Immutable Infrastructure
Treat systems and applications as immutable components and
replace them in their entirety when necessary to maintain integrity
Situations where Live Forensics
should be performed even when
power is off
6
The evidence collection process in Live Forensic

## Page 7

01
Mechani
smsLinux
Hash
Funct
ion
Digital
signat
ures
fileDirectory
Tripwire Cryptographic
 Verification
IMA
Concept Design
Security software that monitors the integrity of system files
and configuration files and detects changes.
It periodically scans files for changes using hash-based
checksums and sends out alerts if there are any violations. The
tool is available in commercial and open source versions for
increased compliance and security.
TripWire
Measure the integrity of files on Linux systems and
generate hash values of files during validation boot
and production to ensure system integrity and
monitor them for tampering in real-time by storing
them in a trusted platform module (TPM)
Validate that your implementation of a cryptographic
algorithm complies with the standards of the U.S. National
Institute of Standards and Technology (NIST).
Operates in conjunction with the Cryptographic Module
Validation Program (CMVP), which provides validation
according to the IPS 140 standard.
Cryptographic Algorithm
Validation Program
Integrity Measurement Agent
System integrity
verification tools
7
The evidence collection process in Live Forensic

## Page 8

01
Windows
Individual
Memory Dump
8
The evidence collection process in Live Forensic

## Page 9

01
1
2
3
Advanced system
settings
Startup
And
recovery
-> Settings
System error
-> Write Debugging
Information Full memory
dump
Windows
Full Memory Dump
9
The evidence collection process in Live Forensic

## Page 10

01
Run the Registry Editor
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet \Services\i8042prt\Parameters
(i8042prt is the registry key for the PS/2 keyboard and mouse driver)
Restart
Restart to apply changes
Create a new registry key
DWORD (32-bit) value - Create CrashOnCtrlScroll
Value Data 1 - Enabled
Conclusion When the system fails or you manually create a dump, a memory dump file is created at
 in the specified location (%SystemRoot%\MEMORY.DMP).
Blue Screen
 -System Error Occurred
Windows
Causing system errors
10
The evidence collection process in Live Forensic

## Page 11

01
Seizing the target's entire data or device
Blanket seizure
Legal basis and scope Purpose and necessity
of the investigation
Time and resource
constraints
Consider privacy and
human rights
Search warrants
Legal restrictions
Clarity of purpose
The importance of evidence
Time constraints
Resource efficiency
Privacy and human rights
considerations
Targeting only specific data or information to seize

Selective seizure
11
The evidence collection process in Live Forensic

## Page 12

The Evidence Gathering Process in Dead Forensics02
Dead Forensic
Collecting data
12

## Page 13

02
01
02
03
Requires real-time monitoring
If your system needs to be monitored in real time and shutting it down would
result in the loss of critical volatile data
Continuous service needs
 Systems that require continuous operations, such as hospital systems,
financial transaction systems, emergency services, etc.
Distributed systems
 In cloud services or large distributed networks, data is distributed across
multiple locations.
When Dead Forensic is not available
13
The Evidence Gathering Process in Dead Forensics

## Page 14

02
Storage medium
 A physical device or medium used to store digital data.
HDD
Storing data using magnetic storage technology,
which uses a head that writes and reads data onto
a spinning disk (platter).
SSD
Storing data using flash-based memory
Storing data electronically without any moving parts
USB
Use flash memory to store data Connect to a
computer via USB interface
SD Card
SD card is a flash memory based
portable storage medium
14
The Evidence Gathering Process in Dead Forensics

## Page 15

02
•Keyword
•Keyword
Collect and analyze key evidence files
After creating an image of the data from the storage media, collect
and analyze key evidence files within that image that may be legally
significant or provide crucial information to an investigation. The
evidence collected may later be used in court, so systematic
documentation and report writing is critical.
Media-separated storage
The separation of different storage media on a target device.
This is necessary to protect integrity and ensure that data is
stored and analyzed safely on each medium.
Separated media are protected from data being overwritten
using tools such as write blockers and image copies.
The Evidence Gathering Process in Dead Forensics
15
The Evidence Gathering Process in Dead Forensics

## Page 16

Imaging03
Image dump
Copying the entire contents of a computer storage device (e.g., hard drive, SSD) or
 memory in the form of a file
Dump
A term that refers to the act or result of making a comprehensive copy of data in its entirety.
16

## Page 17

Imaging03
Mount an image
The process of connecting a disk image file to a computer as a virtual drive

Mount
The process of connecting storage media to the system and getting it ready to use
17

## Page 18

Imaging03
Raw image
(.img, .dd)
Advanced
Forensic Format
 (.aff)
Smart Forensic
Format
 (.s01)
Virtual Hard Disk
(.vhd/.vhdx
Expert Witness
Format
 (.E01)
Virtual Machine
 Disk Format
 (.vmdk)
Disk image files contain an exact copy of a computer storage device and exist in a variety of formats
 Each format has specific properties and compatibility, and is chosen based on the forensic tool or purpose being used.
An exact copy of the
data at the bit level,
with no additional
 metadata or
 structure.
Open source,
supports
compression and
metadata
Formats widely
used by EnCase
forensic software
Optimize
 for SMART
Forensics
 software
The format used by
VMware to store a
virtual machine's
disk
Formats used by
Microsoft's
virtualization
solutions
18

## Page 19

Imaging03
01
02
03
First-Party Program
 The company that created your computer's operating system.
Second-Party Program
 Users on the computer
Third-Party Program
Software created by companies or developers
First-Party
Program
Second-Party Program
Third-Party Program
Third-Party Program Features
•Provide additional functionality: Offer features or
services that the operating system doesn't provide
natively.
•Compatibility: Works with a wide range of
operating systems
•Diversity: Developed from a variety of sources and
for a variety of purposes,
increasing user choice
•Buy, get free: Many third-party programs are free
Some are available through purchase
19

## Page 20

Hibernation04
Hibernation
A phenomenon in which an animal or plant
minimizes its physical activity and enters a state
of dormancy for an extended period of time to
survive in cold or starvation conditions.
A computer's "hibernation mode" used to
store the user's current session and work state
on disk and preserve that state even after the
computer is turned off or put to sleep.
20

## Page 21

Hibernation04
Reselect
A term referring to being brought back to
life or resurrected after eternal death.
In digital forensics, system redirection refers
to the process of restoring a computer to a
previous state using hibernation.
Source: https://nexon.maple.com
21

## Page 22

Hibernation04
Hiberfil.sys Related Article Reviews
22

## Page 23

Hibernation04
Options Whether to save memory
data to the Hiberfile.sys file
The memory area where it
is stored
Whether to enable by
default
Shutting
down the
system
Quick Start
ON O Kernel O
Quick Start
OFF X -. X
Restart X -. O
Sleep mode X -. X
Hibernate O Kernel + Users O
Hybrid power saving
modes O Kernel O
23

## Page 24

Hibernation04
24

## Page 25

Hibernation04
25
