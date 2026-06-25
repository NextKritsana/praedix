---
title: "29강_Incident Response_(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\29강_Incident Response_(1)_v1.2.pdf"
source_size_bytes: 1104376
source_modified: 2025-11-12T13:25:12
imported_at: 2026-06-14T14:26:48
tags:
  - acs
  - acs-advanced
  - imported
---

# 29강_Incident Response_(1)_v1.2

- Source: [29강_Incident Response_(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/29%EA%B0%95_Incident%20Response_%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Incident Response (1)
• Responding to a cyber security incident with
Powershell
• Registry
• Account
• File Metadata
• USB History
29
1

## Page 2

Responding to a cyber security incident with Powershell01
How to use Powershell
Usability
Powershell provides powerful scripting and automation capabilities in the
Windows environment, simplifying complex, repetitive tasks and saving
time
Monitorable
With Powershell, you can monitor network traffic in real-time and easily
detect suspicious network connections or unusual traffic patterns
2

## Page 3

1
2
Detect
Correspondence
• Event logs contain records of various activities on the
system, and you can analyse them to identify unusual
system activity or security events
• To view the event log by using the Get-EventLog or
Get-WinEvent cmdlets
• Detect anomalous behaviour, such as sudden spikes
in CPU or memory utilization, or unknown processes
running on the system
• View and manage running processes
• Identify malicious processes and perform tasks to end them
• The Get-Process cmdlet allows you to view running
processes, and the Stop-Process cmdlet allows you to stop
specific processes
• Disconnect an attacker from the network, isolate the
network segment from which the attack is occurring, and
so on
01 Responding to a cyber security incident with Powershell
3

## Page 4

1
2
Reactive
Recover
• Identify vulnerable system settings, unknown user
accounts, abnormal network settings, and more
• With Powershell, you can automate security
hardening tasks
• For example, you can write scripts to periodically
check system settings and fix security violations.
• Perform automated tasks through scripts
• Minimize mistakes that can occur during recovery
operations
• Improve the accuracy of your work
01 Responding to a cyber security incident with Powershell
4

## Page 5

system, security, sam, application
NTUSER.DAT
Key registry keys
Timeline for files, logs
Timeline
About USB
Name, Time
USB History
Signed in account
User account information
Account
Artifact
Powershell
01 Responding to a cyber security incident with Powershell
5

## Page 6

Timeline
Track attacker behaviour and understand attack patterns
by determining when actions such as creation,
modification, and access occur within a system
Use the Get-Item cmdlet in PowerShell to collect
metadata about files, such as when they were created,
modified, accessed, etc.
Use the Get-EventLog or Get-WinEvent cmdlets to collect
Windows event logs
Accessing key registry keys
By changing or adding to registry information, an
attacker can potentially manipulate a system or
perpetuate an attack
Take action to detect and repair registry changes
Using cmdlets such as Get-ItemProperty and Set-
ItemProperty, you can view or change the value of
registry keys
01 Responding to a cyber security incident with Powershell
6

## Page 7

Account information
You can use PowerShell cmdlets such as Get-
LocalUser and Get-ADUser to collect account
information on your system
This includes information such as the account name,
last login date, and account status
Use cmdlets such as Get-LocalGroupMember and
Get-ADGroupMember to collect group membership
information for an account
USB History
USB devices are convenient for transferring or
storing data, but they also pose security threats
Attackers can use USB devices to spread malicious
code or extract sensitive information
Use the Get-EventLog or Get-WinEvent cmdlets in
PowerShell to collect and analyse these event logs
01 Responding to a cyber security incident with Powershell
7

## Page 8

Registry02
$RegistryKeys = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings",
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System",
    "HKLM:\System\CurrentControlSet\Control\SecurityProviders"
)
foreach ($Key in $RegistryKeys) {
    if (Test-Path $Key) { if (Test-Path $Key) {
        if ($Key -eq "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System") {
            $Properties = Get-ItemProperty -Path $Key -Name "EnableLUA"
        } else {
            $Properties = Get-ItemProperty -Path $Key
        }
        Write-Output "Registry Key: $Key"
        Write-Output $Properties
        Write-Output "----------------------------------------"
    } else {
        Write-Output "Registry Key: $Key does not exist."
        Write-Output "----------------------------------------"
    }
}
• Manage user-specific internet connection settings
• Used to specify various advanced settings of the Internet
connection, but malicious programs can exploit this key to
manipulate the system's Internet connection
• Malicious programs can use this key to redirect all of your
system's internet traffic to a malicious proxy server, or change
SSL/TLS settings to eavesdrop on encrypted communications
Internet Setting
• Manage system-wide security policies
• Used to control features such as User Account Control
(UAC), System Restore, Remote Desktop, etc.
• Malicious programs can change the system's security
settings to penetrate deeper into the system or bypass
security softwareEnableLUA value controls UAC settings
System
• Define the security providers used in the system
• Provide security services such as authentication, encryption,
decryption, signing, and message integrity checking
• If a malicious DLL is added as a security provider, it can gain
privileges, such as encrypting or decrypting all network traffic
on the system
Security Provider
8

## Page 9

$RegistryKeys = @(
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings",
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System",
    "HKLM:\System\CurrentControlSet\Control\SecurityProviders"
)
foreach ($Key in $RegistryKeys) {
    if (Test-Path $Key) { if (Test-Path $Key) {
        if ($Key -eq "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System") {
            $Properties = Get-ItemProperty -Path $Key -Name "EnableLUA"
        } else {
            $Properties = Get-ItemProperty -Path $Key
        }
        Write-Output "Registry Key: $Key"
        Write-Output $Properties
        Write-Output "----------------------------------------"
    } else {
        Write-Output "Registry Key: $Key does not exist."
        Write-Output "----------------------------------------"
    }
}
Start a loop for each registry key stored in the variable
foreach
• Using the Test-Path cmdlet to verify that the current registry key
actually exists
• If the registry key does exist, run the following block of code
• Print the path to the current registry key
• Print the value of the registry property stored in the $Properties
variable
Else
• If we determine that the registry key does not exist, we print a
message that the registry key does not exist
1st Conditional statements
• Verify that the current registry key is ~\Policies\System
• Using the Get-ItemProperty cmdlet to Get "EnableLUA"
Else
• If the current registry key is not ~\Policies\System, use the
Get-ItemProperty cmdlet to get all of the properties of the
registry key
2nd Conditional statements
Registry02
9

## Page 10

• Output the path to each registry key and the properties of
that key
• If the key doesn't exist, you'll get a message saying so
• Can help you check system or software settings or
diagnose problems
Run Result
Registry02
10

## Page 11

$LocalUsers = Get-LocalUser
$UserInfo = @()
foreach ($User in $LocalUsers) {
    $UserObject = New-Object PSObject
    $UserObject | Add-Member -MemberType NoteProperty -Name "Name" -Value $User.Name
    $UserObject | Add-Member -MemberType NoteProperty -Name "Enabled" -Value $User.Enabled
    $UserObject | Add-Member -MemberType NoteProperty -Name "LastLogon" -Value $User.LastLogon
    $UserObject | Add-Member -MemberType NoteProperty -Name "Description" -Value $User.Description
    $UserObject | Add-Member -MemberType NoteProperty -Name "PasswordChangeableDate" -Value $User.PasswordChangeableDate
    $UserObject | Add-Member -MemberType NoteProperty -Name "PasswordExpires" -Value $User.PasswordExpires
UserInfo += $UserObject
}
$UserInfo
Simple account information can be extracted
$LocalUsers
Name : Username
Enabled: Enabled status
LastLogon: Last login time
Description: Description of the account
PasswordChangeableDate: Password changeable date
PasswordExpires: Password expiration date
Looping statements
Used to store information for each user account
$UserInfo
Account03
11

## Page 12

• Print information about your account
• Name : ACS
• Enabled : True
• LastLogon : 2/20/2024 10:34:53 PM
• Description : -
• Password Changeable Date : 1/7/2024/10:22:27 PM
• PasswordExpires : -
Run Result
Account03
12

## Page 13

File Metadata04
$Path = "$env:USERPROFILE\Desktop\make_ACS_test"
$startTime = Get-Date "2024-01-01 00:00:00"
$endTime = Get-Date "2024-02-10 00:00:00"
$changedFiles = Get-ChildItem -Path $Path -Recurse | Where-Object { $_.LastWriteTime -gt $startTime -and $_.LastWriteTime -lt $endTime }
$changedFiles
Roles
A script that finds files in a specific folder ($Path) that have changed between a specified time range, say $startTime and
$endTime, and outputs a list of them
env:USERPROFILE: The user's home directory
Point to the folder named Make_ACS_test
$PATH
• With Get-ChildItem, this command recursively lists all files and
folders in the path specified in $Path
• The '-Recurse' option lists all files including subdirectories
• Passing this result to a Where-Object using a pipe
• Filter files with 'LastWriteTime' (last modification time) later than
$startTime and earlier than $endTime
• Select only files that have changed within the specified time range
and store them in $changedFiles
$changedFiles
The script is looking for files that changed from 1 January
2024 to 10 February 2024
$Time
13

## Page 14

•Output files in a specific directory whose
changes occurred within a specific time
Run Result
File Metadata04
14

## Page 15

$startTime = Get-Date -Year 2024 -Month 1 -Day 1 -Hour 0 -Minute 0 -Second 0
$endTime = Get-Date -Year 2024 -Month 2 -Day 22 -Hour 6 -Minute 32 -Second 0
Get-WinEvent -FilterHashTable @{LogName='*'; StartTime=$startTime; EndTime=$endTime} | Where-Object { $_.Message -match 'USB\\VID' }
Roles
Find and print events in the Windows event log within a specific time period that contain the string 'USB\VID' in the
message
Different from the Get-Date collected before this
Setting a specific date and time using the '-Year', '-Month',
'-Day', '-Hour', '-Minute', '-Second' parameters

Time
• Get-WinEvent is a command to get Windows event logs
• '-FilterHashTable' option to filter event logs
• The 'LogName', 'StartTime' and 'EndTime' parameters can be used
to get event logs with specific log names and time ranges
Get-WinEvent
Condition that returns True if a message in the event log contains the string 'USB\VID'
Find and print event logs that contain the string 'USB\VID' in a message within a specified time range
Indicates USB device connection and disconnection events, etc.
WhereObject
USB History05
15

## Page 16

• Event log output with the string USB\VID_ in it
• EventID 576: Device Connection
• EventID 1010: Device disarmed
Run Result
USB History05
16

## Page 17

Features
• If your USB devices include storage devices such as
external hard drives and USB flash drives, the Storport
driver manages those USB storage devices
• Microsoft-Windows-Storport event logs can contain
activity related to USB storage devices
A storage port driver, which is used by high-performance storage systems (e.g., RAID systems)
Helps communicate between storage hardware such as disks and the operating system
Microsoft-Windows-Storport
Name
Microsoft-Windows-Storage-Storport%4Operational.evtx
Event ID to check
576
What you can see
AdapterHardwareId
USB History05
17

## Page 18

Identify USB connection and disconnection times, device
type and manufacturer information, and error conditions
such as driver load failure
Audit trail of USB device usage, detect data breaches,
detecting data breaches, troubleshooting, etc.
Using the 'Get-WinEvent' command, you can view the
Microsoft-Windows-Kernel-PnP logs
Play an important role in logging events related to USB devices, logging information related to plug-and-play (PnP) devices, that is, devices that are automatically recognized
when they are plugged into or removed from the system
. USB devices are one of these plug-and-play devices, so events that occur when a USB device is plugged into or removed from the system are logged in the Microsoft-Windows-
Kernel-PnP log
Microsoft-Windows-Kernel-PnP
Name
Microsoft-Windows-Kernel-PnP%4Device Management.evtx
Event ID to check
1010
What you can see
DeviceInstanceID
USB History05
18
