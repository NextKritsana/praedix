---
title: "32강_Active Directory Configure_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\32강_Active Directory Configure_v1.2.pdf"
source_size_bytes: 3090662
source_modified: 2025-11-12T13:27:08
imported_at: 2026-06-14T14:26:52
tags:
  - acs
  - acs-advanced
  - imported
---

# 32강_Active Directory Configure_v1.2

- Source: [32강_Active Directory Configure_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/32%EA%B0%95_Active%20Directory%20Configure_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Configuring Active
Directory
• Windows Server 2019 Down
• Virtual Network Settings
• Installing Windows Server 2019
• Install AD Server
• Install Sub AD Server
32
1

## Page 2

Windows Server 2019 Down01
Computer Name : ACS_AD_SERVER
Domain
Windows Server 2019
OS
Computer Name : ACS_AD_SERVER_S
Sub Domain
Windows Server 2019
OS
2

## Page 3

https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019
Install Windows Server 2019
Installing Windows Server to Build an AD Server
Select Download the ISO to download the image file
1
Download a trial
Enter your information to download the trial
Available for 180 days
Windows Server 2019 Down01
3

## Page 4

ISO Downloads
On the screen above, select ISO downloads and click
Download
About
File Name
177763.3650.221105-
1748.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_e
n-us.iso
Size
Approx. 5.2 GB
Windows Server 2019 Down01
4

## Page 5

Virtual Network Settings02
Virtual Network Editor
Run the Virtual Network Editor
> Select Change Settings
Setting
Select VMnet8
Subnet IP : 10.10.10.0
Subnet mask : 255.255.255.255.0
Select DHCP Settings...
• Starting IP address : 10.10.10.5
• Ending IP address : 10.10.10.254
5

## Page 6

Installing Windows Server 201903
Step 1 Step 2 Step 3
Select I will Install the operating system later
When running from the installer disk image,
 fails to run due to issues with the license key
Select Microsoft Windows
Version : Windows Server 2019
Virtual machine name : ACS_AD_SERVER
6

## Page 7

Step 4 Step 5 Step 6
Disk Size : 60GB Enter Edit virtual machine settings and click
Select Use ISO image file for New CD
Select the downloaded Windows Server 2019
Select Processors
Number of Processors : 1
Number of cores per processor : 4
03 Installing Windows Server 2019
7

## Page 8

Results screen Run
03 Installing Windows Server 2019
8

## Page 9

Run Select a language
Select the language you want to use
Lectures are taught in English
03 Installing Windows Server 2019
9

## Page 10

Install Select a language
Windows Server 2019 Standard Evaluation
 Select Desktop Experience
03 Installing Windows Server 2019
10

## Page 11

01
02
Windows Server Datacenter
Ideal for large and highly virtualised data centres
Provides unlimited virtualisation rights, ideal for running multiple
VMs on one server
Advanced features like Software Defined Networking (SDN) and
Storage Spaces Direct are available
Windows Server Standard
Ideal for small or medium-sized businesses
Provides the basic functionality needed to run a server in a
physical or virtualised environment
Includes a physical server with support for up to two virtual
machines (VMs) or hyper-threads
03 Installing Windows Server 2019
11

## Page 12

After agreeing, click Next Install type
Select Custom : Install windows only (advanced)
03 Installing Windows Server 2019
12

## Page 13

Select Drive Wait
Select Drive 0 Unallocated Space
03 Installing Windows Server 2019
13

## Page 14

Installing Enter the administrator password
Entering a relatively complex password, such as Activeir123!
The Windows Server Administrator password is an authentication
mechanism used to control access to administrator accounts on
Windows Server, which have the highest level of privileges on the
system
03 Installing Windows Server 2019
14

## Page 15

Login screen Initial screen
Enter password when pressing Ctrl + Alt + Delete
This means that SAS is applied
Run Server Manager
03
15

## Page 16

Dashboards
View key alerts and events in your system, performance metrics, and more
Quickly understand the overall health of your system and react immediately
if something goes wrong
Manage roles and capabilities
Provides all the tools you need to manage the roles and features of your server
Add or remove server roles, such as Active Directory, DNS server, DHCP server, etc.
Manage server groups
Especially useful in large networks
By grouping multiple servers together, system administrators can monitor multiple
servers at once and make bulk changes to settings
Windows
Server
2019
03 Installing Windows Server 2019
16

## Page 17

Bottom right IP
Verify your license Check the values you set in Virtual network
03 Installing Windows Server 2019
17

## Page 18

My PC -> Properties Change settings
03 Installing Windows Server 2019
18

## Page 19

Rename your PC Restart
Change... -> Set Computer Name Restart to reflect settings
03 Installing Windows Server 2019
19

## Page 20

Check the change history using %computername%, whoami
Confirm setting changes
03 Installing Windows Server 2019
20

## Page 21

Setting > Change adapter options
>Ethernet0 > Properties > internet Protocol 4
IP address : 10.10.10.11
Subnet mask : 255.255.255.255.0
Default gateway : 10.10.10.1
Preferred DNS server : 10.10.10.1
Static IP assignment
03 Installing Windows Server 2019
21

## Page 22

When running the Ipconfig command, see that the value of
ipv4 is changed to 10.10.10.11
Confirm setting changes
03 Installing Windows Server 2019
22

## Page 23

Install AD Server04
Server Manager Initial screen
Run Server Manager for AD Installation Select Manage > Add Roles and Features
Used to extend the server's capabilities and define the
server's role
23

## Page 24

Install AD Server04
Server Roles Add Features
Installing Active Directory Domain Services
Install DNS Server
Installing add-ons
24

## Page 25

Install AD Server04
Selection screen Install
Check Active Directory Domain service, DNS Server Select Install
25

## Page 26

Install AD Server04
Domain Control Domain Name
When the installation is complete, click the text promote this server to a domain
controller
A domain controller runs Active Directory Domain Services (AD DS)
An important role in managing user accounts, computers, groups, and other
resources within a network
Set to acsad.com
26

## Page 27

Install AD Server04
DSRM PW NetBios setting
DSRM is a mode of repairing Active Directory Domain Services (AD DS) or Active
Directory Lightweight Directory Services (AD LDS) in the Windows Server
operating system
It can be selected at system boot time, allowing system administrators to
troubleshoot database problems in Active Directory, repair misconfigurations,
correct system errors, and more
Net Bios: Abbreviation for Network Basic Input/Output
System
NetBIOS domain names are used as part of Active
Directory domains, especially for compatibility with legacy
systems
27

## Page 28

Install AD Server04
Login screen Install
Once set up, click Next
28

## Page 29

Install AD Server04
Reboot Wait
As fast as 3 minutes, as long as 20+ minutes
29

## Page 30

Install AD Server04
Reboot Wait
Active Directory Users and computers can be found at acsad.com
DNS can resolve acsad.com under Forward Lockup Zones
In Server Manager, select Active Directory Users and computers and DNS
under Tools to check if Active Directory is enabled
30

## Page 31

Sub_AD IP NetBios setting
IP address : 10.10.10.12
Subnet mask : 255.255.255.255.0
Default gateway : 10.10.10.1
Preferred DNS Server : 10.10.10.11
Net Bios: Abbreviation for Network Basic Input/Output
System
NetBIOS domain names are used as part of Active
Directory domains, especially for compatibility with legacy
systems
Install Sub AD Server05
31

## Page 32

Install Sub AD Server05
Credentials
The Credentials window pops up when you set up your domain
Enter the administrator account information for your ad-server
Join
Join the Acsad.com domain
32

## Page 33

Verify AD Verify DNS
Tools > Active Directory Users and Computers
ACS_AD_SUB_S registered on computers under acsad.com
Tools > DNS
ACS_AD_SUB_S registered at acsad.com under
Forward Lookup Zones under ACS_AD_SERVER
Install Sub AD Server05
33
