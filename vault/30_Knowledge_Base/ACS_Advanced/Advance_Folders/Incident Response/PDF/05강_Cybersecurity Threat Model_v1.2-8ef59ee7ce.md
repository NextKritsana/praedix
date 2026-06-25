---
title: "05강_Cybersecurity Threat Model_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\05강_Cybersecurity Threat Model_v1.2.pdf"
source_size_bytes: 890406
source_modified: 2025-11-12T12:16:46
imported_at: 2026-06-14T14:26:23
tags:
  - acs
  - acs-advanced
  - imported
---

# 05강_Cybersecurity Threat Model_v1.2

- Source: [05강_Cybersecurity Threat Model_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/05%EA%B0%95_Cybersecurity%20Threat%20Model_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

What is a Cyber Threat
Model?
• What is a Cyber Threat Model?
• Cover Kill Chain
• Target Attack Life Cycle
• Mitre Att&ck
05
1

## Page 2

01
2
Incidentstructure and function of the system to be protected
• Identify attack vectors and design security measures
• Respond quickly and effectively
The importance of the information that the system processes and
most valuable asset
• Utilize security resources most effectively
• Differentiate the level of protection for that information based on
its importance
What an attacker is most likely to be interested in
• Increase monitoring of targets
• Helping you recover your system
What you need to know?
Methodology for assessing and preparing for the likelihood of a
cyberattack
Specifically identify and analysis of defensive strategies to counter
attacks.
What is a cyber threat model?
What is a Cyber Threat Model?

## Page 3

01
3
What is a Cyber Threat Model?

## Page 4

01
Cyber Kill
Chain
Target Attack
Life Cycle
MITRE
ATT & CK
Originally developed by Lockheed Martin
A model that categorizes cyberattacks into stages
Enables you to detect, defend, and respond to attacks
Cyber Kill Chain
Developed by a nonprofit research organization called MITRE
Representation of strategies, techniques, and general
knowledge
Categorize and describe different strategies and techniques
Developed by Mandiant
Main stages of a more advanced intrusion
Typical attack lifecycle
Target Attack Life Cycle MITRE ATT&CK
M
4
What is a Cyber Threat Model?

## Page 5

KillChain
Recon
Delivery
Installation
Action on Object
Weaponization
Exploitation
Command & Control
Cover Kill Chain02
5

## Page 6

02 Cover Kill Chain
6
Recon
Gather information about your attack targets
Publicly available information, social media, websites
These and more sources
Weaponization
Preparing attack tools
Email containing malware
Malicious websites and malicious
tools
Delivery
Delivering prepared attack tools to
targets
Email, web, USB
Exploitation
Exploit a vulnerability to infiltrate
a system
Systems that are not security
updated
Weak passwords

## Page 7

Installation
Backdoor
A hidden path or feature that bypasses a system's security
measures and allows for secret access or control
Rootkit
Manipulate key parts of the operating system to control the
system by elevating privileges to the highest level
킬체인02 Cover Kill Chain02
7
Command & Control
Remote control
Lateral Movement
Moving to another system on the network
Action on Object
Data breach
System compromise
Dos, DDoS

## Page 8

킬체인02 Cover Kill Chain
8
In today's cybersecurity environment Based on
traditional perimeters that are not sufficient
Doesn't account for an organization's internal
threats
Fault
Mandiant
Target Attack Life Cycle
MITRE
MITRE ATT&CK
Alternatives

## Page 9

Target Attack Life Cycle03
Initial
Reconnaissance
Initial
Compromise
Establish
Foothold
Escalate
Privileges
Internal
Reconnaissance
Complete
Mission
Maintain
Presence
Move
Laterally
Target
Attack
Life Cycle
9

## Page 10

Target Attack Life Cycle03
Initial
Reconnaissance
Initial
Compromise
Establish
Foothold
Target Attack Life Cycle
10
Identify websites
Analyze the target's current or expected business ctivities
Understand the target's internal organization and products
Researching conferences employees attend
Social engineering sites
Phases of successful malware execution
Social engineering attacks
Exploiting vulnerabilities in Internet-connected
systems
To Maintain Continuous Control
Install a permanent backdoor
Download additional utilities

## Page 11

Target Attack Life Cycle03
04
03
02
01
Target Attack Life Cycle
11
Maintain Presence
Gain continuous access to your environment
Install backdoors that provide a pathway
for remote access and control
Install and manipulate additional malware
Access remote access services, such as corporate
virtual private networks (VPNs).
Move Laterally
Leverage permissions to access other systems, expand the
area
Access new systems through network shares
Run specific programs using the Windows Task Scheduler
PsExec to remotely control systems and execute
commands
Interact through graphical user interfaces such as RDP,
VNC, etc.
Internal Reconnaissance
Understanding the victim's environment after an
examination
Estimate and locate critical information
Build an attack plan based on the information gathered
Hack specific accounts and exploit privileges
Targeted and efficient access to targets
Escalate Privileges
Gain broader access to systems and data
Password hash dump password
cracking hash pass attack
Keystrokes, which record everything you type on
your keyboard
Obtaining a public key infrastructure (PKI) certificate

## Page 12

Target Attack Life Cycle03
$
Ransomware
Denial of Service Attack
Mission Complete
Target Attack Life Cycle
12
Cripple a competitor's website or service
Disrupt business
Disrupt services targeting specific organizations, government agencies, etc.
for political purposes
Distract security experts or IT teams
• Perform other types of attacks during this time
• Used to hide previously penetrated attacks
Encrypt data on a victimized system
Goal is to make the attacker pay to recover sensitive data

## Page 13

Cyber Threat Model
MITRE ATT&CK04
13
Cyber risks continue to grow
The level of attackers also continues to increase
Systems or applications are constantly being created
Increase in cyber threats

## Page 14

MITRE ATT&CK04
MITRE ATT&CK
Adversarial Tactics, Techniques, and Common Knowledge
Categorizing by attack objective
Different techniques for different situations
14 Tactics
Consequences of meeting goals
Different techniques for different tactics
400+ Techniques
Standardized data categorizing and cataloging information about various attack vectors
Improve detection of advanced attacks
Homepage : https://attack.mitre.org
MITRE ATT&CK
14

## Page 15

https://attack.mitre.org/
MITRE ATT&CK04
Quick
Update
MITRE ATT&CK
15

## Page 16

MITRE ATT&CK04
2
3
4
Reconnaissance
 Resource
development
Initial
access
 Execution
MITRE ATT&CK
1
16
Reconnaissance
Exploring to move to another system
• Publicly available websites
• Information phishing
Initial access
Obtaining information about a user's environment to enter a
network
• Spear phishing
• Supply chain attacks on hardware, software,
etc.
• Obtaining accounts with appropriate
permissions
Execution
Execute malware through local or remote systems
• Malicious images, malicious links, etc.
• Scheduled tasks
• Command & Scripting Interpreter
Resource development
Acquire information such as accounts in order to
move on to other systems
• Compromise accounts such as email,
cloud accounts, etc.
• Acquire infrastructure, such as botnets,
web services, etc.
• Creating malware

## Page 17

MITRE ATT&CK04
6
7
8
Persistence
 Privilege
escalation
Defense
evasion
Credential
access
MITRE ATT&CK
5
17
Persistence
The act of maintaining a base of operations and gaining
continuous access to a system
• Autorun on boot and login
• Account registration
• Scheduled tasks
Defense Evasion
Aims to avoid detection during the time of the intrusion
• File obfuscation
Signature-based detection evasion
• Registry modifications
Credential Access
Aimed at gaining access to and controlling systems,
domain services, etc.
• Brute force attacks
• Keylogging
• Hijacking sessions, cookies
Privilege Escalation
Attacker gains high privileges on systems and network
• Horizontal privilege escalation
To access features or data from other users at the same level
• Vertical privilege escalation (Credential, Exploit)
To access a parent account from a lower-privileged account

## Page 18

MITRE ATT&CK04
9
10
11
12
Discovery
 Lateral
Movement
 Collection
 Command
And Contorl
MITRE ATT&CK
18
Discovery
Obtaining information about the system and internal
network
• Account discovery
• Peripheral device discovery
• System information discovery
Collection
Collection data for attack purposes or containing
relevant information
• Screen captures
• Keylogging
• Local system data
Command And Control
Communicate with and control systems inside an
intruded target network
• Proxy
• Remote access software
PsExec ...
Lateral Movement
A set of techniques used to gain access to additional
assets after a breach
• Inner sphere phishing
• Leveraging remote services
• Software distribution tools

## Page 19

MITRE ATT&CK04
ImpactExfiltration
GDPR :
GDPR stands for General Data Protection Regulation, a regulation that protects the privacy and personal data of all the populations in EU member states.
For a serious violation, a fine of at least 25.5 billion won can be imposed, and for general violations, a fine of at least 12.7 billion won
MITRE ATT&CK
19
Achieving attack goals
The goal is usually monetary in nature, other than maliciously destroying the target or manipulating and deleting data for
concealment.
Monetary objectives can be achieved through encryption via ransomware, leaking organizational secrets, or leaking personal
information, and in Europe, the GRPR regime has increased the importance of personal information, making it a prime target.
Exfiltration through C2 channels
Breach via physical media
Breach via web services
Behavior to steal data
Data Manipulation
Encryption (Ransomware)
Stopping services
Shutting down and rebooting the system
Behaviors that destroy and
compromise attack targets
