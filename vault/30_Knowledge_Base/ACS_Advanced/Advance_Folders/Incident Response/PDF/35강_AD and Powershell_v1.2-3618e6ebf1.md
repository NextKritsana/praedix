---
title: "35강_AD and Powershell_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\35강_AD and Powershell_v1.2.pdf"
source_size_bytes: 1057156
source_modified: 2025-11-12T13:30:05
imported_at: 2026-06-14T14:26:55
tags:
  - acs
  - acs-advanced
  - imported
---

# 35강_AD and Powershell_v1.2

- Source: [35강_AD and Powershell_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/35%EA%B0%95_AD%20and%20Powershell_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

AD and Powershell
• Create an OU
• Applying GPOs
35
1

## Page 2

Create an OU01
New-ADOrganizationalUnit
To create a new Organizational Unit (OU) within Active Directory (AD) using PowerShell,
 is a cmdlet that is used to create a new Organizational Unit (OU) within Active Directory (AD)
Name
Path
Description
ProtectedFromAccidentalDeletion
ManagedBy
PassThru
Parameter
Name the OU you want to create
Specify the path to the parent OU from which the new OU will be created, such as DC=example,DC=com
Add a description of the OU
Setting the parameter to $true enables protection to prevent OUs from being accidentally deleted
Specifies the user or group managing the OU
Parameter causes the cmdlet to output the generated OU object.
2

## Page 3

Accidental Deletion
Accidentally deleting important objects such as user accounts, organizational units (OUs), groups, etc.
To help prevent this, AD provides a feature called "Accidental Deletion Protection"
• Refers to the ability of a user or administrator to remove an
object within AD
• If Accidental Deletion Protection is enabled, this permission is
restricted and the object cannot be deleted in the normal way
• If the Object: Protect object from accidental deletion option is
enabled, this protection must be turned off before the object
can be deleted
Delete permission?
• Prevent accidental loss of sensitive data
• Before deleting an object, make sure that the object is no
longer needed and that you have selected the correct
object
• Perform the standard delete confirmation procedure in AD
before deleting an object, even after turning off protection
Caveats
Turn it off using the ADUser and Computer administrative tool
Open the properties of the object, go to the "Object" tab and uncheck the "Protect object from accidental deletion" checkbox
Using Powershell commands
Change protection settings for large numbers of objects, especially useful in large AD environments
Unprotect
Create an OU01
3

## Page 4

Description
• $path: an optional parameter that specifies the path to create the new OU, the default is "DC=acsad,DC=com", which is the path to the Domain
Components
•  Create a new OU with the specified name ($ouName) and path ($path) by using the New-ADOrganizationalUnit cmdlet
• Automatically protects against AccidentalDeletion without having to set -ProtectedFromAccidentalDeletion
• When the OU creation completes successfully, the PowerShell console displays the following success message
• If an error occurs during execution, the catch block will be executed to output an error message
Create an OU01
4

## Page 5

Create-funcOU -ouName test
command
Create an OU named test
Run Result
Create an OU01
5

## Page 6

• Access additional information and management options not
available in the default view
• This feature enables deeper management and analysis of AD objects,
and is useful for advanced users and administrators
Advanced Features
• Access additional property tabs for AD objects such as users,
computers, and OUs
• Includes security settings for the object, editing properties, the
object's unique identifier (SID), the object's class information,
and more
• Enables the "Security" tab of an AD object, where you can set
detailed access rights to the object and manage permission
inheritance
Benefits
How to set it up
View Options > Enable Advanced Features
Create an OU01
6

## Page 7

test > Properties > Object
Properties
Uncheck Protect object from accidental deletion
Disable
Create an OU01
7

## Page 8

Description.
• $path: an optional parameter that specifies the path to create the new OU, the default is "DC=acsad,DC=com", which is the path to the Domain
Components
•  Create a new OU with the specified name ($ouName) and path ($path) by using the New-ADOrganizationalUnit cmdlet
• Automatically protects against AccidentalDeletion without having to set -ProtectedFromAccidentalDeletion
• When the OU creation completes successfully, the PowerShell console displays the following success message
• If an error occurs during execution, a catch block will be executed to output an error message
Create an OU01
8

## Page 9

Get-ADOrganizationalUnit
The cmdlets used to get information about Organisational Units (OUs) within Active Directory (AD) by
using PowerShell
Get results
Get-ADOrganizationalUnit -Filter 'Name -eq "OU"' -Properties ProtectedFromAccidentalDeletion | Select-Object Name,
ProtectedFromAccidentalDeletion
Create an OU01
9

## Page 10

Explain the logic
• Navigation: Use the Get-ADOrganisationalUnit cmdlet to search all OUs under a given $searchBase, but only one level below the specified $searchLevel
option, which performs the search only for the child OUs immediately below the specified path
• Output: For each OU, output the name of the OU, appropriately appending spaces to match the indentation level
• Recursive call: For each OU, the function calls itself again, setting $searchBase to the DistinguishedName of the current OU and incrementing $level by 1
• This process is repeated until all OU hierarchies in AD have been traversed
Create an OU01
10

## Page 11

Tree-structured presentation for better
visibility
Benefits
Create an OU01
11

## Page 12

Remove-AdOrganizationalUnit
Remove-ADOrganizationalUnit is a cmdlet in the Active Directory module of PowerShell,
used to delete organizational units from Active Directory
-Identity
-Recursive
-Confirm
-WhatIf
Parameters
Specify a unique identifier for the OU to delete
If you specify this parameter, all child OUs and other objects contained in that OU are also deleted.
The user is prompted to reconfirm the deletion
Shows the cmdlet without actually running, and what would happen if it did run
Caveats
The Recursive option can be particularly dangerous, so make sure it's absolutely necessary before using it,
know exactly what you're deleting in the OU you want to delete
Create an OU01
12

## Page 13

Delete
•Even after you turn off protection, AD runs the standard delete confirmation before deleting objects
•If you set the value of Confirm to False, you will not be presented with this window, but it is worth checking anyway because
deleting an OU incorrectly can cause major disruption to system operations
Create an OU01
13

## Page 14

UserOU
acsad.com
AOU KOU
a1 a2 a3 k1 k2 k3
POU
p1
Create an OU01
14

## Page 15

function Create-NewADUser {
    param(
        [Parameter(Mandatory=$true)]
        [string]$UserName,
        [Parameter(Mandatory=$true)]
        [string]$SOU
    )
    $SecurePassword = ConvertTo-SecureString "ACS_P@ssw0rd123" -AsPlainText -Force
    $OUs = $SOU -split ',' | ForEach-Object { "OU=$_" }
    $UserPath = "$($OUs -join ','),DC=acsad,DC=com"
    New-ADUser -Name $UserName -Path $UserPath -AccountPassword $SecurePassword -Enabled $true
}

Changes
•Changed to allow multiple organizational units (OUs) to be specified using the $SOU parameter
•Use split ',' to separate the $SOU string with commas, and use ForEach-Object to prefix each OU with "OU=" and store in the
$OUs array
Why?
•The old code only performed actions on a single OU, the new code accepts multiple OUs separated by commas
•Dynamically configure $UserPath based on $SOU to increase script flexibility and reduce hardcoding
Create an OU01
15

## Page 16

function Show-ADOUTree {
    param (
        [string]$searchBase = "DC=acsad,DC=com",
        [int]$level = 0
    )
    $ous = Get-ADOrganizationalUnit -Filter * -SearchBase $searchBase -SearchScope OneLevel
    foreach ($ou in $ous) {
        if ($level -eq 0) { Write-Host "" }
        $indent = " " * $level
        Write-Host "$indent" -NoNewline
        Write-Host $ou.Name
        $indentUsers = " " * ($level + 1)
        $users = Get-ADUser -Filter * -SearchBase $ou.DistinguishedName -SearchScope OneLevel
        foreach ($user in $users) {
            Write-Host "$indentUsers*" -NoNewline
            Write-Host $user.SamAccountName
        }
        Show-ADOUTree -searchBase $ou.DistinguishedName -level ($level + 1)
    }
}
Output to User, not just OU
Add a * in front of User
Additions
Results screen
Create an OU01
16

## Page 17

Execution order
•Create subordinate OUs named "AOU" and "KOU" under "UserOU
•Create an OU named "POU" in the domain "acsad.com"
•Under "UserOU", create users named a1, a2, and a3 inside the "AOU"; create users k1, k2, and k3 inside the KOU; and create
user p1 inside the POU
Create an OU01
17

## Page 18

Applying GPOs02
UserOU
AOU
a1 a2 a3
KOU
k1 k2 k3
Deploying registries to AOUs
Purpose: Add Notepad to Startup
AOU
Deploying the registry to KOUs
Purpose: Add a calculator to your startup
programs
KOU
Notes
• With Powershell, most of the activity around GPO policies is centered around application and deployment
• While registry-related items can be easily implemented with Powershell, policies that turn on or off the policies listed
are more easily implemented through the Group Policy Management Console GUI at

18

## Page 19

New-GPO, Get-GPO
Create a new Group Policy object, create a new GPO, and subsequently add policy settings to this GPO, or link to a specific Active
Directory container
Search for information about one or more GPOs, viewing details such as the GPO's name, ID, status, description, and more
Output information about all GPOs in the
domain
What's printed
•DisplayName
•DomainName
•Owner
•Id
•CreationTime
•ModificationTime
Get-GPO -All
Requiring appropriate permissions to create
or view GPOs in Active Directory
Incorrect use can negatively impact system
operations
Before you use
Applying GPOs02
19

## Page 20

Set-GPRegistryValue
Used to configure registry-based policy settings within a Group Policy object (GPO), allowing you to add or modify registry settings to the GPO
Useful for managing registry settings locally or in a domain, and when you want to set a value for a specific registry key
Name
Key
ValueName
Type
Value
Parameter
Name of the GPO to change
Path to the registry key to change
Name of the registry value
Registry data types
Data to set
If possible, registry changes should be tried out in a
test environment first, and only applied to
production after you've confirmed that there are no
issues
Caveats
Applying GPOs02
20

## Page 21

$gpoName = "StartNotepadWithWindows"
New-GPO -Name $gpoName -Comment "This GPO will add Notepad to the startup programs."
$gpoId = (Get-GPO -Name $gpoName).Id
$keyPath = "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
$valueName = "Notepad"
$valueData = "C:\Windows\System32\notepad.exe"
$valueType = "String"
Set-GPRegistryValue -Guid $gpoId -Key $keyPath -ValueName $valueName -Type $valueType -Value $valueData
$ouPath = "OU=AOU, OU=UserOU ,DC=acsad, DC=com"
New-GPLink -Name $gpoName -Target $ouPath
Description.
•Automate the process of creating Group Policy objects (GPOs) and linking them to specific user organizational units (OUs)
•Implement a setting to add the Notepad application to a user's Windows Startup Programs list
•Create a new GPO named StartNotepadWithWindows and use the Comment parameter to add the following description to the
GPO: "This GPO will add Notepad to the startup programs."
•Use the Get-GPO cmdlet to retrieve the identifier (ID) of the GPO that you just created, which you can use later to set registry
values
•Set the registry with Set-GPRegistryValue
•Linking GPOs that you create by using the New-GPLink cmdlet to a specific OU
Applying GPOs02
21

## Page 22

Confirm that Notepad is running
User : a1
You'll see Notepad added
Run
AOU
a1 a2 a3
Applying GPOs02
22

## Page 23

function Create-StartProgramGPO {
    param(
        [string]$GPOName,
        [string]$OUPath,
        [string]$ProgramPath,
        [string]$ValueName
    )
    $domain = "DC=acsad,DC=com"
    New-GPO -Name $GPOName -Comment "This GPO will add a program to the startup programs."
    $gpoId = (Get-GPO -Name $GPOName).Id
    $keyPath = "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
    $valueData = $ProgramPath
    $valueType = "String"
    Set-GPRegistryValue -Guid $gpoId -Key $keyPath -ValueName $ValueName -Type $valueType -Value $valueData
    $fullOUPath = "$OUPath,$domain"
    New-GPLink -Name $GPOName -Target $fullOUPath
}

Change to a function
•Create and configure GPOs to set specific programs to run automatically when a user starts Windows
•Use parameters to make functions universally available
•Takes GPO name, ou path, program path, and value name as parameters to apply the policy to specific ou's
Applying GPOs02
23

## Page 24

Confirm that Notepad is running
User : k1
You can see that startcalc has been added
Run
KOU
k1 k2 k3
Applying GPOs02
24
