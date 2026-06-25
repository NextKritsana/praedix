---
title: "12강_Document files_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\12강_Document files_v1.2.pdf"
source_size_bytes: 1575817
source_modified: 2025-11-12T12:23:43
imported_at: 2026-06-14T14:26:28
tags:
  - acs
  - acs-advanced
  - imported
---

# 12강_Document files_v1.2

- Source: [12강_Document files_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/12%EA%B0%95_Document%20files_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Document file
• What Is a Document File?
• Recent Docs
• Open/Save MRU
• Shortcuts
• Jumplist
12
1

## Page 2

What Is a Document File?01
PDF MS
office Text
IMG
Web
● PPT
● Excel
● Word
● Jpg
● bmp
● Html
● php
● txt
● md
https://www.ired.team/offensive-security/initial-access/phishing-with-ms-office/inject-macros-from-a-remote-dotm-template-docx-with-macros
• File formats that contain a variety of information, typically text, graphics,
tables, charts, and more
• These files are used to create and store documents, and each file type is
defined by a specific application or standard
What is a documentation file?
2

## Page 3

01
https://www.ired.team/offensive-security/initial-access/phishing-with-ms-office/inject-macros-from-a-remote-dotm-template-docx-with-macros
The Let me show you
What we hope to achieve in the short and long run
• Office documents support macro functionality, which can be used to perform malicious
actions
• This attack takes advantage of the fact that the executor is normal software such as MS
Word, Excel, or PowerPoint, which makes it undetectable by signature-based security
products
• Macros allow users to reduce repetition and provide convenience, such as pasting forms
• However, when used maliciously, for example by inserting a macro command such as Sub
Auto_open, macros can be used to execute malware hidden in a document file
• In the case of Word, there was a malware that used the DDE vulnerability
MS Office
pptx
docx
excel
MS OFFICE PDF • Malware using PDFs can inject JavaScript into the document file, which can then execute the
malware when the document file is executed
• Other techniques such as hyperlinks and attaching malicious attachments are used to execute
malicious behavior
• Infostealer-type malware uses PDF's Attachment feature to attach malicious attachments
• The attacker attaches an Excel attachment in the form of xlsx to make the victim open the
PDF, and when the Excel file is executed, it connects to the external network using the
eqnedt32.exe vulnerability and downloads and executes additional malware
PDF
MS PDF
What Is a Document File?
3

## Page 4

문서파일이란01
https://www.ired.team/offensive-security/initial-access/phishing-with-ms-office/inject-macros-from-a-remote-dotm-template-docx-with-macros
The Let me show you
What we hope to achieve in the short and long run
• Although rare, there is also malware associated with image files
• In 2004, a vulnerability in Microsoft's GDI+GdiPlus.dll library was exploited through a
vulnerability in GDI+'s image processing method, which caused an overflow
• In addition to this, there is malware in the form of a Trojan horse called RockyBot, which
uses PNG files to distribute malware
• There was malicious code behind the PNG file, and there is a possibility that the malicious
code can be executed depending on the APP that outputs the image file to the screen
Image File
png
jpg
bmp
Image File
php
html
Web File • For PHP, commonly used to upload webshells
• A webshell is a malicious PHP script that runs on a web server, providing an
environment for an attacker to access and control a web application
• They are installed by exploiting server vulnerabilities and have the ability to
manipulate the file system, execute commands, and more
• HTML is also a technique that inserts malicious JavaScript code within an HTML
document to run in the user's browser
• Can hijack a user's cookies, sessions, etc. or perform a variety of malicious behaviors
Web File
What Is a Document File?
4

## Page 5

문서파일이란01
Camouflage Files
Document Files Containing Malware
Unmarked extensions
Document file caveats
Check View-Show-FileNameExtension and Hidden Items in File Explorer
folder option - uncheck Hide protected operating system files from View and uncheck show hidden files, folders or drives
Once you've done that, you'll be able to view folders and files that the system has hidden because it doesn't think you'll ever use them
Prepare in advance
What Is a Document File?
5

## Page 6

문서파일이란01
Chaos with white space
A simple technique
If you look at the captured image at the top, it says normal.txt, but if you expand the Name field to the side, you can see the actual extension
In the above case, it's easy to recognize it because of the icon, but malware that has a unique icon is usually hard to tell,and some tools can
change the icon
Explanation
What Is a Document File?
6

## Page 7

RecentDocs02
Recent Docs
A feature in the Windows operating system that keeps track of a user's recently used documents and files
Affects the list of files viewable in the "Recent Documents" or "Recent Files" sections of the Start menu
Organizes a list of files or documents that a user has recently opened or edited, allowing users to quickly
access those files
Recent Tab
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecntDocs
%appdata%\Microsoft\Windows\Recent
PATH
RecentDocs can be analyzed to determine a user's recent activity history, especially to find files or documents
associated with malicious activity
Incident Response Perspective
7

## Page 8

RecentDocs02
Decimal format
Registry PATH
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
Analyzing the registry, we see that there are entries
under RecentDocs with different extensions
Various extensions
In the .pptx, you can see the numbers written in decimal
and the value MRUListEx at the bottom of the page
In pptx
8

## Page 9

IMG
MRU
Most Recently Used
A list of the item's most recent uses
Recorded in hexadecimal when recorded here
i n f o
IMG
RecentDocs02
Notice that the value with a value of 18 in decimal has a name that starts with
chap2_3_3_1
Analyzing 0x12
9

## Page 10

OpenSave MRU03
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU
OpenSaveMRU
Traces of Files Opened or Saved
Through Windows Dialog Boxes
Saves information about files
opened or saved through Web
Browsers and Applications
Registry PATH
10

## Page 11

L n k  f i l e
• Short cut file
• Provides quick
• Access to linked file
IMG
 IMG
 IMG
Recent Folder MS Office
Recent Quick Launch
OpenSave MRU03
Shortcut files provide easy access to frequently used
items for many users, and can be easily modified via
properties if the destination changes location
Features
C:\Users\Default\AppData\Roaming\
Microsoft\Windows\Recent
%AppData%\Microsoft\Office\Recent %AppData%\Microsoft\Internet Explorer\
Quick Launch
Lnk Check
11

## Page 12

Shortcuts04
Check the .lnk structure
Tips
When dragging a shortcut file to HxD, the hex code of the short cut file is not visible and the hex value of the original file is loaded
Shortcut file must be opened via 'open' in HxD
HxD
12

## Page 13

Shortcuts04
4C 00 00 00 01 14 02 00 00 00 00 00 C0 00 00 00
00 00 00 46 9B 00 08 00 20 00 00 00 AC 14 B1 8C
5B 3B DA 01 60 23 F0 F5 E2 3C DA 01 36 08 BB 8C
5B 3B DA 01 1A FA 01 00 00 00 00 00 01 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 ACS
.lnk Structure
Value by color
Header Size : 4C 00 00 00 Fixed
LinkCLSID : Pinning a class identifier
LinkFlags : Various flags in the target
File Attributes : File attribute information
Creation Time : Link target creation time
Access Time : Link target access time
Write time : Link target write time
File Size : Link target size
13

## Page 14

T i m e  V a l u e  C a l c
Name Value Name Value
C Time 01DA3B5B8CB114AC W Time 01DA3B5B8CBB0836
A Time 01DA3CE2F5F02360 File Size 01FA1A
Shortcuts04
2024-01-05 13:13:09 (+ UTC 9) 2024-01-05 13:13:09 (+ UTC 9) 2024-01-05 13:13:09
 (+ UTC 9)
Analyze
14

## Page 15

jumplist05
Jumplist
A feature provided by the Microsoft Windows operating system that allows users to quickly access recently used items when starting a particular program or opening a file
This feature is usually provided on the taskbar or the icon for that program on the Start menu
• Artifacts, new in Windows 7
• Group by application
• Link files that manage documents or programs that users frequently use or have recently used
• Because they are only deleted by the user's deletion actions, information about file or program usage can be obtained unless they are
deleted intentionally
• If traces of deletion are found, suspect attacker intent in the incident
Features
• C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestination
• C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Recent\CustomDestination
PATH
15

## Page 16

jumplist05
Example
• Pinned
• Recent Folder
• Recent File
Display information
Explanation
The information in the red box is present in the jumplist
16

## Page 17

jumplist05
AutomaticDestinations
Configure a Jump List that appears when you
right-click the corresponding program icon
on the taskbar, or when you right-click the
corresponding program on the Start menu
Track usage patterns to identify frequently
used files, folders, and task history and
display them in a Jump List so that users can
quickly perform specific tasks from that list
CustomDestinations
Custom-Destination files consist of a file header, a
set of linked file entries, a file footer, and
sometimes additional data
The exact structure is still unknown
As far as we know, there is a 32-byte header, a
link file entry
The file's footer signature is 0xbabffbab
17

## Page 18

jumplist05
Specify the number of Jumplists
Registry PATH
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
• Create with Dword Type
• Adjustable number of items displayed in Recent Items
What if there are no Jumplist items?
18

## Page 19

jumplist05
D00655D2AA12FF6D
Microsoft PowerPoint 2016 64-bit
https://github.com/EricZimmerman/JumpList/blob/master/JumpList/Resources/AppIDs.txt
Name AppID
Ppt 2016 D00655D2AA12FF6D
Word 2016 FB3B0DBFEE58FAC8
Chrome
5D696D521DE238C3
D249D9DDD424B688
6da48f37c95d6e1
powershell ea64ce14e5470c33
Dropbox 7B7F65AAECA20A8C
19

## Page 20

jumplist05
https://www.nirsoft.net/utils/jump_lists_view.html
Jumplist View
• It automatically imports jumplists stored on your PC and analyzes the structure to display the file
name, full path, record time, created time, modified time, and accessed time
• You can open and analyze externally imported jumplist by pressing advanced option in options
Download PATH
20

## Page 21

jumplist05
Jumplist Explorer
• A tool that analyzes and interprets the structure of Jumplists in the Microsoft Windows operating system and presents it
visually to the user
• Jumplist Explorer provides more detail and visibility into the internal structure and information of these jumblists
• Better visibility than Jumplist View
• Shows the number of link files associated with the AppID
of each Jumplist item
• See how much a particular application has been utilized
through the Jumplist
• Shows creation time, modification time, and access time,
along with time values
Useful features
https://www.sans.org/tools/jumplist-explorer/
Download PATH
21
