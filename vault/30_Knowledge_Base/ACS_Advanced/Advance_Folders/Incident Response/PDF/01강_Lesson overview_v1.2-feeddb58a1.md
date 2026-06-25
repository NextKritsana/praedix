---
title: "01강_Lesson overview_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\01강_Lesson overview_v1.2.pdf"
source_size_bytes: 1422716
source_modified: 2025-11-12T12:05:49
imported_at: 2026-06-14T14:26:21
tags:
  - acs
  - acs-advanced
  - imported
---

# 01강_Lesson overview_v1.2

- Source: [01강_Lesson overview_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/01%EA%B0%95_Lesson%20overview_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Incident response
ACS Education
1

## Page 2

•Lesson Overview
•What is Incident Response?
•Key Artifacts
•Powershell
•Active Directory
•Various Analytics
•Create a timeline with hands-on
•Comprehensive hands-on
Index
2

## Page 3

Lesson overview
• Lesson overview
• Install a Windows Virtual Machine
• Other installation and configuration settings
01
3

## Page 4

Lesson overview01
02 03
0401
Assets owned
Data is a valuable asset to organizations and individuals
When data is exposed, sensitive data such as business secrets,
personal information, financial information, etc. are lost
Privacy breaches and financial losses
Business Continuity
Causes problems like service interruptions
Organizations, businesses ensure continuous
service delivery
Maintain business continuity by responding
effectively
Incident Response
How organizations and individuals respond to information security issues
Serious damage if not responded to effectively and appropriately
Rules and regulations
Organizations comply with information
security regulations
Working with regulators in the event of a
cybersecurity incident help minimize fines
and legal problems
Reputation and
reliability
Consumers and partners want to do business
with organizations that are safe and reliable, so
Incident
response
reputational damage can
occur if you don't respond
effectively to a
cybersecurity incident 4

## Page 5

Lesson overview01
What to do by virtual asset
Initial response to a cybersecurity incident
Dealing with situations
Rapid Response vs Accurate Analysis
What we collect
Prioritize protection
Good judgment
Recent Attack Techniques
Trending Attack Techniques
Incident Types
Documents, Executables
Network
Memory
And many more analysis targets, techniques
Analytics techniques
Incident response
A lot of information
5

## Page 6

Incident Theory Main artifacts Powershell
ADVariety of labsCreate a timeline
Courses
Incident overview and history
Introducing trends and guides
Introducing the Cyber Threat Model
What are TTPs, Scenario Creation
Volatile & non-volatile
Artifacts
Processes
Create online collection tools
Reasons for automation
Powershell Automation
Incident Analysis with Powershell
Powershell Malicious Script
Memory analysis
Documented malware
Collaborating with other tracks
Ransomware
Creating an incident A to Z
Analytics and timelines
Build reports
What is AD?
Configure an AD environment
AD and Powershell
AD Environment Labs
Lesson overview01
6

## Page 7

Install a Windows Virtual Machine02
VMWare Workstation
• A company that provides virtualization solutions and cloud computing services, developing software that enables virtualization technology to create and
manage virtual machines
• Used in a variety of areas from server virtualization to cloud management to network virtualization
• Workstation is virtualization software that allows you to create and run virtual machines on your personal desktop
• Typically used by developers or system administrators to experiment and test virtualization in a local environment
Benefits of Virtual Machines
Isolation from the host
• Virtual machines offer many benefits for incident response by providing an environment that is completely isolated from the host system
• By providing an environment that is independent of the host system, virtual machines ensure that applications or processes running within the virtual machine do
not directly impact the host system
• This provides the advantage that if an intrusion occurs, the intrusion will only affect the virtual machine and not the host system, which is not directly at risk
Provide snapshots
• Saves the state of a virtual machine at a point in time, allowing you to quickly restore it to a previous, secure state in the event of a cybersecurity incident
Build an experimental environment
• Explore and analyze the causes and effects of a cybersecurity incident without impacting real systems, develop new response strategies, or test countermeasures
against specific attack patterns
• Conduct training and education on incident response, enabling you to safely experience difficult scenarios or high-risk situations in a virtual environment and
improve your response capabilities
7

## Page 8

02
https://www.microsoft.com/en-us/software-download/windows10
Windows 10 iso file
https://developer.microsoft.com/en-us/windows/downloads/virtual-machines
https://www.VMware.com/products/workstation-pro/workstation-pro-evaluation.html
Vmware download
Install a Windows Virtual Machine
8

## Page 9

kusti
Vmware workstation 17 player
02 Install a Windows Virtual Machine
9

## Page 10

Installing a Windows 10 ISO
02 Install a Windows Virtual Machine
10

## Page 11

You can see that windows 10 is installed
Interim results
02 Install a Windows Virtual Machine
11

## Page 12

Select Install nowSelect Next
02 Install a Windows Virtual Machine
12

## Page 13

Select Windows 10 ProSelect I don’t have product key
02 Install a Windows Virtual Machine
13

## Page 14

Select Custom installSelect Next
02 Install a Windows Virtual Machine
14

## Page 15

Select Next
02 Install a Windows Virtual Machine
15

## Page 16

Select a country
02 Install a Windows Virtual Machine
16

## Page 17

Select Offline accountSelect Next
02 Install a Windows Virtual Machine
17

## Page 18

Enter an account nameSelect Limited experience
02 Install a Windows Virtual Machine
18

## Page 19

Uncheck and AcceptSelect Not now
02 Install a Windows Virtual Machine
19

## Page 20

Complete the installation
02 Install a Windows Virtual Machine
20

## Page 21

Sysinternals Suite
• Suite is a collection of system utilities and tools developed by Sysinternals, Microsoft's technical advisory consulting company
• It is primarily used for various system administration and diagnostic tasks on Windows operating systems
• The Sysinternals Suite is a valuable resource for developers and system administrators, providing powerful debugging, process monitoring,
system information gathering, and more
Programs that show autorun lists
Autorunsc
Task Manager, which provides detailed information about
processes running in the Microsoft Windows operating system
Procexp
A tool used to monitor and log the activity of processes
running on Windows operating systems in real time
Procmon
Tools to run commands on remote systems
Send commands to a remote system and receive results via a command
prompt or script
Psexec
Tool to display a list of currently running processes on a Windows operating system
Primarily used in the CLI
Pslist
System monitoring tools running on Windows operating systems
Tools that help you record various activities happening within your system
and use them for security analysis and anomaly detection
Sysmon
Download PATH
https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite
02 Install a Windows Virtual Machine
21

## Page 22

Once you have downloaded the Sysinternals suite, register it in your system environment variables so that it is available
anywhere on your local system
This is what you do when you type calc.exe or notepad.exe on the command line, like a calculator or notepad, so that
the commands can run
Setting environment variables
• Type edit the system environment variables in the Window search
box to run it
• Select environment Variables
02 Install a Windows Virtual Machine
Setting environment variables
22

## Page 23

Selecting a Path for System Variables
Register the PATH value for SysinternalsSuite
Flow
02 Install a Windows Virtual Machine
Setting environment variables
23

## Page 24

Check environment variable settings
• Once you've done that, you'll be able to bring up
the tool even if you don't have it in your location
• In addition to this, you can move all the tools you
need to that folder and use them anywhere
Check
Caveats
However, malware can exploit this feature, and if malware is installed in System32, it can execute malware anywhere
02 Install a Windows Virtual Machine
24

## Page 25

FTK Imager
• FTK Imager is part of the Forensic Toolkit (FTK), one of the free tools used in the field of digital forensics
• Primarily used for disk imaging and data collection, it offers a wide range of features for collecting and preserving digital evidence
• Used for analysis in incident response as it allows the contents of a disk to be duplicated and later analyzed
Download flow
Click on the phrase Download FTK Imager Now!
Enter your information in the red boxed area on the screen
and receive a download link to the email you entered
Download PATH
https://go.exterro.com/l/43312/2023-05-03/fc4b78
02 Install a Windows Virtual Machine
25

## Page 26

Follow the link in the email to download and once the download is complete, you can run FTK Imager
Keyword
How to use
When you click on the File-Add evidence item, you'll get a message in the top right corner, and you can choose your options from that message
Physical Drive selects a storage device currently attached to your computer, such as a hard disk, SSD, or USB
The target of the image can be a drive, current memory, or a specific file
You can select a View Mode, Text will show the selected target as text, and Hex will show the selected target as a hex value
02 Install a Windows Virtual Machine
26

## Page 27

Registry Explorer
Registry Explorer is a GUI tool designed to analyze the registry more easily
• An important database that stores system configuration information in the Microsoft Windows operating system
• The registry is an important part of the operating system in many ways, as it contains vital information about the behavior
and configuration of the Windows system
What is the registry?
• Information about various areas, including network settings, user account information, hardware configuration, software installation information, service
and driver settings, and more
• When the system boots, this information is loaded as needed so that the system can operate correctly
• Many software and applications use the registry to store their own settings and environmental configuration information
• User account and permission management, Group Policy, security options, and more are managed through the registry
Retained information
• Boot-related settings in the registry can be manipulated incorrectly, causing the system to fail to boot or boot unreliably
• Because it contains important information related to system security, malicious manipulation can weaken security settings, potentially
leaving the system vulnerable to hacking or malicious software
• There is a so-called "startup program" that runs during the boot process, and an attacker can register malware in the startup program
and execute the malware every time the system, or computer, is turned on
Caveats
Download PATH
https://f001.backblazeb2.com/file/EricZimmermanTools/net6/RegistryExplorer.zip
02 Install a Windows Virtual Machine
27

## Page 28

Dcode
Dcode is a tool to interpret and decode time information in hexadecimal form found in Windows artifacts or log files
In Windows, date and time information is usually represented in hexadecimal, which is the internal representation used by the computer system
Time information typically found in log files or registry entries is expressed in hexadecimal, such as Coordinated Universal Time (UTC) or Epoch Time
Dcode interprets this hexadecimal time information and converts it to a common date and time format
The top red box is the input valueYou can set hexadecimal in
little endian or big endian, decimal is also possible
The second box means Timezone
The third box means Data output type
About Tool
https://www.digital-detective.net/download/download.php?downcode=ae2znu5994j1lforlh03
Download PATH
02 Install a Windows Virtual Machine
28
