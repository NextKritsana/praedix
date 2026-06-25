---
title: "06강_MITRE ATT&CK 시나리오_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\06강_MITRE ATT&CK 시나리오_v1.2.pdf"
source_size_bytes: 663637
source_modified: 2025-11-12T12:16:54
imported_at: 2026-06-14T14:26:23
tags:
  - acs
  - acs-advanced
  - imported
---

# 06강_MITRE ATT&CK 시나리오_v1.2

- Source: [06강_MITRE ATT&CK 시나리오_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/06%EA%B0%95_MITRE%20ATT%26CK%20%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

MITRE ATT&CK Scenarios
• Pyramid of pain
• TTPs
• Cybersecurity incident analysis based on TTPs
• Scenarios that might be happening around you
• Related articles
06
1

## Page 2

Pyramid of pain01
Hash Value
IP Address
Domain Names
Network /
Host Artifacts
Tools
TTPs Tough!!
Challenging
Annoying
Simple
Easy
Trivial
https://www.attackiq.com/glossary/pyramid-of-pain/
• The vast majority of attackers are primarily motivated by financial gain
• Choose a different target if the attacker determines that the gain is not
significant compared to the effort invested, or
 is unsure
• For this reason, it is important for a business or organization to have
security measures in place to prevent attackers
 from getting in, and if they do, to minimize the damage
• Minimize the damage done by attackers by having a strong security posture
and an effective cybersecurity strategy
Reasons for the attack
Pyramid of Pain
The pyramid of pain is a useful model for increasing an attacker's cost and effort to make your response to a threat more effective.
Designed in 2013 by security expert David J Bianco,
Articulates that defenses are most effective when security personnel understand the strategies, tactics, and processes of attackers like TTPs.
From the bottom, we have hashes, IP addresses, domain names, network/host artifacts, tools, TTPS, and as you move up, it gets harder for attackers
 The goal of security people in organizations is to get attackers to the Tough!! stage
2

## Page 3

Pyramid of pain01
Hash value
If a security officer defends against malware
based on a hash value, an attacker can change
the hash value to and bypass that security policy
Hash value
The value generated during the process of
converting arbitrary data into a fixed-length
string, which expresses the characteristics of the
original data
Ensure that different inputs generate unique
hash values and ensure that they have different
identifiers
IP address
If security personnel block the attacking IP, not
the hash value, attackers can bypass and access
via proxy
Proxy: typically used to mediate network
communication and improve improve security
and performance
Attackers can also use proxies for malicious
purposes to bypass security policies
Anoymizing Proxy: A proxy that focuses on
hiding the user's real IP from the the user's real
IP
Domain Name
If a security officer uses a domain name to
block, an attacker can bypass it, which is a
little more tricky than an IP
More time-consuming and expensive than
 security policies using hashes, IPs, etc.
because it requires the process of purchasing,
registering, and hosting a domain
If blocked without including a subdomain,
you can use the subdomain to get around it
https://www.csnp.org/post/tryhackme-pyramid-of-pain-room
<#>
<#>
3

## Page 4

TTPs02
TTPs
TTPs?
Tactics, Techniques, and Procedures
A comprehensive term for the strategies,
techniques, and procedures employed by cyber
attackers
Roles
Essential for security professionals to analyze
and understand the details of cyberattacks
Play a key role in threat intelligence and
cybersecurity
Necessity
Key concepts essential to the study of terrorism and cybersecurity
Identify the behaviors and patterns of specific terrorist organizations and understand their
characteristics to develop prevention and response strategies
Prepare for future threats and strengthen your organization's cybersecurity
4

## Page 5

TTPs02
Tactics
1
Techniques
2
Procedures
3
A strategy expresses a high-level plan or method for achieving an attacker's goals
Includes strategies to achieve goals such as data exfiltration, equipment destruction,
and information manipulation
Goal setting and planning
Attackers set their goals and create a plan to achieve them
In this phase, you decide what kind of information or assets you want to target,
 how you want to infiltrate them, etc.
Cyber Penetration Planning
If you are targeting a business or organization, develop a plan to bypass the
organization's defenses and penetrate more effectively
Exam : Tactics
5

## Page 6

Tactics
1
TTPs02
Techniques
2
Procedures
3
Technology describes a specific technique or mechanism used to achieve a specific goal
Malware injection, use of command and control servers (C2), phishing, etc.
Using malicious code
An attacker develops or uses malicious code to infiltrate a target system and execute
commands
Viruses, Trojans, ransomware, and more
Vulnerability exploitation
A technical method of infiltrating a system by discovering and exploiting a vulnerability
in a system or software
Social engineering techniques
Use social engineering techniques, such as getting people to trust you or tricking them
into giving you information
Exam : Techniques
6

## Page 7

Tactics
1
TTPs02
Techniques
2
Procedures
3
Detailed steps or procedures for actually implementing the technology
Specific actions that an attacker takes to infiltrate a system using a particular technique
or to accomplish their goals
Cyber penetration
Establish a step-by-step process to reach your goal
Initial penetration from outside to inside, movement from inside, elevation of privilege,
etc.
Retention and concealment
Attackers establish procedures to conceal their presence and remain inside the system
for extended periods of time
To avoid detection and maximize the effectiveness of an attack
Achieve your goals
Follow specific procedures to achieve your goals
Data breaches, system destruction, information tampering, etc.
Exam : Procedures
7

## Page 8

TTPs02
Understanding the nature of
security attacks
When attackers are using a specific TTPS to
conduct attacks, identify and understand
their behavior and techniques used so you
can prepare for similar attacks that may
occur in the future
Conduct user security training to identify
 spear phishing and suspicious emails in
order to be prepared in case email spear
phishing or social engineering is used to gain
access to information and cause damage
through ransomware
Develop cybersecurity policies
and procedures
Respond to security threats by implementing
standardized protocols and effective policies
and build a consistent security culture within
your organization

Collect threat intelligence to understand the
current cybersecurity situation and develop
cybersecurity policies suitable for the
organization based on TTPs analysis to
establish
Response and defense strategies
Continuous assessment and remediation to
keep security up to date
Threat Intelligence and Chip
Intrusion Detection
TTPs provide critical information for threat
intelligence collection and analysis, and
understanding them can help organizations
detect intrusions more quickly, improve security
intelligence, and prepare for future threats
Example: Phishing attack
Examine the TTPs used in the attack to gather
details such as the language of the phishing
emails and the structure of the malicious links,
and set up an intrusion detection system to
enable a quick response if similar patterns are
found
Important aspects of TTPs
8

## Page 9

TTPs02
Detect and respond to
cyberattacks
An approach based on TTPs helps
organizations proactively understand known
attack behaviors and optimize detection
systems based on them, enabling
organizations to quickly detect threats in real
time and respond effectively
By proactively learning and analyzing TTPs,
organizations can maintain a higher level of
security

Expect to see an increase in the ability to
respond quickly and effectively to the latest
threats
Threat Modeling & Simulation
TTPs can be a key tool for organizations to
improve their own security
Develops realistic and diverse cyber threat
scenarios and accurately analyzes attacker
behavior patterns and techniques used to
help organizations prepare for a variety of
threats
Test real-world responsiveness to see how
your security team and infrastructure behaves
 in the real world to identify room for
improvement
Important aspects of
TTPs
9

## Page 10

Analysis stepsMachining stepsIngest phase Application steps
The collection phase involves gathering various forms of
information from multiple sources
This information can come from a variety of sources, ranging
from external sources to internal logs and events, open source
intelligence, and intelligence provided by providers, i.e.,
attackers
Ingest phase
Turning collected information into analyzable form
During this process, the malware is randomized and de-
obfuscated
Machining Steps
Analyzed by experts or security systems, this stage involves a
deeper analysis to understand the type of threat, the attacker's
intent, the techniques and tools used, and the goal of the attack
Analysis steps
Analyzed threat intelligence is applied to real-world security
strategies to strengthen the organization's defenses
Ensure your security tools and systems are up to date with the
latest threat actions taken
Application steps
Collect and analyze threat intelligence
TTPs02
10

## Page 11

Analyze TTPs to identify attacker patterns and harden your response based on them
For example, if a particular attack technique is used, build defenses and detection
mechanisms against that technique, understand the attacker's procedures, and be
proactive
Response hardening
A comprehensive, multi-layered defense strategy is required, using a combination
of tools and technologies, including an Intrusion Detection System/Intrusion
Prevention System (IDS/IPS), firewalls, antivirus solutions, endpoint security
solutions, and other tools and technologies
Solution
User training is an important factor in strengthening your security environment
and minimizing insider threats
A mistake by someone with low security awareness can have catastrophic
consequences that can determine the fate of the entire organization
Organizational members need to develop security awareness by learning about
 real-world threats and appropriate responses
User training
TTPs02
11

## Page 12

03
A Company
• The attacker used the acquired employee's email account to
send an official-looking email to a specific person within the
organization
• This email contains a malicious link or malicious file, which, if
clicked or executed by a specific person, will execute malware
• Gain control over the work activities of specific people and
access to inside corporate information
Secondary phishing emails
• Write a phishing email to one of your employees regarding a
statement or work related
• Phishing emails contain malicious attachments or phishing
links to , which can be used to obtain an employee's login
information
• An attacker could use this information to gain access to
 to a specific employee's email account
Primary phishing email
12
Cybersecurity incident analysis based on TTPs

## Page 13

Analyzing breaches based
on TTPs03
A Company
• If a user opens or executes a malicious file, backdoor
installs on the system
• The installed backdoor allows communication with
the attacker and has the ability to maintain access to
on an ongoing basis.
Primary phishing emails
• Attempts to access various resources and sensitive
information within the system based on the privileges it
initially gained
• Attempting to gain higher privileges by combining privilege
escalation techniques with the initial privileges gained by the
attacker
Privilege escalation
13
Cybersecurity incident analysis based on TTPs

## Page 14

Analyzing breaches based
on TTPs03
****
• Attacker leverages elevated privileges to deploy a backdoor
that allows command and control within the system
• Malicious code is tampered with, encrypted, and
obfuscated using a variety of techniques to evade antivirus
programs
• If an antivirus detects based on a signature or hash value,
replace the signature to bypass it
Vaccine avoidance
• Attackers use keylogging to monitor and record keystrokes typed on a system
• Unless you're a large company, it's not uncommon for an individual to wear multiple
hats, in which case they may have access to all different systems
• Analyzing information gathered through keylogging to gain access to another
account and stealing the credentials of that account
• Use acquired account information to extend access to other systems or services
Keylogging
A Company
• If the DB server is compromised, the attacker can steal sensitive information inside
the organization and send it to the command-and-control server encrypted and
compressed
• When exfiltrating data, it goes through multiple relay servers to evade detection and
make it difficult to trace back to

Spills
14
Cybersecurity incident analysis based on TTPs

## Page 15

Analyzing breaches based
on TTPs03
The reconnaissance phase is responsible for selecting targets
for attack
Acquire an email account within Company A through social
engineering techniques
Recon
https://attack.mitre.org/techniques/T1589/
Steps to build the infrastructure for an attack
Infiltration was planned via malicious attachments, and malicious attachment
development, phishing emails, etc. fall into this phase
Resource Development
https://attack.mitre.org/techniques/T1587/001/
Proceed with a phishing attack through the email account obtained in the reconnaissance phase
Initial penetration
https://attack.mitre.org/techniques/T1566/001/
15
Cybersecurity incident analysis based on TTPs

## Page 16

Analyzing breaches based
on TTPs03
When running attachments, the user gets permissions and can remotely
command them
Run
Registering malware in the registry and startup programs via remote commands
Maintaining persistence
Encryption, tampering, and evasion of signature-based malware detection
devices
Defense Evasion
https://attack.mitre.org/techniques/T1204/002/
https://attack.mitre.org/techniques/T1547/001/
https://attack.mitre.org/techniques/T1027/010/
16
Cybersecurity incident analysis based on TTPs

## Page 17

Analyzing breaches based
on TTPs03
Use programs like keylogging to gather information and find your next
attack target
Collect
Leaking information you collect
Spills
https://attack.mitre.org/techniques/T1056/001/
https://attack.mitre.org/techniques/T1041/
****
17
Cybersecurity incident analysis based on TTPs

## Page 18

04
Logon laptop
To get coffee, to find a book, to go
to the bathroom
I left the house without turning off
my laptop screen
Malicious USB
Firewall off
UAC off
Add an account
Install the remote control
program exists
18
Scenarios that might be happening around you

## Page 19

Scenarios that might be
happening around you04
Scenarios
You're a college student, and you're out with your laptop to study
You walk into a cafe, leave your laptop open, and step away to use the restroom
You didn't turn off your laptop screen because you were leaving for a quick trip, and when you got back to your desk, you noticed that your
computer had rebooted
Nothing seemed to be wrong and my laptop was safe and sound, so I sat down and went back to studying, thinking it must have rebooted
due to a routine update
But as time went on, you noticed that your computer was getting slower and sluggish, and you eventually closed the laptop and went home
In reality, it's not uncommon to leave your laptop screen unlocked and walk away for a few minutes
Plugging in a USB with a few features and running an executable doesn't make your computer safe if someone with malicious intent is nearby
In between these moments
Firewall off
UAC off
Add an account
Install the remote control program
Malicious USB
19
Scenarios that might be happening around you

## Page 20

Scenarios that might be
happening around you04
This scenario will be covered with labs in Chapter 5
• Access your computer from within the same network
using the program, which allows remote control
• An attacker logging in with a pre-created administrator
account would have a relatively easy time stealing sensitive
information from your computer
• Slowing down the user's computer in the process
After running using USB
20
Scenarios that might be happening around you

## Page 21

Related Refs05
https://www.picussecurity.com/resource/glossary/what-is-pyramid-of-pain
•Title: The Pyramid of Pain: Towards a Principle of Cyber Security
•Author: David J. Bianco
•It discusses "The Pyramid of Pain" model, emphasizing the
importance of TTPs and suggests a cybersecurity strategy based on
this model
Related resources
URL
21
