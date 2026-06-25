---
title: "18강_Dead_Forensic_분석기법_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\18강_Dead_Forensic_분석기법_v1.2.pdf"
source_size_bytes: 595365
source_modified: 2025-10-18T19:41:59
imported_at: 2026-06-14T14:25:09
tags:
  - acs
  - acs-advanced
  - imported
---

# 18강_Dead_Forensic_분석기법_v1.2

- Source: [18강_Dead_Forensic_분석기법_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/18%EA%B0%95_Dead_Forensic_%EB%B6%84%EC%84%9D%EA%B8%B0%EB%B2%95_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Dead Forensic Analysis
Techniques
• Scenario overview
• Scenario goals
• Lab Procedure
18
1

## Page 2

2
Scenario overview01
Your organisation's research and
development department has discovered
that sensitive technical documents have
been leaked externally.
Initial investigation suspects the PC of
recently departed researcher A as the
source of the breach
Live forensic analysis collected and analyzed
technical documentation leak information from
Researcher A's PC, The analysis reveals that
Researcher A had a conversation with a colleague,
Researcher B, about the technical breach.
TOP SECRET

## Page 3

3
Scenario goals02
03
04
01
02
Obtain evidence of technical breach-related conversations
 Find chat logs, emails, messages, etc. between researchers A and B to obtain
evidence of conversations about the breach.
Analyze communications with those involved
 Analysing Researcher B's communications with others involved in the breach
Investigate data transfers to external sources
Investigate traces of leaked documents being sent externally via
email, cloud storage, external memory device usage history, etc.
Determine the existence of a technical document
 Finding a copy of or reference to a suspected compromised technical
document on Researcher B's PC

## Page 4

4
Lab Procedure03
Purpose
Evidence preservation: To maintain the integrity and authenticity of digital
evidence. it is important to preserve it in its original state
Legal compliance: The seizure and imaging process must be conducted in
accordance with legal procedures, and documentation of due process is
essential
Courses
Seizure: Researcher B's PC was seized based on legal authority.
The seizure is recorded in a chain of custody document
Imaging: Create an exact copy of the hard drive using a forensic imaging tool
(e.g. FTK Imager, dd). Use the image file created during this process as a
working copy for analysis.
STEP 1. Seize and image Researcher B's PC

## Page 5

5
Secure legal permissions
Obtain a warrant: A warrant must be issued by a court to authorise
the seizure and imaging of evidence.
The warrant must specify the seizure and examination at a particular
location or the copying of specific data.
The Scope of the warrant: The warrant must clearly define the type of
equipment that can be seized, the type of data to be seized, and the
time and place where the seizure and imaging can take place.
Seizure process
Create a seizure inventory: All equipment and storage media seized
should be accurately recorded, as this list will serve as important
documentation in subsequent legal proceedings.
Document the seizure: The seizure process should be documented in
detail by taking photographs, recording video, etc. This will be used in
subsequent legal challenges to prove the condition of the evidence
and the legality of the seizure.
STEP 1. Seize and image Researcher B's PC
Lab Procedure03

## Page 6

6
The imaging process
Forensic imaging: Forensic imaging tools are used to create an exact
replica of the digital storage media The imaging process is performed
using write protection tools to maintain the integrity of the data
Hash value generation: Generates a hash value (e.g. MD5, SHA-1) to
ensure the integrity of the imaged data. This hash value is used to verify
that the original data and the imaged data are an exact match.
Maintaining the chain of custody
Chain of custody documentation: All movements, accesses, and changes to
seized evidence and created image files are detailed in chain of custody
documentation. Documentation ensures the integrity of the evidence and
allows it to be used as evidence in court.
Legal Hold and Access Control
Secure storage: Confiscated equipment and image files should be stored in a
secure, restricted-access
secure and restricted access
Access control: Access to evidence is only allowed to authorized personnel,
all access is recorded in a chain-of-custody document
STEP 1. Seize and image Researcher B's PC
Lab Procedure03

## Page 7

7
STEP 2 . Analyze the file system
Purpose
Find evidence: Gain evidence by finding traces of leaked technical documents or related data.
Courses
Recover deleted files
Tools to use : File recovery tools such as Recuva, TestDisk, FTK, EnCase, etc.
Course description: Deleted files have their addresses removed from the file system, making
them inaccessible by normal means Recovering files using file recovery tools works in a way
that doesn't compromise the integrity of the file system during the recovery process
Time analysis
Tools to use : Forensic tools such as EnCase, FTK, Autopsy, and others.
Course Description: Analysing the metadata of files to determine when they were created,
modified, and accessed to estimate the timeframe of the breach event and track activity
related to the event.
Lab Procedure03

## Page 8

8
STEP 2 . Analyze the file system
DEC
Recover deleted files
When you "delete" a file from your computer or other digital storage device, the data doesn't immediately physically disappear.
In most cases, the file system merely marks the space the file was occupying as "free," but does not immediately erase the data itself.
These characteristics make it possible to recover deleted files using digital forensic tools and techniques.
Basic principles of deleted file recovery
Understand the nature of deleted files: In most file systems, when you delete a
file, the file metadata is removed or the area where the file was stored is marked
for reuse. However, the actual data may still remain on the storage medium
Understand the structure of the file system: Different types of file systems (e.g.,
NTFS, FAT, HFS, etc.) store files differently and handle deletions differently. It is
important for forensic investigations to understand the exact structure of the file
system in question.
Detecting unallocated space: Deleted files are usually left in unallocated space on
the file system. The recovery process intensively scans this space to find
recoverable files.
Cautions
Prevent data overwriting: During the process of recovering deleted files, care
must be taken to avoid performing write operations on the original storage
media. Write operations may permanently corrupt recoverable data.
Legal and ethical considerations: File recovery operations must be conducted
under appropriate legal authority and require ethical considerations related to
individual privacy. Deleted file recovery plays an important role in digital forensic
investigations and can contribute to understanding the circumstances of an
incident and securing evidence.
How to recover deleted files
Use digital forensic tools: Forensic tools such as EnCase, FTK, and
Autopsy provide the ability to find and recover deleted files. These tools
scan unallocated space, analyze file signatures or file structure to
identify deleted files.
Analyze file signatures: A file signature (or magic number) is a unique
sequence of bytes at the beginning of a file that can identify the file
type. Analytics tools can use this signature to find specific file types.
Consider slack space and file fragmentation : File recovery can be
complicated by slack space or file fragmentation. Slack space refers to
the unused space between the end of a file and the end of a cluster,
while file fragmentation refers to the state in which files are stored in
multiple locations.
Recover metadata and file contents: If possible, recover the file's
metadata (creation date, modification date, file size, etc.) along with its
actual contents. Metadata can provide important clues to the
investigation
Lab Procedure03

## Page 9

9
Time analysis
Analyse the time information recorded in files and directories to determine when specific activities occurred and reconstruct the timeline of an
incident. Temporal analysis can help investigators understand the sequence and timing of activities related to an incident based on when data was
created, modified, accessed, deleted, etc.
Key elements of time analytics
MAC time
Modified: The last time the file was modified.
Accessed: The last time the file was accessed.
Created: The time the file was created.
Modified File Time (MFT) record change time
 (on NTFS file systems): The time the file's metadata was modified.
Log files and system events
 Time information collected from operating system and application log files.
Includes the timing of activities such as system events, login attempts, and
software installation and execution.
The importance of time analytics
Reconstructing the chronology of activity: Reconstruct a complete timeline of
events by understanding the sequence of file and system activity.
Malicious activity detection: Identify times of malicious activity, such as
malware execution, unauthorized access, and data exfiltration.
Correlate evidence: Analyze associations between related evidence based on
temporal information collected from different sources.
The importance of time analytics
Reconstructing the chronology of activity: Understand the sequence of file and
system activity to build a complete
timeline of events
Malicious activity detection: Identify the timing of malicious activity, such as
malware execution, unauthorized access, and data exfiltration.
of malicious activity
Correlate evidence: correlate related evidence based on temporal information
collected from different sources
based on temporal information collected from different sources.
How to analyze time
Extracting time information: Extract time information from file system metadata,
log files, event logs, and more
Timezone verification and adjustment: Adjusting collected time data to reflect the
correct time zone. This is especially important for international incidet investigations.
Create a timeline: Use the extracted temporal information to create a timeline of
incident-related activities. In this course, you will be able to use visualisation tools to
clearly present the results of your analysis
Verify the reliability of time information: System clock errors, changes in timezone
settings, and timestamp manipulation can affect the accuracy of time information,
requiring reliability verification.
Lab Procedure03
STEP 2 . Analyze the file system

## Page 10

10
Purpose
Collect conversational evidence: Find evidence of conversations or discussions about the breach
incident
Courses
Message and email analytics using
Tools to use : Email analysis tools such as X-Ways Forensics, EnCase, Autopsy, and others.
Course Description: Analysing the databases of email clients and messaging apps to find breach-related
conversations. This course includes analysing email headers, bodies, and attachments to gather direct or
indirect evidence of the breach.
SNS research
Tools to use : Open source intelligence (OSINT) tools, SNS analysis platforms
Course description: Analyse activity logs and public posts from SNS accounts to identify breach-related activity.
This includes analysing not only public posts, but also private information such as login history and message
exchanges. It is important to comply with privacy and legal regulations in this process.
Lab Procedure03
STEP 3 . Analyze communication history

## Page 11

11
DEC
Message and email analytics
The process of analyzing the content of incident-related communications to gather evidence and trace the path of an incident.
This is especially important when analyzing communication between individuals or communication within an organization.
The importance of message and email analytics
Identify communications: Understand the context of the incident by
identifying dialogue, instructions, and information exchanges related to
the incident.
Securing evidence: Find direct or indirect evidence of the incident in the
content of messages and emails.
Identify the people involved: Identify the people involved in the incident
and the relationships between them.
Time zone and activity tracking: Timestamps in messages and emails
help you understand the timeframe of events and track related activity
Tools and techniques
Forensic software: Forensic tools such as EnCase, FTK, and Autopsy
support the extraction and analysis of email and message data for
extraction and analysis.
Email analytics tools: Use professional email analytics tools like
MailXaminer, Emailchemy, and others to efficiently analyse your email
data.
Communication analysis tools: Mobile forensics tools such as Cellebrite
and Oxygen Forensics support message extraction and analysis from
mobile devices. Message and email analysis is a key component of
digital forensic investigations, playing an important role in
understanding the full context of an incident and securing evidence.
Lab Procedure03
STEP 3 . Analyze communication history

## Page 12

12
DEC
Message and email analytics
The process of analyzing the content of incident-related communications to gather evidence and trace the path of an incident.
This is especially important when analyzing communication between individuals or communication within an organization.
How to analyze messages and emails
Data extraction and retention: Extract messages and email data from email servers, clients, mobile devices, and more.Copying and preserving data using
forensic methods to maintain data integrity.
Metadata analysis: Analyses the metadata of messages and emails to determine information such as sender, recipient, time sent, IP address, and more.
Content analysis: Analyzing the content of messages and emails in detail to find information relevant to the case.
This process may utilize keyword search, pattern analysis, and language analysis tools
Attachment analysis: Analyse attachments included in messages or emails to find leaked documents, malware, critical evidence, and more.
Social network and relationship analysis: Identify the networks involved in an incident by analysing the relationships between senders and receivers. This
helps to identify the parties involved in the incident and understand the communication patterns between them.
Legal requirements and privacy: Comply with legal requirements in your analytics, respect privacy principles
Lab Procedure03
STEP 3 . Analyze communication history

## Page 13

13
DEC
Analyzing SNS databases
Critical to digital forensic investigations, especially in analyzing communications, behavior patterns, and relationships between individuals
SNS data can provide critical evidence in a variety of cases, including cyberbullying, fraud, data breaches, copyright infringement, and more.
The importance of analyzing SNS databases
Track communications: understand the context of an incident by
recording conversations, shared content, and message exchanges
between those involved. records, etc. to understand the context of the
incident
Behavioral pattern analysis: Analyze a user's posts, likes, comments,
sharing activity, and more to determine to identify patterns of behavior
at specific times of day or changes in behavior before and after an event
Understand the network of relationships: through friend lists,
follow/following relationships, co-participating groups, etc.
connections between people involved in an incident
Identify incident-related content: images of leaked documents,
copyrighted content, fraud-related ads, and other content directly
related to the incident.
Analyzing SNS databases is becoming increasingly important in digital
forensic investigations, and can provide crucial evidence to solve cases .
Always keep ethical considerations such as privacy and legal compliance
in mind during the analysis process
Lab Procedure03
STEP 3 . Analyze communication history

## Page 14

14
Analyzing SNS databases
Critical to digital forensic investigations, especially in analyzing communications, behavior patterns, and relationships between individuals
SNS data can provide critical evidence in a variety of cases, including cyberbullying, fraud, data breaches, copyright infringement, and more.
How to analyze SNS databases
Serving legal process: To access SNS databases
comply with appropriate legal process
Law enforcement can request the data they need from SNS companies through a court order or search warrant
Data extraction and retention: Data obtained through requests must be extracted and retained securely for analysis.
securely extracted and retained for analysis Maintaining data integrity and chain of custody is critical
Leverage analytics tools: Leverage specialized tools for SNS data analysis (e.g., X1 Social Discovery, Magnet AXIOM) to analyze data
These tools are designed to efficiently process large amounts of data and, Helps you identify relevant information
Content and metadata analysis: Analyzes not only the content of posts, but also metadata such as time of publication, geolocation, device
information, and more. This helps you understand the full context of the incident and the behavior patterns of those involved.
Lab Procedure03
STEP 3 . Analyze communication history

## Page 15

15
Purpose
Device connection tracking: Track external storage devices, such as USB drives, external hard
drives, SD cards, etc. connected to a computer or network device.
Identify data leakage paths: Understand how external devices may have been used to leak data
Courses
Review system logs: Review the operating system's system logs and event logs to understand
when external devices were connected and removed.
Analyze the registry (Windows): On Windows systems, analyze the registry keys such as
SYSTEM\CurrentControlSet\Enum\USBSTOR, etc.
registry keys to determine information about connected USB devices.
File access history: Stored on a connected external device or in the
Examine the history of accessed files to understand what data was moved
Lab Procedure03
STEP 4 . Investigate external device usage history

## Page 16

16
DEC
Analyze external storage device usage history
External storage devices, such as USB drives, external hard drives, and SD cards, can be tracked and analyzed when they were connected to a
particular computer or device. This information can provide critical evidence in a variety of cases, including data breaches,illegal content transfers,
and malware propagation.
The importance of analyzing external storage usage history
Data breach tracking: Determine if data was exfiltrated via external storage devices and what kind of data was exfiltrated
Determining malware infection vectors: Whether malware was propagated via external storage devices via external storage
Monitor user activity: You can track user activity by looking at the history of when external storage devices were connected during specific times of day
Cautions
Secure a legal basis: We need lawful authorization to analyze external storage device usage history. It is important to comply with legal processes.
Maintaining the chain of custody: Ensuring the integrity of evidence during analysis, chain of custody of evidence during the analysis process
Analyzing external storage device usage history is an important part of digital forensic investigations, providing critical information that can contribute to
securing evidence and solving cases.
Lab Procedure03
STEP 4 . Investigate external device usage history

## Page 17

17
DEC
How to analyze external storage usage history
Investigate log files
The operating system records external storage devices in log files when they are connected. The registry contains the connection history of external
storage devices. By analysing the USBSTOR key and the MountedDevices key, you can determine when the device was connected, the device name,
and when the device was last connected.
Analyze system log files (Linux, macOS)
Linux and macOS record the connection and disconnection of external storage devices in a system log file. This log file can be analysed to determine
the device's connection history.
Analyze the file system of an external storage device
If you can obtain a physical external storage device, you can analyse the device's file system to investigate file creation, modification, access times,
etc. This is useful for determining when data was copied to or modified on the device
Lab Procedure03
Analyze external storage device usage history
External storage devices, such as USB drives, external hard drives, and SD cards, can be tracked and analyzed when they were connected to a
particular computer or device. This information can provide critical evidence in a variety of cases, including data breaches,illegal content transfers,
and malware propagation.
STEP 4 . Investigate external device usage history

## Page 18

18
DEC
Cloud storage analytics
The process of extracting and analyzing data from cloud-based services to obtain evidence for a case.
Because data in cloud environments has no clear physical location and can be shared among many different users and devices, it requires a different
approach than traditional digital forensics methods.
The importance of analyzing cloud storage
Data accessibility: Cloud services allow data to be accessed anytime, anywhere.
This means cloud storage can be used by criminals to store, share, and delete data.
to store, share, and delete data.
Multi-user environments: Cloud environments allow multiple users to access and work on data simultaneously.
This makes it important to track changes to data and identify the activity of specific users.
Data synchronization and backup: Cloud storage offers automatic synchronization and backup, giving you the possibility to recover deleted data
or even older versions of documents.
How to analyze cloud storage
Serving legal process: To access cloud data.
Need appropriate legal authorization (e.g., search warrant)
Obtaining data access from cloud service providers through legal process
Data extraction: With the cooperation of the cloud service provider or,
using forensic tools to extract data from cloud accounts.
It's important to maintain the integrity of the data during the extraction process
Lab Procedure03
STEP 4 . Investigate external device usage history

## Page 19

19
DEC
Cloud storage analytics
The process of extracting and analyzing data from cloud-based services to obtain evidence for a case.
Because data in cloud environments has no clear physical location and can be shared among many different users and devices, it requires a different
approach than traditional digital forensics methods.
Analyze your data
Analyze account information: Analyze user account information, access permission settings, account activity logs, and more to identify relevant
activity.
File analysis: Analyze stored files, documents, images, and more to find evidence related to an incident; file metadata analysis can reveal when they
were created, modified, deleted, and more.
Shared and collaboration history analysis: Analyze sharing history in cloud storage, change history of collaborative documents, etc. to track
communication and activity between involved users
Write a report: Write a report on the incident based on the data you collected and analyzed.
Report should include evidence found within cloud storage and the results of your analysis
Tools and techniques
Tools for cloud storage analysis include ElcomSoft, Oxygen Forensics, and Magnet AXIOM Cloud, which specialize in extracting and analyzing data
from cloud services.
Lab Procedure03
STEP 4 . Investigate external device usage history

## Page 20

20
Analyze network traffic
The process of capturing and analyzing data packets sent over a network to obtain and analyze evidence of an incident.
This method is used to investigate a variety of incidents, including cyberattacks, data breaches, and illegal content transfers.
The importance of network traffic analysis
Trace the path of an incident: Network communication records can reveal the attacker's IP address, the time of the attack attempt, the tools used,
and more.
Investigate data breaches: Track how and when sensitive data was exfiltrated and determine what kind of data was compromised.
Malware communication detection: Detect the presence and activity of malware by capturing malware as it communicates with command and
control (C&C) servers over the network.
User behavior analysis: Analyze network usage patterns to identify unusual activity or policy violations.
Caution
Secure the legal basis: It is important to have the right permissions and procedures in place before capturing and analyzing network traffic.
Privacy: You may handle personal information during analysis, so you must comply with privacy laws and policies.
Lab Procedure03
STEP 4 . Investigate external device usage history

## Page 21

21
DEC
How to analyze network traffic
Capture traffic: Use tools such as Wireshark and tcpdump to capture network packets. These tools allow you to monitor the network in real time and
capture data packets.
Data flow analysis: Analyze captured data packets to determine the direction of network communication, source and destination IP addresses, port
numbers used, protocols, etc.
Session reconstruction: Reconstruct network communication sessions by piecing together multiple packets and verifying the content of the data
transmitted, which is especially useful for unencrypted text communications.
Protocol analysis: Analyze communications using specific protocols, such as HTTP, FTP, and SMTP, to investigate web browsing history, file transfer
history, email communication history, and more.
Malicious behavior detection: Detect signatures of known malware, unusual communication patterns, communication with known malicious IP
addresses, and more in network traffic.
Leverage analytics tools: Perform analysis using network analysis tools (Nmap, Nessus, Snort, etc.), packet analysis tools (Wireshark, tcpdump, etc.),
log analysis tools (Splunk, ELK Stack, etc.), etc.
Lab Procedure03
Analyze network traffic
The process of capturing and analyzing data packets sent over a network to obtain and analyze evidence of an incident.
This method is used to investigate a variety of incidents, including cyberattacks, data breaches, and illegal content transfers.
STEP 4 . Investigate external device usage history

## Page 22

22
What is the forensic timeline
The process of creating a visual representation of all activities related to an incident, arranged in
chronological order. This analysis allows investigators to systematically understand the activities
before, during, and after the incident, and provides a complete picture of the incident. Timeline
analysis is conducted by integrating temporal information from various data sources (file systems,
log files, emails, communication records, etc.).Translated with www.DeepL.com/Translator (free
version)
Purpose of forensic timeline analysis
Reconstruct the chronology of activities: Reconstructing the chronology of an incident by
arranging all relevant activities and events before and after the incident in chronological order.
Identify critical events: Identify specific events or activities that played a role in the incident.
Cross-evidence correlation: Analyze temporal correlations between evidence from different
sources to understand the full context of an event.
Visualization of analysis results: Create visual representations of incident-related information for
better understanding, report writing, and presentations.
Lab Procedure03
STEP 5 . Analyze the forensic timeline

## Page 23

23
Lab Procedure03
STEP 5 . Analyze the forensic timeline
Forensic timeline analysis process
Data collection: Collect data, including time information, from file system metadata, log files,
email headers, communication logs, and more.
Extract temporal information: Extract temporal information such as creation, modification, access,
and deletion times (MAC time) from the collected data.
Generate a timeline: Create a timeline based on the extracted time information; you can use the
tool to automatically create a timeline or manually arrange important events.
Timeline analysis: Analyze the generated timeline to understand the key events and the
chronological sequence of activities in an incident, identifying key inflection points along the way.
In the process, you can identify how events unfolded and critical inflection points
Visualize and report on your results: Visualize the results of your analysis in the form of tables,
graphs, time axes, etc. and include them in your reports. A visually represented timeline can
enhance your understanding of a case and can be used to present evidence in court.
Tools and techniques
Tools such as Autopsy, Log2Timeline, Plaso, and TimeSketch are often used for forensic timeline
analysis. These tools provide the ability to extract temporal information from large amounts of
data and automatically generate timelines to efficiently support the analysis process.

## Page 24

Build reports
Organize evidence and analysis gathered during the investigation and present conclusions about the incident.
Analyzing the cause of the incident and identifying the source of the breach, and proposing recommended actions to prevent similar
incidents in the future.
Drafting: Based on all evidence and analysis, draft a report that includes an overview of the incident, investigation methods, analysis
results, conclusions, and recommended actions.
Organize the content: Your report should be easy to understand and organized, and if necessary, you can use graphs, tables, images,
etc. to visually represent your findings.
Conclusions and recommended actions: Draw conclusions about the incident based on your findings and provide specific
recommended actions to prevent breaches and enhance security.
Lab Procedure03
STEP 6 . Organize and report analysis results

## Page 25

25
Review and approval
Undergoing internal review and approval to ensure the accuracy and completeness of the report.
Gain the understanding and buy-in of relevant parties to ensure the credibility of the investigation findings.
Internal review: Draft reports are reviewed within the investigation team to correct errors, missing information,
inaccurate analysis, etc.
Involved party submission: Submit the final report to the involved parties (management, security, legal, etc.) for review.
Approval and feedback: Get feedback from the involved parties, make any necessary changes, and get final approval.
Lab Procedure03
STEP 6 . Organize and report analysis results

## Page 26

26
Incorporate feedback received to further improve the accuracy and completeness of reports.
Increase understanding of your findings and ensure the credibility of your reports.
Collect feedback: Gather feedback on submitted reports.
Corrections and updates: Revise and update the content of the report based on feedback, and perform additional analysis if necessary.
Finalize: Submit the revised report for finalization and recommend any necessary actions.
Lab Procedure03
STEP 6 . Organize and report analysis results
Incorporate feedback
