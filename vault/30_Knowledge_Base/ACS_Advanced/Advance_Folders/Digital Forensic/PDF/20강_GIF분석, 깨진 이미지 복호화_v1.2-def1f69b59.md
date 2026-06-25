---
title: "20강_GIF분석, 깨진 이미지 복호화_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\20강_GIF분석, 깨진 이미지 복호화_v1.2.pdf"
source_size_bytes: 502034
source_modified: 2025-10-18T19:43:16
imported_at: 2026-06-14T14:25:11
tags:
  - acs
  - acs-advanced
  - imported
---

# 20강_GIF분석, 깨진 이미지 복호화_v1.2

- Source: [20강_GIF분석, 깨진 이미지 복호화_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/20%EA%B0%95_GIF%EB%B6%84%EC%84%9D%2C%20%EA%B9%A8%EC%A7%84%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EB%B3%B5%ED%98%B8%ED%99%94_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Analyze GIFs, decrypt
broken images
•Analyzing GIFs
•Decrypting broken images
20
1

## Page 2

2
01. current page topic
Analyzing GIFs01
GIF
Graphics Interchange Format
Image formats are designed to exchange graphical data
Originally developed by CompuServe in 1987
To provide a standardized way to easily share and transfer
image files between different computer systems.

## Page 3

3
01. current page topic
What is a GIF01
GIF is an 8-bit color format that
supports up to 256 colors
Support for 256 colors
Losslessly compress image data
using Lempel-Ziv-Welch (LZW)
algorithm
Lossless compression
Provides the ability to create
simple animations that include
multiple frames
Animation support Simple graphic conformance
Better for simple graphics, web
art, icons, etc. than high-
resolution photos
G
Analyzing GIFs

## Page 4

4
01. current page topic
GIF Structure01
Signature and Version
Signature: A signature that begins with the three letters "GIF“ indicates
that the file is in GIF format. The signature is immediately followed by a
string indicating the version of the GIF format. Typical versions include
"87a" and "89a"."87a" is the initial version, while "89a" is an enhanced
version that supports additional features such as transparency,
animation, and interlacing.
Logical Screen Descriptor
Setting the overall organization of your image.
Logical screen width and height: Define the size of a GIF image in pixels.
The presence and size of the color table: Indicates whether a global color
table is used and, if so, its size.
Background color index: Set the default background color to of the
global color table.
Percentage of pixels: Defines the pixel aspect ratio of the image. This
value is used primarily for compatibility with older software.
GIF Structure
GIF HEADER
logicalscreendescriptor
globalcolortable
IMAGE DATA
TRAILER
Analyzing GIFs

## Page 5

5
01. current page topic
GIF Structure01
GIF Structure
GIF HEADER
logicalscreendescriptor
globalcolortable
IMAGE DATA
TRAILER
Global Color Table
If the GIF file uses a global color table, it is located immediately after the
Logical Screen Descriptor. This table defines up to 256 colors used
throughout the image. Each color is represented by three bytes and has
an RGB (Red, Green, Blue) value.GIF files can have various segments
(e.g., image blocks, animation control blocks, etc.) after this header
information, which are used to include complex animations or various
metadata. In the "89a" version, they may also contain extension blocks
that control additional functionality. This structure gives GIFs the
flexibility to represent dynamic animations as well as simple static images.
Image Data
The part where the actual image information is stored, compressed using
the Lempel-Ziv-Welch (LZW) compression algorithm.
Terminator (Trailer)
Indicates the end of the file, expressed as "3B" (hexadecimal)
Analyzing GIFs

## Page 6

6
01. current page topic
GIF Structure01
GIF Structure
GIF HEADER
logicalscreendescriptor
globalcolortable
IMAGE DESCRIPTOR
local color table
IMAGE DATA
TRAILER
Image Descriptor
An image descriptor is a block that contains information such as the position, size,
and whether a local color table is used for individual frames. The image descriptor
appears at the beginning of each frame.
Position of the frame Indicates the coordinates where the frame is located within the
image, which determines where the frame will appear in the overall image.
Size of the frame: Defines the width and height of the frame in pixels.
Use local color table or not: This flag indicates whether the frame uses its own local
color table. Local color tables allow you to specify different color palettes for different
frames.
Local Color Table
A local color table is a color table that is specific to a particular frame and is used only
in that frame. It can be used in place of the global color table, or it can exist to
complement the global color table. Local color tables are characterized by the
following
• Independent color management: Each frame can have a different color palette
than the global color table, allowing for different color representations within the
animation.
• This allows for a wide range of color representations within the animation.
Per-frame optimization: By using local color tables, you can optimize image quality by
selecting the most efficient color palette on a frame-by-frame basis. Image descriptors
and local color tables ensure the independence of each frame in a GIF animation, and
are essential components for implementing complex animation effects.These features
have helped the GIF format become the standard way to present simple animations
on the web.
Analyzing GIFs

## Page 7

7
01. current page topic
GIF Structure01
LZW
Lempel-Ziv-Welch
A method of data compression developed by Terry Welch in 1984.
A variant of the Lempel-Ziv compression method that provides lossless
compression and is particularly efficient for compressing string data.
The LZW algorithm is widely used in GIF, TIFF, and PDF file formats,
among others.It works by registering recurring data patterns in a
dictionary, then compresses the data by replacing the same pattern with
the code stored in the dictionary whenever it appears.code.
Analyzing GIFs

## Page 8

8
01. current page topic
GIF Structure01
LZW Algorithm Example behavior
Example: "ABABABAB"
1. initialize the dictionary Initialize the dictionary for every single possible character before starting compression
For example, if the alphabets 'A' and 'B' are each registered in the dictionary
Dictionary: {A:1, B:2}
2. Process the input stream
Enter: "ABABABAB"
Processing:
'A' is in the dictionary, so check for the next character -> type "AB"
Since 'AB' is not in the dictionary, output code '1' for 'A',
 add 'AB' to the dictionary (new code: 3) -> output: 1, dictionary: {A:1, B:2, AB:3}
The next input is "BABAB", 'B' is in the dictionary, so check for the next character -> input "BA"
Since 'BA' is not in the dictionary, output code '2' for 'B', and add 'BA' to the dictionary
 (new code: 4) -> output: 1,2, dictionary: {A:1, B:2, AB:3, BA:4}
Repeat the process, processing 'AB', 'BA', 'AB', 'B', and outputting the code found in the dictionary
3. final output
Through processing, the input "ABABABAB" is compressed into the code "1,2,3,4,3,2".
In the LZW algorithm, the output code is stored in binary form to achieve more efficient compression.
Analyzing GIFs

## Page 9

9
01. current page topic
Attributes JPEG JPG GIF
Compression
methods Lossy compression Lossless compression Lossless compression
Color support 24-bit color
(approximately 16 million colors)
24-bit color + 8-bit alpha channel
(transparency) 8-bit color (up to 256 colors)
Alpha Channel
(Transparency) None Support Only supports single color transparency
Animation
support None Support via APNG extension
(not supported by all viewers) Support
Use cases Save high-quality photos and images High-quality image storage and web
graphics
Simple graphics, icons, and animated
web graphics
File size Generally small due to high compression relatively large due to lossless
compression Small with limited colors
Key Pros High compression ratio for efficient
storage of high-quality photos
Support for high quality images and
transparency
Support for simple animations and
transparency
Major Cons Quality loss may occur File sizes can be large Limited number of colors, outdated
formats
Analyzing GIFs01

## Page 10

10
01. current page topic
APNGWebP
An unofficial extension of PNG that supports full-color
images and transparency via the alpha channel, provides
the ability for multi-frame animations.
APNG allows for more colors and better transparency
handling than GIF, but can result in larger file sizes.
An image format developed by Google that supports
both lossless and lossy compression.
WebP is particularly compression-efficient and can
save images of the same quality as JPEGs.
It can also produce lossless images with a file size
that is 25% to 34% smaller than the same quality as
PNG (26% smaller) and supports transparency and
animation via the alpha channel.
GIF alternative formats
While the GIF format has long been popular for its ability to support simple animations and transparency,
Has a limited color palette of 256 colors and often inefficient file sizes
Analyzing GIFs01

## Page 11

11
01. current page topic
Decrypting broken images02
02 04
03
0501
Software errors
If the software that creates, edits, or saves
image files is buggy or malfunctioning, the
files may not be saved properly and become
corrupted. Happens when software
processes files in an unexpected way or
saves them in the wrong format.
Hardware errors
If your computer's hardware,
especially storage devices (hard
drives, SSDs, etc.), is damaged or
malfunctioning, data may not be
written or read correctly, resulting
in corrupt image files.
Errors during file transfer
When transferring files over the internet or
network, they can become completely or partially
corrupted due to connectivity issues or data loss.
This is especially likely to happen when
transferring large image files.
Storage media
corruption
When transferring files over the
internet or network, it is possible for
files to become completely or
partially corrupted due to
connection issues or data loss.
This is especially likely to happen
when transferring large image files.

Impact of malware
If the physical storage medium (hard
drive, SSD, USB drive, SD card, etc.)
on which the image file is stored
becomes corrupted due to physical
damage, wear and tear,
manufacturing defects, etc. Files
stored on that medium may also
become corrupted.

## Page 12

12
01. current page topic
Basic recovery principles and
approaches02
The importance of backup
and data recovery
Backups can be the only way to
restore original data if it is
corrupted or lost.
Maintaining data corruption
It's important to take steps to
prevent further damage to
compromised data
Preparation and precautions
before recovery
The importance of backups Determine the type of damage
Basic procedures
for analyzing corrupted files
When loss of critical information
occurs, knowing how to
effectively recover can help
maintain business continuity and
protect sensitive information
The importance of recovery There is a wide variety of data
recovery software, so you need to
choose the right tool for your
situation
Select data recovery software
Before starting the recovery
operation, back up the data in
its current state.
Backup before a recovery operation
Select the appropriate
recovery tool
Attempt to recover
Validate results
Decrypting broken images02

## Page 13

13
01. current page topic
Advanced techniques in image
recovery03
Binary Editor Or
Hex Editor
Diagnose corruption: Open the corrupted file in a hex editor to determine the type and extent of the damage.
For example, for image files, you can review if the header information is corrupt, if the data section is correct, etc.
Compare to a healthy file: Open an undamaged, identically formatted file in a hex editor and compare it to the normal structure.
This helps you understand what went wrong and what needs to be fixed.
Fix: Fix the corruption directly or add the necessary data, for example, copying corrupt header information from a healthy file.
Save and verify: Save the modified file and verify that it opens correctly Sometimes multiple rounds of edits and verification are required
Manual recovery using a binary editor
It allows you to read and modify the contents of a file
directly, byte by byte, and displays the file's raw data in
hexadecimal form. Binary editors are used by developers,
system administrators, forensic analysts, and others to
analyze data structures or repair corrupted files.
Decrypting broken images02

## Page 14

14
01. current page topic
Advanced techniques in image
recovery03
When an image file is so badly corrupted that it is impossible to
recover it in its entirety, important data or parts of the image
can be extracted.
Identify the data: Use a hex editor or data extraction tool to
Identify blocks of data that are not corrupted.
Extract task: Extract the identified data blocks and save them to
a new file, which can be effective if you use a specific data
extraction tool during the process.
Partial recovery: The extracted data is used to restore important
parts of the image or information. It may not be a complete
recovery, but it can provide valuable information.
Extracting data from corrupted image files
Decrypting broken images02

## Page 15

15
01. current page topic
Advanced techniques in image
recovery03
from zlib import crc32
 data = open("C:\\Users\\exe2.png","rb").read() index = 12
ihdr = bytearray(data[index:index+17])
width_index = 7
height_index = 11
For x in range(1,2000):
 height = bytearray(x.to_bytes(2,'big'))
 for y in range(1,2000):
  width = bytearray(y.to_bytes(2,'big'))
  for i in range(len(height)): ihdr[height_index - i] = height[-i -1]
  for i in range(len(width)):
   ihdr[width_index - i] = width[-i -1]
  if hex(crc32(ihdr)) == '0x00000000':
   print("width: 0x {} height: 0x
{}".format(width.hex(),height.hex()))
for i in range(len(width)):
 ihdr[width_index - i] = bytearray(b'\x00')[0]
Width Height Recovery Code via CRC32 in PNG File
Output result - width : 0x 0000, height : 0x 0000
Decrypting broken images02

## Page 16

16
01. current page topic
Advanced techniques in image
recovery03
Importing libraries
Read a file
Extracting IHDR chunks
Navigating horizontal
and vertical lengths
from zlib import crc32
1.Get the crc32 function from the zlib library,
which is needed to compute the CRC32 checksum.
data = open("C:\\Users\\exe2.png","rb").read()
reads a PNG file in the specified path in binary
mode and stores it in the data variable
Double for loop
Explore all possible combinations while varying the
horizontal (x) and vertical (y) lengths from 1 to
1999
ihdr = bytearray(data[index:index+17])
Read 17 bytes from the index position, which
represents the beginning of the IHDR chunk, and
store them as a byte array in the ihdr variable
from zlib import crc32
 data = open("C:\\Users\\exe2.png","rb").read() index = 12
ihdr = bytearray(data[index:index+17])
width_index = 7
height_index = 11
For x in range(1,2000):
 height = bytearray(x.to_bytes(2,'big'))
 for y in range(1,2000):
  width = bytearray(y.to_bytes(2,'big'))
  for i in range(len(height)): ihdr[height_index - i] =
height[-i -1]
  for i in range(len(width)):
   ihdr[width_index - i] = width[-i -1]
  if hex(crc32(ihdr)) == '0x00000000':
   print("width: 0x {} height: 0x
{}".format(width.hex(),height.hex()))
for i in range(len(width)):
 ihdr[width_index - i] = bytearray(b'\x00')[0] CRC32 checksum
Calculations and comparisons
Reset horizontal length
Last for loop
Initialize the horizontal length
portion of the IHDR array used
during navigation to 0
if hex(crc32(ihdr)) == '0x4ec2ee58
Calculate the CRC32 checksum for the modified
ihdr array and check if it matches the target
checksum value
Decrypting broken images02

## Page 17

17
01. current page topic
File Carving04
File Carving
The process of recovering data from a storage medium, even if the file
system's metadata is missing or corrupted.
Basic principles of file carving
Works based on the structural characteristics and contents of a file.
Most file types have a unique header (beginning) and footer (end), and
these patterns can be identified for file recovery.
Decrypting broken images02

## Page 18

18
01. current page topic
File Carving04
Header and footer search: Scans the entire
storage medium to find headers and
footers that indicate the beginning and
end of files
Content-based carving: Analyze the content
or structural characteristics of a file type to
recover files even when the header and
footer are not clear.
File Signature Analysis: Use a file's unique
binary signature to identify a specific file
type
How to approach
There are a variety of file carving tools, each
of which may be optimized for specific file
types or scenarios.
Some of the most popular tools include
Scalpel, Foremost, and PhotoRec, which you
can choose based on the type of data you
want to recover.
Tools
Fragmentation: If files are stored spread
across storage media (fragmentation),
the recovery efficiency of file carving may
be reduced
Error recovery: Might misidentify other data
or file fragments with similar patterns
and cause errors
Limitations
File Carving
Digital forensics: Recover deleted files or
corrupted data that could be used as
evidence in a criminal investigation.
Data recovery: Restore sensitive data from
accidentally deleted files or corrupted
storage media
Applications
Decrypting broken images02

## Page 19

19
01. current page topic
File Carving04
Fragmentation
Impact
What to do
Cause
File creation and deletion: As users create and delete files, the storage space is partitioned,
resulting in a number of empty spaces. When a new file is stored in these empty spaces, if the file
size is larger than the contiguous empty space, it is stored in multiple pieces.
File extensions: When adding data to an existing file, if there is not enough contiguous space in
the original location of the file, the added portion is stored in a different location.
System operations: Fragmentation also occurs when the operating system updates system files or
creates and deletes temporary files.
System operations: Fragmentation also occurs when the operating system updates system files or
creates and deletes temporary files.
The splitting of files or data into multiple, non-contiguous pieces on a computer storage device.
Slower performance: Slower file access, especially on storage devices that use mechanical
read/write heads, such as HDDs, because the head must move to different locations on the disk
to read different pieces of a file.
Storage space inefficiency: Fragmentation leads to underutilization of storage space and
inefficient use of disk capacity.
Data recovery difficulties: If a file is corrupted or deleted while fragmented, it increases the
complexity and difficulty of data recovery operations such as file carving.
Disk defragmentation: Regularly defragmenting a disk can rearrange file fragments into
contiguous space and improve read/write performance of the disk. Most operating systems
provide disk defragmentation tools.
SSD optimization: For SSDs, fragmentation has less of an impact on performance than for HDDs,
but they support the TRIM command to manage unused blocks on SSDs and maintain
performance.
Decrypting broken images02
