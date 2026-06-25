---
title: "22강_Video(MP4,MOV,WMV)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\22강_Video(MP4,MOV,WMV)_v1.2.pdf"
source_size_bytes: 706459
source_modified: 2025-10-18T19:54:58
imported_at: 2026-06-14T14:25:12
tags:
  - acs
  - acs-advanced
  - imported
---

# 22강_Video(MP4,MOV,WMV)_v1.2

- Source: [22강_Video(MP4,MOV,WMV)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/22%EA%B0%95_Video%28MP4%2CMOV%2CWMV%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Video
• What is Video Forensic
• Video analytics techniques
• Detect video manipulation
• What is an MP4 file
• Structure of the MP4 file format
• What is a MOV file
• Structure of the MOV file format
• What is a WMV file
• Structure of the WMV file format
• Compare MP4,MOV,WMV
22
1

## Page 2

2
01. current page topic
What is Video Forensic01
Video forensics is the art of scientifically analyzing how digital
video is created, processed, and stored to determine its
authenticity, using a variety of techniques such as analyzing
metadata, detecting image manipulation, identifying sources, and
determining whether content has been tampered with. Video
forensics is important for establishing the reliability of evidence,
detecting manipulation of digital media, and uncovering the truth.
Definition and Importance
Early work focused primarily on qualitative analysis of analog video,
but with the advent of digital technology, complex techniques were
developed to analyze the digital nature of the data. Since the late
1990s, the use of digital video content has exploded, and video
forensics has required more sophisticated and diverse analysis tools
and techniques. The principles of digital image forensics were applied
to video, allowing for more sophisticated analysis.
History
Video forensics
A scientific methodology for verifying the authenticity of digital video content and analyzing it for manipulation.

## Page 3

3
01. current page topic
What is Video Forensic01
Cybercrime investigation
Videos circulating in cyberspace can defame individuals or spread false
information.
Video forensics can be used to obtain evidence of these crimes and track
down the perpetrators.
Copyright and content infringement
In cases of unauthorized use or copyright infringement of digital content,
video forensics is used to prove ownership of the original content or to
uncover infringement.
Security and surveillance
Video from surveillance cameras in public places or critical facilities
can play an important role in getting to the bottom of an incident.
Forensic evidence
The authenticity and integrity of video evidence is critical in court.
Video forensics can prove that video submitted as evidence has not been
tampered with or, conversely, uncover signs of tampering.
Key applications of video forensics

## Page 4

4
01. current page topic
What is Video Forensic01
Structure and format of digital video
A digital video file consists of a container that
contains video data, audio data, and
information that synchronizes the two data
streams.
Each video file has a specific format, which
determines how the file is encoded and stored.
Common video file formats include MP4, AVI,
MOV, and WMV, each of which offers different
compression methods, compatibility, and
quality.
Video forensics requires an understanding of
the characteristics of these formats to accurately
analyze video files.
Understanding video metadata
Video metadata is additional information
embedded in a video file, including data
such as the date and time it was shot,
camera type, file creator, and more.
In video forensics, metadata provides
important clues to determine the source
and authenticity of a video.
Metadata analysis can help you track when,
where, and by whom a video file was
created, and can also help you determine if
a file has been tampered with..
Digital video compression technology
Digital video compression techniques help make
high-quality videos take up less storage space or
transmit them quickly over the internet.
There are lossy and lossless compression, each of
which strikes a different balance between video
quality and file size.
Some of the most common video compression
standards include H.264 (AVC), H.265 (HEVC),
VP9, and AV1.
Understand these compression techniques and
identify changes to the data that can occur during
compression to analyze whether a video has been
tampered with.

## Page 5

5
01. current page topic
Video analytics techniques02
Examine the individual frames that make
up a video to identify if certain parts of the
image have been modified or manipulated.
Frame analysis
Track the movement of objects or people in
a video to determine if the movement is
natural or artificially generated.
Behavioral analytics
Analyzing video content

## Page 6

6
01. current page topic
Video analytics techniques02
Identify the source Analyze metadata
Each camera leaves a unique "fingerprint"
on the video due to microscopic
imperfections in the sensor.
Camera fingerprint
The type of codec and its settings give a video file its
unique characteristics, which can be analyzed to infer
what software or equipment the video was processed
through.
Codec characterization
The metadata in a video file records the
date and time the file was created or last
modified.
Creation date and modification history
Some video files contain information about
where they were shot.
Location data

## Page 7

7
01. current page topic
Detect video manipulation03
Substitute
Delete Compositing
Insert
A manipulation that combines two or more video or
image sources to create a new sequence.
Composition
Manipulation methods that replace the
original frame or sequence of a video
with another frame or sequence.
Replacement
Manipulation methods for adding
additional frames or sequences to specific
parts of a video sequence.
Insertion
Operations to remove a specific frame or
sequence from a video
Deletion
Main types of video manipulation

## Page 8

8
01. current page topic
Detect video manipulation03
Compare videos
Analyze visual differences between the original
video and the suspect video
Consistency checks
Evaluate whether the various elements in your
video match natural physical laws and
environmental conditions.
Machine learning-based
methods
Can train on large datasets to distinguish
between legitimate and manipulated patterns
in video

## Page 9

9
01. current page topic
Detect video manipulation03
Forevid
Free tool for video forensic analysis,
helping law enforcement and forensic
professionals determine if video has been
manipulated
Amped FIVE
Advanced video analytics software
designed for forensic experts and
investigators
Video Cleaner
Open-source video forensics software
designed to help users determine the
authenticity of video evidence, enhance
video, and identify manipulation

## Page 10

10
01. current page topic
What is an MP4 file04
W h a t  i s  M P 4
Short for MPEG-4 Part 14; digital multimedia container
format. Allows a variety of content, such as video,
audio, subtitles, and images, to be stored in a single
file; primarily used for storing and transmitting digital
video and audio streams. It provides highly efficient
compression, allowing high-quality multimedia content
to be stored in relatively small file sizes.
H i s t o r y  o f  M P 4
Officially released in 2001 by the International
Organization for Standardization (ISO).Developed as part
of the MPEG (Moving Picture Experts Group) standard, it
builds on the previous MPEG-1 and MPEG-2 formats,
offering improved compression technology and flexibility.
The advent of MP4 revolutionized the storage,
distribution, and accessibility of digital multimedia
content and continues to be one of the most important
video file formats today.

## Page 11

11
01. current page topic
What is an MP4 file04
It uses high-efficiency video coding (H.264 or H.265) and advanced audio coding (AAC)
technologies to deliver superior compression efficiency and quality.
Features
High compatibility, efficient compression, and multimedia support
Pros
Loss of quality due to compression, limited editing, and copyright issues
Cons and limitations

## Page 12

12
01. current page topic
Structure of the MP4 file format05
The structure, formatting, and compression technology of MP4, and how it works.
Structure of the file
MP4 files are composed of several small
units, also known as 'boxes' or 'atoms’.
These boxes are responsible for different
aspects of the file, and are categorized into
two main types: moov (movie) boxes, and
mdat (media data) boxes.
Moov boxes contain metadata and store the
video's metadata, track information, and
information needed for decoding.
Mdat boxes store the actual audio and video
data.
Formats and compression
technologies
The MP4 file format follows the MPEG-4
standard, which uses advanced video coding
standards such as H.264/AVC or
H.265/HEVC to compress video data.
Audio data is primarily compressed using the
Advanced Audio Coding (AAC) codec.
These codecs provide excellent compression
efficiency while maintaining the quality of
the video and audio.
Compression principles
Minimize redundancy in data to reduce
reducing file size by minimizing redundancy
of data.
Video compression reduces the amount of
data by storing only the differences between
frames.
This is accomplished through intra-frame (I-
frame) and inter-frame (P-frame and B-
frame) coding. Audio compression reduces
data size by removing information from
sounds that the human ear cannot detect,
and by efficiently encoding redundant parts
of the audio signal.

## Page 13

13
01. current page topic
What is a MOV file06
W h a t  i s  M O V
A digital video file format developed by Apple.
It was designed for the QuickTime media player
and functions as a container format that can
store various types of data, including video,
audio, text, and effects. MOV files are intended
for storing and editing high-quality video and
are widely used in professional-level video
production and the movie industry.
H i s t o r y  o f  M O V
Introduced by Apple in the early 1990s, it emerged
alongside early advances in digital video and audio
streaming technology. Also known as the QuickTime
format, MOV offered a revolutionary way to store and
share multimedia content at the time. The format has
evolved over time to include a variety of features that
allow for efficient compression and editing of high-
definition video.

## Page 14

14
01. current page topic
What is a MOV file06
High-quality video support
Rich multimedia integration
Ease of editing
Pros
Compatibility Issues
File size
Limited to a specific audience
Cons and limitations

## Page 15

15
01. current page topic
Structure of the MOV file format07
The structure, formatting, and compression technology of MP4, and how it works.
Structure of the file
A multimedia container format developed by
Apple that is designed to store many different
types of data. The file structure is composed of
several components called "atoms" or "boxes."
Each atom can contain different types of media
data, such as video, audio, subtitles, etc, Each
atom can contain different kinds of media data,
such as video, audio, text subtitles, or provide
metadata about the file as a whole.
The main atoms include 'moov' (movie data),
'trak' (track data), 'mdia' (media data), and
'mdat' (actual media content).The 'moov' atom
contains the video's metadata and references to
other atoms, providing the information needed
when playing or editing the file..
Formats and compression
technologies
The MOV format supports a variety of video and
audio codecs. The video codec is primarily H.264
(MPEG-4 Part 10), which is widely recognized for
its ability to efficiently compress high-quality
video.
Audio primarily uses the Advanced Audio Coding
(AAC) codec, which provides a high-quality audio
stream. In addition, professional codecs such as
Apple ProRes are also supported in MOV files,
making them ideal for high-definition video
applications such as filmmaking.
Compression principles
Depends on the video and audio codec selected.
For the H.264 video codec, it compresses data
using techniques such as prediction (inter- and
intra-frame prediction), transform (using
transform coding instead of fixed-length coding),
quantization (reducing the number of bits in the
data), and entropy coding (compression using the
statistical properties of the data). The purpose is
to reduce the file size by removing redundant or
unnecessary information in the video, while
maintaining the quality of the original video as
much as possible. The AAC audio codec uses
similar compression principles to efficiently
compress audio data by removing sound
information that is difficult for the human ear to
detect.

## Page 16

16
01. current page topic
What is a WMV file08
W h a t  i s  W M V
A video codec and file format developed by
Microsoft. It is part of the Windows Media
framework and is designed for internet streaming,
high-definition video delivery such as HD DVD and
Blu-ray discs, and video playback on a variety of
portable devices. It provides a high degree of
compression while maintaining video quality,
allowing for efficient video transmission over
networks.
H i s t o r y  o f  W M V
First introduced by Microsoft in the late 1990s.
Initially started as a simple internet video
streaming format. Over time, WMV evolved into
several versions supporting high-definition video.
In particular, WMV 9 proved so successful that it
was adopted as one of the standard video codecs
for HD DVD and Blu-ray discs.

## Page 17

17
01. current page topic
What is a WMV file08
Highly efficient compression
Broad compatibility
DRM support
Pros
Platform limitations
Quality degradation due to compression
Standardization issues
Cons and limitations
*DRM: Technology developed to prevent unauthorized copying and distribution of copyrighted content.

## Page 18

18
01. current page topic
Structure of the WMV file format09
The structure, formatting, and compression technology of WMV, and how it works.
Structure of the file
Use Advanced Systems Format (ASF) containers to
store video and audio streams. ASF is a container
format that can contain media streams and metadata,
specifically designed to support streaming media and
digital rights management (DRM).
Header section: Contains general information about
the file, including the length of the file, total number of
frames, and ASF version information.
Stream properties object: Defines the characteristics of
video and audio streams, including codec information,
bitrate, sampling frequency, etc.
Data object: Contains the actual video and audio data
and is composed of multiple data packets.
Index section: Contains index information to help you
quickly locate specific locations within the media
stream.
Formats and compression
technologies
Developed to efficiently compress and distribute
video content within Microsoft's Windows Media
framework.
The format uses several versions of the WMV
codec to compress video data.
Starting with the initial version, WMV7, and
evolving to WMV8 and WMV9 (VC-1), each
codec introduces different techniques to improve
compression efficiency and video quality.
Compression principles
Based on Advanced Video Compression (AVC)
technology.
This technology includes the following main
mechanisms
Predictive coding: predicts the content of the current
frame based on previous frames, and only stores the
difference between the actual and predicted (error
signal). This can significantly reduce redundancy in the
data.
Transform coding: converts frame data into a more
compressible form using transforms such as the
Discrete Cosine Transform (DCT). The transformed data
is then quantized again to reduce bitrate.
Entropy coding: Analyzes the statistical properties of
data patterns to encode data in a way that allows
information to be represented in fewer bits.

## Page 19

19
01. current page topic
Compare MP4,MOV,WMV10
Feature MP4 MOV WMV
Compatibility High Medium Low
Compression
Efficiency High Medium High
Editing Flexibility Good Excellent Fair
Platform Support Universal Apple Devices Windows-centric
Quality Preservation Very Good Excellent Good
Compatibility: MP4 is rated 'High', meaning it is widely compatible across almost all devices and platforms
Compression efficiency: MP4 and WMV offer high compression efficiency, which means you can compress high-quality video into a smaller file size
Editing flexibility: The MOV file format is rated as 'Excellent', offering great flexibility in video editing and creation
Platform support: MP4 is 'Universal', meaning it's compatible across a wide range of platforms
Quality preservation: MOV is 'Excellent', preserving as much of the original quality as possible, especially for high-definition video creation and editing
