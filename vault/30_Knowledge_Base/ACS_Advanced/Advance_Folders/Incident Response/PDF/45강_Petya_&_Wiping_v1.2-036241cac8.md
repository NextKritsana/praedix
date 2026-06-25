---
title: "45강_Petya_&_Wiping_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\45강_Petya_&_Wiping_v1.2.pdf"
source_size_bytes: 1646533
source_modified: 2025-11-12T13:45:18
imported_at: 2026-06-14T14:27:09
tags:
  - acs
  - acs-advanced
  - imported
---

# 45강_Petya_&_Wiping_v1.2

- Source: [45강_Petya_&_Wiping_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/45%EA%B0%95_Petya_%26_Wiping_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Wiping & Petya Execute
• What is Petya Ransomware?
• Wiping Function
• Run Petya Ransomware
45
1

## Page 2

What is Petya Ransomware?01
• Encryption-based malware that first gained global attention
after its discovery in 2016
• Infects the system's master boot record (MBR), causing the
system to execute the malware's payload during the boot
process
• The payload encrypts the system's hard drive file system tables,
preventing the operating system from functioning normally
What is Petya
• Petya asks users to pay a ransom in Bitcoin to regain access to
their systems
Bitcoin
Petya
2

## Page 3

• One of the variants, Not Petya, has a wiping function that destroys data.
• Malware with this capability is typically designed to make data unrecoverable,
differentiating it from ransomware, which simply encrypts information and demands a
ransom
Unrecoverable
• While most ransomware focuses on encrypting files, Petya uses a unique method of
infecting a system's master boot record (MBR)
• This ensures that the malware's payload is the first thing to execute when the
computer boots up, effectively disabling the entire system and preventing users from
accessing the operating system
MBR infection
What is Petya Ransomware?01
3

## Page 4

Wiping features02
Data Wiping
What is wiping
The process of permanently deleting data from a data storage device
The primary goal is to completely erase information within the target's computer or network so
that it cannot be recovered
Target
Use in cyberwarfare, cyberterrorism, or competition between companies
Used when an attacker wants to delete specific data or render the entire system unusable
4

## Page 5

Data destruction
• Wiping overwrites or deletes files on the system, making the data unrecoverable
• Rather than simply deleting files, the process involves overwriting the disk space where the files are stored with random data or
data in a specific pattern
• Some wipers have the ability to destroy the boot sector or system files to prevent the system from booting
Severe impact
• Attacks using wipers go beyond simple data loss to severely impact an organization's operations
• Data loss that is difficult or impossible to recover can result in monetary loss, reputational damage, operational disruption, and
more
Wiping features02
5

## Page 6

Reduce the risk of
information
breaches
By wiping used computers or storage devices before they are disposed of or resold, you can effectively prevent previously
stored data from leaving the organization
An important measure to protect against a variety of security threats, including social engineering attacks
Compliance
HIPPA is a privacy law that protects individuals' health information in the United States
HIPAA requires that electronic devices containing health-related information be completely destroyed before they can be discarded
or reused
Wiping can be used for this
Many countries have specific data erasure regulations to protect personal information during the disposal of electronic devices
Wiping features02
6

## Page 7

BCWipe
BCWipe is data erasure software developed by Jetico and is used in the field of information security
Designed to allow users to permanently delete data stored on disk drives
Primarily used in enterprise environments when you need to securely erase sensitive data
• Delete Files and Folders :
Permanently delete selected files or folders, including Windows swap files or
temporary files
• Completely deleting disk space :
Completely deletes unused disk space, making past deleted files unrecoverable
Key features
https://bcwipe.softonic.kr/support
Download
Wiping features02
7

## Page 8

Peter Gutmann
Consists of 35 total passes
• The first four passes overwrite data with a specific byte pattern
• The next 4 passes overwrite with the opposite byte pattern
• Overwrite with randomized data for 27 passes
• Finally, overwrite with the initial pattern for another 4 passes
What to do
Algorithm proposed by
computer scientist
 Peter Gutmann in 1996
When
The goal is to make data stored on a
hard drive or other storage media
unrecoverable
Goals
Peter
Gutmann
It aims to make data recovery extremely difficult when
applied to different types of storage media, but modern
storage technologies can be overkill
This method is consistently referenced to ensure depth
and reliability of data erasure
Wiping features02
8

## Page 9

• Target : ddd.bmp
• When a file is normally deleted from a filesystem, it only disassociates it from
the space it resides in, but does not initialize the space itself
• When deleting files using wiping, the space is overwritten with other data
• Data is overwritten with zeros because the wiping will be done using the Peter
Gutmann method
Wiping features02
9

## Page 10

Wiping features02
10

## Page 11

Right-click the Target file
> Select Delete with wiping
Wiping
Click More
Wiping features02
11

## Page 12

• Scheme: Wiping method
• One random pass: A wiping method that overwrites a file with random
data only once
• Passes: Number of times data is overwritten, unchangeable in free
environments
Wiping targets
• MFT Records
• Directory Slacks
• NTFS Transactions Log File
View this file before deletion
• View files before wiping them
• Helps prevent accidental deletion of important files
More
Wiping features02
12

## Page 13

Before After
Wiping features02
13

## Page 14

Run Petya Ransomware03
Sharing malware
Malware sharing sites are platforms used by cybersecurity researchers, analysts, and educators to share and analyze
malware samples, contributing to the advancement of security research and threat intelligence
• Service that scans files and URLs to determine if they're
malicious
• Allows you to upload suspicious files or URLs to be
scanned by multiple antivirus engines
• A subscription service called VT Enterprise allows you to
download malware from a database
• However, it has a significant price tag, so we won't be
downloading from that site in this lesson
Virus Total
• MalShare is a free, public repository for cybersecurity researchers
and IT professionals to share and study malware samples
• Thousands of new malware samples are collected daily, allowing
users to stay informed about the latest threats and improve their
analysis and detection methods
• Provides an API that allows researchers to search and download
samples through programming
Malshare
14

## Page 15

1
2
Analytics environment
• Downloaded files can contain actual malicious
code, and should only be opened in a secure
environment
• In a virtual machine or isolated test environment
Law, ethics
• Use of malicious code to engage in illegal
activities or damage other systems is strictly
prohibited
• You must comply with privacy laws because
some of the data or samples provided on
MalShare may contain personal information
Malware
Caveats
Run Petya Ransomware03
15

## Page 16

02
01
03
04
Downlaod
Download Petya from Malshare site
Configure your environment
Windows 7 settings
Simple Analysis
Simple analysis with Virus Total
Run
Run Petya Ransomware
Run Petya Ransomware03
16

## Page 17

https://malshare.com/
Recovery is possible if a few conditions are met
Why?
Search for that hash value on the Malshare site
How to download
26b4699a7b9eeb16e76305d843d4ab05
 e94d43f3201436927e13b3ebafa90739
SHA256
Run Petya Ransomware03
17

## Page 18

• Require user authentication when searching • Press the Download button to download
Captcha Check Check the results
https://malshare.com/
Run Petya Ransomware03
18

## Page 19

• Switch to Client and log in to debug kim • Confirms that the last login time was Sunday, February 25,
2024 at 09:12:23
Client Check the results
Run Petya Ransomware03
19

## Page 20

• Verify that the Downloads folder is added to Windows Defender's
exception list
• Files in that folder are not subject to real-time scanning by Windows
Defender
• This procedure is primarily required on Windows 10 and later
operating systems
• Because older versions of operating systems, such as Windows 7,
may not have Windows Defender built in, or may have different
default security levels
• However, an additional installation may be required due to Internet
Explorer's end-of-life
Confirm adding exceptions Tips
Run Petya Ransomware03
20

## Page 21

https://www.virustotal.com/gui/
Upload the downloaded Petya to Virus Total
Virus Total Analysis
When scanned by 72 engines, this means that 66
engines determined it to be malware
66/72
AhnLab-V3 and AlYac confirm that they know it's
Petya
Detection
Run Petya Ransomware03
21

## Page 22

https://www.virustotal.com/gui/
View information such as hash value, file type,
magic number, etc.
Details
md5, sha-1, sha-256 ...
Hash
File Type and Magic Number identify it as a
Windows executable
Check the executable
Run Petya Ransomware03
22

## Page 23

https://www.virustotal.com/gui/
• Abbreviations for Import Hash
• Generated based on a list of external calls that a file
makes, that is, libraries and functions that it imports to
use functions of the operating system or other
programs
• Useful for grouping and categorizing malware
samples
• Files with the same imphash value are often likely to
be part of the same malware family or campaign
• Calculated based on data extracted from the Import
Address Table (IAT) of PE files
Imphash
Run Petya Ransomware03
23

## Page 24

• Store virtual disk as a single file for easy analysis later
Installing Windows 7
Etc
Windows 10
Winsdows 7
Windows 8.1Windows XP
Etc Windows 10 Winsdows 7 Windows 8.1 Windows XP
• As it occurred in 2016, it was active on Windows 7, which
had the overwhelming share at the time
Why?
Run Petya Ransomware03
24

## Page 25

•Move the petya malware to a virtual machine in a
Windows 7 environment and execute it
•Run with exe extension
Run
Run Petya Ransomware03
25

## Page 26

• Short for Check Disk; used by the Microsoft Windows operating system to
scan the file system of a hard drive and correct logical file system errors
• If chkdsk finds errors in the file system, it automatically corrects them
• This may include reestablishing the associations of files and directories, or
repairing damaged file system structures
• May run automatically when Windows detects a disk error, when an
unexpected power loss or system crash may have caused corruption to the file
system
• In this case, PETYA Ransomware caused the hard disk to fail and reboot
CHKDSK
Run Petya Ransomware03
26

## Page 27

• No desktop and an infection screen
Client
• Press any key to get the following screen
Ransom note
Run Petya Ransomware03
27
