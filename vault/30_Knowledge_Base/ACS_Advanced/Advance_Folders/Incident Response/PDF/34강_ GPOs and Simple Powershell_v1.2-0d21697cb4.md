---
title: "34강_ GPOs and Simple Powershell_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\34강_ GPOs and Simple Powershell_v1.2.pdf"
source_size_bytes: 2406907
source_modified: 2025-11-12T13:29:59
imported_at: 2026-06-14T14:26:54
tags:
  - acs
  - acs-advanced
  - imported
---

# 34강_ GPOs and Simple Powershell_v1.2

- Source: [34강_ GPOs and Simple Powershell_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/34%EA%B0%95_%20GPOs%20and%20Simple%20Powershell_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

GPOs and simple
Powershell
• Previous logon information
• Deploying the registry
• AD and Powershell
34
1

## Page 2

Previous logon information01
Logon
GPO
Logon GPO
Collecting and analyzing previous logon information from Active Directory (AD) is important for network security
and management
Previous logon information provides detailed information about when, where, and how a user account has been
used
Analyze previous logon information to detect unusual logon attempts or suspicious activity
Check for logon attempts from unusual times or locations
Identify anomalous login attempts from specific user accounts or IP addresses to recognize and respond to attacker
patterns
Previous logon information provides critical data for incident investigation and analysis
Enhanced security
Repeated login failures can be a sign of a brute force attack, and can help you detect these attacks early
Identify dormant accounts that haven't been logged on for an extended period of time
These accounts can often be security vulnerabilities and should be reviewed periodically
Identified dormant accounts should be deactivated or deleted as needed to reduce unnecessary security risks
Analyze user behavior
2

## Page 3

Logon Login
Log on
• Logging on is the process of authorizing access to a system or service
• Apply to a variety of systems or services, including computers, networks,
databases, and more
• A logon occurs when a user accesses a system physically or remotely
• The sign-in process involves the user interacting with the application's
user interface
Sign in
• The process of authenticating a user's identity to access a specific account
• The login process involves the user interacting with
 through the application's user interface
• When you log in to a particular website in a web browser, you enter your
credentials on the login page
Previous logon information01
3

## Page 4

• Select Group Policy Management under Tools • Built-in Group Policy objects
• Contains basic security settings, such as password policy, account
lockout policy, etc.
• In the forest acsad.com, right-click Domains > acsad.com > Group
Policy Objects > Default Domain Policy > select Edit
GPO Default Domain Policy
Previous logon information01
4

## Page 5

Provide the ability to automatically log users back into the last user account they
interacted with when the system performs an automatic restart for reasons such as
updates or maintenance
Sign-in last interactive user automatically
after a system -initiated restart
A security feature that displays information about previous logon attempts when a
user logs on
Display information about previous logons
during user logon
Provide the ability to notify users that the logon server was unavailable when they log on.
To provide appropriate feedback to users when network issues or server failures occur
Report when logon server was available
during user logon
Option to disable or enable software-based "security alert sequences
Disable or enable software Secure Attention
Sequence
Previous logon information01
5

## Page 6

• Select Display information about previous logons during user logon
from and select Enabled
• Run gpupdate /force to apply the policy
Enabled Apply policies
Previous logon information01
6

## Page 7

• Switch to Client and log in to debug kim • Confirms that the last login time was Sunday, February 25,
2024 at 09:12:23
Client Check the results
Previous logon information01
7

## Page 8

Deploying the registry02
Deploying the registry
• Registry deployment in Active Directory is the process of applying registry settings in bulk across multiple computers within
a network
• This process is primarily performed through Group Policy, which centrally manages registry changes to help maintain
consistency and efficient management of the IT environment
• Use for software settings, security policies, user
preferences, and more
• Ensure consistency by deploying changes in an automated
way through Group Policy, rather than manually changing
registry settings for each computer
• Enforce security-related configurations by controlling
password policies, user permissions, and more through
registry settings
Benefits
• Registry settings can have a significant impact on your
system, so be sure to verify the accuracy of your settings and
test them thoroughly in a test environment before
deployment
• In case registry changes cause problems, have a plan in place
to back up and, if necessary, restore the registry settings
before the changes are made
Caveats
8

## Page 9

• Create a new policy in Group Policy Objects
• The name is open_calc
• Right-click the generated open_calc and select Edit
Create Edit
Deploying the registry02
9

## Page 10

• In User Configuration, under Preferences, under Windows Settings,
right-click Registry, select New, and click Registry Item
• Click More in Key PATH to open the Registry Item Browser
window
Registry Item Run
Deploying the registry02
10

## Page 11

• Enter open calc as value name and value data as C:\Windows\System32\calc.exe
• The path where the calculator is installed by default in physical Windows
• Hit Apply and you should see the result, as shown on the right
Settings Check the results
Deploying the registry02
11

## Page 12

• Right-click the OU to which you want to apply the policy and select Link
an Existing GPO
• Select the open_calc policy and click OK
Apply settings Select a policy
Deploying the registry02
12

## Page 13

• You can see that the block_con_pan and open_calc policies previously
applied to the block_control OU have been applied to

• Apply the policy using the gpupdate /force command
Verify policy enforcement gpupdate
Deploying the registry02
13

## Page 14

• Log in with the debug kim account • See the calculator run
Apply settings Check the results
Deploying the registry02
14

## Page 15

• Run Regedit to enter HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run to view startup programs
• You can see that a Value named open calc has been created and the Data is C:\Windows\System32\calc.exe, which you entered in the GPO
settings of AD Server
Apply settings
Deploying the registry02
15

## Page 16

AD and Powershell03
AD Powershell
Using PowerShell to control Active Directory (AD) can be very beneficial in many ways
It's a powerful scripting language that increases automation, flexibility, and efficiency, providing many features for AD
management
• The biggest benefit of automation is saving time, effort, and
reducing repetitive and tedious tasks
• When you have a large influx of employees, you can run a
script to quickly create their accounts instead of manually
creating them
Automate and save time
• Transform AD tasks into simple, easy-to-understand
commands
• Security policies that apply to all users in a specific department
can be updated in bulk at

Efficiency and productivity
Significantly reduce human error when performing
tasks manually
Scripts allow you to double-check your code before
execution and make corrections if necessary
Reduce errors and maintain consistency
Custom scripts can be written to meet your organisation's
specific needs
Easily adapt and better manage as your organisation's IT
infrastructure grows and changes
Flexibility and scalability
16

## Page 17

New-ADUser
The New-ADUser command is used to create a new user account in Active Directory (AD) by using PowerShell
Provides a variety of parameters for creating AD user accounts, allowing you to set the user's name, password, organizational unit (OU), and
other properties
Name
GiveName
Surname
SamAccountNAme
UserPrincipalName
AccountPassword
Path
Enabled
Parameter
Name used to identify the user in AD, required parameters
The user's name
The user's last name
Security Account Manager (SAM) account name, used for login
A user's UPN is in the form of an email (for example, user@domain.com) and uniquely identifies the user
Set a password for the user
Path to the OU where you want to create the user
Whether to set the account to active status
AD and Powershell03
17

## Page 18

Description
• A role that creates and activates users with an initial password of ACS_P@ssw0rd123 and a name of the value entered as -UserName in the acsad.com domain -OU path
• ConvertTo-SecureString uses the cmdlet to convert the plain text password ACS_P@ssw0rd123 to a secure string Use to convert a plain text string to a 'SecureString' object
 SecureString objects are designed to handle sensitive information more securely because they store data encrypted in memory
• To use this function, you can provide the desired username and OU name as parameters
AD and Powershell03
18

## Page 19

Run the script Access your account
• Confirm that Ku5ti is created • Check for the phrase This is the first time you've interactively signed
in to this account
• Message that appears on Windows operating systems the first time
a user performs an interactive login with a specific account
AD and Powershell03
19

## Page 20

The account you just created is affected by the
GPOs that apply to block_control because it's part
of the block_control OU
Enforce policies on account access
Once in the registry, you can check the existence of
open calc in the Run entry of HKCU
Run
AD and Powershell03
20

## Page 21

Remove-ADUser
Used to delete a user account from Active Directory (AD),
Identify
Confirm
Option
Identify the user account to delete, using the user's SAM account name, GUID, Distinguished Name, UserPrincipalName, etc.
If-Confirm:$false, the user is prompted to confirm the deletion before the command is executed; if-Confirm:$false, the user account is
deleted immediately without further confirmation.
Tips
This command is useful for cleaning up accounts that are no longer used, such as when a user leaves your organization
AD and Powershell03
21

## Page 22

Description.
• If you declare a function called Remove-funcADUser and enter the user's name via the -Username parameter, it will remove the user without popping up a confirmation window if
the user exists and print User name has been removed successfully, or User name not found if the user does not exist
• Available in the following format: Remove-funcADUser -UserName ku5ti
AD and Powershell03
22

## Page 23

Confirmation that the ku5ti account that existed in the block_control
OU is gone
Check the results
Remove-funcADUser -UserName ku5ti
Command
AD and Powershell03
23

## Page 24

Get-ADUser
Used to retrieve information about a user account
Allows you to view a variety of information about AD user accounts and provides a variety of options for filtering,
selecting properties, sorting, and more
Filter
Identify
Searchbase
Properties
Option
Search only for user accounts that meet certain criteria
Identify the user account to delete, using the user's SAM account name, GUID, Distinguished Name, UserPrincipalName, etc.
Specify a specific path in AD to start the search
Specify additional attributes to be included in search results
AD and Powershell03
24

## Page 25

Create users kusti1, kusti2, and kusti3 using the Create-
NewADUser function
Create a User
• Script to retrieve information about all users in a
specific organisational unit and output the results in
tabular format
• Use this function to quickly identify users within a
specific OU
Create a User
AD and Powershell03
25

## Page 26

Run Result
DistinguishedName
• Identifies exactly where a user account is located within the hierarchy of AD, using LDAP formatting
• CN stands for the user's name or distinguished name of the target object, OU stands for the organisational unit to which the user belongs, and DC
stands for the name of the domain to which the user belongs
• One of the essential attributes in AD management, and plays an essential role in accurately identifying and managing AD objects
Enabled
• Represent the activation status of a user account
• If Enabled is $true, the user account is enabled and available for login; if $false, the account is disabled
AD and Powershell03
26
