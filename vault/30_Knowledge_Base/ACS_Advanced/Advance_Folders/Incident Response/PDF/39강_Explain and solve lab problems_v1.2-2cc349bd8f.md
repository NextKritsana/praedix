---
title: "39강_Explain and solve lab problems_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\39강_Explain and solve lab problems_v1.2.pdf"
source_size_bytes: 1058085
source_modified: 2025-11-12T13:36:43
imported_at: 2026-06-14T14:26:59
tags:
  - acs
  - acs-advanced
  - imported
---

# 39강_Explain and solve lab problems_v1.2

- Source: [39강_Explain and solve lab problems_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/39%EA%B0%95_Explain%20and%20solve%20lab%20problems_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Explain and solve lab
problems
• Introduction to Lab Files
• Problem 1
• Problem 2
39
1

## Page 2

01. current page topic
Introduction to Lab Files01
Problem 1
 Problem 2
6689ee84c05d5e84f4e4417061f22b24
MD5
6557f975d1ac951ae9fd18488141f4f0
MD5
2

## Page 3

01. current page topic
Issue 1 Environment
Something is happening in CMD
Describe the problem
No VMs are shared, only vmem files are shared
Determine what behavior occurred with just the
memory file
Shared files
Introduce the problem01 Introduction to Lab Files
3

## Page 4

01. current page topic
Prepare in advance
Additions
• More taxonomies
• More tools
Introduce the problem01 Introduction to Lab Files
4

## Page 5

01. current page topic
PLUGINS AND COMMANDS TO
USE
ETC FILE CMD
PROCESS DUMP
Imageinfo
Strings.exe
filescan Cmdline
Dumpfiles
Memdump
Pslist
Pstree
psxview
Introduce the problem01 Introduction to Lab Files
5

## Page 6

01. current page topic
Strings.exe
• Part of the Sysinternals Suite of utilities developed by Microsoft's Sysinternals team, strings.exe is a tool used to extract ASCII or Unicode
strings from within a file
• Can extract human-readable strings from within files
• Useful when analysing or debugging malware or malicious files, it can help detect hidden information or malicious behaviour inside a file
• The tool can be run from a command prompt or PowerShell by registering it as an environment variable
-n: specify the minimum length of strings to extract, -n 5 to extract only strings longer than 5 characters
-s: allows you to specify the starting position of the string to extract, if set to -s 0x1000 it will extract the string from position 0x1000 of the file
-e: allows you to specify the end of the string to extract, -e set to 0x2000 will only extract strings up to position 0x2000 in the file
-u: extract only Unicode strings
-p: extract strings from running processes
Options
Save the output
• You can use -o to specify the output, but for the purposes of this lesson, we'll use the redirect to save
Introduce the problem01 Introduction to Lab Files
6

## Page 7

01. current page topic
kusti
kusti
Win7SP0x86
Profile
Verifiable information
OS: Windows
Version : 7
Problem 102
7

## Page 8

01. current page topic
command PATH
Result
Run Volatility, specify the file, then specify the profile, enter the plugin to use, and save it under the result_file directory via redirection
You can see that the file was saved successfully
Problem 12 Problem 102
8

## Page 9

01. current page topic
Pslist result
pslist
Abbreviation for Windows Management Instrumentation Provider Service
Providing information about your system
Provides information about your system, such as the operating system, installed
software, currently running processes, and hardware status.
This information can be useful for system administration tasks or troubleshooting
Change system settings
This process gives you the ability to change system settings
Change network settings, start or stop services, and more
WmiPrvSe.exe
Provide information about the script
Enables scripts to provide a standardised way to request
information about the state and data of the Windows
operating system
Problem 12 Problem 102
9

## Page 10

01. current page topic
Windows Search Index Service Components
• Manages and updates the Windows Search Index to speed
up searches when users search for files
• Monitors changes to the file system and reflects them in the
search index to ensure that search results are up-to-date
and fast when users search for files
• Also used to retrieve all files and metadata needed to return
the results of a search query
SearchProtocolhost.exe
Windows Search Index Service Components
• Filters appropriate files based on a user's search query
• Makes search results more accurate, excluding unnecessary files and
showing only the results the user wants
• Retrieves the metadata of files and reflects it in the results of search queries
• Includes information such as file name, extension, creation date,
modification date, etc.
SearchFilterHost
Commonalities
A process that usually runs in the background and works automatically without user intervention
However, you should be suspicious if it's using excessive memory or running in a strange location
Why?
• In this example, all of the files are legitimate and run from legitimate locations, but security personnel should identify the processes that malware
commonly uses or create their own cheat sheet
• It's also important to know the normal processes so that you can identify the abnormal ones, so be sure to look up any process you don't recognise
Problem 12 Problem 102
10

## Page 11

01. current page topic
Timeout.exe
• timeout.exe is a command-line tool provided by the Windows operating system
• It is used to create a pause for a specified amount of time, or to wait for a specific amount of
time to pass
• It is often used in batch files to create delays before certain processes start, wait for certain
tasks to complete, etc.
• When viewing the problem screen, you may notice that it appears to time out periodically
Pslist result
Timeout.exe
• When I checked via Pslist, timeout was executed after the cmd was executed, so I can confirm that this works via cmd
Problem 12 Problem 102
11

## Page 12

01. current page topic
pstree result
pstree
• Pstree shows that cmd.exe is running under explorer.exe
and timeout.exe is running under it
• In fact, if you check through PID and PPID, you can see that
the parent and child processes are well connected
Verify the pstree
explorer
regsvr32 cmd
timeout
Problem 12 Problem 102
12

## Page 13

01. current page topic
psxview
If the results in the pslist are all True
Nothing found in the rest
Hidden process x
Result
Problem 12 Problem 102
13

## Page 14

command
result
pslist
A keyword search for 1348, the PID of Cmd, reveals that Users\Kust\Destop\test.bat is running
Also verify that test.bat is located at C:\Users\kusti\Desktop
Cmd also searches for timeout, and we can see that it takes 5 as an argument using the /t option
This means that we have a wait time of 5 seconds, because we ran test.bat from cmd, and the subprocess of cmd, timeout.exe, was given the
/t option to wait for 5 seconds
Problem 12 Problem 102
14

## Page 15

01. current page topic
command
filescan
reuslt
• If you use the filescan plugin to save the results as filescan.txt
and check that file, you can find the offset as shown in the
capture screen by searching for the keyword test.bat
• These offsets will be used when extracting this file
Problem 12 Problem 102
15

## Page 16

01. current page topic
File dump
command
reuslt
We see that the offset is 0x000000003fcab4e0, so use the -Q option to get this offset and the -D option to set the path to
store it
The path to save is export_file
Dumping Test.bat creates a .dat extension file
Batch script
A script that creates a folder named test in the current location and
saves the results of the tasklist every 5 seconds to a folder named
tasklist.log inside the test folder
Problem 12 Problem 102
16

## Page 17

01. current page topic
volatility_2.6_win64_standalone.exe -f .\win7.vmem --profile=Win7SP0x86 dumpfiles -Q 0x000000003fce8620 -D
.\export_file\
File dump
command
Target
The process for dumping that file is the same as before
Problem 12 Problem 102
17

## Page 18

01. current page topic
File dump
When I checked the list of running processes with volatility, there was no
tasklist.exe, but instead there was timeout.exe, and in this output, a process
called tasklist.exe exists
When the tasklist process was executed, timeout.exe had finished its job and
was terminated, and the process information when tasklist was executed was
in tasklist.log
Tasklist.exe
Problem 12 Problem 102
18

## Page 19

01. current page topic
Problem 203
About the problem
● I was getting base64 decoded messages back and forth over Discord
● The user deleted the message
● Let's dump the Discord Process to see what messages were sent and received
Formatting exists because it was an issue in
the CTF
Format : debugCTF{}
The answer you want
19

## Page 20

01. current page topic
Prepare in advance
For this issue, we will create an export_file directory and a result_file directory as before.
We also need to create a directory to store the results of the Strings, so we create \export_file\str
Problem 203 Problem 2
20

## Page 21

01. current page topic
commands results
Description.
• Check the profile information using imageinfo, which shows that the target OS is Windows and version is 7
• Save results using the pslist, psscan, psxview, filescan, cmdline, and consoles plugins
• The Consoles command displays the commands the user has used in the cmd window
• How long does it take
Problem 203 Problem 2
21

## Page 22

01. current page topic
Verify the PID
Verify the Discord.exe process via the output of the pslist
You can see that there are multiple Discord.exe's running under Discord.exe with a PID of 2380
Discord
2380
Discord
3776
Discord
....
Discord
3576
Discord
2296
Process dump
We don't know which processes and in which memory the results are stored, so we'll start by dumping all Discord processes
Problem 203 Problem 2
22

## Page 23

01. current page topic
Strings.exe
Use strings.exe to extract strings in a .dmp
Problem with extracting only 3776 using strings.exe to save time X
Discord is built using React
React is a library for building user interfaces that uses HTML and CSS, but instead of writing them directly, it uses a syntax
called JSX to create components that have a similar structure to HTML
Why?
There is a possibility that the messages sent and received are written inside a span
What is the message?
Takes a very long time
20 minutes to 2 hours
Caveats
Problem 203 Problem 2
23

## Page 24

01. current page topic
3776str.txt
ZGVidWdDVEZ7dl90aGlzX2lzX2U0NXlfdn0=
Check out 3776.txt, where the strings extracted from 3776.dmp are stored
</span> as a keyword
Base64 estimation
Problem 203 Problem 2
24

## Page 25

01. current page topic
• Convert source data to 8-bit binary data
• Breaks binary data into 6-bit units and fills in the gaps with padding characters
• Converts each 6-bit unit of data into one of the 64 characters defined in a Base64 string,
which consists of 52 upper and lower case alphabets (A-Z, a-z), 10 numbers (0-9), and
the '+' and '/' characters
• Concatenate the converted characters to produce the final Base64 encoded result
How it works
• Base64 is one of the encoding methods for converting binary data to text format.
• Primarily used to securely transfer binary data in text-based systems like email
Base64?
BASE64
 • Approximately 33% longer than the original data
• The = character is followed by padding or consists of 52 upper and lower case alphabets (A-Z, a-z), 10 numbers
(0-9), and '+' and '/’
• Often used to cause cyber security incidents,Among the functions of Powershell, there is a command that
converts to base64, and attackers can use it to enter or execute the system without being detected by antivirus
or blocking programs
Features
Problem 203 Problem 2
25

## Page 26

01. current page topic
Base64 Decoding
PATH
https://emn178.github.io/online-tools/base64_decode.html
debugCTF{v_this_is_e45y_v}
result
Problem 203 Problem 2
26
