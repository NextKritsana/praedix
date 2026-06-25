---
title: "17강_Live_Forensic_분석기법_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\17강_Live_Forensic_분석기법_v1.2.pdf"
source_size_bytes: 679660
source_modified: 2025-10-18T19:35:34
imported_at: 2026-06-14T14:25:08
tags:
  - acs
  - acs-advanced
  - imported
---

# 17강_Live_Forensic_분석기법_v1.2

- Source: [17강_Live_Forensic_분석기법_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/17%EA%B0%95_Live_Forensic_%EB%B6%84%EC%84%9D%EA%B8%B0%EB%B2%95_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Live Forensic Analysis
Techniques
• Scenario overview
• Scenario goals
• Lab Procedure
17
1

## Page 2

2
Scenario overview01
TOP SECRET
The suspected target is a PC belonging to
a recently departed researcher, from
which technical documentation may
have been exfiltrated.
Discovering that critical technical
documents were leaked from an R&D
department within your organization
Perform Live Forensic analysis of the
affected PC to investigate this incident

## Page 3

3
Scenario goals02
Collect volatile data such as processes running in system memory, network connections, login sessions, etc.
Collecting volatile data
Analyze network traffic at the time of the breach to investigate external communication activity
Analyze network traffic
Analyze security logs, system logs, application logs, and more to find traces of compromising behavior
Analyzing log files
Investigate access, modification, and deletion history for sensitive documents
Investigate document access history
Analyze usage history from USB drives, external hard drives, etc.
View external storage device usage history

## Page 4

4
Lab Procedure03
Prepare
Collect
Analytics
Reporting
Live Forensic lab procedure
Have what you need on hand
Follow Digital Forensics collection procedures to collect data
Analyze the data you collect with analytics tools
Build reports with procedures

## Page 5

5
Lab Procedure03
Preparing for Live Forensics
Prepare 1. Data collection tools
Forensic software kit: Software for securely collecting and analyzing digital
evidence (e.g., EnCase, FTK, Wireshark, etc.)Live boot USB/CD: A live boot
tool that allows you to access your system without making any changes.
External storage device: External hard drive or USB drive to store collected
dataWrite
Protection tools: Physical or software-based write protection tools that
protect evidentiary data from alteration.

## Page 6

6
Lab Procedure03
Preparing for Live Forensics
Prepare 2. Documentation and recording tools
Report form: A report form for recording collected data and observations.
Investigative journal: A notebook or digital recording tool to record
fieldwork, time, date, actors, and other information.
Camera or video recorder: Photographic or videographic equipment to
record scene conditions and the condition of evidence.
Labeling and marking tools: Pens, stickers, and tags to record identifying
information about evidence and evidence envelopes.

## Page 7

7
Lab Procedure03
Preparing for Live Forensics
CoC
Electronic
Evidence
Submission
Form
Chain of custody (CoC) form
To document the collection, movement, and storage of evidence to demonstrate the integrity and reliability of the evidence.
This includes the date and time the evidence was collected, who collected it, a detailed description of the evidence, the route it
traveled and who traveled with it, and the condition of the evidence.
Documentation that is essential to establish the reliability of the evidence if it is used as evidence in court.
Incident Report
To document the occurrence of a security incident, such as a technical breach, and record the details of the incident.
Includes the date and time of the incident, evidence of the breach found, types of technical documents compromised, possible
breach vectors, circumstances surrounding the incident, and initial response actions.
Serves as a starting point for incident investigations and contributes to policy formulation to prevent similar incidents in the future.

## Page 8

Analysis
Report
Incident
Report
8
Lab Procedure03
Preparing for Live Forensics
Electronic Information Verification Form (Electronic Evidence Submission Form)
Used when submitting collected electronic evidence to an analysis department or outside expert to record the details of the
evidence submitted.
Includes the type of evidence (hard drive, USB, email, etc.), the physical/logical state of the evidence, how it was collected, and the
requested analysis of the evidence.
Provides information needed during the evidence analysis process and helps ensure that the results of the analysis accurately
match the context of the case.
Analysis Report
To organize the results of the analysis of the evidence collected and document the facts discovered during the analysis.
Includes the tools and methodology used in the analysis, the evidence found and the facts to which it points, and the
interpretations and conclusions about the results of the analysis.
To be decisive in the determination of the case and provide a key basis for resolving the case.

## Page 9

9
Lab Procedure03
Preparing for Live Forensics
Prepare 3. evidence archiving tools
Antistatic bags: packaging to protect electronic equipment from static
electricity.
Evidence envelopes: envelopes for evidence storage made of paper or
plastic; envelopes should have space to record the details of the evidence.
Security seal or tape: A security seal or tape that seals an evidence envelope
or box and makes it easy to determine if it has been opened.
Evidence storage box: A box for categorizing and storing multiple items of
evidence.

## Page 10

10
Lab Procedure03
Preparing for Live Forensics
Prepare 4. Plan ahead and check for compliance
Antistatic bags: packaging to protect electronic equipment from static
electricity.
Evidence envelopes: envelopes for evidence storage made of paper or
plastic; envelopes should have space to record the details of the evidence.
Security seal or tape: A security seal or tape that seals an evidence envelope
or box and makes it easy to determine if it has been opened.
Evidence storage box: A box for categorizing and storing multiple items of
evidence.

## Page 11

11
Lab Procedure03
Live Forensic Ingestion Process
Determine system health: Determine the current state of the system and gather initial information that does not impact
analysis (e.g., current time, running processes)
Obtain authorization: Access the PC under investigation with the appropriate permissions and procedures; if necessary,
take steps to obtain legal authority.
Start documenting: Document every step you take during the analysis process, including the time you started, tools used,
initial system state, etc.
Perform a memory dump: Securely dump a complete memory image of your system, which provides important
information for subsequent analysis.
Running processes and services: Collect a list of all currently running processes and services.
Network connection information: Collect information about currently active network connections, open ports, network
statistics, etc.
User accounts and login sessions: Collect information about the currently logged in user and recent login sessions.
Initial research and documentation
Volatile data

## Page 12

12
Lab Procedure03
Log file review: Review system logs, security logs, application logs, and more to detect activity related to the breach
incident.
Examine documents and files: Examine access, modification, and deletion history of suspected compromised documents
and files.
Examine external storage device usage history: Trace the path of a data breach by examining the connection history of
external storage devices such as USB.
Secure collected data: Store collected data in a secure location and generate hash values for data integrity.
Documenting the collection process: Documenting in detail the type of data collected, the time it was collected, the tools
and techniques used, and the initial facts discovered.
Live Forensic Ingestion Process
Non-volatile data
VolatileData protection and additional documentation data

## Page 13

13
Lab Procedure03
Memory Dump
Aim to capture all information stored in system
memory, including the status of running processes,
open files, network connections, and more. Using a
memory dump tool such as Volatility, FTK Imager, or
DumpIt. Depending on the tool, a memory dump
should typically be performed via command execution
or GUI with as little system impact as possible.
Running processes and services
Identify suspicious activity or malicious processes by
understanding the processes and services running on
your system. In Windows, you can use Task Manager,
Process Explorer, PowerShell, etc.; in Linux, use ps, top
command, etc. Capture a list of running processes
using the appropriate tool for your system and, if
necessary, record the process ID, username, execution
path, etc.
Network connectivity and status
Check the currently active network Identify connections
to the outside world by viewing currently active
network connections and open ports, which can help
you trace the path of a leak. Use the commands
netstat, tcpview on Windows, netstat, ss on Linux. Use
the network health check tool to gather a list of
currently active connections and open ports, recording
the external addresses and port numbers connected.
Login sessions
View information about the current and last logged-in
users to get information about system access. Use the
quser and qwinsta commands or PowerShell scripts on
Windows, or the who, w, and last commands on Linux.
Use a tool to view user session information to gather
information about the currently logged in user and
recent login sessions.
Volatile data
Live Forensic Ingestion Process

## Page 14

14
Lab Procedure03
Live Forensic Ingestion Process
Non-volatile data
Secure storage media
Identify and secure all storage media on the system
under investigation, which can include hard drives,
external hard drives, USB drives, SD cards, etc. It is
important to prevent data loss or tampering during the
storage media acquisition process.
Data imaging
The process of creating an exact copy (image) of the
data from the storage media under investigation is to
preserve the original data for data analysis while
preventing data corruption during the analysis process.
Various imaging tools are used, including FTK Imager,
dd (Linux), EnCase, Disk Drill, etc. Data imaging is done
while blocking write operations to the original data
using write-protection tools. When creating an image,
a hash value (e.g., MD5, SHA-1) can be generated to
verify the integrity of the image.
Collect log files and system information
Collecting operating system logs, security logs,
application logs, and system settings and
configuration information from your system. This
information is used to understand user behavior,
system access attempts, critical system changes, and
more. Log files and system information provide
important clues about system status and activity
before and after an incident occurs.
Preparing for data analysis
Getting your collected data images and information
ready for analysis can include organizing your data,
setting up analysis tools, and configuring your analysis
environment. It is important to properly prepare the
data to be analyzed for systematic and efficient
analysis.

## Page 15

15
Lab Procedure03
Live Forensic Analysis Course
The process of categorizing collected data by type.
This step organizes all the data obtained during the research process to facilitate
the analysis process.
Data types can include the following
Document files: Includes document files such as Word, PDF, Excel, etc. These
files may directly contain the content of the leaked information.
Emails: Email bodies and attachments can be important in tracing the path of a
breach or the flow of compromised information.
Log files: System logs, security logs, application logs, etc. may contain
information about when the breach occurred, associated user activity, suspicious
events, etc.
Memory dumps: These include running processes, network connections, in-
memory data, and more, and are important for understanding the state of the
system at the time of the incident.
Data classification

## Page 16

16
Lab Procedure03
Live Forensic Analysis Course
The process of deciding which of your categorized data to analyze first.
This process is necessary to make the most effective use of limited time and
resources.
Factors considered in prioritization include
Importance of the event: Prioritize analysis of data with high severity or impact.
Sensitivity of the data: Data containing sensitive information, such as personal
information or confidential documents, may be prioritized for analysis.
Potential for leakage: Data with a high potential for compromise, for example,
data that has been externally transferred or suspiciously accessed, is prioritized.
Evidentiary value: Data that contains evidence directly related to the incident or
information critical to tracing the path of the breach is prioritized for analysis.
Classifying and prioritizing data helps to organize the forensic analysis process,
increase the efficiency of the investigation, and quickly identify critical
information needed to resolve the incident.
Set analytics priorities

## Page 17

17
Lab Procedure03
Live Forensic Analysis Course
Analyzing volatile data
Volatile data is data that is lost when the system is turned off, and is stored in
the system's memory.
Analyzing memory dumps: Using memory dump files to extract information such
as running processes, open files and network connections, and login sessions.
Using tools like Volatility to analyze the contents of memory and identify
suspicious behavior or the presence of malicious code related to the breach.
Examine running processes: Identify and investigate running processes that may
be related to the breach event and find malicious processes or tools that may
have been used in the breach.
Analyze network connections and sessions: Analyze active network connections
to understand network activity at the time of the breach and track external
connections.
Data analysis process

## Page 18

18
Lab Procedure03
Live Forensic Analysis Course
Analyze non-volatile data
Non-volatile data is data that survives power outages and is stored on hard drives
or SSDs.
Hard drive image analysis: Create and analyze images of hard drives to recover
and review file access history, document creation and modification times,
deleted files, and more.
Log file analysis: Analyze system logs, security logs, and application logs to
identify activity related to the breach event.
Data analysis process

## Page 19

19
Lab Procedure03
Live Forensic Analysis Course
Analyze network traffic
Analyze network logs and captured traffic to investigate the path of a breach
and suspicious external connections.
Analyze network logs: Analyze logs generated by network equipment or servers
to identify attempted or successful exfiltration events.
Traffic capture analysis: Use tools like Wireshark to analyze network traffic and
trace the flow of exfiltrated data.
Data analysis process

## Page 20

20
Lab Procedure03
Live Forensic Analysis Course
Analyze documents and emails
Review documents and emails suspected of being compromised to identify
compromising information.
Review document content: Review the content of suspected leaked documents
to identify content related to the leaked information.
Email analysis: Examine email accounts to find communications or attachments
related to the breach Analyze email headers to determine sender and recipient
information, path of the message, and more.
Data analysis process

## Page 21

21
Lab Procedure03
Live Forensic reporting process STEP 1. Organize your analysis results
Analytics overview
Evidence and findings
Analysis results
Conclusions and recommended actions
Appendices
Incident overview: Provides an overview of the background, purpose, and work performed in the investigation.
Summary of collected data: Provides a summary by type of data collected, including volatile and non-volatile data, network traffic, documents, and emails.
Evidence found: A detailed description of key evidence found during the analysis.
This could include leaked documents, suspicious network activity, the presence of malicious code, etc.
Significance of evidence: Analyzes what each piece of evidence means to solving the case.
Explain how the evidence contributes to revealing how the breach occurred, when it occurred, who was involved, etc.
Breach vectors and methods: Provides an analysis of how the breach occurred and what methods were used.
Actors involved: If there were insiders or external attackers involved in the breach, provide information about their identities and roles.
Scope of compromised data: Describe the scope and significance of the compromised information.
Conclusions: Present conclusions drawn based on the results of the analysis.
Include a comprehensive assessment of the cause of the breach, the systems affected, and the actors involved in the breach.
Recommended actions: Recommendations for preventing similar incidents, enhancing security, and repairing the damage, which may
include improving security policies, updating system security, and enhancing employee training.
Tools and techniques used in the analysis: Provide details about the tools and analytical techniques used during the investigation.
References: Include a list of documents, guidelines, standards, etc. that were consulted during the analysis.
The process of compiling your findings provides an important foundation for developing a comprehensive understanding of all aspects of
the breach and identifying specific actions to strengthen your organization's security.
As such, this process should be very organized and detailed

## Page 22

References: Identify the sources, guidelines, legal standards, etc. that were consulted in preparing the report.
Evidence list: Include a list of evidence collected and analyzed during the investigation.
A report on a technology breach should be organized and clearly structured, detailing all aspects of the incident so that those involved can
fully understand the incident and formulate an effective response.
Conclusions: Conclusions drawn based on the results of the analysis about the cause of the incident, the scope of the information
compromised, and the people or groups involved.
Recommendations: Recommend specific actions to prevent the incident from happening again and to improve security, which may include,
for example, improving security policies, implementing security solutions, or increasing employee training.
Collection methods: Describe the data collection methods and tools used.
Analysis Techniques: Detailing the techniques and processes used to analyze the data.
Tools and techniques: Document the forensic tools and techniques used in the investigation.
22
Lab Procedure03
Live Forensic reporting process STEP 2. Build a report
Introduction
Survey methodology
Analysis results
Conclusions and recommendations
Appendices
Incident overview: Provides background and an overview of the incident investigated, including basic information about when and how it happened.
Purpose: Clarify the purpose of the report, which could be, for example, to determine the cause of the breach, identify those responsible, or recommend security
enhancements.
Scope: Describes the scope of the investigation, including which systems were investigated, what type of data was analyzed, and how long the investigation lasted.
Results of analyzing volatile data: Information gained and evidence found through memory analysis.
Non-volatile data analysis results: Includes results from analyzing hard drives and other storage media.
Network traffic analysis results: Describe the path of the breach and related information obtained through network logs and traffic analysis.
Document and email analysis results: Presents the results of the analysis of documents and emails suspected to have been compromised.

## Page 23

23
Lab Procedure03
Review and approval
Accuracy and integrity checks: Review the accuracy and integrity
of the analysis reports and findings, and ensure that the
investigation process complied with the organization's policies
and applicable laws.
Approval process: Ensuring that the final report and
recommended actions are approved by higher levels of
management or relevant departments in the organization, which
is important to ensure follow-up actions are enforceable.
Internal review: Review the report first within the investigation
team to ensure there are no errors or missing information.
Expert review: If necessary, an external expert can be asked to
review the report to further ensure the accuracy of the analysis.
Request approval: Submit the reviewed report to higher levels of
management for approval. Clearly present the report's key
findings and recommended actions.
Reporting and feedback
Share findings: Share findings and recommended actions with
stakeholders inside and outside the organization to maintain
transparent communication about the incident.
Gather feedback: Gather feedback on the report to identify
improvements to the investigation process and prevent similar
incidents.
Present the report: Present the approved report to relevant
departments and stakeholders. This can be done in a variety of
ways, including meetings, workshops, and emails.
Gather feedback: Collect questions and feedback from
stakeholders after the presentation. Feedback is used to improve
understanding of the report's content, refine investigation
methodologies, and update security policies.
Follow-up plan: Develop and execute a specific follow-up plan
based on the report's recommended actions and feedback.
Live Forensic reporting process
STEP 3. Review and approve
STEP 4. Reporting and feedback

## Page 24

24
Lab Procedure03
Archiving
Physical and digital security of evidence
Evidence should be stored in a secure, restricted-access location.
This applies to evidence in the form of digital files as well as
physical storage media.
For digital evidence, use encrypted storage devices or secure
network storage to protect it.
Maintain Chain of Custody
Accurately recording and maintaining the chain of custody of
evidence, including a record of who came into contact with the
evidence at all stages of its collection, transmission, storage, and
analysis. Chain of custody is essential to demonstrate the
integrity of evidence and can be used as a legal document.
Chain of custody (CoC) is a term used to track the handling of
evidence in a legal context, documenting the movement,
storage, and processing of evidence from the moment it is
collected until it is presented in court.
Recordkeeping
Documenting the investigation process
Document every step of the investigation.
Include all activities, from initial incident response to evidence
collection, analysis methods, analysis results, conclusions, and
recommended actions.
Documentation provides a basis for the investigation in later reviews or
legal proceedings.
Archiving analysis results and reports
Securely archive analysis results and final reports.
These may be used in future responses to similar incidents, as training
materials, or in any necessary legal proceedings.
Complying with legal requirements
Complying with the retention periods for evidence and documents in
accordance with applicable laws and organizational policies.
Some laws may require certain types of data to be retained for a
certain period of time.
Periodic review and update
Review evidence and documents in storage regularly to ensure they
meet current security requirements.
If necessary, update or add security measures.
In the investigation of a technology breach, archiving and
recordkeeping is an essential part of the process for accurate resolution
of the case and legal protection.
It helps to maintain the reliability of the information and evidence
collected and demonstrates the legitimacy of the investigation process.
Live Forensic reporting process STEP 5. Archiving and recordkeeping
