---
title: "21강_Powershell Modules and Functions_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\21강_Powershell Modules and Functions_v1.2.pdf"
source_size_bytes: 659403
source_modified: 2025-11-12T12:44:53
imported_at: 2026-06-14T14:26:37
tags:
  - acs
  - acs-advanced
  - imported
---

# 21강_Powershell Modules and Functions_v1.2

- Source: [21강_Powershell Modules and Functions_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/21%EA%B0%95_Powershell%20Modules%20and%20Functions_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Powershell modules and
functions
• Function
• Modules
21
1

## Page 2

Function01
• Allows users to write and use their own
functions as needed
• When creating functions, you can make
them cmdlet-like for better readability
In-house development
• Automate repetitive and tedious tasks
• Make functions into reusable blocks so
you don't have to write the same logic
over and over again in different scripts
Scalability and reusability
• Use variable and function names to
make sure they clearly indicate their
role, and use consistent indentation and
appropriate whitespace to visually
represent blocks of code
Improve readability
• Functions can accept parameters to pass
information from the outside world, and
return results that can be utilized by the
part that called them
Utilizing return values
What is a function?
The main purpose of utilizing Powershell functions is to improve maintainability by making code more modular and
better organized
Features
2

## Page 3

Function01
What is Powershell ISE
• ISE provides multi-line editing, tab completion, syntax coloring, selective
execution, context-sensitive help, and support for right-to-left languages
• Allows you to do the same things you do in the Windows PowerShell
console
01
Script editor support
The editor window provides an environment for writing and editing PowerShell
scripts, and multi-tab support allows you to work with multiple scripts
open at the same time
Tabs are independent, so you can write code for different scripts or tasks separately
Provides an efficient working environment for developers and system administrators
using PowerShell ISE
02
Support for autocomplete
Auto-complete part of a command or function by pressing the tab key after
typing it
Speeds up development by eliminating the need for developers to type the
entire command or function name
Write consistent code by selecting the correct command or function name
faster
03
Debugging features
Find and fix errors in your code as you run the script
Set breakpoints on any line in the code editor
04
Integrated Output Pane Support
ISE provides script execution results and errors in a unified output window
Quickly view and debug error messages
Immediately see the execution results of commands
Features
Set-PSBreakpoint -Line 5 -Script debugtest.ps1 -Action {
if ($i.Name -match "notepad.exe") { break }}
$list = Get-ChildItem C:\Windows
foreach ($i in $list)
{ {
    Write-Output $i.Name
}
3

## Page 4

Function01
https://learn.microsoft.com/ko-kr/powershell/scripting/windows-powershell/ise/introducing-the-windows-powershell-ise?view=powershell-7.4
Verify version
$PSVersionTable
ISE was first introduced in Windows PowerShell
V2 and redesigned in PowerShell V3
ISE is supported in Windows PowerShell V5.1 and
earlier
How to run
Search for "PowerShell ISE" in the Start menu
In the taskbar, type "PowerShell ISE" in the search box,
and in the results that appear, click to run it
Type powershell_ise in the Run window to run it
4

## Page 5

Function01
Exam 1
Exam 2
Exam 3
Exam 4 (Advanced Functions)
Function ACS { "Hello ACS" }
$str1 = "hello"
$str2 = "ACS"
Function ACS { $str1 + " "+ $str2 }
$str1 = "hello"
$str2 = "ACS"
$output = $str1 + " " + $str2
Function ACS { Write-Host $output }
function ACS{
    param (
        [Parameter()]
        $str1 = "hello",
        [Parameter()]
        $str2 = "ACS"
    )
    Write-Output "$str1 $str2"
}
Advanced functions
Functions that utilize various features and options to improve modularity, reusability, and readability. The result of a function can be returned using the
You can use the param keyword to define a parameter to a function, which has a name and data type.
[CmdletBinding()] can be used to enable advanced parameter functionality
Same output
5

## Page 6

Function01
Exam 1
• Simply start a function using the Function keyword and define the name of the function as ACS
• The part in curly braces is the body of the function, which in this case returns "Hello ACS"
Exam 2
• Start a function with the Function keyword, define the name of the function as ACS, and use
variables and string operators in the body
• When calling with ACS, you should see hello ACS
6

## Page 7

Function01
Exam 3
• Before defining a function, declare a variable to set the value to be output
• Similarly, you start a function by using the Function keyword and define the name of the function as
ACS
• Inside the function, we use cmdlet commands, and again, when ACS is called, hello ACS is the output
Execute Permissions
The reason for setting execute permissions is to enhance security and safety and prevent the execution of malicious scripts or code
By default, the Execution Policy is set to Restricted, which prevents externally downloaded scripts from running automatically
Locally generated scripts can run unsigned, but externally downloaded
scripts must be signed
RemoteSigned
This means that all scripts must be digitally signed, and if the
script is not signed, execute X
Allsigned
Grant execute permission for all scripts
Override policies
Bypass
In the lab, we will be testing with safe code, so we will set the
ExecutionPolicy to Bypass for the lab and lecture
In the lesson
7

## Page 8

Function01
https://learn.microsoft.com/ko-kr/powershell/module/microsoft.powershell.core/about/about_functions?view=powershell-7.4
Enrollment and verification
After registering a function, you can use Get-Command or Get-ChildItem to get a list of currently registered functions
Get-Command is used to get the different command types, while Get-ChildItem function:\ gets the list of functions in the function location, function:\
Get-Help provides more information about the function, parameters, examples of usage, etc.
8

## Page 9

Function01
remove-item
remove-item function:\ACS
Command
Commands to delete the ACS function, the function you
just used
Why?
• When a registered function is no longer needed, deleting it allows you to efficiently manage system resources, a large number of unnecessary functions can potentially
overwhelm memory and performance
• Deleting functions that perform sensitive functions for security reasons, deleting functions improves security because the code or logic of the function is not exposed to
the outside world
• Improve code readability and maintainability by periodically cleaning up registered functions, functions that are no longer needed as the code changes and evolves over
the course of the project
• Deleting unnecessary functions to avoid conflicting or duplicate function names
9

## Page 10

Function01
Write-Output to output that variable
Output
The function takes two parameters, $str1 and
$str2, which default to "hello" and "ACS"
respectively
Parameterfunction ACS{
    param (
        [Parameter()]
        $str1 = "hello",
        [Parameter()]
        $str2 = "ACS"
    )
    Write-Output "$str1 $str2"
}
The Parameters section defines the parameters
of the function, and assigns default values to
those parameters
These default values are used if the parameter
does not pass a value when the function is
called
Parameter
Save .ps1
• Save the function with the ps1 extension because we'll be fleshing it out more and more and
giving examples
• .ps1 is the extension for PowerShell script files
• A PowerShell script is a text file written using the PowerShell scripting language that contains a
set of PowerShell commands and scripting syntax
• When you run a script file, the PowerShell commands in the file are executed one after the
other, performing the task for which the script was designed
10

## Page 11

Function01
Calling functions
Function descriptions
If you define a function as an advanced function, you can get detailed help for
that function using the Get-Help command

Detailed options
SYNTAX confirms that -str1 and -str2 can be used to insert characters
User settings
• Substitute the string hi for -str1 and the string ACS!!! for -str2
• Output the value hi ACS!!! on execution
• Setting the param directly using -str1 and -str2 to output the user-set value
Description
In general, you will see the same output as before when calling the
function
This means that the default value defined in param is output
Run a function
11

## Page 12

Function01
• When you define a parameter in a function, you can use the Mandatory
property to specify whether the parameter must be supplied
• Normally, parameters are optional, and if you don't pass a value when the
function is called, the default value is applied to that parameter
• Use the Mandatory property when you want to make a specific parameter
mandatory
• Helps to make your code more reliable by clearly defining the interface of the
function and enforcing required input from the function user
Mandatory
• For $Mandatory=$True, $str1 is set as a mandatory parameter, so you must pass
a value when calling the function
• If you don't, the output X
Example
Tips
• If Mandatory=$false, you can attach more options, such as Mandatory=$false followed by Default="DefaultHello" to indicate that $str1 is optional and defaults to "DefaultHello“
• If no parameters are provided when the function is called, it means that the default value can be applied
12

## Page 13

Function01
Must take arguments
Export $str1 to the 2nd position
Must take arguments
Export $str2 to position 1
Run Result
• The Position property is used to order the
parameters of a PowerShell function
• Allows you to pass parameter values in a specific
order
• Increases the readability of the interface and
makes it easier for users to understand and utilize
the function
• Note that when using the Position property, you
can omit parameters X
position
Description
• Using the Mandatory property to require a mandatory value to be entered
• Call the ACS function and substitute the string ACS for the first parameter $str1 and the string hello for the second parameter $str2
• If there is no Position property, the ACS hello is output in order, but in this script hello ACS is output
13

## Page 14

Function01
CmdletBinding
• An attribute that provides advanced functionality to a PowerShell function or script
• You can add a number of useful features to your functions
CmdletBinding(SupportsShouldProcess=$true)
• An option to enable the ShouldProcess feature in a PowerShell function or script
• ShouldProcess informs the user of the impact of a given action or change and asks for approval
• Used in conjunction with whatif and Confirm
• This option is used in conjunction with
ShouldProcess to allow you to see how the action
will run without actually making any changes
-whatif
• Prompt users for confirmation
-confirm
• Write commands for debugging and tracing a
script or function
• You can print specific messages to help you
understand the execution flow of a script or
function or to troubleshoot problems
• In this script, the strings input strings and add 2
str are printed as output when the verbose option
is given
Write-Verbose
14

## Page 15

Function01
Other Parameters
• Properties used to define parameter sets
• Suppose a function has two different modes of behavior for
reading and writing files, ParameterSetName can be used to
define the parameters required for the two modes of behavior
• Functions can be configured to respond appropriately in
different situations
ParameterSetName
• Set parameters to accept input through a pipeline
• Simplify your code, increase flexibility, and process data more effectively
ValueFromPipelineByPropertyName
•  Automatically assigns the value of an object's property to a parameter
when it is accepted from a pipeline
• Useful when the property name of an object matches the parameter
name of a functionparameter name
ValueFromPipeLine
• Provide help messages for specific parameters to help you use the function
• Useful when functions are complex or provide multiple options
Help Message
Other attributes
• Used when the parameter represents the user's credentials
• Allow username and password to be entered in the corresponding
parameters when calling a function
[PSCredentail]
• Indicates that the parameter must be one of a specific value
• Raise an exception if you don't specify a specific value when calling the
function
[ValidataSet("Option1", "Option2")]
• Parameter Validation Attributes
• Verify that the value provided in a parameter passes through a specific
script block
• In the example, the parameter indicates the condition that it must be
positive to be valid
[ValidataScript($_ -gt 0)]
15

## Page 16

Modules
.dll .psd1.psm1
Modules02
• Script Module Files in PowerShell Modules
• Storing Scripts and Organizing Code into
Modules
• To make your module available externally,
specify the variables and functions that
you want to export in the .psm1 file
• Primarily used to leverage external libraries in a
PowerShell environment
• Powerfully extend PowerShell scripts with external
libraries that handle database connections,
encryption, external API calls, and more
• PowerShell Data Module File Extensions
• Used to define metadata and configuration
information for a PowerShell module
• Holds information related to the code as well as
version, author information, dependencies, and
other settings
• Increase code structure and reusability
• Supports versioning, allowing multiple versions of a module
to be used simultaneously
• Enables functions and variables to be encapsulated in the
module's namespace
• Provide help and explanations to users to help them
understand how to use the module
Pros
• How to organize and reuse code, functions, variables, and
resources in your PowerShell environment
• Includes elements such as scripts, binary files, functions,
help files, etc.
• Can be loaded into a session by using the Import-Module
command
Module?
Namespace encapsulation
• The concept of organizing code by logically grouping and separating code to avoid name conflicts 16

## Page 17

Modules02
Verify modules
Create functions named Ps-top, acs, and showps and save
them as a file named ACS_Module.psm1
Creating modules
• Ps-top: A function that takes the property value of the
$p_top3 variable created in the previous time and
 output count as arguments
• ACS: A function created this time
• showps: output a string named hihi
Function
17

## Page 18

Modules02
Execution Bypass
Import Module
Kind of Command
Execution Policies • A separate execution policy is required to import external modules
• Set execution policy to bypass
Warning statements • Execution policy When the module is loaded from another PowerShell session, a warning is printed, indicating that
unauthorized syntax exists
• Ignore that warning because the module was created by following the lecture
Use the Get-command command to see the functions in a
module
Verify that the ACS, ps-top, and showps functions exist
Verify Module
18

## Page 19

Modules02
ps-top
• Set the descending destination to WorkingSet and the number of
outputs to 3
ACS
• Enter ACS and HELLO as arguments
Showps
• Result: hihi
Verify operation
Command
Result
19
