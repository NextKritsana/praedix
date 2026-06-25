---
title: "19강_PNG, JPEG분석_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\19강_PNG, JPEG분석_v1.2.pdf"
source_size_bytes: 454719
source_modified: 2025-10-18T19:42:19
imported_at: 2026-06-14T14:25:10
tags:
  - acs
  - acs-advanced
  - imported
---

# 19강_PNG, JPEG분석_v1.2

- Source: [19강_PNG, JPEG분석_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/19%EA%B0%95_PNG%2C%20JPEG%EB%B6%84%EC%84%9D_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Different forensic
disciplines
• What is PNG
• PNG Structure
•IHDR
•IDAT
•IEND
• What is JPEG
• .jpg , .jpeg
• JPEG Structure
• JPEG Compression Methods
19
1

## Page 2

2
What is PNG01
PNG
Portable Network Graphics
Since
First introduced in 1996
Alternatives to the GIF file format
Interlacing
Ability for images to load gradually
on web pages
*Adam7 interlacing algorithm
How an image gradually comes together over multiple stages
Cross-platform compatibility
Lossless compression
Portable

## Page 3

3
PNG Structure02
➢Signature
Every PNG file starts with a unique 8-byte signature
89: Byte is set to a value unreadable by the computer
50: 'P' in ASCII code - stands for "P" in PNG
4E: 'N' in ASCII code - stands for "N" in PNG
47: 'G' in ASCII code - stands for the "G" in PNG
The three bytes together make up the name of the file type named "PNG"
0D: Carriage Return (CR) character in ASCII code
This is used to indicate the start of a new line, and on some systems it is
used to indicate the end of a line.
0A: Equivalent to the Line Feed (LF) character in ASCII code.
Used to indicate the start of a new line,
used to mark the end of a line on other systems
1A: Substitute (SUB) character, one of the ASCII control characters.
Used to indicate the end of text data,
used to indicate the end of a file on systems such as MS-DOS.
0A (hexadecimal): Another Line Feed character,
marks the second newline at the beginning of the file
89 50 4e 47 0d 0a 1a 0a
CRITICAL
ANCILLARY

## Page 4

4
PNG Structure02
➢Critical Chunks
Image Header (IHDR)
The first at the beginning of the file.
Defines the basic unknown metadata.
Includes the width and height of the image, bit depth, color type, compression
method, filter method, interlacing method, etc.
PLTE (Palette)
Defines the palette of colors used in an image.
Used in index color images, where each color is represented by an RGB value.
Chunks that are essential to a particular PNG image (index color image).
Image Data (IDAT)
Multiple IDAT chunks may appear in a row.
Contains compressed image data.
Contains the actual pixel data that makes up the image (compressed using the zlib
compression algorithm) and is required to restore the image.
IEND (Image End):
Appears at the end of the file.
Indicates the end of the image data stream.
Does not contain data, just marks the end of the file.
CRITICAL
ANCILLARY

## Page 5

5
PNG Structure02
CRITICAL
ANCILLARY
pHYs
sRGB
zTXt
gAMA
iCCPsBIT
tRNS
hIST
cHRM
tIME
tEXt
bKGD
oFFs
pCAL
eXIf
sPLT
sCAL
gIFg
gIFx
➢Ancillary Chunks

## Page 6

6
PNG Structure02
CRITICAL
ANCILLARY
sRGB
pHYs
gAMA tIME
eXIf
iTXt
A chunk stating that the
image follows the
standard RGB color
space
Chunks to specify the
physical dimensions of an
image
A chunk containing
information about the
gamma value of the
image.
Chunks containing
international text
information
Chunks containing
Exchange Image File
Format (Exif) data used by
digital cameras.
Chunks that record the
last time the image was
modified
➢Common Ancillary

## Page 7

7
IHDR03
Signature
I D H R
49 48 44 52
Width
4bytes
Height
4bytes
*BD
1
CRC32
*CT
1
*CM
1
*Bit Depth
*Color Type
*Compression Method
*Filter Method
*Interlace Method
1 1
13
144
*FM
1
*IM
1
1 1

## Page 8

8
IHDR03
Width
4bytes
Height
4bytes
A file named dog.png on your
desktop
 Checking the horizontal length in the
010 Editor
Metadata from the
actual file
For horizontal lengths
calculator for the horizontal length

## Page 9

9
IHDR03
Bit Depth
BIT Depth represents the amount of color, or depth, that each pixel in an image can represent
Grayscale (Color Type 0)
Bit Depth: 1, 2, 4, 8, 16
Each pixel represents a grayscale value.
The higher the bit depth, the more grayscales can be represented and the more detailed the image.
True Color (Color Type 2)
Bit Depth: 8, 16
Each pixel has a color value of red (R), green (G), and blue (B).
Higher bit depths allow more colors to be represented, increasing the color expressiveness of the image.
Index Color (Color Type 3)
Bit Depth: 1, 2, 4, 8
Images represent colors using a predefined palette of colors (color table).
Bit Depth determines the number of colors within the palette.
Grayscale Alpha (Color Type 4)
Bit Depth: 8, 16
Each pixel contains a grayscale value and transparency (alpha channel).
Higher Bit Depth allows for finer grayscale and transparency levels.
TrueColor Alpha (Color Type 6)
Bit Depth: 8, 16
Each pixel has an RGB color value and transparency (alpha channel).
This allows for the most color expression and transparency control.
Color Type

## Page 10

10
IHDR03
Color Type determines the color composition of the image and whether or not the alpha channel (transparency) is used.
Bit Depth is 08 and Color Type is 06,
This means that PNG images use an 8-bit bit depth in True Color Alpha (Color Type 6) mode.
True Color Alpha (Color Type 6, Bit Depth 08)
True color alpha is an image format in which each pixel has three color channels: red (R), green (G), and blue (B), plus
additional transparency (alpha channel) information.
An 8-bit bit depth means that each color channel (RGB) and alpha channel uses 8 bits. This indicates that each channel
can have values from 0 to 255, or 256 levels.
What is grayscale?
Grayscale is a colorless image format in which each pixel has only brightness information, meaning that the image is
represented only by the change in brightness from black to white. For example, an 8-bit grayscale image can represent
256 levels of grayscale, which includes intermediate brightness values from black (0) to white (255).Grayscale is often
used for photos, scanned documents, artwork, etc. that don't require color information, and has the advantage of
smaller file sizes compared to color images. By combining Bit Depth and Color Type, PNG images can efficiently express a
wide range of visual information and characteristics.
Color Type
Bit Depth

## Page 11

11
IHDR03
Compression Method specifies the type of compression algorithm used when storing image data.
PNG compresses data for efficient image storage
Use lossless compression, which means your images don't lose quality.
Current PNG standard supports only one compression method = Deflate/Inflate compression algorithm
-> Compression Method value: Fixed to 0
The only compression method used by PNG files, which uses the 'Deflate' compression algorithm to compress the image
data, and the 'Inflate' algorithm to decompress it.
The Deflate algorithm is a combination of the LZ77 algorithm and Huffman coding, which efficiently encodes repeating
patterns in data to reduce file size.
It is widely used to compress various forms of data, including text files, images, web pages, and more. PNG's compression
method is lossless compression, which means that no information in the image is lost during the compression process, so
the uncompressed image is exactly the same as the original image.
LZ77 Algorithm
How to compress data by finding repeats in text and replacing them with their position and length.
Huffman coding
A method of compressing data by assigning short codes to frequently occurring characters and long codes to infrequently
occurring characters.
Deflate algorithm
Using a combination of the two methods above.
First, LZ77 to reduce repetitions, then Huffman coding to compress data by allocating efficient bits to each part.
Compression
Method

## Page 12

12
IHDR03
Filter Method is a preprocessing process applied to pixel data before efficiently compressing image data.
None (filter type 0): No filtering is applied; each pixel is saved as is.
Sub (filter type 1): Each pixel is stored as the difference between itself and the previous pixel on the same
scanline.
This is effective for reducing duplication in the horizontal direction.
Up (filter type 2): Each pixel is stored as the difference between itself and a pixel in the same position on the
scanline directly above it.
This is used to reduce duplication in the vertical direction.
Average (filter type 3): Each pixel is stored as the difference between its previous pixel and the average of the
pixels immediately above it.
This can handle duplicates in both horizontal and vertical directions simultaneously.
Paeth (Filter Type 4): Using a more complex algorithm, the previous pixel, the pixel directly above it,
and the previous pixel directly above it, predicts the optimal value based on the relationship between them,
stores the difference between this prediction and the actual pixel value.
This is useful for increasing compression efficiency in complex image patterns.
The "None" filter (Filter Method 00) is widely used because
Because this approach simplifies image data processing and ensures compatibility with all PNG decoders. The
filter uses the image data as it is, without any additional computation, which can reduce computational cost
and balance compression efficiency, especially for images with few overlapping patterns. Nevertheless,
depending on the characteristics of the image, other filter types can be selected to increase compression
efficiency, and image creation software can automatically or manually select the optimal filter type.
Filter Method

## Page 13

13
IHDR03
Interlace Method determines how image data is stored within the file.
PNG supports two interlacing methods - non-interlaced, Adam7 interlaced.
Non-Interlace Method (Interlace Method 00)
Loading method: Images load sequentially from top to bottom Users see the images appear one after the other,
starting at the top, and must wait for the entire file to load to see the entire image.
Pros: Simple processing and fast decoding speeds, less complexity when editing or processing images, efficient.
Cons: On slow connections, it can take a significant amount of time for users to see the full image.
Adam7 Interlace Method (Interlace Method 01)
Loading method: Load the image gradually, dividing it into seven passes.
Initially, a low-resolution image is displayed, gradually adding more detail until the entire image is sharpened.
Pros: Even on low-speed connections, users can quickly get an idea of what the image looks like.
The gradual sharpening of the image can improve the user experience.
Cons: Image processing and decoding can be more complex and slower than non-interlaced methods.
File sizes can be slightly larger, and it takes time for all the details to load.
Comparison summary
Non-interlaced for simple and fast processing,
especially when you need to check the overall quality of an image at once.
The Adam7 interlacing method allows users to view images progressively and quickly.
Useful when you want to provide a good user experience and your web page needs to load images on slow
connections.
For this reason, most Interlace Methods have a value of 00.
Interlace Method

## Page 14

14
IDAT04
CRITICAL Chunks
IDHR
PLTE
IDAT
IEND
IDAT is short for Image Data.
Chunks that store the actual pixel information of an image in a compressed form.
IDAT chunks contain the visible content of an image, i.e., pixel-by-pixel color
information, They provide all the data needed to construct the image when the PNG
file is displayed or processed.
Compressed image pixel data: PNG uses the Deflate algorithm to losslessly compress
image data for efficient file size management. IDAT chunks store this compressed
data, which must be decompressed to display the image correctly.
Filtered pixel data: Each scanline (horizontal line) in an image can have a filter
applied to it. This filtering process is based on differences between neighboring
pixels and is used to reduce redundancy in the data to increase compression
efficiency. The data stored in IDAT chunks is the result of this filtering process.
Because IDAT chunks store image data in a compressed form, they can be used to
hide potentially malicious code.
For this reason, it's important to only use files from trusted sources or use secure
image processing libraries when working with PNG files.

## Page 15

15
IEND05
CRITICAL Chunks
IDHR
PLTE
IDAT
IEND
PLTE (Palette)
PLTE chunks are used in indexed color images and define the palette of colors used
within the image. This chunk contains the set of RGB color values needed for color
indexing.
When used: PLTE chunks are required when the Color Type is 3 (indexed color). An
indexed color image is one in which each pixel does not directly represent a color, but
rather references a specific index in the color table defined in the PLTE chunk.
Structure: A PLTE chunk consists of an array of 3-byte (RGB) color values, with each
color consisting of 1 byte of red, 1 byte of green, and 1 byte of blue values.
Function: Allows for efficient storage of different colors within an image,
Especially suitable for web graphics or small images with a limited number of colors.
Image End (IEND)
The IEND chunk indicates the end of the image data, and is the last chunk of the PNG
file. The IEND chunk does not contain any actual data, but acts as a signal to indicate
that the file has been successfully terminated.
When used: Located at the end of every PNG file, indicating that the file contains no
further image data.
•Structure: An IEND chunk has a data field of 0 bytes and contains 4 bytes with a
chunk type of 'IEND’.
•Function: Indicates the end of the file and is used to verify that the PNG file is
complete and error-free. PLTE and IEND are important components of a PNG image file,
playing an essential role in representing the color information of the image and
ensuring the integrity of the file.

## Page 16

16
What is JPEG06
JPEG
Joint Photographic Experts Group
Since
First introduced in 1992.
To efficiently compress, store, and
transmit high-quality digital image data.
Highly adaptable
User adjustable compression ratio
EXIF data support
Includes EXIF.
(Exchangeable Image File Format) data to store metadata.
Lossy compression method.
Standardized formats.
Portable

## Page 17

17
.jpg, .jpeg07
Difference between .jpg and .jpeg files
There is no technical difference between .jpg and .jpeg files.
Both extensions refer to image files that use the Joint Photographic Experts Group (JPEG) compression method.
Originally, MS-DOS and early versions of Windows supported only three-letter extensions, so
 .jpeg file extensions were shortened to .jpg.
Although the .jpeg extension has since become available as operating systems support longer file names,
The .jpg extension was already widespread and continues to be in heavy use
There is no difference in the file format itself or functionality,
and both extensions use the same JPEG compression algorithm and image quality.

## Page 18

18
JPEG Structure08
General JPEG File Structure - 010Editor
Start of Image (SOI)
JPEG files always start with a Start of Image (SOI) marker.
It consists of bytes at 0xFFD8, indicating that the file is in JPEG
format.
Header segments
Application Segment (APPn): This section can contain
metadata, for example, Exif data or Adobe Photoshop
information is stored here.
JFIF (JPEG File Interchange Format):
Most JPEG files follow the JFIF standard.
It contains basic information about the image.
For example, version, units, resolution, thumbnail image, etc.
Frame Segments
Start of Frame (SOF): Contains structural information about
the image, such as the width and height of the image, the
number of color components, the sampling factor for each
component, and how the colors are represented.
Huffman Table Segment (DHT)
This segment defines the Huffman coding table used for
compression of image data.
*Segment: a block of data with a specific structure

## Page 19

19
Quantized table segments (DQT)
A quantization table defines a quantization matrix for each
component of an image, which is used to increase
compression by reducing color information.
Start of Scan (SOS)
This section represents the actual start of the compressed
image data. It contains the details of the Huffman table for
each component used to decode the image data.
Image data
The most important part of the JPEG file, where the actual
compressed image data is stored. This data is decoded using
the Huffman table and quantization table defined earlier.
End of Image (EOI)
JPEG files end with an End of Image (EOI) marker. This
consists of a byte at 0xFFD9, indicating the end of the image
data.
JPEG Structure08
General JPEG File Structure - 010Editor

## Page 20

20
01. current page note
How JPEGs are compressed09
JPEGs typically convert an image from the
RGB color space to the YCbCr color space.
During this process, the image is separated
into brightness information (Y) and color
difference information (Cb and Cr).
Color Space Conversion
The Cb and Cr components may be sampled
less than the Y component.
Subsampling
The converted image is converted to the
frequency domain via the Discrete Cosine
Transform (DCT).
Quantization
Quantized data is further compressed using
entropy coding techniques such as Huffman
coding or arithmetic coding.
Entropy Coding
Compressed data is stored in the same form as
IDAT chunks in a JPEG file.
Saving to JPEG file structure
1
2
3
4
5
*YCbCr color space: JPEGs store luminance (brightness) information and chrominance (color and saturation) information separately.
This helps to reduce file size more efficiently by taking advantage of the fact that the human eye is more sensitive to brightness than color.
