---
title: "33강_Active Directory Environment Configuration and Policies_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\33강_Active Directory Environment Configuration and Policies_v1.2.pdf"
source_size_bytes: 2565328
source_modified: 2025-11-12T13:27:30
imported_at: 2026-06-14T14:26:53
tags:
  - acs
  - acs-advanced
  - imported
---

# 33강_Active Directory Environment Configuration and Policies_v1.2

- Source: [33강_Active Directory Environment Configuration and Policies_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/33%EA%B0%95_Active%20Directory%20Environment%20Configuration%20and%20Policies_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Active Directory
Environment
Configuration and Policies
• Configure your lab environment
• Configure and join clients
• What is a GPO?
• GPO Labs
33
1

## Page 2

Configure your lab environment01
Domain
Sub
Domain Client1 Client2
A control panel used to manage settings related to
network connections on Windows computers
Easily accessible by typing the corresponding
command in the Run window
Client 1
IP address : 10.10.10.13
Subnet mask : 255.255.255.255.0
Default gateway : 10.10.10.1
Preferred DNS server : 10.10.10.11
Client 2
2

## Page 3

Configure and join clients02
Create a virtual machine from scratch for a new client PC
Includes operating system installation, network setup, basic
software installation, and more
Create New
Use a previously set up virtual machine as a client PC
Using ACS_WIN10, the virtual machine created in Chap0
Existing virtual machinesClient
3

## Page 4

Configure and join clients02
A control panel used to manage settings related to
network connections on Windows computers
Easily accessible by typing the corresponding
command in the Run window
ncpa.cpl
IP address : 10.10.10.13
Subnet mask : 255.255.255.255.0
Default gateway : 10.10.10.1
Preferred DNS server : 10.10.10.11
Settings
4

## Page 5

Configure and join clients02
An executable file to open the System Properties window in
your operating system
Easily set up a name and domain for your computer
sysdm.cpl
Computer name : ad-client
Domain : acsad.com
Settings
Domain connection complete
5

## Page 6

Configure and join clients02
6

## Page 7

What are GPOs?03
Security
settings
1
Deploying
software
2
Registry
3
• Manage network security settings through GPOs
• Set password policies, user permissions, file system permissions, and
more
• Set password complexity, minimum length, validity period, lockout policy,
and more
• Detect unusual sign-in attempts and lock accounts after a certain number
of attempts
• Assign or restrict specific permissions to specific users or groups to
improve security
• Monitor system events, security logs, login and logoff activity, and more
to record security-related activities that occur within your network
Security settings
7

## Page 8

What is a GPO?03
Security
settings
1
Deploying
software
2
Registry
3
• Automatically install or update software on all networked computers
• Ensure consistent versioning of software
• Immediately deploy critical security patches to enhance the security of your
network Quickly remediate security vulnerabilities and protect your
network from cyber threats
• Out-of-date software or misconfigured GPOs have the potential to
introduce security vulnerabilities
• This means that malicious users can exploit these vulnerabilities to gain
access to your network, which can lead to data breaches or system
compromise
Deploying software
8

## Page 9

What is a GPO?03
Security
settings
1
Deploying
software
2
Registry
3
• Used to centrally control and manage registry settings for the Windows
operating system
• Registry settings related to user interface can be used to adjust the user
experience of the Start menu, desktop, taskbar, etc. or registry settings related
to system security can enhance the security level of the operating system
• Includes disabling unnecessary services, setting security-related warnings and
notifications, etc
• Incorrect registry settings can lead to system errors, performance degradation,
or security vulnerabilities, so it is essential to centrally manage these settings
effectively
• Centralised registry management through GPOs can help maintain consistent
system configuration and minimise the risk of individual setting changes
Registry settings
9

## Page 10

What is a GPO?03
How it works
Using hierarchical structures
Apply and manage policies at different levels of your Windows network, including domains, sites, and
organizational units
GPOs apply to the entire domain
Policies applied at this level affect all users and computers within the domain
Domain
OUs are containers used to organize users, groups, computers, and more within a domain
Applying a GPO at the OU level applies a specific policy only to objects contained in that OU
Granular control over policies for specific departments or teams within your organization
OU
10

## Page 11

What is a GPO?03
The computer has its own Local Group Policy object,
 which is the lowest priority
Local Group Policy
Sites
GPOs applied at the Active Directory site level
For organizations that span multiple sites
Domains
GPOs that apply to a specific domain
Domain-level GPOs have higher priority than site-level
GPOs
OU
GPOs applied at the OU level have the highest priority
If there are nested OUs within an OU, the GPOs in the
lowest-level OU have the highest priority at

Prioritizatio
n
11

## Page 12

What is a GPO?03
Policies in that GPO take precedence over all policies at lower levels
Enforce
• Inheritance from higher levels to lower levels
• Policies set at the domain level are inherited by all OUs within that domain
• If the same setting is configured in more than one GPO,
 the setting in the GPO with the higher priority is applied
Features
• Apply specific policies only to that OU, or override higher-level policies
Blocking inheritance
12

## Page 13

What is a GPO?03
Group Policy Management Console
GPMC enables administrators to manage GPOs at the domain, site,
and OU levels
Configure GPOs to be concatenated, reordered, inherited, enforced,
etc.
Used to configure detailed settings for individual GPOs
Run with Windows' 'gpedit.msc' command, software settings,
 Windows settings, administrative templates, and many more options
Manage advanced features like security settings, scripts, folder
redirection, and more
GPMC
Group Policy Editor
13

## Page 14

GPO Labs04
Refers to the process of creating a new user account by a network
administrator
The process is essential to allow employees or users within an
organisation to access network resources and use the organisation's
computer systems
What is user creation?
Using Active Directory Users and Computers'
Select acsad.com
Under Users, right-click, and select New Users
Create a user
14

## Page 15

GPO Labs04
First Name : debug
Last name : kim
User logon name : debug
User creation settings
15

## Page 16

GPO Labs04
Create a password with a combination of English letters,
numbers, and special characters
Set a password
User must change password at next logon
• Setting to require newly created users to change their
password at their next logon
User cannot change password
• Users can't change their own passwords
• Used when administrators want to manage the security of
specific accounts or for special types of accounts
Password never expires
• The password for that account is not expiring
• Use when you need to keep a persistent password for a
specific account
Account is disabled
• Disable specific accounts to prevent them from logging in
• Use when suspicious activity is detected or an employee
leaves the organization
Options
16

## Page 17

GPO Labs04
Full name : debug kim
User logon name : debug@acsad.com
Option : user must change the password at next logon
Finalize settings
Verify the created User
17

## Page 18

GPO Labs04
Enter your initial account Change wording Reset your password
18

## Page 19

GPO Labs04
Change Complete Sign in
19

## Page 20

GPO Labs04
• Refers to the creation of a single container within the directory
structure of AD
• Enables logical grouping of a specific range of objects for tasks
such as security, delegated administration, and Group Policy
enforcement
What is OU creation?
Using Active Directory Users and Computers'
On acsad.com, right-click and select New > Organizational Unit
Create an OU
20

## Page 21

GPO Labs04
The appearance of the 'New-Object Organisation Unit' pop-up
window indicates that an administrator is creating a new
organisational unit to better manage resources and users within the
organisation
Organizational Unit
Name : block_control
Since we will be restricting the execution of the Control Panel through
policy assignments in the future, we clarify the function and intent of this
OU by naming it 'block_control’
This provides an intuitive advantage for identifying and managing policies in
the future, and has the benefit of clearly communicating the scope of the
policy to both administrators and users
Setting the Name
21

## Page 22

GPO Labs04
Confirm that the Organization Unit has been created
Confirm OU creation
22

## Page 23

GPO Labs04
• Under Tools, select Group Policy Management • Forest acsad.com > Domains > acsad.com
 > Right-click Group policy Object
23

## Page 24

GPO Labs04
• The moment the 'New GPO' pop-up window appears,
administrators start creating new policies, which are used to
restrict certain user behaviours or configure system settings
• Create Block_con_pan
• The name clearly reflects the purpose of the policy: to block
access to the 'Control Panel'.
• After the 'block_con_pan' policy has been successfully
created within 'Group Policy Objects', the administrator can
right-click and select the 'Edit' option to configure this policy
• The 'Group Policy Management Editor' will open, allowing
the administrator to make detailed policy settings through
this interface
New GPO
Select Edit...
24

## Page 25

GPO Labs04
• In the Group Policy Management Editor, navigate to User Configuration under
Administrative Templates and Policy definitions, which will give you the option
to access and modify various policy settings
• In the Control Panel related settings, you can find a policy called 'Prohibit access
to Control Panel and PC settings'
• When the 'Prohibit access to Control Panel and PC settings'
option is clicked, a pop-up window will appear allowing the
administrator to configure the policy
• When this setting is 'Enabled', users affected by this GPO will be
restricted from accessing the Control Panel and PC settings
25

## Page 26

GPO Labs04
• After completing the setup, you can see that Prohibit access
to control panel and pc settings is changed to enabled
• Right-click the pre-created ou, block_control, and select link
an existing GPO
26

## Page 27

GPO Labs04
• In the Select GPO window that pops up, set the policy to
apply
• Apply the block_con_pan policy we created earlier
• Once that's done, you can restrict the control panel from
running to users inside the block_control ou
• Use the debug account that you previously created in users
• In Debug, right-click and select move
27

## Page 28

GPO Labs04
• Outputs a pop-up window named Move
• Select block_control
• Verify that the User has been moved to the appropriate OU
28

## Page 29

GPO Labs04
• Windows automatically refreshes Group Policy at regular intervals
• When a user logs into the system, Group Policy is applied to the user's
configuration
• Administrators can manually refresh Group Policy at any time using the
'gpupdate' command
• If you log in as guest on the client PC and run the control
panel, a warning window pops up and you can see that it is
not running
Apply settings Check the results
29
