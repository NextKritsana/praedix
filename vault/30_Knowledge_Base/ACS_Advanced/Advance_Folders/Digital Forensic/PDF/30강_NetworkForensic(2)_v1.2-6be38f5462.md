---
title: "30강_NetworkForensic(2)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\30강_NetworkForensic(2)_v1.2.pdf"
source_size_bytes: 642025
source_modified: 2025-10-18T20:17:16
imported_at: 2026-06-14T14:25:20
tags:
  - acs
  - acs-advanced
  - imported
---

# 30강_NetworkForensic(2)_v1.2

- Source: [30강_NetworkForensic(2)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/30%EA%B0%95_NetworkForensic%282%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Network Forensic (2)
• Collecting Network Packets
• Decrypting Encrypted Packets
30
1

## Page 2

2
01. current page topic
Collecting Network Packets01
Artifacts on Wi-Fi connections
SSID
(Service Set Identifier)
MAC address
(Media Access Control Address)
IP address
(Internet Protocol Address)
About DHCP
(Dynamic Host Configuration Protocol)
Security settings
Connection logs and events
The name of the connected Wi-Fi network.
This is used to identify the network to which the user is connected.
The unique address assigned to the device's network interface card (NIC).
Includes the MAC address of the connected device and access point (AP).
The IP address assigned to a device connected to the network.
Can include internal IP addresses and gateway addresses.
A protocol that provides network settings information, such as IP addresses,
subnet masks, DNS servers, and router (gateway) addresses.
Can include lease information from a DHCP server.
Information about the Wi-Fi network's security protocols, such as WEP, WPA, and WPA2.
Includes the type of encryption and authentication method used for the connection.
Logs of network events, such as network connections and disconnections, authentication
failures, IP address renewals, etc.

## Page 3

3
01. current page topic
Collecting Network Packets01
How to collect artifacts from Wi-Fi connections
Network analysis tools
You can use network analysis tools like Wireshark, tcpdump,
and others to capture and analyze real-time network traffic.
This allows you to capture and analyze data packets as they
occur over the course of a connection.
Security tools
Can use network security management and monitoring tools
(e.g., Nmap, Kismet, etc.) to investigate the security settings
and vulnerabilities of connected networks.
Operating system logs
Most operating systems store logs related to network
connections in the system log file. You can find this
information in Event Viewer on Windows and in the system
log files (/var/log/syslog, /var/log/wifi.log, etc.) on Linux and
macOS.
Network settings file
Profile and settings information for the connected Wi-Fi
network is stored in a settings file, depending on your
operating system. For example, on Windows, you can view
Wi-Fi profiles using the netsh wlan show profiles command.
Collecting Network Packets

## Page 4

4
01. current page topic
Collecting Network Packets01
Artifacts on LAN connections
MAC address
(Media Access Control Address)
IP address
(Internet Protocol Address)
About DHCP
(Dynamic Host Configuration Protocol)
ARP tables
Network connection logs
About network shares and services
The unique physical address assigned to a network interface card (NIC).
Contains the MAC addresses of all connected devices.
The internal IP address assigned to a network-connected device.Assigned by a
DHCP server, or specified through static IP address settings.
Network settings information, such as the IP address, subnet mask, gateway address, and
DNS server information assigned to the device from a DHCP server. Includes DHCP lease
duration and assignment history
Information that maps an IP address to the MAC address of the device with that IP address.
Provides information needed to communicate between devices on the network.
Logs that record events such as network connection and disconnection events,
authentication failures, IP address renewals, and more.
Information shared with services running on the LAN, such as file shares,
printer shares, web servers, FTP servers, etc.
Collecting Network Packets

## Page 5

5
01. current page topic
Collecting Network Packets01
How to collect artifacts from LAN connections
Network analysis tools
Use network analysis tools such as Wireshark and tcpdump to
capture and analyze network traffic, which can help you gather
network communication patterns, traffic volumes, protocol
usage information, and more
Network management tools
Uses network scanning tools such as Nmap and NetScan to
discover and gather information about devices, services, open
ports, and more on
 's LAN.
Operating system commands
MAC addresses and IP addresses can be viewed with the
following commands: ipconfig /all (Windows), ifconfig (Linux,
macOS), arp -a (ARP table lookup). For DHCP lease information,
use the ipconfig /displaydns command on Windows, or check the
/var/lib/dhcp/dhclient.leases file on Linux.
System log files
On Windows, you can view network-related logs in Event Viewer.
On Linux, you can find network events in system log files such as
/var/log/syslog and /var/log/messages.
Security tools and log management systems
Collect security-related artifacts from logs and alerts generated by security
information and event management (SIEM) systems, firewalls, intrusion
detection systems (IDS), and more.
Collecting Network Packets

## Page 6

6
01. current page topic
Encrypted Packet02
Security for each protocol
HTTP
HyperText Transfer Protocol
HTTP itself does not provide encryption
Sends text data in plain text, making it
vulnerable to man-in-the-middle attacks
HTTPS (HTTP with SSL/TLS) encrypted over

SSL/TLS ensures the confidentiality and
integrity of data and provides secure
communication between client and server.
FTP
File Transfer Protocol
Username, password, and file contents
being sent are sent in plain text to
 because no encryption is provided
Sessions and data transfers to
 can be encrypted over FTPS (FTP with
SSL/TLS) and SFTP (FTP with SSH)
FTPS adds an SSL/TLS layer to encrypt
your data,
SFTP provides encryption for file
transfers over the SSH protocol

## Page 7

7
01. current page topic
Encrypted Packet02
Security for each protocol
DNS
Domain Name System
Traditional DNS queries and responses
are sent in plain text, unencrypted
This can cause multiple issues with user
privacy and data security
DNS over HTTPS (DoH) and
 DNS over TLS (DoT) encrypt
 DNS queries using HTTPS and TLS
protocols, respectively.
This method helps secure DNS queries
and protect user privacy from man-in-
the-middle attacks
FTP
File Transfer Protocol
SSL and its successor, TLS, are standard
protocols for encrypting data over a network.
These protocols negotiate an encrypted
connection between the server and client
during a handshake, and encrypt data transfers
using symmetric key cryptography.
SSL/TLS not only provides encryption to ensure
confidentiality of data, but also supports
authentication of both parties communicating
with
and verification of the integrity of the data
It is the foundation of many encrypted
protocols, including HTTPS, FTPS, DoH, DoT,
and more.
Encrypted Packet

## Page 8

8
01. current page topic
Encrypted Packet02
TLS Protocol - Handshake
The handshake process
A TLS connection is initiated through a handshake process
 During this process, the client and server verify each other's identity and negotiate the algorithm and key to use for
encryption.
01.
ClientHello:
A cipher available to the client
suite (a set of encryption algorithms)
and random data to the server.
02.
ServerHello:
The server sends the selected cipher
suite and
and its own random data
to the client.
03.
Server authentication and key exchange:
The server sends its certificate to the client, along with key
exchange information if necessary.
04.
Client authentication and key
exchange:
If required, the client must also
provide a certificate and perform a
perform a key exchange
05.
Generate a pre-master secret:
The client and server derive the pre-
master secret using their respective
random data and the key information
exchanged.
06.
Generate a session key: Generates a
session key (symmetric key) based on
a pre-master secret and random data
Encrypted Packet

## Page 9

9
01. current page topic
Encrypted Packet02
Encryption Methods in the TLS Protocol
Data encryption
If the client and server are
using the same key to
encrypt and
decrypt data using the
same key.
Verify message
integrity
Ensure message integrity by
using message authentication
codes (MACs) or Authenticated
Encryption with Associated
Data (AEAD) mode.
Session
resumption and
tickets
Stores information from
already established
connections and uses it to
quickly reconnect
Encrypted Packet

## Page 10

10
01. current page topic
Encrypted Packet02
VPN (Virtual Private Network)
A technology that enables secure data transfer over a
public network (the Internet) by acting as if it were a
private network.
Creates an encrypted virtual tunnel between a user and a
remote network, providing a secure connection that is
invisible to the outside world.
Businesses can use VPNs to allow remote employees to
securely access corporate networks, and individual users
can use them to protect their privacy, maintain
anonymity, access geo-restricted content, and more.
Encrypted Packet

## Page 11

11
01. current page topic
Encrypted Packet02
How a VPN works
User authentication
Establish a connection between the VPN client and
the VPN server
Encryption key exchange
Transferring data
Data processing at the destination
Transmission and decryption of response data to the
VPN client
Ending a session
Encrypted Packet

## Page 12

12
01. current page topic
How VPNs encrypt
Handshake encryption
Used at the beginning of a VPN connection to establish a secure
communication channel between you and the VPN server.
This process involves authenticating each other's identities and
negotiating encryption keys to be used during the session.
Rivest-Shamir-Adleman (RSA): One of the most widely used public key
cryptography methods, used for user authentication and key
exchange.
Elliptic Curve Cryptography (ECC): An algorithm that provides the
same level of security with a smaller key size compared to RSA, and is
increasingly being used.
Diffie-Hellman: Used for secure key exchange and, when implemented
in a way that supports "Perfect Forward Secrecy" (PFS), ensures that
traffic captured in the past cannot be decrypted even after key
exposure.
Encrypted Packet02

## Page 13

13
01. current page topic
Encrypted Packet02
How VPNs encrypt
Advanced Encryption Standard (AES): The most widely used symmetric-key
encryption algorithm, supporting 128, 192, and 256-bit key sizes.
Encryption method: AES uses multiple rounds of a permutation-transposition
network to encrypt data.
Each round performs a complex transformation (byte substitution, row shift,
column shuffle, XOR with the round key) using the round key.
ChaCha20: Alternative algorithm that offers high performance and good
security, especially faster than AES on mobile devices
Encryption method: ChaCha20 uses an initialization vector (IV) and counters
to create an initial state, and then performs 20 rounds of complex
computation (iterations of quarter rounds) to generate a key stream.This
keystream is encrypted using an XOR operation with the real data
Authentication is another important aspect of a VPN connection, ensuring the
integrity of the data and the identity of the sender.Authentication methods
primarily use Hash-Based Message Authentication Codes (HMACs), which use
hash functions from the Secure Hash Algorithm (SHA) family to provide
message authentication.
Encrypted Packet

## Page 14

14
01. current page topic
Encrypted Packet02
VPN tunneling HOW VPN TUNNELING WORKS
SETTINGS FOR
ENCRYPTED
CONNECTIONS
ENCAPSULATI
NG DATA
DECRYPTION
AND
FORWARDINGUSING TUNNELING
PROTOCOLS
SENDING
ENCRYPTED DATA
A secure connection is
established between the VPN
client and VPN server
Your data is packaged into
"packets" by the VPN tunneling
protocol, which are then
"encapsulated" with additional
header information.
The VPN server decrypts the
received data packets, removes
the encapsulation, and forwards
the data to its final destination.
Encapsulated data packets are
encrypted and sent over the
internet to the VPN server
Wrapping (encapsulating) data using a
specific protocol and sending it over an
encrypted connection
Encrypted Packet

## Page 15

15
01. current page topic
Encrypted Packet02
Padding
P a d d i n g  i n  e n c r y p t i o n
Cryptographic algorithms often require
blocks of data of a specific size. For
example, block cipher algorithms process
blocks of a fixed size, such as 128 bits or
256 bits. If the source data doesn't
exactly match the block size of the
encryption algorithm, padding can be
used to resize the data blocks to fit. This
ensures that the encryption process runs
smoothly.
D a t a  s t o r a g e  a n d  t r a n s f e r
Databases or network protocols sometimes
require data to be a certain length.
If the actual length of the data falls short of
the requirement, padding can be added to
adjust the length.
Ensure consistent processing of data and meet
the requirements of the protocol or storage
mechanism.
Padding plays an important role in information security. Poorly handled padding in encrypted messages can create security vulnerabilities, which can
be exploited through attack techniques such as padding oracle attacks. Therefore, when using padding, it is important to choose the appropriate
method to maintain security and to take care during encryption and data processing.
Encrypted Packet

## Page 16

16
01. current page topic
Encrypted Packet02
PKCS#7 (Public-Key Cryptography Standards #7) / CMS (Cryptographic Message Syntax)
Key features and uses
Support for different types of data: PKCS#7 can encrypt and sign any type of data, including binary
data, text data, etc.
Supports multi-signature: Multiple users can digitally sign a single document or message, which can
be useful in collaborative environments.
Certificate-based encryption: PKCS#7 uses public key cryptography based on X.509 certificates. This
authenticates the sender of the message and ensures the integrity and confidentiality of the data
Ensure data integrity and confidentiality: Digital signatures ensure that messages have not been
tampered with, and public key encryption keeps message content safe and secure
Certificate chain embedding: PKCS#7 format can include a certificate chain with the message
This ensures that the recipient of the message has all the information they need to validate the
signer's certificate.
Usage examples
Digital signatures: Apply digital signatures to documents, emails, software update packages, etc. to
authenticate the identity of the sender and verify the integrity of the data
Data encryption: By encrypting data using PKCS#7 when transmitting sensitive information, you can
protect it from viewing by unauthorized parties
Certificate management: PKCS#7 can also be used for certificate distribution and management,
especially useful for managing multiple certificates and keys
Encrypted Packet

## Page 17

17
01. current page topic
Encrypted Packet02
Zero Padding Zero Padding
One of the padding techniques used to make data into blocks of a
specific length. Block ciphers used in cryptographic processes typically
require blocks of a fixed size. If the length of the input data is not an
integer multiple of the block size, padding is required to make the data
blocks fit into the appropriate length. As the name implies, the gaps are
filled in with zeros (zeroes).
Source data 0x12 0x34 0x56 0x78 0x9A
After applying
padding 0x12 0x34 0x56 0x78 0x9A 0x00 0x00 0x00 0x00
Features
Very simple to implement, no additional information is required to pad the
data. Padding can be applied regardless of the actual length of the data.
Limitations
During the de-padding process, it can be difficult to distinguish between the
original data and the padded zeros. If the original data naturally ends in a
zero, errors can occur because there is no information to distinguish
between the padded zeros and the zeros in the original data.
Encrypted Packet
