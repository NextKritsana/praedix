---
title: "04강_Cybersecurity Incident Guide and Manual_v.1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\04강_Cybersecurity Incident Guide and Manual_v.1.2.pdf"
source_size_bytes: 587127
source_modified: 2025-11-12T12:14:56
imported_at: 2026-06-14T14:26:22
tags:
  - acs
  - acs-advanced
  - imported
---

# 04강_Cybersecurity Incident Guide and Manual_v.1.2

- Source: [04강_Cybersecurity Incident Guide and Manual_v.1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/04%EA%B0%95_Cybersecurity%20Incident%20Guide%20and%20Manual_v.1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Cybersecurity Incident
Guide and Manual
• Cyber Safety Manual
• Data sharing schemes
• Cyber crisis alert stages
• Additional strategies
04
1

## Page 2

Cyber Safety Manual01
NIST SP 800 Series
2
• The NIST 800 series covers a variety of computer
security topics
• Includes guidelines and documents on information
security
NIST SP 800-53
Information Security Framework
and Guidelines
Provide a standardized framework
Reduce risk in the event of a cyber incident
NIST SP 800-171
Security Requirements for Nongovernmental
Organizations with Secret Information
Security requirements for organizations handling classified
information
Guidelines for manufacturers and contractors
NIST SP 800-61
Computer Incident Response Guidelines
Provide basic principles and guidance
Guidelines for some sort of incident response readiness
concept
NIST SP 800-30
Risk Management Guidelines
Proactively identify and manage risks to reduce harm
Proactively prevent harm to organizations and entities
NIST SP 800-171 A
Supplemental Guide to the Assessment Process of
NIST 800-171
Provides guidelines for assessing organizations to meet the requirements
of NIST 800-171

## Page 3

Efficient transfer
You need to react and respond quickly
Gather the latest threat information
Security
Appropriate passwords and permissions
Protect sensitive information
Data sharing schemes02
3
A data sharing scheme is a set of structures and processes for efficiently exchanging and sharing information and data between
organizations
Efficient transfer of information, use of standardized data formats and protocols
Security and privacy considerations
Requires standardized data formats and protocols, security and privacy, processes and regulations, and technical infrastructure
For sensitive information, appropriate access to and encryption of that data is required
Standardized data
Seamlessly communicate across
organizations
Ensure data consistency
Standardized protocols
Efficient communication
Seamlessly add new features or devices
Data sharing schemes?
The reason why a data sharing system in cyber is to prevent the spread
If a virus called A comes out and targets company B, company B can share that information with
other organizations to help them be more secure and improve the quality of their proactive response

## Page 4

Data sharing schemes02
https://www.cloudflare.com/ko-kr/learning/security/what-is-stix-and-taxii/
TAXII
 STIX
Protocol
Language
4
TAXII / STIX
Goals
Improve threat intelligence sharing
Enhance threat detection and response
Improve intelligence accuracy
Build
TAXII is a standard protocol created by an international standardization organization called
OASIS
STIX is a standard language developed by MITRE Corporation
Commonalities
• Quickly share threat information among various organizations and businesses
• Developed through the efforts and collaboration of international standardization
organizations and specific companies and research institutions
• Recognized as an important effort to enhance cooperation and information sharing in the
security community
• Seamless integration between applications, security tools, and services
Benefits
Security professionals can respond to cyber threats in real time
Get new threat information quickly
Encourage cross-organizational collaboration and automation

## Page 5

Data sharing schemes02
TAXII(Trusted Automated Exchange of Indicator Information)
TAXII
➢Features
5
■ Based on protocols such as HTTP and HTTPs, enabling secure and reliable
information exchange
■ Supports a variety of message exchange patterns, including Discovery, Inbox,
Poll, etc.
■ There are several versions, each of which evolves the protocol's features
■ Latest versions emphasize rapid transfer of data and responsiveness to
requirements
HTTP?
HTTPs use Transport Layer Security (TLS) for secure data exchange
Enhances security through authentication and authorization between client and server
Ensures the integrity of data in transit
Prevents data from being modified or tampered with in transit
Protocols that enable secure communication in terms of confidentiality, integrity, and security
of data, including identity verification

## Page 6

데이터 공유 체계02
STIX(Structured Threat Information eXpression)
Data sharing schemes
6
Provide multiple profiles
Gain flexibility by providing representations specialized for
specific security domains
Integrate with TAXII to securely exchange security information
Enables fast and effective information exchange between
organizational security personnel
Version 2.0
Enhanced version of the initial version
Contains more objects and properties
More flexible and expressive
Features
A language for structuring and exchanging threat
information
Promotes standardization and uniformity of security
information
Designed to be exchanged consistently across platforms
Standard data model
Define a common data model to represent security threat information
Exchange information in a consistent manner across different organizations or
systems
Represent different security information using different objects and attributes

## Page 7

Data sharing schemes02
시나리오
Company A expresses threat information in STIX for the first cybersecurity incident that occurred in Company A.
The information expressed as STIX is transmitted to the relaying agency through TAXII, and the intermediary organization stores the
received content and determines the authenticity of the information.
After that, it delivers the information to the participating organizations via TAXII.
Participating organizations receive threat information shared with them from the STIX relay server and can respond quickly once the
authenticity of the information is determined.
Relay
TAXII
7
Determining
authenticity?
Because it's important information that you
need to act on quickly
May contain misinformation
Possibility of confusion and incorrect
responses due to misinformation
Caveats
This is a simplified example
Factors such as determining coverage for
threat information X
Consider your own incident response
readiness X

## Page 8

Cyber crisis alert stages03
CIS
CIS Benchmarks CIS RAMCIS Controls
8
CIS is a non-profit organization founded in 2000
Develops professional standards and guidelines in the field of information technology and cybersecurity
Goal is to help businesses and government agencies stay safe from cyberattacks
Develops and provides cybersecurity standards and guidelines for businesses and government agencies
Provide a security
setup guide
Cybersecurity
risk assessment20 controls
• To strengthen core security
functions
• Reduce your cyber attack surface
• Defends against more than 85%
of the most prevalent
cyberattacks
• 7 core technology categories
• 140+ CIS benchmarks
• Security settings and
configuration guides for various
platforms and programs
• Comply with and complement
standards such as ISO 27005,
NIST SP 800-30 or RISK IT
• Bridging two different risk
analysis methods

## Page 9

Cyber crisis alert stages03
1.CIS
• U.S. Federal Government Agency
• Develop and provide standards and
guidelines in science and technology
• Standards in many fields, not just
cyber
2 . N I S T
• Nonprofit organizations
• Primarily for businesses and organizations
• Provides specific actions to counter
     cyber threats
CIS NIST
CIS vs NIST?
9

## Page 10

Cyber crisis alert stages03
Severe
High
Elevated
Guarded
Low
Alert Level Indicator – Severity
• Green : -8 ~ -5
• Blue : -4 ~ -2
• Yellow : -1 ~ +2
• Orange : +3 ~ +5
• Red : +6 ~ +8
C y b e r  c r i s i s  a l e r t  s t a g e s
Alerting systems for cybersecurity response implemented by organizations or countries
Various organizations and countries have established their own cyber crisis alert systems and defined different alert levels to respond to different levels of risk.
https://www.cisecurity.org/cybersecurity-threats/alert-level
10
Calculation method
• (lethality + Criticality of the target ) –
      (System Countermeasures + Network Countermeasures)

## Page 11

Lethality Target Importance System
countermeasures
Network
countermeasures
Cyber crisis alert stages03
11
5 : Exploit Exists (root)
4 : Exploit Exists (client)
3 : Exploit x, (root)
2 : Exploit x, (client)
1 : Exploit X, inaccessible
5 : Core Services, Firewall
4 : Web, DB, Critical App
      Server
3 : General App Server
2 : Business Computer,
     System
1 : Personal users
5 : Hardened Verified System
4 : Latest Patches & Anti-Virus
3 : Latest Patches Applied
2 : Some Patches Missing
     Operating System
1 : Past Operating System
5 : Limited, Tested
4 : Limited, external
   connection protection
3 : Limited, attachment
     filtering
2 : Allowed firewall
1 : Implement firewall x

## Page 12

Cyber crisis alert stages03
Blue Alert
Green Alert
Example Action Notification
Network Probing Security Monitor x
Low-risk Virus Internal cybersecurity training
Update your signature file
12
Example Action Notification
Privilege takeover Consider network
disconnection
Change alert level
Vulnerability exploitation, severe
impact
Email x, consider alternative
communication method
Notify via website
Continuous DDoS against primary
service
Include previous advisories

## Page 13

Cyber crisis alert stages03
Orange Alert
Yellow Alert
Example Action Notification
취약점에 의한 심각한 피해가능성 주요 시스템 모니터링 이메일을 통한 ISAC 알람 제공
취약점 악용, 중간정도의 영향 보호대책 즉시 구현 이전 권고사항 포함
DDoS, 바이러스 확산 이전 권고사항 포함
13
Example Action Notification
Vulnerability could cause serious
harm
Monitor critical systems Provide ISAC alerts via email
Vulnerability exploitation, medium
impact
Implement protective
measures immediately
Include previous advisories
DDoS, Spreading viruses Include previous advisories
Example Action Notification
Vulnerability could cause serious harm Monitor critical systems Provide ISAC alerts via email
Vulnerability exploitation, medium
impact
Implement protective
measures immediately
Include previous advisories
DDoS, Spreading viruses Include previous advisories

## Page 14

Example Action Notification
Complete network failure Connect partners before
taking action x
Organize a national conference
call
Failure of key system administrative
controls
Internal network isolation Previous recommendations
include
Potential for loss of life, economic
security
Includes previous advisories
Cyber crisis alert stages03
RED Alert
The color-coded alert system set by the CIS is an important tool to help organizations quickly understand their cybersecurity situation and respond
appropriately
The security level clearly demonstrates the current state of risk, which allows organizations to prioritize future security measures and increase their level of
protection
Organizations can respond to advanced cyber threats and build appropriate response strategies
Continuous monitoring and updates are essential to maintain security levels and ensure a quick and effective response to new threats
14

## Page 15

Additional strategies04
Even if the best experts check the security systems, regularly updating your antivirus, systems, and applications, and monitoring
them in real time, there's still a chance that someone on the inside will accidentally, or even semi-coercively, click and get
infected with malware.
15
Top experts
Regular antivirus updates
The best firewalls
Real-time monitoring

## Page 16

Additional strategies04
This is important
Security file
You must install that
file
StelIa@gmail.com
Steve
Steve@google.com
Stella
Stella@google.com
Sender : StelIa@google.com
What: A serious security issue has occurred, please run the latest
attached patch.
16

## Page 17

Additional strategies04
Steve
Steve@google.com
Hi Partner
Our Company is
Move account
Partner Company.DOCX
Execution File
Document Files
Vaccine, Trust?
100%?
17
Antivirus Scan Results Normal
Document files are fine
Email addresses are fine
So Should You Trust That Email?
Possibility of email hijacking by social engineering
Possible cybersecurity incidents at partner companies
Possibly malware
Big threat when running indiscriminately
Macros are possible
Malware can be injected into document files

## Page 18

Additional strategies04
Incident response readiness
18
Effective response to a cybersecurity incident and how to prepare in
advance
Effective follow-up procedures for a cybersecurity incident
WHY?
The ability to respond quickly and effectively in the face of an intrusion
Organizational credibility
Businesslike appearance
Incident response readiness advantages

## Page 19

Additional strategies04
What if you don't have incident response readiness?
19
Delayed Response Causes More Damage
Failure to respond results in ongoing
damage and increased costs
Quick response
Late response results in system downtime
This impacts business continuity
Business continuity
Psychological anxiety among customers
during a cybersecurity incident
Lack of credibility if response is poor
Customer trust
Big impact on an organization's image
Organization's brand values
For example, if you have companies A and B that make electronics, and you see a news story that company A has been hacked?

## Page 20

Log Enhancement
LOG
Additional strategies04
20
What is a log?
A record of what your computer is doing and how it's being used over time
But how are these logs structured, where are they stored, what policies do they have and how can they be changed, etc...
For Windows, to avoid consuming storage and excessive
resources on your computer
Disabled
You can enable this policy to harden logs
What is log hardening?
Enhanced logs detail events on systems, networks, and
applications
Monitor access control and authorization status of your system
with logs
Enhanced logs
Build a dedicated server to store logs
There is a limit to how much logs can be stored on regular
Windows
If you have a log server, you can collect a huge amount of logs
and check logs from the past to some extent
Log Server
