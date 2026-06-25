---
title: "41강_Solving the labs you created2_v.1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\41강_Solving the labs you created2_v.1.2.pdf"
source_size_bytes: 2772991
source_modified: 2025-11-12T13:40:15
imported_at: 2026-06-14T14:27:01
tags:
  - acs
  - acs-advanced
  - imported
---

# 41강_Solving the labs you created2_v.1.2

- Source: [41강_Solving the labs you created2_v.1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/41%EA%B0%95_Solving%20the%20labs%20you%20created2_v.1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Solved exercises you
created (2)
• Deleting an account
• View, delete files
• Check and delete ports
• Repair and reboot the firewall
• Sysmon
41
1

## Page 2

Deleting an account01
Incident response process
• The incident response process can be broken down into a few
key steps
• Identifying attack vectors and recovering compromised systems
is the second half of the process, which we'll cover in this hour
Progress flow
• Delete any accounts, services, etc. that were created
based on the evidence you've gathered so far
• Last time, we saw that Psexec and openssh server
were running, so we removed those services and
programs
• You may be able to prevent further damage by
taking these actions
2

## Page 3

• Discover the added account, control
• The first thing I noticed
Account
• Check event logs for attacker access to the control
account using SSH
Related information
Deleting an account01
3

## Page 4

Verify that the Control account is in the admin
group
Confirm the added account
Deleting an account01
4

## Page 5

You can delete an account by using the Remove-LocalUser cmdlet.
Delete the control account, optionally giving it a name, control, which is the name of
the account to delete
Powershell
To delete the account named ‘control’ using the cmd command prompt on Windows,
you can use the net user command to do so
Command : net user control /delete
cmd
Deleting an account01
5

## Page 6

1
2
Unable to log in
• Username and password are no longer valid, as
the account is completely removed from the
system
• Attackers can no longer access the control
account using SSH
Delete
• Deletes the user profile folder, i.e. the account
under C:\Users, and all the personal data,
documents, photos, music, and other files in it
• Depending on your settings, but usually applied by
default unless explicitly specified when running
the command
Deleting an account01
6

## Page 7

Net user control /delete
Using Cmd
You'll notice that control has disappeared from the list of
accounts you currently have
Verify your account
Deleting an account01
7

## Page 8

View, delete files02
Check the program
From 13:52 to 53 minutes on 1 March 2024, there were actions such as adding accounts and adding firewall rules, so
check the files created during that time
$StartTime = Get-Date "2024-03-01 13:50:00"
$EndTime = Get-Date "2024-03-01 13:55:00"
$Path = "C:\"
$changedFiles = Get-ChildItem -Path $Path -Recurse -ErrorAction SilentlyContinue |
Where-Object { $_.CreationTime -gt $StartTime -and $_.CreationTime -lt $EndTime } |
Select-Object -property Mode, Name, CreationTime
Output files under drive C with creation dates within the timeframe of the cyber security incident
Track creation dates
8

## Page 9

• Confirmation that the Psexec programme was created on 1 March
2024 at 1:53:17pm
• Since psexec allows for remote control and was installed at the time of
the attack, we assume that the attacker used this programme and
installed it
Discover PsExec
• Delete PsExec in Windows\System32 using the Rm command
Delete
View, delete files02
9

## Page 10

• For an attacker to use Psexec successfully, UAC, a security technology in Windows that alerts users when a programme attempts
to make system changes, must be turned off
• This can be checked using get-registrykeyinfo, a function that checks key registry keys, including UAC, in the imported module
irmod
UAC
• Verify that EnableLUA in HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System has a value of 0
Run Result
View, delete files02
10

## Page 11

Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name EnableLUA -Value 1
Command
Result
After executing the command, run the get-registrykeyinfo function and you can see that the EnableLUA value is changed to 1
View, delete files02
11

## Page 12

Some of the output from the Get-RegistryKeyInfo function
Winlogon
In the last lesson, we saw that UserInit has the PATH of the
control panel registered, but you can use the Get-
RegistryKeyInfo function to check it more easily
Userinit
View, delete files02
12

## Page 13

Before After
View, delete files02
13

## Page 14

Check and delete ports03
• 20, 21
• 22
• 23
• 53
• 80
• 443
• 445
• 3389
• 8080
Port
FTP
SSH
Telnet
DNS
HTTP
HTTPS
SMB
RDP
Alternative
HTTP
Closed
Open
Closed
Closed
Closed
Closed
Open
Closed
Closed
14

## Page 15

• Verify that a process called Sshd is using port 22
on
• The sshd service provides a secure
securely over a network to remotely
or execute commands on another computer in a
secure manner over a network
• Shut down the port at your own risk
Port
Check and delete ports03
15

## Page 16

Stop the service
Use the simple script we created in the last lesson to stop the service using port 22
We can see that process #2676 is stopped
Check and delete ports03
16

## Page 17

Can Stop : True
Status : Running
Before
Can Stop : False
Status : Stopped
After
Meaning
If the sshd service is down, remote access via SSH is not possible
Remote admins can't access the system or run remote commands
Check and delete ports03
17

## Page 18

Verify Version
Deleting an OpenSSH server
Delete the openssh server installed by the attacker
Delete
Check and delete ports03
18

## Page 19

04
Run Control Panel
> Select System and Security
> Select Windows Defender Firewall
> Select Advanced Settings
Execution order
Repair and reboot the firewall
19

## Page 20

Delete a rule (GUI)
• Set the firewall rule you want to delete and
right-click
• If you select Delete, the rule is deleted
Disable Rule?
• Network traffic rules defined by this rule are disabled
• As a result, the rule becomes inoperable
04 Repair and reboot the firewall
20

## Page 21

Before
Use the imported module, irmod
Use the get-myfirewallrules function
Verify firewall rules
Delete the firewall rule named "OpenSSH Server (sshd)2"
Remove-NetFirewallRule -DisplayName "OpenSSH SSH Server (sshd)2"
Delete a firewall rule
04 Repair and reboot the firewall
21

## Page 22

After
Use CMD
You can delete the TCP-445 firewall rule using the command Netsh adfirewall firewall delete rule name="TCP-445"
04 Repair and reboot the firewall
22

## Page 23

1
2
Flexibility
While GUIs give users a visual representation of
what's going on, there may be situations where
you need to use PowerShell or CMD for remote
server administration or environments where
only the CLI is accessible
Large networks
In large network environments, manually
managing firewall rules for hundreds or
thousands of devices is inefficient
powershell CMD GUI
04 Repair and reboot the firewall
23

## Page 24

• Windows Firewall profiles are groups of settings in Windows Firewall that provide different levels of security for
different types of networks
• Each profile sets firewall rules based on the security needs of a specific network environment
• You can check the firewall status using a script that passes the Get-NetFirewallProfile command into a pipe and outputs
only the profile and its Enable status via Select-Object
• When you run the script, you can see that Domain, Private, and Public are all set to False
Firewall profile?
04
24

## Page 25

1
2
What is a domain profile?
Applies when the computer is connected to a
corporate or organisational domain network
Meaning of deactivation
A disabled firewall in a domain profile means that
computers are unprotected from threats that may
come from the organisation's internal network
Domain
Profile
Activate command
Set-NetFirewallProfile -Profile Domain -Enabled
True
04 Repair and reboot the firewall
25

## Page 26

Private
Profile
1
2
What is a private profile?
• One of the network profiles used by Windows
Firewall and other security software
• Designed for private network environments that
users trust
Meaning of deactivation
• Even within a trusted private network, systems
can be vulnerable to unauthorised access or
attack
• Risk may increase if other insecure devices are
connected to the same network
Activate command
Set-NetFirewallProfile -Profile Private -Enabled
True
04 Repair and reboot the firewall
26

## Page 27

Public
Profile
1
2
What is a public profile?
Used when connecting to networks with low
confidence in security, such as Wi-Fi in public places
like cafes
Meaning of deactivation
No protection at all from unauthorised access in public
places, network sniffing, hacking attempts, etc.Activate command
Set-NetFirewallProfile -Profile Public -Enabled
True
04 Repair and reboot the firewall
27

## Page 28

Reboot
On the first screen, notice that the control account in the bottom left corner is gone
Attackers can no longer access the control account
04 Repair and reboot the firewall
28

## Page 29

Error The User name or password is incorrect because the Control account does not exist
It means that it's impossible to access the account
Incorrect
04 Repair and reboot the firewall
29

## Page 30

Couldn't access 10.10.10.18 because UAC is enabled and the firewall is turned on normally
Access Denied
Repair and reboot the firewall04
30

## Page 31

Sysmon05
https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
sysmon
• A tool that provides detailed system activity logging and monitoring on Windows systems
• Collect a variety of information
Why?
• When you create a very simple cyber security incident and try to analyse it, you find that it takes more time than you
thought
• Larger organisations or well-structured organisations have separate monitoring personnel and various logging
systems, which makes it easier to collect traces and make judgements, but it is not practical
• You can collect more diverse logs using Sysmon tool
Download link
31

## Page 32

Sysmon.exe
Run Sysmon.exe -i from the installed path using cmd.exe
The -i option: install options
Sysmon05
32

## Page 33

PATH
Applications and Service Log > Microsoft > Windows > Sysmon > Operational
Sysmon05
33

## Page 34

USB Recognition
Run a batch script
UAC Off
Firewall Off
Set up firewall rules
Create a user
Scenario progression
Sysmon05
34

## Page 35

Take additional actions
Verify your account using the Whoami command
Install Openssh server using PsExec.exe and copy files using SCP
Sysmon05
35

## Page 36

Logs that show whoami.exe was run from the Control
account
Whoami
Verify that scp.exe was run from the Control
account
scp.exe
Sysmon05
36
