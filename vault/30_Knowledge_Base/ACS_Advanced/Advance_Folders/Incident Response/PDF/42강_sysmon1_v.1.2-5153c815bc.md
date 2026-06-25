---
title: "42강_sysmon1_v.1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\42강_sysmon1_v.1.2.pdf"
source_size_bytes: 922263
source_modified: 2025-11-12T13:40:50
imported_at: 2026-06-14T14:27:03
tags:
  - acs
  - acs-advanced
  - imported
---

# 42강_sysmon1_v.1.2

- Source: [42강_sysmon1_v.1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/42%EA%B0%95_sysmon1_v.1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Sysmon
• What is Sysmon
• Install
• Configuration files
• Hands-on
42
1

## Page 2

What is Sysmon01
Sysmon
What is Sysmon
A system monitoring tool, part of Microsoft's Sysinternals suite, that provides detailed
security event logging of Windows system activity
What to use it for?
Monitor critical activities occurring on your system in real time, such as network
connections, process creation, and file creation time changes, and generate logs for
system security analysis, forensic investigations, and cybersecurity threat detection
2

## Page 3

What is Sysmon01
Key features
Top features supported by Sysmon
• Capture the creation and termination of all processes running on your system, logging detailed information about each process.
• Provides critical data during security analysis, incident response, system monitoring, and troubleshooting
• Verifiable information includes the process identifier and parent process identifier, executable path, process hash, etc.
Process tracking
Track files created, modified, or deleted on your system
Monitor file creation
Logging inbound and outbound network connections that occur
on your system
Monitoring network connectivity
Monitor registry key creation, modification, and deletion
events
Registry tracing
Track drivers and services loaded by the system
Monitor driver services and loading
3

## Page 4

Install02
Commands used to send web requests in PowerShell
Can be used to download data from a specified URL
Invoke-WebRequest
iwr https://download.sysinternals.com/files/Sysmon.zip -outfile
 "$env:USERPROFILE\DESKTOP\SYSMONDIR\sysmon.zip"
Download Command
Unzip the downloaded sysmon.zip with the expand-archive
command
Command : expand-archive sysmon.zip
Decompress
4

## Page 5

01. current page topic
General installation
•The simplest way to install Sysmon using default settings
•Sysmon is installed and ready to use out of the box, with no configuration files provided by the user
•Useful when you want to quickly take advantage of the many monitoring features Sysmon has to offer
Change the directory to the location of the downloaded sysmon.exe file
Run the "sysmon.exe -I" command
How to install
• No need to specify a separate configuration file
• After a successful installation, Sysmon starts monitoring and logging
system events to
Features
Install02
5

## Page 6

01. current page topic
Custom installations
•Advanced installation options that allow users to specify in detail how Sysmon behaves
•Custom installations can be configured using configuration files to prevent users from monitoring certain event types or
logging certain data
•Maximize the effectiveness of security monitoring with minimal impact on system performance
• Assume you have a configuration file named micro.xml under the
SYSMONDIR directory on your desktop
• When you run the command to install Sysmon, supply the path to
the configuration file with the -I option
How to install
Install02
6

## Page 7

01. current page topic
https://learn.microsoft.com/ko-kr/sysinternals/downloads/sysmon
• Syntax from Microsoft's official documentation
Example
• Sysmon
• HashAlgorithms
• EventFiltering
• DriverLoad
• Signature
• ...omit...
Tag
Install02
<Sysmon schemaversion="4.82">
 <!-- Capture all hashes -->
 <HashAlgorithms>*</HashAlgorithms>
 <EventFiltering>
  <!-- Log all drivers except if the signature -->
  <!-- contains Microsoft or Windows -->
  <DriverLoad onmatch="exclude">
   <Signature condition="contains">microsoft</Signature>
   <Signature condition="contains">windows</Signature>
  </DriverLoad>
  <!-- Do not log process termination -->
  <ProcessTerminate onmatch="include" />
  <!-- Log network connection if the destination port equal 443 -->
  <!-- or 80, and process isn't InternetExplorer -->
  <NetworkConnect onmatch="include">
   <DestinationPort>443</DestinationPort>
   <DestinationPort>80</DestinationPort>
  </NetworkConnect>
  <NetworkConnect onmatch="exclude">
   <Image condition="end with">iexplore.exe</Image>
  </NetworkConnect>
 </EventFiltering>
</Sysmon>
7

## Page 8

Configuration files03
Schema Version
schemaversion=‘4.82’ indicates the version of the Sysmon schema you are using
Schema Version is a value that specifies the version of the Configure File and must be specified when writing the
Configure File
How to verify
Can be verified with the Sysmon.exe -? config command
This may change whenever Sysmon is updated, and it is recommended that you always use the latest schema version
when writing configuration files
<Sysmon schemaversion="4.82">
8

## Page 9

01. current page topic
<HashAlgorithms>*</HashAlgorithms>
Hash Algorithms
• Used as part of the Sysmon configuration file, this component specifies the hash algorithm to use when capturing
hashes of files associated with events monitored by Sysmon
• Tells Sysmon to generate file hashes using any type of hash algorithm it supports
• MD5
• SHA1
• SHA256
Available hashes
• Useful for determining whether a file is malicious in the event of a security
incident
• If the hash value of a file matches the hash value of known malicious code, the
file can be considered malicious
• Hash is a very effective way to verify the integrity of a file, as it will result in a
completely different value if the contents of the file are changed even slightly
Utilization
Configuration files03
9

## Page 10

01. current page topic
EventFiltering
• Define filtering rules that are used in Sysmon's configuration file to exclude driver load events that meet certain condition s from logging
• onmatch="exclude" means that this filtering rule "excludes when the condition is met"
DriverLoad on match="exclude"
• The <Signature> tag applies filtering rules based on digital signature information of the driver being loaded
• If the drive signature contains the strings Microsoft and "windows", it means that the driver is not logging driver load even ts to
Signature condition="contains"
Configuration files03
<EventFiltering>
  <DriverLoad onmatch="exclude">
   <Signature condition="contains">microsoft</Signature>
   <Signature condition="contains">windows</Signature>
  </DriverLoad>
10

## Page 11

01. current page topic
Condition property values
• Used within the Sysmon configuration file to specify the conditions under which to apply a specific rule
• Provide information that Sysmon needs to examine whether certain conditions are met to determine whether to
record an event
is: condition met when value matches exactly
Contains: condition is met when the value contains a specific string
is, contains
Condition met when field value starts with a specific
string
Begin with
Condition met when field value ends with a specific
string
End with
Specify conditions on the path to the image file of a running
process
Image
Condition met when field value equals specified
value
Equals
Condition met when field value is different from
specified value
Not equals
Configuration files03
11

## Page 12

01. current page topic
<EventFiltering>
    <ProcessTerminate onmatch="exclude" />
    <ProcessTerminate onmatch="include">
        <Image condition="is">C:\Windows\System32\notepad.exe</Image>
    </ProcessTerminate>
</EventFiltering>
ProcessTerminate
• Enable logging of process end events in the configuration file
• If the onmatch="include" property is set, all process termination events that occur on the system are included in the log
Tips
• ProcessTerminate onmatch="exclude" /> sets all process termination events to be excluded from the log by default
• In the <ProcessTerminate onmatch=‘include’> section, use <Image condition=‘is’>C:\Windows\System32\notepad.exe</Image> to
include events in the log only when the Notepad process (notepad.exe) is terminated
• This way, Sysmon only logs events that occur when Notepad is exited from the system, ignoring exit events from all other proc esses
Configuration files03
12

## Page 13

01. current page topic
NetworkConnect
• Specify that network connection events that meet certain conditions be included in the logs
• By using this setting, you can monitor and analyse only the specific network connections that occur on your system that you are
interested in
Identify malicious traffic
• Identify malicious web traffic or data exfiltration attempts by monitoring connections to specific destination ports, such as 443 and 80
Analyze network activity
• Analyse usage patterns of specific applications within your organisation, or detect unusual network connection attempts, for example,
attempts to connect to ports that are not normally used
Filtering data
• By capturing only specific connections, you can focus on relevant data and improve the efficiency of your analyses
Use cases
Configuration files03
<NetworkConnect onmatch="include">
   <DestinationPort>443</DestinationPort>
   <DestinationPort>80</DestinationPort>
</NetworkConnect>
13

## Page 14

01. current page topic
• Define rules to exclude network connection events from the log that meet specific conditions
• Set to exclude from the log all network connections made by processes with executable file names ending in iexplore. exe
• Used when you do not want to collect network connection logs from trusted processes, such as Internet Explorer
NetworkConnect
Storage can be managed by making exceptions to lists that are deemed safe processes by security personnel or
administrators
In addition to these...
Configuration files03
<NetworkConnect onmatch="exclude">
  <Image condition="end with">iexplore.exe</Image>
</NetworkConnect>
14

## Page 15

01. current page topic
Network
• Enable to include connections to 443 (HTTPS traffic)
• Set to include connections to 80 (HTTP traffic)
• Do not log network connection events with image paths
ending in iexplore.exe
Process End Events
• All log history
Driver Load
• Microsoft excludes loading for drivers with a signature
named Windows
Set rules
Configuration files03
15

## Page 16

01. current page topic
1
2
Rule group?
• Ability to group and manage related rules
• Rule Groups allow you to logically categorise and
manage related rules, which can help you
manage rules efficiently and create easy-to-
understand configurations
Ease of management
• Rule Groups allow you to manage related rules
together, making rule configurations more
readable
• By grouping different event and condition rules
together, you can monitor and analyse events
efficiently
Rule
Group
Configuration files03
16

## Page 17

01. current page topic
<Sysmon schemaversion="4.90">
    <RuleGroup name="NetworkMonitoring" groupRelation="or">
        <NetworkConnect onmatch="include"> <NetworkConnect onmatch="include">
            <DestinationPort condition="is">443</DestinationPort>
        </NetworkConnect>
        <NetworkConnect onmatch="include"> <NetworkConnect onmatch="include">
            <DestinationPort condition="is">80</DestinationPort>
        </NetworkConnect>
    </RuleGroup>
    <RuleGroup name="ProcessMonitoring" groupRelation="or">
        <ProcessTerminate onmatch="include">
            <Image condition="is">C:\Windows\System32\notepad.exe</Image>
        </ProcessTerminate>
        <ProcessCreate onmatch="include">
            <Image condition="is">C:\Windows\System32\cmd.exe</Image>
        </ProcessCreate>
    </RuleGroup>
</Sysmon>
• Monitor HTTP (port 80) and HTTPS (port 443) connections
• The groupRelation=‘or’ attribute means that if any of the
rules in this rule group are matched, an event will be logged
Network Monitoring Group
• Monitor process termination and creation events
• The <ProcessTerminate> rule catches the notepad.exe
process when it is terminated
• A <ProcessCreate> rule catches the cmd.exe process when it
is created
Process Monitoring Group
Configuration files03
17

## Page 18

Hands-on04
CONFIGURE A SIMPLE LAB
01
STEP
03
STEP02
STEP
04
STEP
Install
 SYSMON on
the virtual
machine
With SSH
Applications
Run
Event logs
Confirm
Rule
description
and applying
rules
18

## Page 19

•Create a directory
•Download SYSMON with IWR
•Decompress
Installation process
4.90
Schema version
Hands-on04
19

## Page 20

Use custom XML
Hands-on04
<Sysmon schemaversion="4.90">
 <HashAlgorithms>*</HashAlgorithms>
 <EventFiltering>
  <!-- Network Monitoring Rule Group -->
  <RuleGroup name="NetworkMonitoring" groupRelation="or">
  <NetworkConnect onmatch="include">
   <DestinationPort condition="is">443</DestinationPort>
   <DestinationPort condition="is">80</DestinationPort>
   <DestinationPort condition="is">22</DestinationPort>
  </NetworkConnect>
  </RuleGroup>

  <!-- Process Monitoring Rule Group -->
  <RuleGroup name="ProcessMonitoring" groupRelation="or">
    <ProcessTerminate onmatch=＂include">
      <Image condition="is">C:\Windows\System32\notepad.exe</Image>
      <Image condition="is">C:\Windows\System32\cmd.exe</Image>
    </ProcessTerminate>
    <ProcessCreate onmatch=“include">
      <Image condition="is">C:\Windows\System32\notepad.exe</Image>
      <Image condition="is">C:\Windows\System32\cmd.exe</Image>
    </ProcessCreate>
  </RuleGroup>
 </EventFiltering>
</Sysmon>
20

## Page 21

<Sysmon schemaversion="4.90">
 <HashAlgorithms>*</HashAlgorithms>
 <EventFiltering>
  <!-- Network Monitoring Rule Group -->
  <RuleGroup name="NetworkMonitoring" groupRelation="or">
  <NetworkConnect onmatch="include">
   <DestinationPort condition="is">443</DestinationPort>
   <DestinationPort condition="is">80</DestinationPort>
   <DestinationPort condition="is">22</DestinationPort>
  </NetworkConnect>
  </RuleGroup>

  <!-- Process Monitoring Rule Group -->
  <RuleGroup name="ProcessMonitoring" groupRelation="or">
    <ProcessTerminate onmatch=＂include">
      <Image condition="is">C:\Windows\System32\notepad.exe</Image>
      <Image condition="is">C:\Windows\System32\cmd.exe</Image>
    </ProcessTerminate>
    <ProcessCreate onmatch=“include">
      <Image condition="is">C:\Windows\System32\notepad.exe</Image>
      <Image condition="is">C:\Windows\System32\cmd.exe</Image>
    </ProcessCreate>
  </RuleGroup>
 </EventFiltering>
</Sysmon>
01. current page topic
Name
• NetworkMonitoring
Role
• Set the rule to include network connections to port
443 (HTTPS), port 80 (HTTP), and port 22 (SSH)
1st Rule Group
Name
• ProcessMonitoring
Role
• Monitor process creation and termination events
• C:\Windows\System32\notepad.exe
• C:\Windows\System32\cmd.exe
2nd Rule Group
Hands-on04
21

## Page 22

01. current page topic
•calc.exe
•notepad.exe
•cmd.exe
•control.exe
Run list
SSH connections
 notepad.exe
cmd.exe
Hands-on04
22
