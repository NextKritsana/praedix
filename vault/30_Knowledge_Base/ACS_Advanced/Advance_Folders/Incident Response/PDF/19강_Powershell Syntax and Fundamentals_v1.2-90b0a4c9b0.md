---
title: "19강_Powershell Syntax and Fundamentals_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\19강_Powershell Syntax and Fundamentals_v1.2.pdf"
source_size_bytes: 771366
source_modified: 2025-11-12T12:43:36
imported_at: 2026-06-14T14:26:35
tags:
  - acs
  - acs-advanced
  - imported
---

# 19강_Powershell Syntax and Fundamentals_v1.2

- Source: [19강_Powershell Syntax and Fundamentals_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/19%EA%B0%95_Powershell%20Syntax%20and%20Fundamentals_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Powershell Syntax,
Fundamentals
• What is Powershell?
• Powershell commands
• Simple Utilization
19
1

## Page 2

Powerful commands
Flexible and powerful commands, available as a scripting
languageAutomate tasks ranging from simple commands to
complex scripts
Convenience
Because the output is treated as an object, it's easy to
manipulate the data and pass it to other commands or
functions
.NET
Fully integrated with the .NET framework, so you can do more
advanced things with .NET libraries and assemblies
Powershell
Scripts
Help you write concise, readable scripts
Support for programming constructs like variables, conditional
statements, functions, and more
Remote
Facilitates remote management by providing the ability to
execute commands and run scripts on remote systems
Multiple OS
It is used in Windows environments, but there is also a cross-
platform version called PowerShell Core that is open source
and available for Linux and macOS
PowerShell is a command-line interface and scripting language developed by Microsoft
It is used to perform various tasks and automation related to the Windows operating system and is often used for tasks such a s system administration
automation and configuration
Similar to Unix-like shell scripting languages, but based on the .NET framework, it provides COM and WMI, making it particularly powerful on
Windows platforms
01 What is Powershell
2

## Page 3

01
Powers
hell
Critical to your computer if used
incorrectly
Requires proper permission settings
Convenience Automation Lots of featuresPowerful
commands Policy settings
What is Powershell
What is Powershell
Deleting files
Be careful, as this can delete important files such as computer
setup information and logs if used incorrectly
Registry modifications
Incorrect modifications can affect your system and may disable
Windows Firewall, automatically execute malware, etc.
Change account permissions
Incorrect permission settings can lead to vulnerabilities
Caveats
3

## Page 4

How to run
1. Press Windows + R keys, type "powershell" and run it
2. Run by typing "powershell" from the Start menu or search bar
Why?
• During the course, you may need to make changes to system settings
that require administrator privileges
• When you need to disable the security policy with administrator rights
during the module installation and download process
• You may need to access the System32 folder, which requires
administrator privileges
Color by permission
Powershells run with administrator privileges appear in a blue window,
while Powershells run with normal privileges appear in a black window
If it's a black window and the lesson requires administrator privileges, specify above
that it requires administrator privileges
01 What is Powershell
4

## Page 5

01
Verb
• Get
• New
• Set
Command
Connection
Path
What is Powershell
You can print information about a command with Get-Command, or get a list of running processes with Get-Process
You can use New-Item to create a new item
The Get-Process -Name Explorer command uses the name parameter to the get-process command to get information about the
explorer process
example
noun parameter arguments
5

## Page 6

02
Output all commands
Command
Get-Command
Cmdlet Command Output
Get-Command -CommandType cmdlet
Alias command output
Get-Command -CommandType alias
Powershell commands
• Simple aliases or shortcuts for commands or
cmdlets used in PowerShell
• Used to make scripting more convenient
Alias
• A portmanteau of "Command-let", meaning a small
command
• Small, reusable commands designed to perform
specific behaviors in the Powershell environment
cmdlet
6

## Page 7

CMDlet Alias
Cmdlet Alias
Description
• The cmdlet to view processes is get-process, but we've given it the nickname ps so that you can use ps to see the results of get-process
• In addition to this, you can use a pipeline to add one more condition using the results of the previous command
02 Powershell commands
7

## Page 8

02
P r o c e s s  R e l a t e d  C o m m a n d s
Get-Help *process*
Powershell commands
D e s c r i p t i o n
• Get-Help *process* to get Help information about all the cmdlets
and functions that are related to the keyword "process“
• Get-Command -Name *process* to get a list of all Cmdlets and
functions that contain the "process" keyword
• You can use any keyword to search for a command and get
information about it
8

## Page 9

02
P r o c e s s  O u t p u t
Cmdlet Command: Get-Process
alias command: ps
S t a r t  P r o c e s s
Cmdlet Command: Start-Process
Ex: Start-Process calc.exe
Powershell commands
Tips
You need to enter the following path: Start-Process In the case of calc.exe, it is located in System32, and System32 can be run from any location because it is registered in
the system environment variable
The list of system environment variables can be found in Edit the System environment variable - environment variable - System variable – PATH
Enter Stop-Process calc.exe to stop the currently running calculator
9

## Page 10

Process
Get-command *process*
ItemProperty
Get-command *itmpro*
Object
Get-command *-object*
EventLog
Get-command *eventlog*
Img Img
02 Powershell commands
Additional Get-command
examples
10

## Page 11

02 Powershell commands
--EXAMPLE
Example shows a variety of examples of how you can use these commands
Examples show that you can use Pipe to reduce the scope or use Where
object or foreach to do different things
Where object and foreach will be discussed in more detail in the next lesson.
Select-Object
Select-Object is used to control output by selecting or manipulating the properties of an object
Use the -First option to print the top n results
Use the -property option to output only the results the user wants
If you give -property * as an option to Select-object, you can see about 50+ properties
11

## Page 12

02 Powershell commands
Overwrite a file
Example
Get-command -commandtype cmdlet > a.txt
Append to a file
Example
Get-command -commandtype alias >> a.txt
> >
>>
12

## Page 13

02 Powershell commands
S W
mkdir
The mkdir command is short for "make
directory" and is a command that creates a
new directory.
You can find mkdir using the Get-Command
command, and it is categorized as a function
cd
Short for "change directory", used to change
the current working directory
The cmdlet called Set-Location in Powershell
does the same thing, and you can use it as
cd, but you can see that Set-Location has an
alias registered as alias
Tips
mkdir can also create a directory in a specific path by specifying a path, which can use system environment variables, and cd can also use system
environment variables for absolute paths.
Environment variables like windir or appdata can be used to point to specific directories
13

## Page 14

02 Powershell commands
You can create files, directories, and registry keys, but by default, you can give New-Item the ItemType option to determine what type of item to
create, the -Path option to determine where to create it, and the Name option to determine what to name it
New-Item
Create the ACS_DIR directory
Item Type : Directory, PATH : $env:USERPROFILE\Desktop, Name : ACS_DIR
New-Item -ItemType Directory -Path $env:USERPROFILE\Desktop -Name ACS_DIR
Create an ACS_DIR file
Item Type : File, PATH : $env:USERPROFILE\Desktop\ACS_DIR, Name : ACS_FILE
New-Item -ItemType File -Path $env:USERPROFILE\Desktop\ACS_DIR -Name ACS_FILE
Create directories and files
Create Notepad shortcuts
Alias:Note means "Note on an alias item", combined with New-Item means "Add a note to an alias item",
and -value is the path to notepad
New-Item alias:Note -value C:\Windows\System32\notepad.exe
Create an alias
14

## Page 15

02 Powershell commands
NI uses the Alias in New-Item
Type NI Registry:: and enter the location to add, add an entry named TEST under
HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMUR
Command : NI Registry::HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU\TEST
Create a registry key
By default, verification is available through the Get-Item command and the Get-Childitem command
The Get-item command returns the properties of the selected item
By default, itemtype, Mode, LastWirteTime, Length, and Name are output, and for registries, Hive and Name and Property are output
Alias : NI
Get-ChildItem is a command that returns a list of child items (files, directories, etc.) in a specified path
Get a list of all files or directories in a specific path
Alias : ls
Confirm
15

## Page 16

Simple Utilization03
Change the properties of commands, files, registry keys, directories, etc. that are used to set the properties of items in a specific path
New-ItemProperty
This command can be used to change the value of a key in the registry, and most malware uses it to perform a number of actions, including registering itself as a startup
program so that it starts automatically when the computer starts
Requires administrator privilegesAdd Notepad to your startup programs
Set the path to add to the PATH option of New-ItemProperty
PATH : HKCU\Software\Microsoft\Windows\CurrentVersion\Run, Name : Notepad value : C:\Windows\System32\notepad.exe
Command : New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "Notepad" -Value "C:\Windows\System32\notepad.exe"
Create a registry key
16

## Page 17

Simple Utilization03
Variables
$variableName = value
Variables are identifiers used to store and reference data, allowing you to preserve values and increase the flexibility of your code
Variables begin with the $ sign, variable names begin with a letter, and you use the equals sign (=) to assign a value to a variable
The data type is automatically set based on the value assigned to the variable, such as 3 for an integer, 3.3 for a real number, or ACS for a string
Variables
Global: Variables accessible throughout the script or session
Script: Accessible only from within the script file
Local: Accessible only within a specific function or block
Scopable
17

## Page 18

Simple Utilization03
If you enter the value 1 in Test, you can see that the BaseType
is System.valueType and declared as Int32
If you add .fullname after Gettype, you can see the full name
of the variable type. When an integer like 1 is declared,
System.Int32 is declared
Check Type - Integer
If you put the string abc in the variable named test, the value
of string is output when checking with gettype
In addition to this, System.double is declared when it is a real
number such as 1.1, and System.Boolean when True or False is
declared
Check Type - etc
18

## Page 19

Simple Utilization03
Variables
The get-command Command
Store the get-command command in a variable named Test2
BaseType is System.Array and the fullname of that type is system.object
Why?
If you know what type a variable is declared as when you declare it, you can
later determine why it doesn't work and where the error is coming from
When creating a large amount of scripts or modules that may be used in the
real world, being able to see the types of variables being declared can help
prevent errors or fix errors that do occur
19

## Page 20

Simple Utilization03
• A hashtable is a data structure that represents a collection of pairs of keys and
values
• It is defined using curly braces {}, with each key-value pair separated by a
comma
Hash Talbe
• A custom object is an object that has a format that you define
yourself
• Create an object using the [PSCustomObject] format
• Custom objects provide a more intuitive way to represent structured
data
• Useful when representing data in a tabular format
Custom object
Summary
Hashtables primarily manage a series of key-value pairs, while custom objects are used to represent structured data
When using a hash table, access to each entry should be $hashTable["Key"], and in a custom object, access to each property should be $customObject.Property
20

## Page 21

powershell
Strong commands
Scripts
Lots of features
registry
System settings
Lots of features
permission
Permissions
Protect
Enhanced security features
Simple Utilization03
Why?
Powershell is a powerful tool for IT administrators and security professionals and can be utilized in a variety of scenarios, including automation and system monitoring
By writing scripts to check values for the items you need to manage with Powershell, you can run those scripts periodically to reduce checking time and increase convenience
21
