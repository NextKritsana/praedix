---
title: "26강_Anti-Forensic_(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\26강_Anti-Forensic_(1)_v1.2.pdf"
source_size_bytes: 757059
source_modified: 2025-10-18T20:12:32
imported_at: 2026-06-14T14:25:17
tags:
  - acs
  - acs-advanced
  - imported
---

# 26강_Anti-Forensic_(1)_v1.2

- Source: [26강_Anti-Forensic_(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/26%EA%B0%95_Anti-Forensic_%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Anti-Forensic
26
• Anti-Forensic
• Data concealment
• Data destruction
1

## Page 2

2
Anti-Forensic01
Anti - Forensic
Includes all techniques, strategies, and methods to disrupt, evade, or neutralize
the digital forensics process
Purpose of Anti-Forensic
Avoiding or delaying legal liability by impeding law enforcement from obtaining,
interpreting, or using digital evidence related to a crime.

## Page 3

3
01. current page topic
Anti-Forensic01
Data Hiding
Data hiding is a technique for hiding sensitive
information or files in a way that makes them
undetectable by normal means.
Data Destruction
The process of permanently deleting or overwriting
data that could be evidence, making it unrecoverable,
which hinders the tracking and analysis of evidence.
Data Encryption
Data encryption is a technique for encrypting data
using secret codes or algorithms to limit who can
access that data.
Data Tampering
Intentionally altering or manipulating the content
of data, metadata (e.g., creation date,
modification date), or system logs.

## Page 4

4
01. current page topic
Anti-Forensic01
Conceal, destroy, or tamper with evidence
Hiding or concealing digital evidence related to a
crime to prevent law enforcement from discovering it
Avoiding detection and liability
From digital forensics tools and techniques
 aimed at hiding malicious activity or malicious code
Privacy
In some cases, anti-forensic techniques may be
used for purposes to protect the privacy of
 individuals and to enhance data security

## Page 5

5
01. current page topic
Anti-Forensic01
Legal and regulatory enforcement / Improve the legal framework
Establish or strengthen laws that prohibit and penalize anti-forensic behavior, which should include legal definitions and
penalties for the intentional manipulation or destruction of digital evidence.
Increased international cooperation
Because crimes involving digital evidence can cross borders, international cooperation and legal coordination is critical to
combat anti-forensic behavior.
Technical response and tool development / Development of advanced forensic tools and techniques
Develop advanced forensic tools and techniques to detect and overcome anti-forensic techniques, which may include
decryption of encrypted data, discovery of concealed data, and recovery and analysis of data.
Ongoing research and development:
As new anti-forensic techniques continue to emerge, research and technology development is needed to keep up.
Legal Response Strategies for Anti-Forensic Techniques (1)

## Page 6

6
01. current page topic
Anti-Forensic01
Education and training / Training for Law Enforcement and Forensic Professionals
Provide training to ensure that professionals in the field of digital forensics are well versed in the latest anti-
forensic techniques. Training should include not only technical knowledge, but also legal and ethical aspects.
Improving legal professionals' understanding of digital evidence
Educate legal professionals, including lawyers and judges, to understand the complexities of digital evidence
and the impact of anti-forensic techniques. This enables fair and efficient legal judgment.
Develop policies and procedures / Proper evidence collection and storage
Developing and adhering to strict procedures and protocols in the collection, storage, and processing of digital evidence,
which is critical to ensuring the integrity and reliability of evidence.
These strategies are complementary to each other and contribute to building an effective legal framework to counter anti-
forensic techniques. Through a triangular approach of law, technology, and education, we can overcome the challenges of
digital forensics and ensure justice and efficiency in legal investigations.
Legal Response Strategies for Anti-Forensic Techniques(2)

## Page 7

7
01. current page topic
Data concealment02
Data masking is a data protection technique that hides the original data by replacing sensitive
information with realistic but fake data. It is often utilized when there is a need to protect sensitive data
but still use the data in non-production environments such as development, testing, and training.
The main purpose of data masking
1. Privacy: Protect sensitive information, such as personally identifiable information (PII), from unnecessary exposure
to the outside world
2. Compliance: Compliant with data protection regulations (GDPR, HIPAA, etc.) across countries and industries
3. Enhanced security: Increases information security because data breaches expose masked data, not real data
Techniques for data masking
1.Static Data Masking: Masking the original data in a database or file to create a new copy, which is used for
development or testing purposes. The original database is preserved.
2.Dynamic Data Masking: Masking data in real time as it is requested.
The degree of masking can be adjusted based on the user's role or permissions, while the actual data remains in the
database.
3.On-the-fly data masking: Masking data in real time while it is being moved to another system.
data masking in real time while moving data to another system. Used to protect sensitive information during data
migration.
Application examples
Development and testing: Use real-world-like data for development and testing while protecting sensitive
information.
Data sharing: Ensure data safety by masking sensitive information when sharing data with external parties or other
departments
Data analytics and reporting: Perform data analytics or reporting while hiding sensitive information
Enhance privacy while maintaining the value of your data

## Page 8

8
01. current page topic
Data concealment02
How to detect data masking
1. Analyze patterns and consistency
Masked data often has repetitive patterns or consistent shapes.
For example, fictitious phone numbers or addresses used in a test environment may differ from real-world patterns.
By analyzing these unrealistic patterns or consistencies in the data, you can detect masked data.
2. Metadata analysis
You can identify masked data by analyzing the metadata that was changed during the data masking process.
For example, data fields such as masked dates may show metadata differences from the original data.
3. Rule-based inspection
If you know the rules or algorithms your organization applies to mask data, you can apply these rules in reverse to
detect masked data. For example, if the same fictitious data is used repeatedly in a particular field, you can detect it
How to analyze data masking
1. Analyze how it compares to the original data
Where possible, compare the masked data to the original data to see what information has been changed,
This can help you understand the nature of the masked data and the masking process.
2. Reverse engineer the algorithm
Reverse engineer the algorithm used to mask data to understand the masking process, analyze what type of data
was masked. This method can be useful for uncovering the details of masking rules
3. Evaluate data quality
Evaluate the quality of the masked data to identify any loss or distortion of information that may have occurred
during the masking process. This can be important for evaluating how useful the masked data is in the real world.

## Page 9

9
01. current page topic
Data concealment02
Steganography is a data hiding technique that hides information within multimedia files such as messages,
images, audio, and video. The method masks the presence of information, making it difficult for outsiders to
recognize that it is hidden. It can be used for a variety of purposes, including the transmission of confidential
information, copyright protection, and privacy.
How steganography works
Steganography typically consists of two main components
Carrier and payload.
The carrier is the host file (e.g., image, audio file) in which you want to hide information,
The payload is the actual information you want to hide (e.g., a text message).
Steganographic Techniques
Least Significant Bit (LSB) modification: One of the most common steganographic techniques, it hides
information by modifying the least significant bit (LSB) of the bits per pixel in an image file. Effective because
the change is almost undetectable visually.
Masking and filtering: These techniques are used to hide information in specific areas of an image.
Usually hiding data in more important parts (e.g., lighter or darker areas).
Pros: Highly secure because it can hide the existence of information. Flexible because it can be applied to a
wide variety of multimedia files.
Cons: May increase the size of the carrier file. May be detected by some steganographic detection techniques.
Compression or conversion of the carrier file may corrupt hidden information.

## Page 10

10
01. current page topic
Data concealment02
How to detect data hiding
Visual analytics
Often performed on images, and useful because hidden information can slightly alter the visual properties
of an image. Statistical analysis of visual files may involve an expert manually inspecting an image for
unusual pixel patterns or color distributions.
Statistical analysis
Detects the presence of hidden data by analyzing enemy attributes. In image files, the statistical
distribution of pixel values may differ from a natural image if the Least Significant Bit (LSB) technique is
used.
Spectral analysis
Especially useful in audio steganography, where the spectrum of an audio file can be analyzed to detect
the presence of hidden information.
Steganography detection tools
Specialized tools such as Stegdetect, Steganalysis, and StegExpose can be used for steganography
detection.
Data covert analysis methods
Extracting hidden data
In order to extract the detected hidden data, it may be necessary to apply the steganographic technique in
reverse, which often requires prior knowledge of the technique or analysis tools.
Content analytics
Analyzing the content of the extracted data to assess the nature, purpose, and significance of the
information. This is important to understand the meaning of the hidden message.
Analyze patterns and metadata
Gain additional insights by analyzing patterns or metadata associated with the extracted data. This can
help you understand the context or purpose behind the data.
Reverse engineering and experiments
For new or complex steganographic techniques, understand their principles and develop analysis methods
through reverse engineering or experimentation

## Page 11

11
01. current page topic
Data concealment02
File system steganography
Hiding data by exploiting hidden space or structural characteristics,
for example, slack space on disk, empty space, metadata areas, etc.
Hides data directly within the file system, so the external
characteristics of the file remain unchanged.
Factors to watch for in detection and analysis
Requires a deep understanding of file systems. Knowledge of the
structure and workings of file systems is necessary to find hidden
data. Digital forensic tools can be used to detect abnormal space
usage in the file system, which is useful for finding data hidden in
slack or empty space. Care must be taken to avoid damaging the
file system during data recovery and analysis.

## Page 12

12
01. current page topic
Data concealment02
Network steganography
Network traffic, protocols, and packet header information are used to transmit data,
e.g., HTTP headers, sequence numbers in TCP/IP packets, etc. It can be used in real-
time communication or data exchange because it hides information during the data
transmission process.
Factors to watch for in detection and analysis
Analysis of network traffic is essential. Use a network packet analysis tool (e.g.,
Wireshark) to look for unusual patterns or traffic. Understanding of protocol details
is necessary: Network steganography relies on the properties of specific protocols, so
it requires a deep knowledge of those protocols. When analyzing real-time
communications, you may need to process large amounts of data, so you need an
efficient data analysis strategy.

## Page 13

13
01. current page topic
Data concealment02
Image Steganography
How to hide information within an image file. The most
common method is Least Significant Bit (LSB)
modification. Hiding information by minimizing visual
changes.
Factors to watch for in detection and analysis
Requires statistical and visual analysis. LSB changes can
change the statistical properties of the image. Hiding
information in high-resolution or complex images can
make detection more difficult.
Audio Steganography
Hiding data using changes in sound waves or amplitude in
an audio file. There are many techniques, including echo
hiding, phase coding, and more.
Factors to watch for in detection and analysis
Audio spectrum analysis is required, as concealed
information can cause subtle changes in the audio
spectrum. Audio quality should be checked for degradation,
as the data hiding process may degrade audio quality.
Video Steganography
Hiding data within video frames or applying
steganography to audio tracks. Data can be hidden
through movement between frames or subtle color
changes.
Factors to watch for in detection and analysis
Frame-by-frame analysis of video is required to detect
subtle changes between frames. Large amounts of data
and long processing times may be required, requiring
efficient analysis methods.
Text steganography
Hiding information within a text document by manipulating
spaces, tabs, and sentence structure. Text with hidden
information is visually indistinguishable from the original
document.
Factors to watch for in detection and analysis
Text pattern analysis is important - need to detect unusual
use of spaces or tabs. Natural language processing (NLP)
techniques can be leveraged to analyze changes in the
linguistic characteristics of a document.

## Page 14

14
01. current page topic
Data concealment02
Digital watermarking is a data concealment technique that takes the form of hiding
information (a watermark) within multimedia content (e.g., images, audio, video). It can
be used to indicate ownership of the content, track the origin of the content, or prevent
unauthorized copying or distribution. Watermarks are designed to be preserved during
the copying process, providing the ability to effectively track unauthorized use of content.
Key Features
Invisibility: The watermark is hidden in the content to the point where it is imperceptible to
the average user and does not or minimally degrade the original quality of the content.
Durability: The watermark remains intact even if the content is modified or transformed
(e.g., compressed, reformatted, resized).
Detectability: With the right tools or software, you should be able to detect and interpret
watermarks. This is necessary to verify ownership or identify the source of the content.
Use cases
Copyright protection: Content creators can embed watermarks in their work to claim
copyright and prevent unauthorized use.
Content tracking: Embed a watermark in your distributed content, so you can track how
that content is being used
Data security: By adding a watermark to important documents or images, verify the
authenticity of the document or image.

## Page 15

15
01. current page topic
Data concealment02
Detection methods
Use of proprietary software: Use of proprietary software or algorithms designed to detect and interpret
watermarks. Such software can verify the presence of a watermark and extract the information
contained in the watermark.
Spectral analysis: Spectral analysis can be performed to detect invisible watermarks in audio or video
files
Statistical analysis: Analyzes the statistical distribution of pixel values to detect invisible watermarks in
image files Can detect abnormal statistical patterns caused by watermark insertion
Comparative analysis: Analyze the original content versus the watermarked content to see the subtle
differences caused by the watermark
Analysis methods
Watermark extraction: Extract and interpret the content of the detected watermark. Can vary
depending on the type of watermark and how it was embedded, often requiring a complex decoding
process.
Authenticating content: Using information in a watermark to verify the authenticity of content,
verify the source or copyright owner of the content
Security assessment: By evaluating the durability and security of the watermark,
analyzing how well it protects against content tampering or unauthorized copying.
Factors to watch out for
Durability of watermarks: Watermarks can be damaged or removed by conversion, compression,
resizing, etc. of content Need detection and analysis methods that take durability of watermarks into
account
Visibility and quality: For invisible watermarks, it is important to effectively hide the watermark without
degrading the quality of the content. Care must be taken to ensure that the original quality of the
content is preserved during watermark detection.
Legal and ethical considerations: Watermark analysis can involve legal and ethical issues such as
copyright protection and privacy It's important to follow proper authorization and procedures

## Page 16

16
01. current page topic
Data concealment02
01
02
03
Copyright infringement
Privacy threats
Legal and ethical issues
Why it's not recommended to extract Netflix's digital watermarking

## Page 17

17
01. current page topic
Data destruction03
File shredding is a data destruction technique, the process of permanently
deleting files stored on digital storage media to make them unrecoverable.
Key Features
Permanent deletion: The typical file deletion process only makes the file
inaccessible to the user, but the actual data is still on the storage medium and
can be restored with certain recovery tools. File shedding blocks this recovery
possibility.
Comply with security standards: Several security organizations or agencies have
standards for data destruction.
For example, Department of Defense (DoD) standards, National Institute of
Standards and Technology (NIST) guidelines, etc. These standards specify the
pattern and number of overwrites that can be applied when shedding files.
Applications
Secure disposal of sensitive information: Used when you need to securely delete
files containing sensitive information, such as personal information, financial
records, confidential documents, etc.
Data erasure before device sale or disposal: Used to securely erase personal data
before selling, donating, or disposing of unused computers or storage media.

## Page 18

18
01. current page topic
Data destruction03
Evaluate the efficiency and reliability of the file shedding process
Review security standards and protocols: Review whether the method used for file shedding
meets international security standards or protocols (e.g., DoD 5220.22-M, NIST SP 800-88).
Verify the overwrite pattern and number of times: Verify that the pattern and number of
times data is overwritten is sufficient to make data recovery practically impossible.
Detect and analyze data that remains unsharded
Use digital forensic tools: Use advanced digital forensic tools (e.g., EnCase, FTK) to scan the
entire storage medium for errors in the shedding process.
scan the entire storage medium and find traces of data that was missed during the shedding
process or deleted in error.
deleted due to errors in the shedding process.
Recovery attempts: If evidence is found that certain areas were not completely overwritten
during the shedding process, you can attempt to recover data from those areas to assess the
integrity of the shedding
Physical analysis: especially for flash memory-based storage devices such as SSDs,
certain data erasure techniques may not always be 100% effective
Specialized equipment can be used to analyze traces of remaining data on a physical level
Factors to watch out for
Legal and ethical considerations: Detecting and analyzing shaded data or traces of it must
follow lawful authority and procedures and adhere to ethical standards such as privacy
Technical limitations: If proper file shedding techniques are used, data recovery may be
virtually impossible, so be aware of these limitations when working with them

## Page 19

19
01. current page topic
Data destruction03
Disk wiping is a data destruction technique that permanently erases data from an entire hard drive or
other storage medium, making it unrecoverable. data across a hard drive or other storage medium, making
it unrecoverable.
Key Features
Permanent deletion: Disk wiping permanently erases stored data so that it cannot be recovered.
This is a level of deletion that cannot be restored using data recovery tools.
Overwriting: The process of wiping overwrites the area where data was stored with random data,
data in a specific pattern, or all 0s or 1s. It is common to repeat this overwrite several times.
Compliance with security standards: Disk wiping is performed in compliance with various security standards
and regulations
Applications
Data security: Used to protect personal or corporate information before securely disposing of or reusing
storage media containing sensitive data.
Information leakage prevention: Block potential data leaks from unused computers or external hard drives
Compliance: May be required by organizations handling sensitive data to meet certain industry regulations
or legal requirements.
Cautions
Legal and ethical considerations: Detecting and analyzing wiped data or traces of it must be done in
accordance with legal authorizations and procedures.
Must follow lawful authority and procedures and adhere to ethical standards, including privacy.
Recognize technical limitations: If the wiping process was performed correctly, data recovery is virtually
impossible. Evaluating the efficiency and completeness of the wiping process focuses primarily on the
appropriateness of the process and technical approach. Disk wiping is an important part of data security
management and, when performed correctly, one of the surest ways to prevent data recovery. Proper
planning and procedures are required to ensure the reliability and completeness of the wiping process.

## Page 20

20
01. current page topic
Data destruction03
Evaluate the disk wiping process
Review wipe records and logs: Review records or logs generated during the
wipe process to verify that the wipe completed successfully, and that the
wiping method used was appropriate.
Verify compliance with security criteria: Review that the wiping method
used meets the security criteria that should apply to your environment(e.g.,
DoD 5220.22-M, NIST SP 800-88) that should apply to your environment.
Detect and analyze data that remains unwiped
Leverage digital forensics tools: Use advanced digital forensics tools to scan
storage media and find traces of data that was missed or not properly
deleted during the wiping process.
Data recovery attempts: If an unwiped area is found, data recovery is
attempted from that area to assess the completeness of the wipe. This
means that some of the data stored in the past may still be recoverable.
Validate wiping methods: Validate that the methods used for wiping are
appropriate for the specific type of storage media (e.g., SSD vs HDD).
Especially for SSDs, general data wiping methods may not always be
effective, so SSD-specific wiping techniques may be required.

## Page 21

21
01. current page topic
Data destruction03
Data overwriting is a data destruction technique that involves writing new data multiple times
to the area where the original data was stored in order to render the stored information
unrecoverable.
Key Features
Prevent recovery: Data is overwritten by replacing the original data with new data,
making it impossible to recover the original data, even with recovery tools.
Using patterns: The data overwriting process uses random data or data in a specific pattern
(e.g., all 0s, all 1s, or a combination of specific patterns) on top of the original data.
multiple overwrites
Standards compliance: The process may be performed in accordance with specific security
standards and guidelines (e.g., DoD 5220.22-M, NIST SP 800-88), which specify the patterns that
should be used when overwriting data and the number of overwrites.
Courses
1.Single-pass overwrite: At its most basic, it overwrites the entire storage space once, which may
be appropriate for relatively low security requirements
2.Multi-pass overwrite: If you require a high level of security, overwrite the data storage area
multiple times (typically three to seven or more times). Each pass can use a different data pattern,
3.Verification: After the overwriting process is complete, some tools provide a process to verify
the storage medium to ensure that the data is finally permanently deleted.

## Page 22

22
01. current page topic
Data destruction03
Detecting data overwriting
"Detecting" the data overwriting process itself is not the same as finding the hidden data.
Rather, it's more of a process of verifying that the overwrite was complete and what method
was used.
1.Identify overwrite patterns: Certain data overwriting software uses specific patterns during
the overwriting process. Digital forensic tools can be used to scan storage media and
determine the presence of these patterns.
2.Review logs and reports: Software that performs the overwrite process often generates log
files or reports
Analyzing data overwrites
Analyzing the traces of data that remain after the data overwriting process is complete is
difficult because a properly performed overwrite renders the data unrecoverable.
1.Leverage forensic analysis tools: Using advanced forensic analysis tools, analyze the drive
that was overwritten and determine if the data was completely erased or not, and identify any
remaining data fragments or areas that the overwrite did not reach.
2.Attempt data recovery: For research purposes, you can attempt to recover data from a drive
that has undergone the overwrite process. This is to evaluate the effectiveness of the
overwrite; successful recovery may indicate vulnerabilities in the overwrite method.
3.Evaluate technical limitations: Some storage media, especially SSDs, may overwrite data
incompletely, which is related to limitations in data overwriting technology
