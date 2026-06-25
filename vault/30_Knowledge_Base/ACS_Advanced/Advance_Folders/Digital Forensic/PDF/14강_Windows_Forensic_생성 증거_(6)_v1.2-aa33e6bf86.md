---
title: "14강_Windows_Forensic_생성 증거_(6)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\14강_Windows_Forensic_생성 증거_(6)_v1.2.pdf"
source_size_bytes: 656098
source_modified: 2025-10-11T21:46:27
imported_at: 2026-06-14T14:25:05
tags:
  - acs
  - acs-advanced
  - imported
---

# 14강_Windows_Forensic_생성 증거_(6)_v1.2

- Source: [14강_Windows_Forensic_생성 증거_(6)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/14%EA%B0%95_Windows_Forensic_%EC%83%9D%EC%84%B1%20%EC%A6%9D%EA%B1%B0_%286%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Windows Forensic -
Generating Evidence (6)
• What is a link file
• Structure of link files
• Link File Analysis Tool
• Analyzing link files
• Limitations of link file analysis
14
1

## Page 2

What is a link file01
They may seem relatively insignificant in the world of digital forensics, We'll explore how these
little icons you see on your desktop or in your documents folder can be a treasure trove of
valuable information for criminal investigations, security breach investigations, and even day-to-
day system monitoring. By learning how to decipher the story behind each link file, you can
further enhance your skills as a digital forensics professional.
2

## Page 3

What is a link file01
Link File 01
03
02
04
History
 Shortcut file format in Microsoft
Windows; first introduced with
Windows 95.
Purpose
 By creating shortcuts to frequently used
programs, files, or directories, users can
access those resources more quickly and
easily.
Concepts and Definitions
 A shortcut file that contains a reference to a
specific file, directory, or network resource.
Pros: Quick accessibility and convenience.
Users can easily access the resources
they need via an lnk file without having
to go out and find them.
Cons: Security concerns. Can hide malicious
code or be used to track user activity
3

## Page 4

What is a link file01
Link File 01
03
02
Necessity
 In the modern computer environment, especially
when dealing with large amounts of data, it is very
important to be able to quickly find and access the
desired resource.
A Digital Forensics Perspective
 This is because it contains information about what files the user
opened and when, what programs they ran and when, and so on.
Processes used
 Contains reference information about the
original resource. When this file is executed, the
operating system reads this reference information
to load or run the resource.
Track user activity: LNK files contain information such as what files the user opened, what programs they ran, and
more. This allows digital forensics experts to track user activity and spot suspicious behavior.
File deletion tracking: When a user deletes a file, an LNK file may still exist for that file. This allows digital forensics
experts to obtain information about the deleted file.
Tracking network activity: LNK files also contain references to network resources. This can help digital forensics
experts track which network resources a user accessed.
Analyzing malicious code: Malware often uses LNK files to infiltrate a system or operate within a system. Digital
forensics experts can analyze these LNK files to understand the behavior of the malware and find out how it got in.
4

## Page 5

Structure of link files02
Link File
Open Chrome
Through 010editor
Chrome LNK FIle Chrome EXE FIle
Chrome.exe
Type: Executable File (Executable File)
Purpose: The main executable file for the Google Chrome web browser;
when run, it starts the Google Chrome browser.
Structure: A file in the .exe format contains compiled binary code. It
contains instructions and data that can be executed directly by the
operating system. On Windows, they follow the Portable Executable (PE)
format.
When analyzing: You can use a binary analysis tool or decompiler to
examine the code and resources inside the file. This allows you to see the
structure of the program, programming techniques used, external library
calls, and more.
Chrome.lnk
Type: Shortcut
fileStructure: A .lnk file has a structure that defines a shortcut in Windows
and includes various attribute information needed to run it, such as the
target path, startup folder, window state, icon location, and more. The
internal structure of the file is in a complex binary format and follows the
specifications of the LNK file format.
When analyzing: Tools are available to review the properties and settings of
shortcut files to determine what the file points to, additional parameters,
icon information, and more. In the security field, .lnk files are sometimes
analyzed to detect security threats because they can be used as a delivery
mechanism for malicious code.
5

## Page 6

Structure of link files02
.lnk Structure
ShellLinkHeader
LinkTargetIDList
LinkInfo
StringsData
ExtraData
ShellLinkHeader: Contains basic information about the link file. This
section is required and stores information such as the size of the link file,
creation time, and characteristics of the target file.
LinkTargetIDList: Optionally included, contains details of the link target.
Only present when the HasLinkTargetIDList flag of the ShellLinkHeader is
set. Contains information such as the full path, file system location,
network location, etc. of the link target.
LinkInfo: Optionally included, providing location information for the link
target. Only present when the HasLinkInfo flag of the ShellLinkHeader is
set. Includes the link target's relative path, volume information, network
share information, etc.
StringData: Contains string information about the link target. Exists
only when various flags in the ShellLinkHeader are set. String information
such as the name, working directory, description, and relative path of the
target file.
ExtraData: Optionally includes screen display information, string code
page information, environment variable information, etc.
6

## Page 7

Structure of link files02
ShellLinkHeader
HeaderSize LinkCLSID
LinkFlags FileAttributes CreationTime
AccessTime WirteTime
FileSize IconIndex ShowCommand
HotKey Reserved1 Reserved2 Reserved3
HeaderSize - the size of the header, always fixed to a value of
0x0000004C
LinkCLSID - the class identifier Class Identifier, always 00021401 - 0000 -
0000 – 0000000000046
LinkFlags - Flag values for various information about the link target.
The LinkFlags field contains a number of bit flags that reference specific
parts of the ShellLinkHeader. Among these, the HasLinkTargetIDList flag
indicates whether the LinkTargetIDList structure is included in the .lnk file.
The HasLinkTargetIDList flag is located in the least significant bit of
LinkFlags, and when this flag is set to 1, it means that the LinkTargetIDList
structure is included in the .lnk file. The reverse is true, that is, if this flag is
set to 0, it means that the LinkTargetIDList structure is not included in the
.lnk.
The HasLinkInfo flag indicates whether the LinkInfo structure is included
in the .lnk file.
The HasLinkInfo flag is positioned in the second bit of LinkFlags if the flag
is set to 1. The reverse is true, that is, if this flag is set to 0, it means that
the LinkInfo structure is contained in the .lnk file.
FileAttributes - attribute information for the file in the link target.
7

## Page 8

Structure of link files02
ShellLinkHeader
HeaderSize LinkCLSID
LinkFlags FileAttributes CreationTime
AccessTime WirteTime
FileSize IconIndex ShowCommand
HotKey Reserved1 Reserved2 Reserved3
CreationTime - Creation time of the link target
AccessTime - Access time of the link target
WriteTime- Write time of the link target
FileSize - The size of the link target
IconIndex - Icon Index
ShowCommand - the application's mode of behavior when the link is executed

0x1 SW_NORMAL
0x2 SW_SHOWMINIMIZED
0x3 SW_SHOWMAXM
HotKey - Information about Hotkeys.
A field that specifies a hotkey to use when running a shortcut file (.lnk file).
The Hotkey field consists of two bytes, which represents a keyboard shortcut
combination.
For example, if you set "Ctrl + A" as the hotkey, the
the shortcut file will run when the 'Ctrl + A' key is pressed.
This Hotkey field allows users to set keyboard shortcuts for frequently used
programs or files, making faster and easier to access those resources.
Reserved1,2,3 Reserved zones
8

## Page 9

LinkTargetIDList
Structure of link files02
LinkTargetIDLIST
LinkTargetIDList is an important structure used to
identify the location and related information of a link
target within a .lnk file, a Windows shortcut file.
Contains a list of identifiers (IDList) for the link target,
included only when the HasLinkTargetIDList flag of the
ShellLinkHeader is set.
HasLinkTargetIDList flag
The LinkFlags field in the .lnk file has several flags, and
HasLinkTargetIDList is one of them. It is located in the
least significant bit of the LinkFlags field, and when this
bit is set to 1, it indicates that a LinkTargetIDList
structure exists in the file.
9

## Page 10

LinkTargetIDList
Structure of link files02
IDList Size
The first part of the LinkTargetIDList contains an IDList Size field,
which indicates the size in bytes of the IDList that follows it. This
size information is needed to properly parse the IDList.
IDList
The set of items that actually contain reference information
about the link target. Consists of multiple ItemIDs, each ItemID
divided into two parts.
ItemID Size: The size of each ItemID in bytes, indicating the
length of the ItemID data.
ItemID: Contains actual item identifier data, representing
the target file, folder, network resource, etc.
Each ItemID can contain information such as the location,
name, and icon of the target, and each ItemID can be of
different sizes.
10

## Page 11

LinkTargetIDList
Structure of link files02
How it works
When a user clicks a shortcut, Windows uses the
LinkTargetIDList to determine the location of the target.
The actual path to the target is constructed by sequentially
interpreting the ItemIDs in the IDList.
This process makes the actual object pointed to by the shortcut
accessible within the file system.
A Digital Forensics Perspective
The LinkTargetIDList plays a key role in providing the specific
location and information about the target the shortcut file is
pointing to.
Digital forensics or security analysis can use this information to
track and analyze a user's activity or the context in which a
shortcut was created.
11

## Page 12

Structure of link files02
LinkInfo
LinkInfo
The LinkInfo structure is used to store the physical
location information of the shortcut target,
inkTargetIDList to provide important information
needed to locate the link target.
Describes the file system location of the
destination to which the shortcut points.
Include references to local and network file
systems.
12

## Page 13

Structure of link files02
LinkInfo
Key elements of a LinkInfo structure
LinkInfo Size: Indicates the overall size of the LinkInfo structure in
bytes. This is used to identify the end of the LinkInfo structure.
LinkInfo Header Size: Indicates the size of the header part of the
LinkInfo.
The header provides the information needed to interpret the rest
of the LinkInfo structure.
LinkInfo Flags: Contains flags for LinkInfo,
This indicates information such as whether the LinkInfo contains a
local path, network path, or both.
VolumeID, LocalBasePath: Contains information about the link
target on the local file system.
link target on the local file system
VolumeID provides information about the volume in which the link
target is located, and LocalBasePath provides the absolute path to
the target within that volume.
CommonNetworkRelativeLink: Contains information about the
link to a network resource.
Indicates the name of a network share, network path, etc.
CommonPathSuffix: For both local and network paths.
common to both local and network paths. 13

## Page 14

Structure of link files02
LinkInfo
How it works
The LinkInfo structure is used when a shortcut points to a local file system or
network location to accurately represent that information. When a user clicks
a shortcut, Windows uses the information stored in LinkInfo to determine the
physical location of the target and access it.
For links to local file systems, the VolumeID and LocalBasePath are used to
access the target file or folder. For network resources, the
CommonNetworkRelativeLink information is used to interpret the network
path and make the connection.
Importance
LinkInfo provides essential information to pinpoint the location of the
destination pointed to by a .lnk file. Create quick access for users to various
resources inside and outside the system.
In digital forensics and security analysis, LinkInfo provides critical information
that can be used to track user activity, analyze file access patterns, detect the
activity of malicious software, and more.
Understanding the LinkInfo structure of .lnk files is important for
understanding how shortcut files work and how to identify target locations,
helps you understand the file system and how it accesses network resources.
14

## Page 15

Structure of link files02
StringsData
StringData
The StringData section is an important part that provides
additional string information related to the shortcut target.
It contains information necessary for the functionality and
user interface of the shortcut, and is only included when
certain flags in the ShellLinkHeader are set.
Key elements of the StringData structure
• CountCharacters: Located at the beginning of each string
data block, indicating the length of the string that
immediately follows, in characters; this value does not
include a null termination character.
• String: The actual Unicode string with the length specified
by CountCharactersThis string provides a variety of
information about what the .lnk file points to
15

## Page 16

Structure of link files02
StringsData
Information that StringData can contain
NameString (the name of the link target): The name of the link as seen
by the user, typically the name of the target file or folder.
RelativePath: Relative file path to shortcut target.
Describes the path from where the shortcut file is located to the target.
WorkingDir (working directory): The path to the default working
directory used when running through a shortcut. Used to set the
required working environment when running a program or script.
IconLocation: Indicates the file path of the icon used for the shortcut,
and the index of the icon within that file. Users can set a custom icon
for visual identification of the shortcut.
Importance and uses
The StringData section enhances the scope and detail of information
that the .lnk file provides to the user, and plays an important role in
improving the user experience.
For example, NameString helps the user identify the shortcut,
WorkingDir is essential for setting up the environment for the program
to run correctly, and IconLocation enhances the visual elements of the
user interface, making the shortcut easier to recognize.
The StringData section of the .lnk file allows developers and users to
provide and receive richer and more useful information through
shortcuts, which contributes to better file management and accessibility
for users.
16

## Page 17

Structure of link files02
ExtraData
ExtraData
The ExtraData structure is used to store additional details in the shortcut
file, This extends the functionality of .lnk files and enriches the user
experience.
ExtraData is optionally included, which can contain various blocks of data.
Each block of data provides information about a specific aspect of the
shortcut or usage experience.
The structure of each data block
BlockSize: A field that represents the overall size of the data block.
This size includes all parts of the data block.
This represents the total size in bytes, including headers and data.
BlockSignature: A unique signature that identifies the type of data block.
This signature is used to distinguish the type of each data block.
BlockData: The section that contains the actual data,
data is stored according to the format defined in BlockSignature.
17

## Page 18

Structure of link files02
ExtraData
Different types of data blocks that can be included in the ExtraData section
ConsoleDataBlock: Stores settings information for the console window (command
prompt), including window size, buffer size, text and background colors, etc.
ConsoleFEDataBlock: Include font information for the console window, especially
for East Asian languages.
DarwinDataBlock: Contains the identifier of the application installed through
Windows Installer, which is used to reference information in the MSI package.
EnvironmentVariableDataBlock: Include information about environment variables
that can be referenced when the shortcut is run.
IconEnvironmentDataBlock: Contains icon location information for the shortcut,
and stores the path and index to the icon file.
KnownFolderDataBlock: The user's known folders. (e.g., documents, images,
downloads folder, etc.
PropertyStoreDataBlock: Contains property information about the file, which can
be used to store metadata or custom properties.
ShimDataBlock: Contains application compatibility layer (Shims) settings
information, which is used to apply specific options to resolve compatibility issues.
SpecialFolderDataBlock: Contains the ID of the special folder, which indicates the
location of the specific system folder to which the shortcut points.
TrackerDataBlock: Includes distributed link tracking information for the link target,
which is used to find the correct file even when the file the shortcut points to has
been moved or renamed.
VistaAndAboveIDListDataBlock: Contains IDLists used by Windows Vista and later
operating systems. This is done by saving the IDList of targets pointed to by the
shortcut for use on newer operating systems.
18

## Page 19

Structure of link files02
Source: [MS-SHLLINK]: Shell Link (.LNK) Binary File Format | Microsoft Learn
19

## Page 20

Link File Analysis Tool03
Made by Eric Zimmerman
Https://github.com/EricZimmerman/LECmd
.\LECmd.exe -f "path to lnk file
-csv "Where you want to save the [CSV file]"
LECmd
Launch Screen
20

## Page 21

Link File Analysis Tool03
Launch
Screen
SourceFile: This represents the full path to the LNK file being analyzed.
It indicates exactly where the LNK file is located, so you know where the file originally
came from
SourceCreated: Indicates the date and time the LNK file was created.
This information tells us when the file was first created, which can be correlated to
specific activities of the user or events
SourceModified: Indicates the date and time the LNK file was last modified.
This information tells you the last time a file's properties or contents were changed.
This helps you know the file's update status
SourceAccessed: Indicates the date and time that the LNK file was last accessed.
This tells you the last time you opened a file, viewed its properties, etc.
This can help you understand the usage patterns of your files.
TargetCreated: Indicates the date and time the target file pointed to by the LNK file
was created.
This information tells us when the target file was first created, which helps us
understand the creation history of the target file
TargetModified: Indicates the date and time that the target file pointed to by the LNK
file was last modified.
This information tells you the last time a property or content of the target file was
changed.
This helps you understand the update status of the target file.
TargetAccessed: Indicates the date and time the target file pointed to by the LNK file
was last accessed.
This tells you the last time a target file was opened or a property of the target file was
viewed, and helps you understand the usage patterns of the target file
CSV file created with LECmd
21

## Page 22

Link File Analysis Tool03
Launch
Screen
FileSize: Indicates the size of the target file pointed to by the LNK file, in bytes
This information will tell you the size of the target file, which can be found at
 This will help you figure out how large the file is
RelativePath: This indicates the relative path to the target file that the LNK file points to.
The relative path indicates the location of the target file relative to the location of the LNK file,
which helps you determine the location of the target file.
WorkingDirectory: Indicates the working directory of the target file that the LNK file points to.
Working directory means the default directory where the program looks for files while running
FileAttributes: Represents the file attributes of the target file pointed to by the LNK file.
File properties include read-only, hidden, system, archive, etc.
HeaderFlags: this indicates the header flags of the LNK file
Header flags are bit fields that represent various settings and states of the LNK file.
DriveType: Indicates the type of drive the target file pointed to by the LNK file is located on
Drive types can include hard disks, network drives, CD-ROM drives, etc.
VolumeSerialNumber: Indicates the serial number of the volume on which the target file
pointed to by the LNK file is located. serial number of the volume where the target file is
located.
The volume serial number is a unique number used to identify the file system.
VolumeLabel: Indicates the label of the volume where the target file pointed to by the LNK is
located.
A volume label is a text label that describes the volume.
CSV file created with LECmd
22

## Page 23

Link File Analysis Tool03
CSV file created with LECmd
Launch
Screen
LocalPath: This indicates the local path to the target file that the LNK file points to.
Local path indicates the location of the target file within the local file system
NetworkPath: This indicates the network path of the target file that the LNK file points to.
Network path is the path used to access the target file over the network
CommonPath: This indicates the common path to the target file that the LNK file points to.
A common path indicates the portion of the target file's path that is common to the path of
the LNK file.
This helps to determine the relative location of the LNK file and the target file
Arguments: These are the arguments used when executing the target file pointed to by the
LNK file.
This argument is additional information that is passed when the program is run,
 used to control the behavior of the program.
TargetIDAbsolitePath: Indicates the absolute path of the target file that the LNK file points to.
An absolute path is the full path to the file, starting from the root directory.
TargetMFTEntryNumber: Indicates the Master File Table (MFT) entry number of the target file
pointed to by the LNK file.
MFT Entry Number: A unique number used to identify a file within the file system.
TargetMFTSequenceNumber: This represents the MFT entry sequence number of the target
file pointed to by the LNK file.
The MFT entry sequence number is a number that increments each time the MFT entry is
reused.
23

## Page 24

Link File Analysis Tool03
CSV file created with LECmd
Launch
Screen
MachineID: This indicates the ID of the machine that created the LNK file
A device ID is a unique identifier used to identify a computer.
MachineMACAddress: This indicates the MAC address of the device that created the LNK file.
A MAC address is a unique address used to identify a network interface.
MACVendor: This indicates the MAC address vendor of the device that created the LNK file.
The MAC address vendor is identified by the first six digits of the MAC address,
 indicating the company that manufactured the network interface card.
TrackerCreatedOn: This indicates the date the tracker in the LNK file was created.
Trackers are information used to track the change history of a file.
ExtraBlocksPresent: This is information about the extra blocks of data included in the LNK file.
Additional data blocks Used to store additional information beyond the basic information in
the LNK file.
This information includes the environment in which the LNK file was created, network
information, and more.
24

## Page 25

TEXT ADD
Smooth like butter Like a criminal undercover Gon' pop like trouble Breakin' into your heart Breakin' into your heart like that
TEXT ADD
Smooth like butter Like a criminal undercover Gon' pop like trouble Breakin' into your heart Breakin' into your heart like that
Analyzing link files04
Fisrt analyzed the Chrome.lnk file, which is contained in a folder named SJM on the desktop on my PC's C drive.
SourceFile is literally the file that was used as a source, showing that the analysis targeted the Chrome.lnk file in the SJM folder on my PC's desktop as mentioned above.
The creation time is correct because we copied the Chrome.lnk file that was previously on the desktop and put it in the SJM folder for analysis. The time reference is UTC +00
Time Accessed Time the target was created - the creation time of the Chrome.exe file Time the target was modified - the modification time of the Chrome.exe file Time the target was accessed - the access time to the
Chrome.exe file
RelativePath Shows the path to chrome.exe, which exists within the Google Chrome Application folder in Program Files, as a relative path to the target file
WorkingDirectory Shows the target's working directory
LocalPath Shows the path to the target of the Lnk file
What you can learn by analyzing a Link file
25

## Page 26

Analyzing link files04
TargetIDAbsolutePath Absolute path to Chrome.exe
Machine ID and MAC address information
It also tells you when the tracker was created, so you know when changes were made
to the file.
Serial information for the volume
File properties
Checking the machine ID of my PC (it matches)
What you can learn by analyzing Link files
26
Device specifications
Device Name

## Page 27

Limitations of link file analysis05
If you delete the putty.exe file
From normally
To completely delete
the putty.exe file
Experiment with deleting link files
.lnk File
Target
Create a shortcut
Delete target generic
Delete a
target completely
Compare results
That an LNK file is simply a "link" to the target file, and does not contain the actual
contents of the file.
Purpose of the experiment
27
