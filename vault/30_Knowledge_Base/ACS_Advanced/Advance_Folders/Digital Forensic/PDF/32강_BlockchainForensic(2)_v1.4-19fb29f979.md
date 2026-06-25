---
title: "32강_BlockchainForensic(2)_v1.4"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\32강_BlockchainForensic(2)_v1.4.pdf"
source_size_bytes: 535652
source_modified: 2025-10-18T20:21:20
imported_at: 2026-06-14T14:25:21
tags:
  - acs
  - acs-advanced
  - imported
---

# 32강_BlockchainForensic(2)_v1.4

- Source: [32강_BlockchainForensic(2)_v1.4.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/32%EA%B0%95_BlockchainForensic%282%29_v1.4.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Blockchain Forensic (2)
• Hot Wallet
• Cold Wallet
• Mnemonic codes
32
1

## Page 2

2
Hot Wallet01
Hot Wallet
Accessibility
Convenience
Vulnerabilities
Versatility
A digital wallet that stores cryptocurrency while connected to the internet.

## Page 3

3
01. current page topic
Hot Wallet01
A typical example of a hot wallet
Desktop wallet
 Mobile wallets Web Wallet
Hot Wallet

## Page 4

4
01. current page topic
Hot Wallet01
How to collect digital evidence in Hot Wallet
05
06
07
08
Web browser and cache analytics
Get third-party service history
Temporal analysis of digital evidence
Tracking transaction history
01
02
03
04
Device imaging and data extraction
Memory analysis
Monitoring network traffic
Analyzing log files
Hot Wallet

## Page 5

5
01. current page topic
Hot Wallet01
How to track and analyze Hot Wallet transactions
Analyze transaction patterns Leverage visualization tools
Tracking money flow Use advanced analytics tools and services
Using Blockchain Explorer
Clustering techniques
Hot Wallet
Analyzing Multisig Transactions

## Page 6

6
01. current page topic
Cold Wallet02
Cold Wallet A digital wallet that stores cryptocurrency without an internet connection.
Protects assets from cyber threats such as online hacking,
phishing, and malware by storing cryptocurrency private keys in a
physically isolated environment
In this level of security, cold wallets are considered a very suitable
storage method for individuals or businesses that want to keep large
amounts of cryptocurrency safe for long periods of time.

## Page 7

7
01. current page topic
Cold Wallet02
Hardware wallets
 Paper wallets
How To Make An Ethereum Paper Wallet? [Easily] (themoneymongers.com)
Bitcoin paper wallet generated using https://bitcoinpaperwallet.com.... | Download Scientific Diagram (researchgate.net)
A typical example of a cold wallet
Cold Wallet

## Page 8

8
01. current page topic
Cold Wallet02
Hardware security Wallet simplicity
Backup and recovery process Sturdy physical structure
Physical isolation Security awareness
Multisig options
Cold Wallet's security mechanisms
Cold Wallet

## Page 9

9
01. current page topic
Cold Wallet02
Attributes Cold Wallet Hot Wallet
Storage methods Offline storage
(hardware wallets, paper wallets)
Save online
(Desktop, mobile, web wallet)
Security levels Very high Low
(Security vulnerabilities due to internet connectivity)
Ease of use Low
(Must be moved online when performing transactions)
High
(easily accessible anytime, anywhere)
Primary purpose Long-term storage and
storing large amounts of cryptocurrency
Daily transactions and storing small amounts of
cryptocurrency
Risk of hacking Very low
(Risk of physical loss exists)
High
(Risk of cyberattacks and hacking)
Difference between cold and hot wallets
Cold Wallet

## Page 10

10
01. current page topic
Cold Wallet02
Evidence preservation and analysis technologies used in Cold Wallet
01.
Physical preservation
of hardware wallets
02.
Forensic imaging of
storage media
03.
Recover deleted data
04.
Decrypting encrypted
data
05.
Use forensic analysis
software
06.
Analyze documents
and metadata
Cold Wallet

## Page 11

11
01. current page topic
Mnemonic codes03
Mnemonic Code
A translation of a cryptocurrency wallet's private key into human-readable words.
Typically consists of 12, 18, or 24 words, selected from a standardized list of words.
Concept and structure of mnemonic codes
Generated in the manner defined by Bitcoin Improvement Proposal (BIP) 39. Provides a way to convert a
user's wallet private key into a list of words that can be easily remembered and recovered. Each word
represents one of a list of 2048 predefined words, the order and combination of which provides sufficient
entropy (randomness) that can be used to generate the private key.
The role of mnemonic code
Backup and recovery, user-friendliness, multi-currency and wallet compatibility, security

## Page 12

12
01. current page topic
Mnemonic codes03
BIP-39
Bitcoin Improvement Proposal 39
Define a standard for how to generate mnemonic phrases (mnemonic codes) that can be used to
recover the private keys of Bitcoin and other cryptocurrency wallets.
Key Features of BIP-39
Generating mnemonic phrases: BIP-39 uses the initial entropy (random data) to generate a mnemonic phrase consisting
of a series of words (typically 12, 18, or 24).
Entropy and security: The length (number of words) of the generated mnemonic phrase is directly related to the
amount of initial entropy; the longer the mnemonic phrase, the more secure it is.
Recovery phrase: The generated mnemonic phrase can be used to recover a user's wallet or private key.
Optional additional security: Users can add an optional security phrase called a "passphrase" to the mnemonic phrase
for additional security.
The importance of BIP-39
User-friendliness: by converting complex private keys into a sequence of easy-to-remember words, users can easily
backup and recover their wallets
Compatibility: BIP-39 is widely supported by multiple wallet providers and platforms
Security: When managed correctly, mnemonic phrases provide a high level of security
Mnemonic codes

## Page 13

13
01. current page topic
Mnemonic codes03
LevelDB and IndexedDB
Why LevelDB and IndexedDB were created
LevelDB is a fast, lightweight, disk-based key-value store developed by Google. In applications like
Metamask, LevelDB is used to securely store sensitive data such as a user's wallet information,
transaction history, private keys, and encrypted mnemonic codes. This information is essential for
managing interactions with the blockchain network and recovering previous state when a user logs
back in.
IndexedDB is one of the APIs that provide storage for browsers, and is a low-level API for storing
complex data on the client side. In Metamask, IndexedDB is used to store user settings, environment
synchronization information, currency exchange rates, and more. This improves the performance of
the application and makes some features available even when offline.
The role of LevelDB and IndexedDB
Data storage and recovery: Securely store users' wallet and transaction information, easily accessible
when needed
Preserving user settings: By saving your preferences and settings, providing a consistent user
experience across browser sessions
Efficient data handling: by processing and managing data directly within the browser reducing server
load and speeding up response times
Support for offline capabilities: Allows users to look up information or perform perform simple tasks
without a network connection
Mnemonic codes

## Page 14

14
01. current page topic
Mnemonic codes03
Mnemonic Code Related Articles
Mnemonic codes

## Page 15

15
01. current page topic
Mnemonic codes03
Mnemonic Code Algorithm
PBKDF2-SHA256
PBKDF2 (Password-Based Key Derivation Function 2) is a password-based key derivation function.
This algorithm takes a user's password and a salt (a random piece of data) as input,
generates a secure key of fixed length through an iterative hashing process.
SHA-256 is the hsash function used in this process, which generates a 256-bit hash value.
PBKDF2-SHA256 is specifically used to generate secure encryption keys based on passwords,
It is used in password-based encryption to increase resistance against brute-force and
brute force and dictionary attacks in password-based encryption.
AES-256-GCM
AES(Advanced Encryption Standard) is a symmetric-key encryption standard.
 AES-256 is a form of AES encryption that uses 256-bit keys, providing a very high level of security.
GCM (Galois/Counter Mode) is one of the operating modes for AES, providing high processing speed
and parallelism.
AES-256-GCM provides the ability to verify the integrity and authenticity of data at the same time as
encryption, increasing safety while protecting data. This mode is used in a variety of applications,
including financial transactions, transmission of sensitive information, and database encryption.
Mnemonic codes

## Page 16

16
01. current page topic
Mnemonic codes03
BIP-0039 conversion process
0xFCCF1AB3329FD5DA3DA9577511F8F137
wolf juice proud gown wool unfair wall cliff insect more detail hub
Generate initial endropy Add a checksum
Convert entropy + checksum to mnemonic code Create a mnemonic phrase
Mnemonic codes

## Page 17

17
01. current page topic
Mnemonic codes03
Decrypting the Mnemonic Code Algorithm
Mnemonic codes
