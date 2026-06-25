---
title: "17강_Build Your Own Online Collection Tool_(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\17강_Build Your Own Online Collection Tool_(1)_v1.2.pdf"
source_size_bytes: 474431
source_modified: 2025-11-12T12:38:53
imported_at: 2026-06-14T14:26:33
tags:
  - acs
  - acs-advanced
  - imported
---

# 17강_Build Your Own Online Collection Tool_(1)_v1.2

- Source: [17강_Build Your Own Online Collection Tool_(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/17%EA%B0%95_Build%20Your%20Own%20Online%20Collection%20Tool_%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Overview & Basics
• Overview & Basics
• Collection Target, Order
• Create
17
1

## Page 2

Overview01
Purpose
• Improve efficiency by collecting only the data you
need
• Save time by using pre-made scripts
Targets
• Recently used Windows 10, 11 targets
• Volatile, non-volatile collection
2

## Page 3

Overview01
Available from the command line
Environment variables represent dynamic values that are used by the operating system to control the behavior and configuration of the system and are used to store and access
computer settings, system paths, and information needed for programs to run. Environment variables are stored in text format and are read and used by the operating system or
application to store global settings, user-specific information, paths to executable files, and more.
Windows Environment Variables
>_
%SYSTEMDRIVE%
%WINDIR%
%COMPUTERNAME%
%UserProfile%
%AppData%
Example
C:
C:\Windows
[Computer Name]
C:\Users\[User_Name]
C:\Users\[Users_Name]\AppData\Roaming
AppData
This directory is primarily used by applications to store user-specific data, settings files, log files, etc.
3

## Page 4

Overview01
Batch script syntax
Redirects
Redirection functions perform tasks such as saving the output of a command to a file or receiving input from a file
The > symbol is used to write the output of a command to a file
The >> symbol is used to append data to a file.
Command Description
Setlocal Declaring local variables
chcp Change the code page
set Declaring variables
set /p Enter variables
: Labels for the Goto command
:: Comment
@echo off Show command execution x
Command Description
goto Jump to a specific label
if Conditional Statements
if /i When If is True
mkdir Make directory
echo Output to the text screen
cd Change Directory
title Prompt name
4

## Page 5

Collection order02
Collection
lists
Network Connection
Information
Logon Sessions
Physical Memory
Process information
Open files
Network settings
information
System time
Item Ingestion tools Item Ingestion tools
Registry forecopy_handy Prefetch forecopy_handy
$UsnJrnl forecopy_handy $MFT forecopy_handy
Event Log forecopy_handy $LogFile forecopy_handy
VBR forecopy_handy Task
Manager
taskschedulerview
Webaddon browseraddonview Web history browsinghistoryview
WER robocopy Timeline robocopy
Web Tools
Web addons and Web history, we'll use a tool called Browseraddonview and a tool called
browsinghistoryview to get results from both Chrome and Edge.
NIST SP 800-86
Decide ingestion order based
on OOV
5

## Page 6

Collection order02
Priority Collection
Prioritize collecting prefetches with a limited number of records
Prefetch data contains records of how specific executables were loaded, including file names, paths, execution times, and DLLs used to load them
Analyzing this information can reveal system usage patterns, application usage history, etc.
Forecopy_handy.exe
Collection tools
https://github.com/proneer/Tools/blob/master/forecopy/forecopy_handy(v1.2).7z
Download PATH
Forecopy_handy.exe -d %SystemDrive%\Windows\Prefetch [OUTPUT_PATH]
Command
6

## Page 7

Collection order02
Prefetch
priority
Collect computer information
in advance because it may not
work on all versions
Computer
informations
Record the names of responsible
parties and operators so they can
be effectively managed in the
event of similar threats in the
future
Operator name
1. Collect both volatiles and
non-volatiles
2. Collect volatile only
3. Collect non-volatile only
4. Exit
Options
Volatile data
Based on volatile sensitivity
Reference : NIST SP 800-86
Non-volatile data
Data that is relatively easy to
collect
7

## Page 8

Collection order02
Non-volatile onlyBoth
Volatile only Exit
Select an option
Volatile Non-volatile
Prefetch
Prefetch
Collecting non-
volatile data after
prefetch
Exit
If you choose the first option, collect both volatile and non-volatile data, you will firstly
collect prefetch and then collect volatile data in line with the volatile data sensitivity
material
Considerations
• Space available for storage
• Load on the system
• Includes considerations from options 2 and 3
Option 1
The second option, Collect volatile data only, does not collect prefetch and collects
only volatile data based on volatility sensitivity
Faster than collecting non-volatile data
Considerations
• Can be affected by the state of the system, potentially causing failures or errors
Option 2
If you select the third option, Collect non-volatile data only, prefetches are collected
first and then the remaining non-volatile data is collected
Considerations
• Can be very lonf time consuming and requires a huge amount of storage, so it's
important to have enough storage space
Option 3
8

## Page 9

Visual Studio Code
• Visual Studio Code, also known as VSCode, is a free and open source code editor developed by Microsoft
• It is popular among developers and offers lightweight yet powerful features. Visual Studio Code offers many features, including support for multiple
languages, rich extensions, debugging, Git integration, and more to effectively support your development work
• It supports IntelliSense and auto-complete when writing batch scripts to improve coding efficiency and detects grammatical errors to make life easier for
developers
Fewer features than other editing tools,
but simple and quick to get started with no
user installation required
Great for simple editing of small batch
scripts
Notepad
A free and powerful text editor with many
benefits for writing batch scripts
Grammar is highlighted to improve
readability, and keywords, variables, and
comments are color-coded for easy visibility
Autocomplete and code folding features
simplify repetitive tasks and make it easy to
organize blocks of code
Notepad++
Supports most of the features of
Notepad++
Provides a feature called Multiple
Selections, which allows you to edit in
multiple places at the same time
Provides a powerful editing environment
that can be utilized for a variety of
languages and tasks, as well as batch
scripting
Sublime Text
NOTE
PAD
NOTE
PAD++
Sublime
text
Visual Studio
Code
Create03
9

## Page 10

@echo off
chcp 65001
title ACS_TEST
color F0
set hostname=%COMPUTERNAME%
if "%PROCESSOR_ARCHITECTURE%" == "AMD64" ( set _yoursystem=Windowsx64 ) else ( set _yoursystem=Windowsx86 )
echo.
echo The system in use is %_yoursystem%.
echo.
set /p CaseName=(!) Please enter the name of the worker. :
echo.
echo The name of the worker you entered is %CaseName%.
echo.
Prompt screen settings
UTF-8 settings
Worker description
Description
• Set the Code page to 65001 with @echo off to remove unnecessary output and 65001 to indicate UTF-8 encoding
• Set the name of the prompt to ACS_TEST and the Color to F0, which means white background and black text
• Get the COMPUTERNAME in a variable called hostname, determine whether the operating system is 64-bit or 32-bit, and print it to the screen
Create03
10

## Page 11

set "tool_path=tools"
set "output_path=%CD%\result"
if not exist "%output_path%" (
  mkdir "%output_path%"
  echo mkdir : result
) else (
  echo 0
)
echo.
set /p _Ss_Disk=(!) Do you want to run the script? ("n" Exit the program on input):
if /i "%_Ss_Disk%" == "y" GOTO:SELECT
if /i "%_Ss_Disk%" == "n" GOTO:END
Set up folders, create
save paths
Confirm execution
Description
• Assign the value tools to a variable named tool_path and put the value %CD%\reuslt in a variable named output_path
• CD% is the system environment variable that represents the current working location
• The conditional statement then creates a folder named result and prints a string if the folder does not exist in the working location
• Because this script requires administrator privileges and uses a lot of resources and storage space when running, it displays a confirmation whether to run the script or not
• If the conditional statement receives y, go to the SELECT label; if it receives n, go to the :END label
Create03
11

## Page 12

:SELECT
echo.
echo (!) Please check the list you want to run.
echo -------------------------------------------------------------
echo  1. Full Execution
echo.
echo  2. Volatile artifacts
echo.
echo  3. Nonvolatile artifacts
echo.
echo   4. END
echo ------------------------------------------------------------
set /p Select=(!) input num :
if "%Select%"=="1" (set _access=all)
if "%Select%"=="2" (set _access=vo-arti)
if "%Select%"=="3" (set _access=non-arti)
if "%Select%"=="4" (set _access=END)
if "%_access%"=="all" GOTO:vo-pre
if "%_access%"=="vo-arti" GOTO:vo-arti
if "%_access%"=="non-arti" GOTO:non-arti
if "%_access%"=="END" GOTO:END
Setting
value
Results so far
Description
• Create 4 options
• Move to different labels based on the value you receive input from the user
Create03
12

## Page 13

:vo-pre
set "result_folder=%output_path%"
set "NON_Volatile_result=%result_folder%\NON_Volatile_result"
if not exist "%NON_Volatile_result%" (
  mkdir "%NON_Volatile_result%"
  echo mkdir : NON_Volatile_result
)
set "forecopy_handy_path=%tool_path%\forecopy_handy.exe"
set "output_forecopy_handy=%NON_Volatile_result%\Prefetch"
mkdir "%output_forecopy_handy%"
"%forecopy_handy_path%" -d %windir%\Prefetch "%output_forecopy_handy%"
:vo-arti
if "%_access%"=="all" GOTO:all-nonv
if "%_access%"=="vo-arti" GOTO:SELECT
When selecting both
When selecting only
volatile data
Collect volatile data
Description
• If you chose option 1, write a script to collect prefetches
• Include folder creation, collection commands, etc.
• If you chose option 2, skip the prefetch and start with the :vo-arti label
• Write a script to collect volatile data in an empty space
Create03
13

## Page 14

:non-arti
set "result_folder=%output_path%"
set "Volatile_result=%result_folder%\Volatile_result"
set "result_folder=%output_path%"
set "NON_Volatile_result=%result_folder%\NON_Volatile_result"
if not exist "%NON_Volatile_result%" (
  mkdir "%NON_Volatile_result%"
  echo mkdir : NON_Volatile_result
)
set "forecopy_handy_path=%tool_path%\forecopy_handy.exe"
set "output_forecopy_handy=%NON_Volatile_result%\Prefetch"
mkdir "%output_forecopy_handy%"
"%forecopy_handy_path%" -d %windir%\Prefetch "%output_forecopy_handy%"
:all-nonv
GOTO:SELECT
When selecting
only non-volatile data
Collect non-volatile data
Description
• The prefetch part is the same as
the previous page
• When option 3 is selected: start with non-arti labels, when option 1 is selected: collect volatile data and move on to
all-nonv labels to collect pre-patch duplicates x
Create03
14

## Page 15

Create03
Network NIC Interface ipconfig
NIC MAC getmac
DNS Cache ipconfig
Local Session net
Network Session TCP/IP netstat
tcpvcon
TCP/IP Open Port Netstat
arp arp
Network
• netstat
• net
• ipconfig
• getmac
• arp
Windows Basic Tools
• tcpvcon
Sysinternals Suite
• cports
• urlprotocolview
• promisdetect
Etc
15

## Page 16

Network
Create03
• A relationship between two computers or network devices on a
network
• What data was transferred and what resources were accessed in a
particular session
Network Session
• The status of a port can be open, closed, or filtered
• An open port can be used by an attacker to enter a system or
attempt to access specific services
TCP/IP open port
• Determine the mapping information between IP addresses and MAC
addresses via ARP
• Detect the presence of unregistered or unauthorized devices on the
network through ARP information
ARP
• Types of NICs include Ethernet, wireless, Bluetooth, and
moreUsed to monitor network traffic, which can be used to
detect anomalies or breaches
NIC Interface
• A unique identifier for a network interface card, used on
Ethernet.Verifies the identity of the device, identifies normal and
abnormal devices
NIC MAC
• Temporarily stores results that result of resolving domain names to IP
addressesUsed to detect access to malicious or inappropriate domains
• Allows you to trace the source of a breach and analyze how the attack was
carried out
DNS Cache
• When you're experiencing a system or network issue that is technically
network-related, checking the currently active local sessions can help
you troubleshoot by determining which users are causing the problem,
or what resources they're accessing
Local Session
16

## Page 17

::network
set "result_folder=%output_path%"
set "Volatile_result=%result_folder%\Volatile_result"
set "Net_result=%Volatile_result%\Network"
if not exist "%Net_result%" (
  mkdir "%Net_result%"
  echo mkdir : Net_result
)
:: arp
set "output_arp=%Net_result%\arp.txt"
arp -a -v > "%output_arp%"
::route
set "output_route=%Net_result%\route.txt"
route PRINT -4 > "%output_route%"
::netstat
set "output_netstat=%Net_result%\netstat.txt"
netstat -nao | findstr LISTENING > "%output_netstat%"
Create Dir
Run
commands
Description
• Arp -a prints the current entry in the arp cache table
• Route-print prints the current state of the ipv4 routing table
• The Netstat -ano command displays network connectivity and port status with options to output more detailed
information
• The other ipconfig, mac, and tcpvcon will be covered at the end of this lecture
Create03
17

## Page 18

Interim check
Create03
18
