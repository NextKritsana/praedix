---
title: "16강_Persistence Technique_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\16강_Persistence Technique_v1.2.pdf"
source_size_bytes: 1490305
source_modified: 2025-11-12T12:38:21
imported_at: 2026-06-14T14:26:32
tags:
  - acs
  - acs-advanced
  - imported
---

# 16강_Persistence Technique_v1.2

- Source: [16강_Persistence Technique_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/16%EA%B0%95_Persistence%20Technique_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Persistence Technique
• Persistence Technique
• Boot
• Add an account
16
1

## Page 2

Persistence Technique01
Persistence techniques
• Persistence techniques is a cybersecurity term that refers to a
number of techniques that allow an attacker to continue to access
or control a system once it has been compromised
What are Persistence techniques?
Why is it dangerous?
• If an attacker compromises a system and remains in place, there is an ongoing risk of sensitive data being stolen
• If an attacker remains active within a system, they can install additional malware, spread to other systems, and more,
expanding the scope of the breach and increasing the time and cost to remediate
2

## Page 3

Persistence Technique01
https://attack.mitre.org/
MITRE ATT&CK
Persistence techniques are also identified in MITRE ATT&CK
Different techniques attackers use to maintain
access within your system
Persistence
 Why do you need to know?
Who needs to know
Incident Response Team
Enterprise security officer
Detect attacker behavior
If an attacker manipulates the registry, startup folder, or
scheduler to automatically execute malware, detecting
these changes is the first step in identifying the attack
After an attack occurs
After an attack, the response team analyzes the
persistence techniques used by the attacker to determine
what actions are needed to remove the malware and
recover the system
Build a strategy
Understanding and analyzing persistence techniques
enables you to better detect and respond to attacks, and
build the strategies needed to prevent future attacks
3

## Page 4

Boot02
Typically, startup programs are managed in System Settings
Add or remove startup programs as needed
Manage
Programs that are set to run automatically when the computer boots
Programs that run automatically as soon as a user logs in and include many types of
programs, such as email clients, antivirus programs, system tools, etc.
What are startup programs?
Startup Programs
Caveats
•Too many startup programs can slow down your system's boot time, so make sure only the programs you need runautomatically
•Malware can add itself to startup programs and attempt to run every time the system starts, so you should periodically check to see
if any unknown programs are added to startup programs
4

## Page 5

Boot
Check your startup programs
Go with the lab
Use the virtual machine you created in the previous Chapter 0
If you don't have a virtual machine
Refer to Chapter0 for recommended installation
02
5

## Page 6

Boot
Check your startup programs
Check your startup programs
Open the Windows Settings window: Windows + I
 Select Apps
02
6

## Page 7

Boot
Check your startup programs
Select Start up
 Start up list available
02
7

## Page 8

Boot02
Check the registry
1.HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
2.HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
3.HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
4.HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
PATH
Registered programs run automatically when you sign in or when the system
starts
This allows needed services or applications to start automatically
As with Startup, they can sometimes be abused
Description
Can be enrolled via command and manually enrolled and unenrolled
Tips
8

## Page 9

Boot02
Add a registry
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
Creation location
9

## Page 10

Boot02
Add a registry
Run will create NotePad.exe
RunOnce includes the Calc.exe creation
Set String Value
Run contains %windir%\system32\notepad.exe
RunOnce includes %windir%\system32\calc.exe
Enter a String Value
10

## Page 11

Boot02
Exit
When you're done setting up the registry, shut down your
computer
Boot
Autorun Notepad and Calculator
11

## Page 12

Boot02
Run has the value Notepad that we set up earlier
Run
RunOnce has the value Exist X
RunOnce
12

## Page 13

Boot02
Simply select Delete
Select Yes in the warning window
Delete
13

## Page 14

Boot02
MITRE ATT&CK
Registry Run Keys / Startup Folder
Persistence
14

## Page 15

Boot
Winlogon helper
An attacker can exploit a feature of a Windows component called Winlogon to set it to run a dynamic link library (DLL) or executable file when a user
logs in
Winlogon.exe is one of the core components of the Windows operating system, managing user logins and logouts
It is also responsible for a security feature called SAS, which is activated by the Ctrl-Alt-Delete key combination
•Secure Attention Sequence abbreviations
• Protects users from fake login prompts or other types of phishing attacks when
they try to log into a computer
• SAS is triggered by pressing the key combination Ctrl+Alt+Delete
• When this key combination is pressed, the operating system verifies that the user
is actually typing via keyboard before displaying the login screen
• This is to prevent other programs or malware from intercepting or simulating this
key combination
• Disabled by default, but some organizations use policies to enable it
SAS
* gpedit.msc > Computer Configuration > Administrative Templates >
 Windows Components > Windows Logon Options >
 Disable or enable software Secure Attention Sequence
02
15

## Page 16

Boot
Registry
HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\
HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Winlogon
• Manage additional helper programs and features associated with the
Winlogon process
Roles
• These registry keys can be used for malicious purposes
• By changing these keys, an attacker could cause the Winlogon process to
load and execute a malicious DLL or executable file

• Malware can be executed every time a user logs in or every time the
system starts up
Caveats
02
16

## Page 17

Boot
Sub Key
Winlogon\Notify
References the Notification Package DLLs that handle Winlogon events
DLLs registered with this key are called by Winlogon when events such as login, logout, and shutdown
occur
By exploiting this key, an attacker can execute malware based on system events.
Winlogon\Userinit
By default, this value points to userinit.exe, which runs as part of the user login process, initializing the
user environment, running the login script, etc.
By modifying this key, it can be manipulated to execute malware.
Winlogon\Shell
Refers to the system shell that runs when a user logs on
By default, this value masks explorer.exe, which provides the Start menu, taskbar, desktop environment,
etc.
By exploiting this key, an attacker can set it to run malware at login
02
17

## Page 18

Boot
Registry
Add the Control.exe PATH
Winlogon\Userinit
If you make the wrong change, your computer may
not boot
Be sure to run in a virtual machine
Caveats
Value
C:\Windows\System32\userinit.exe, C:\Windows\system32\control.exe
02
18

## Page 19

Boot
Result
Boot up and see the Control Panel is on
After booting
Malware runs as soon as the computer boots up
Needs attention
What if it's malware?
Why?
The Windows Startup Program and Run Registry are relatively widely known, so most users are prepared, but the registry related to Winlogon
is relatively unknown and should be checked as well
02
19

## Page 20

Boot
https://attack.mitre.org/techniques/T1547/004/
MITRE ATT&CK
https://attack.mitre.org/
MITRE ATT&CK classifies as Winlogon Helper DLL
Winlogon Helper DLL
Mitigations
Identify and block potentially malicious software that may run through the Winlogon
Assistant process by using tools such as AppLocker, which can audit and/or block unknown
DLLs
Limit the permissions of user accounts so that only authorized administrators can make
Winlogon Assistant changes
02
20

## Page 21

Add an account03
• Attackers can use local accounts to maintain access to victim systems
• A local account is an account configured by your organization to manage users, remote support,
services, or a single system or service
• With sufficient access level, an attacker can create a local account using the Windows net user
/add command
• They can also add the account to the Administrators group, in which case the added account will
have administrator permissions available
Add an account
Risks of adding an account
• Adding administrator privileges in Windows allows you to change various settings or perform actions that fundamentally affect the system
• Administrator privileges mean being given full control of a computer system
• Potential for accidental errors or mistakes to cause serious damage to the system
• If an account with administrator privileges is hacked, the hacker can take full control of the system, so only grant administrator privileges
when absolutely necessary
• If an attacker gains administrator privileges, they can take over the computer
21

## Page 22

Add an account03
Enable multifactor authentication for users and
privileged accounts
Multifactor authentication
Limit the number of accounts that can create other
accounts
Limit the use of local admin accounts for day-to-day
tasks that could expose you to potential adversaries
Manage privileged accounts
Mitigation
22

## Page 23

Add an account03
Detection
Commands
Monitor commands for tasks related to creating local
accounts, such as .Net user /add, useradd, and dscl –
create
Processes
Monitor newly executed processes related to account
creation, such as Net.exe.
Monitoring
• Audit accounts to identify newly created user and service
accounts to detect suspicious accounts that may have been
created by attackers
• Detect Event IDs associated with account creation
Account auditing
23
