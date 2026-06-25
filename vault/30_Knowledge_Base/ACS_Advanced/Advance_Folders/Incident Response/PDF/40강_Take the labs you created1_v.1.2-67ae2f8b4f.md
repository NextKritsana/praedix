---
title: "40강_Take the labs you created1_v.1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\40강_Take the labs you created1_v.1.2.pdf"
source_size_bytes: 3187519
source_modified: 2025-11-12T13:39:28
imported_at: 2026-06-14T14:27:00
tags:
  - acs
  - acs-advanced
  - imported
---

# 40강_Take the labs you created1_v.1.2

- Source: [40강_Take the labs you created1_v.1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/40%EA%B0%95_Take%20the%20labs%20you%20created1_v.1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Solve labs you've created
• Caveats
• Preparation tools
• Prepatches and Event Viewer
• Verify the added firewall rule
• Check external storage devices
• Check your startup programs
40
1

## Page 2

1
2
Settings
• We set up the environment last time we
worked together to create the lab, so we
know what behaviours occurred and
how they were approached, but we'll
assume you don't know this
Progress flow
• Take it one step at a time, building on
your initial discoveries
Caveats01
2

## Page 3

Virtual machine (victim
machine)
Localhost (the computer for
analysis)
Caveats
• The time on the local computer and the time on the computer inside the virtual machine might have different time values
• Be careful not to get confused when analyzing to reflect this
• Use the Get-TimeZone cmdlet to determine the time zone
• 17 hours difference in lecture materials (PPT)
Caveats01
3

## Page 4

See that an account named Control has been added
MITRE ATT&CK
https://attack.mitre.org/techniques/T1136/001/
Confirm the added account
Caveats01
4

## Page 5

Detection
Event logs related to account creation are available via Windows event ID 4720
Caveats01
5

## Page 6

Using a pre-created ACS_TEST
Using batch scripts
• Prefetch
• Collecting volatile data
• Collect non-volatile data
Purpose of use
Caveats01
6

## Page 7

Preparation tools02
• Using a pre-created ACS_TEST
• Select option 1 to collect volatile, non-volatile
Full Execution
If ingestion completed successfully, exit
Collection complete
7

## Page 8

Change existing code to output on function
declaration by simply making it a function
Verify key registry keys
Make Port available for input
Check port information
Put a sequence of steps into a function and output
it in the function declaration
Checking changed files
Preparation tools02
8

## Page 9

Get-MyFirewallRules
• All firewall status information
Get-MyFirewallRues2
• Ensure that the Action is Allow and the
local port number is between 100 and
8000
Check your firewall
What's printed
• Name
• Activation status
• Last login time
• Description
• When you can change your password
• Password expiration date
Verify user information
Combine all the functions
mentioned so far and save as
irmod.psm1
Modularization
Preparation tools02
9

## Page 10

• Set execution Policy to bypass to use the module
• Import irmod module
• Type Get-command -module irmod to verify that the
module was successfully imported
Installing modules
Preparation tools02
10

## Page 11

• Print Registered Accounts
net user
• Verify that the Control account was added
• Accounts with administrator privileges have almost full
access to the system, so unauthorised accounts can pose a
serious risk to the security and integrity of the system
Check the admin group
Preparation tools02
11

## Page 12

• Check local user information
• Can verify that ACS, Control, and sshd are enabled
• Last login time available
Get-LocalUserInfo
• What does Secure Shell Daemon stand for?
• Background services that allow you to access
computers or transfer files securely and remotely
sshd
Preparation tools02
12

## Page 13

Prefetch and Event Viewer03
• create control : 06:53:17 (UTC+9)
• Create sshd : 06:59:07 (UTC+9)
Account creation information
• Proceed with analysis based on that time value
Tips
13

## Page 14

netsh.exe
•If netsh was run in the cyber security incident, there was likely a change in firewall settings
•The netsh command can be used to change a system's network settings for a number of malicious purposes.
•Use netsh to add, modify, and delete firewall rules or disable the firewall completely
•May allow malicious traffic to enter or facilitate data exfiltration by attackers
Prefetch and Event Viewer03
14

## Page 15

net.exe
• Perform tasks such as adding, deleting, and modifying user accounts or managing user groups through commands such as net user and net localgroup.
• Surreptitiously added new user accounts to the system, possibly giving the attacker additional system access
shutdown.exe
• Speculating that the attacker restarted the system to allow the specific behavior to take effect
Prefetch and Event Viewer03
15

## Page 16

Filtering
• Filter by timestamp
• #Check event logs with a Timestamp value greater than 2024-03-02T06:53:16.000000 and less than 2024-03-02T06:53:19.000000
Prefetch and Event Viewer03
16

## Page 17

Change firewall rules
• a rule has been added to the windows defender firewall exception list indicates a new rule has been added to the windows defender firewall
settings
• Suspicious times of day, and exception rules added without user consent, could be signs of a cyber security incident
03 Prefetch and Event Viewer
17

## Page 18

Verify the added firewall rule04
Type Windows Defender Firewall in the Windows search bar
Can see that the firewall is turned off
Firewall off
• Firewalls are usually saved in the order they are
added
• Once saved, see that the rule has been added
with TCP-445 and OpenSSH Server (sshd)2
Verify the added rule
18

## Page 19

Set Protocol to TCP and Local Port to 445
TCP-445
• TCP port 445 is used for various server and client communications, such as
network file sharing, printer sharing, and Windows Domain Services, which use
the Server Message Block (SMB) protocol
• This means that you can share files or printers with other computers on the
network
• When you use PsExec in a Windows environment to issue commands to a
remote computer, PsExec communicates with that computer over the SMB
protocol
Meaning
04 Verify the added firewall rule
19

## Page 20

Set protocol to TCP and local port to 22
OpenSSH Server (sshd)2
• TCP port 22 is a network port primarily used for the Secure Shell (SSH) protocol
• SSH is a protocol that allows you to remotely access another computer securely over a
network or transfer files to it

• This allows us to guess that the file was sent using that port
Meaning
Event ID 2097
04 Verify the added firewall rule
20

## Page 21

Caveats
• Attackers can disable or modify system firewalls to bypass controls restricting network usage
• Changes can disable the entire mechanism, as well as add, delete, or modify specific rules
https://attack.mitre.org/techniques/T1562/004/
04 Verify the added firewall rule
21

## Page 22

OpenSSH Server
•An attacker can use an OpenSSH server to gain remote access to a system, which can be used to perform additional malicious
activities
•Enter the command Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.Server*' to find and display OpenSSH
server-related items among the installed capabilities on your system
•If you can see the status Installed in the State field, this means that the OpenSSH server is installed
You can check the status of the "sshd" service with the Get-
Service sshd command
If Status is Running, the service is running
sshd
04 Verify the added firewall rule
22

## Page 23

View logs related to OpenSSH
Verification information
Applications and Services Log
> OpenSSH
> Operational
Event Viewer
04 Verify the added firewall rule
23

## Page 24

Port22 is listening on 3/1/2024 13:59:13
Verification information
04 Verify the added firewall rule
24

## Page 25

3/1/2024 14:02:13
Connect to a computer with an IP of 10.10.10.17
Verification information
3/1/2024 14:05:38
Accepted Password for control from 10.10.10.17
Successful login
Verification information
04 Verify the added firewall rule
25

## Page 26

https://rot13.com/
Verify obfuscated names with ROT13
Name
Verify that the batch file named E:\acs_hk\speed.bat
was executed

decoding
04 Verify the added firewall rule
26

## Page 27

See the time value written as Windows File Time
Time
2024-03-01 21:53:08:674(utc)
When UTC-8 is applied, the time is 13:53:08:674
decoding
04 Verify the added firewall rule
27

## Page 28

execution
The Windows command prompt is used to control almost every aspect of the system, with different privilege levels required for
different subsets of commands
Attackers can also leverage this to execute various commands and payloads
04 Verify the added firewall rule
28

## Page 29

05
Verify your device
The Vendor ID (VID) and Product ID (PID) of a USB device are uniquely assigned identifiers to distinguish the product from
the company that manufactured it
VID is used to identify the USB device manufacturer, and PID is used to identify a specific product or product version
VID: 2174
PID: 2100
About
Check external storage devices
29

## Page 30

Verification information
• Friendly name : transcend
• DeviceDesc : Ts1TESD310C
Tips
• Google to find USB information
Check external storage devices05
30

## Page 31

Check your startup programs06
All is well
HKLM - RUN
All is well
HKLM - RUNONCE
31

## Page 32

All is well
HKCU - RUN
All is well
HKCU - RUNONCE
06 Check your startup programs
32

## Page 33

Userinit shows that control.exe is additionally
registered with

Userinit
MITRE ATT&CK
https://attack.mitre.org/techniques/T1547/004/
To the registry value that points to userinit.exe, the user initialization program that runs when the user logs on, add
control.exe to the registry value pointing to userinit.exe, the program that runs when you log on
Check your startup
programs06 Check your startup programs
33
