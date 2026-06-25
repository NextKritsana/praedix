---
title: "29강_NetworkForensic(1)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\29강_NetworkForensic(1)_v1.2.pdf"
source_size_bytes: 983409
source_modified: 2025-10-18T20:16:35
imported_at: 2026-06-14T14:25:19
tags:
  - acs
  - acs-advanced
  - imported
---

# 29강_NetworkForensic(1)_v1.2

- Source: [29강_NetworkForensic(1)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/29%EA%B0%95_NetworkForensic%281%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Network Forensic (1)
• Collecting Network Packets
• Network Packet Analysis
29
1

## Page 2

2
01. current page topic
Collecting Network Packets01
Network packet collection approach
Packet capture equipment is placed directly in the data path of the network.
The way packet-capturing equipment is placed outside the data path of the network.
In Path Method
Out Path Method

## Page 3

3
01. current page topic
Collecting Network Packets01
Different approaches to collecting network packets
02 04
03
0501
Inline
Similar to the In Path method,
where traffic must pass directly
through packet capture
equipment.
Virtual Tapping
Collect traffic between virtual
machines (VMs) over virtual
network interfaces
Cloud-based Capture
In a cloud environment, use the network
monitoring tools provided by your cloud
provider to capture packets. Endpoint-base Capture
Collect data at the device level
with agents installed on endpoints
Network Probes
Dedicated equipment that is
placed at specific network
points to collect and analyze
packets.
Network
Packet
Collecting Network Packets

## Page 4

4
01. current page topic
Collecting Network Packets01
Network communication monitoring equipment
TAP
Traffic Access Point
Passive TAP Virtual TAP
1.Physical (Passive) TAP:
Installed directly between network cables, they
create a copy of traffic traversing the network
and send it to a device for monitoring
purposes. Physical TAPs do not provide power
to the network and do not affect network
traffic in the event of a power failure.
2.Virtual TAP:
Used in virtualized network environments to
monitor traffic between virtual machines
(VMs) traversing a virtual switch or virtual
infrastructure Virtual TAPs are software-based,
capturing traffic on a virtual network and
sending it for analysis purposes.
Key advantages of TAP equipment
Transparency, Reliability, Accuracy
Collecting Network Packets

## Page 5

5
01. current page topic
Collecting Network Packets01
Switched Port Analyzer (SPAN) & Port Mirroring
Switched Port Analyzer (SPAN) & Port Mirroring
One of the functions of a network switch,
Allows traffic on a specific network port or an entire virtual local area network (VLAN)
to be copied to another port for monitoring purposes.
Selecting a target port or VLAN: Administrators can select a specific port or VLAN that
they want to monitor, called the source port. All traffic originating from the source
port is copied to the destination port .
Set a destination port: All copied traffic is sent to the destination port.
The destination port is connected to a monitoring tool, such as a network analyzer,
intrusion detection system (IDS), packet capture tool, etc.
Non-intrusive monitoring: SPAN lets you monitor traffic without impacting network
performance without altering the flow of network traffic,
only creating a copy of it to analyze
Limitations of SPAN
Resource usage, traffic loss, and performance dependency of analytics tools
Collecting Network Packets

## Page 6

6
01. current page topic
Collecting Network Packets01
Mobile device packet collection with Termux
Installing Termux: On an F-Droid download and install
the Termux application from F-Droid
Installing Required Packages: On Termux install
network analysis tools pkg update && pkg upgrade
pkg install arp-scan
Run an ARP scan: Use the tools you installed to
scan your network using the tool you installed
arp-scan --interface=wlan0 -localnet
--interface=wlan0 specifies the Wi-Fi interface
Since interface names can vary by device,
Verify using the ip link show command
Collecting Network Packets

## Page 7

7
01. current page topic
Collecting Network Packets01
Wireshark
Run Wireshark Run Wireshark
Collecting Network Packets
Local Area Connection 2
Local Area Connection 10
Local Area Connection 9
Local Area Connection 8
Local Area Connection 1
Bluetooth Network Connection

## Page 8

8
01. current page topic
Collecting Network Packets01
Wireshark
Set capture filters
(optional)
Start capture
Collecting Network Packets

## Page 9

9
01. current page topic
Collecting Network Packets01
Wireshark
Stop capturing Restart capture
Saving packets
Collecting Network Packets

## Page 10

10
01. current page topic
Collecting Network Packets01
Wireshark capture filters
Capture only packets coming from a specific IP address: src host 192.168.1.1
Capture only packets going to a specific IP address: dst host 192.168.1.1
Capture all packets associated with a specific IP address: host 192.168.1.1
IP address-based
To capture packets using a specific port (for example, HTTP traffic): port 80
To capture only packets coming from a specific source port: src port 12345
To capture only packets going to a specific destination port: dst port 12345
Port-based
To capture only ICMP packets: icmp
To capture only TCP packets: tcp
To capture only UDP packets: udp
Protocol-based
01
STEP
To capture only packets from a specific network:
net 192.168.1.0/24
Network and subnet-based
02
STEP
Capture packets that use a specific IP and a specific port at the same time:
host 192.168.1.1 and port 80
Create a complex filter by combining multiple conditions: src net
192.168.1.0/24 and dst port 443 and tcp
Combined filters
03
STEP
04
STEP
05
STEP
Collecting Network Packets

## Page 11

11
01. current page topic
Collecting Network Packets01
Tshark
tshark -i <interface name> host <host address
tshark -i <interface name> port <port number
tshark -i <interface name
Capture packets over a network interface
Capture traffic using a specific port
Capture communication with a specific host
Save captured packets to a file
tshark -i <interface name> -w <filename.pcap>
tshark is the console version of Wireshark, a network protocol analysis tool that can be used
from a terminal or command prompt. tshark allows the core functionality of Wireshark to be used
in environments without a GUI. This is very useful for servers, remote systems, or any environment
that doesn't require a graphical interface. This is very useful for servers, remote systems, or any
environment that doesn't require a graphical interface.
Key features of tshark
Real-time traffic capture:
Supports the capture of real-time data traffic over a specified network interface.
Packet analysis and extraction:
Filter and analyze packets that meet specific conditions from captured packet data.
Read and analyze packets from files:
Read and analyze pre-captured packet data files (.pcap, .pcapng, etc.) using tshark.
Support for multiple output formats:
Capture or analysis results can be output in a variety of formats, which can be useful for further
processing or analysis
Collecting Network Packets

## Page 12

PCAPNG
packet
capture next
generation
12
01. current page topic
Network Packet Analysis02
Packet Capture (PCAP) and Packet Capture Next Generation (PCAPNG) are File formats for
storing network traffic data, each widely used in network analysis tools and designed for
packet capture and analysis
Functionality
PCAPNG provides enhanced functionality over PCAP. For example, the PCAPNG format can
store data captured from multiple network interfaces in a single file, and can include
additional information such as information about each interface, capture time and system
information, and user-defined blocks.
Compatibility
The PCAP format is widely supported by network analysis tools and is available in almost all
network analysis and capture tools. The PCAPNG format, on the other hand, is primarily
supported by tools like Wireshark in newer versions, and may be incompatible with some
older tools.
Extensibility
PCAPNG format is more extensible by supporting multiple types of data blocks (e.g., interface
description blocks, enhanced packet blocks, etc. Can better support additional metadata and
complex network capture scenarios
Metadata support
PCAPNG can store metadata associated with the capture file (e.g., comments, interface
names, resolution of the captured network, etc.
File size and efficiency
The PCAPNG format can store additional information and metadata, which makes the file
size larger than the PCAP format when saving the same network traffic data. However, this
additional information is useful during the analysis process.

## Page 13

13
01. current page topic
Network Packet Analysis02
Information you can get from a Packet file
Timestamps
Provides information about the exact time each packet
was captured. This allows you to analyze the temporal
flow and patterns of traffic
Source and destination addresses
You can see the source and destination IP
addresses and port numbers of packets, allowing
you to analyze communication between specific
hosts
About communication protocols
Packet data can tell you what kind of network protocol
was used (e.g., HTTP, HTTPS, FTP, TCP, UDP, etc.)
Data payloads
Inspect the actual data content within packets, which
allows you to analyze application-level data exchanges.
However, in the case of encrypted communications,
direct viewing of the payload content may be limited
Network performance metrics
Analyze metrics related to network performance such
as packet loss, latency, and transfer rate
Session recovery
You can recover communications from specific sessions,
such as HTTP sessions and FTP transfers, to restore files or
web browsing activity that a user has transferred
About security
Can detect security threats through unusual
traffic patterns, known attack signatures,
anomalous behavior, and more
Network Packet Analysis

## Page 14

14
01. current page topic
Network Packet Analysis02
Components Description.
File headers Located at the beginning of the file and contains the metadata for the PCAP file, which includes information such as
the file type, network type of the captured data, timestamp precision, etc.
Packet headers Located before each packet data and contains information about that packet, such as the timestamp of the packet,
the actual length of the packet, and the length stored at the time of capture.
Packet data Located after the packet header and contains the actual data of the packet as it was sent over the network. This data
is used for analytics.
File header fields
Magic number: A value to identify that it is a PCAP file.
Version number: Specify the major and minor version of the file format
Timezone offset: Local time offset from GMT
Timestamp precision: Determines the precision of the timestamp
Snapshot length: Maximum number of data bytes that can be captured
Network: Link layer type of captured data
Packet header fields
Timestamp (seconds): The number of seconds from the time the packet was captured
Timestamp (microseconds/nanoseconds): Indicates a time in seconds or less
Captured length: the length of packet data actually stored in the file
Actual length: The full length of the packet, only a portion may be captured
Structure of a PCAP File
Network Packet Analysis

## Page 15

15
01. current page topic
Network Packet Analysis02
Deep dive into network packet data
Session recovery
Reconstruct sessions that span multiple packets,
recovering and analyzing high-level communication flows
such as web browsing, email exchanges, file transfers,
and more.
Payload analysis
Examine the body (payload) of packet data to
identify malicious code, suspicious traffic patterns,
sensitive information leaks, and more
Statistical analysis
Analyze the statistical characteristics of network traffic
(such as traffic volume, packet size distribution,
communication patterns, etc.
Behavior-based analytics
Detect unknown threats by analyzing the behavioral
patterns of hosts or applications within your network
Analyze encrypted traffic
Extract and analyze some information (for example,
the IP addresses, port numbers, and TLS handshake
information of the communicating server and client).
Analyzing honeypot and honeynet data
Intentionally deploying vulnerable systems or
networks to lure and analyze attacker behavior
Protocol analysis
Analyze protocol layers within packets (e.g., Ethernet, IP,
TCP, UDP, HTTP, etc.) to understand data flow and state
at each layer
Network Packet Analysis

## Page 16

16
01. current page topic
Network Packet Analysis02
HTTP
HyperText Transfer Protocol
FTP
File Transfer Protocol
Characteristics:
Protocol for transferring documents between a web server and a client
(browser). Usually uses TCP port 80. Transmits data in unencrypted text,
which can be vulnerable to eavesdropping or data tampering.
Analytics points:
Analyze the nature of web traffic and server responses via URLs, methods
(GET, POST, etc.), and status codes (200, 404, etc.). Analyze header
information to determine cache policies, cookies, referrers, user agents, and
more. If HTTP requests are made with an unusual frequency or pattern, you
may suspect a web-based attack or web crawl.
Characteristics:
Protocol for file transfers. Uses a control connection (CMD port 21) and a
data connection (data port 20) to send file commands and file data
separately. Poor security because usernames and passwords can be
transmitted unencrypted.
Analytics points:
Checks for possible exposure of user credentials (usernames and
passwords). Monitor file upload and download commands to detect
unauthorized transfers of sensitive files. Unusual access attempts or large
data transfers may indicate an internal data breach or external attack.
Network Packet Analysis

## Page 17

17
01. current page topic
Network Packet Analysis02
DNS
Domain Name System
SSL/TLS
Secure Sockets Layer/
Transport Layer Security
Characteristics:
A system that translates domain names into IP addresses.
Usually uses UDP port 53.
All web traffic on a network is initiated by a DNS query.
Analytics points:
DNS queries and responses are analyzed to determine the legitimacy of the
domain being attempted to reach. Unusually frequent DNS queries can be
indicative of DNS tunneling, DDoS attacks, and more. Queries to malicious
domains may indicate a malware infection or data exfiltration attempt.
Characteristics:
A protocol for encrypting data to transmit it securely over the Internet.
Mostly used for HTTPS, secure FTP, etc.
Analytics points:
Even though the traffic is encrypted, the certificate information exchanged
during the SSL/TLS handshake allows you to assess the trustworthiness of
the communicating servers. Assess the security level of the communication
by analyzing the version of the encryption protocol and the encryption
algorithm used. Unusual certificate usage or encryption algorithms may
indicate a man-in-the-middle (MITM) attack or misconfiguration.
Network Packet Analysis
