---
title: "27강_Anti-Forensic(2)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\27강_Anti-Forensic(2)_v1.2.pdf"
source_size_bytes: 824374
source_modified: 2025-10-18T20:14:31
imported_at: 2026-06-14T14:25:17
tags:
  - acs
  - acs-advanced
  - imported
---

# 27강_Anti-Forensic(2)_v1.2

- Source: [27강_Anti-Forensic(2)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/27%EA%B0%95_Anti-Forensic%282%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Anti-Forensic
• Data encryption
• Data manipulation
27
1

## Page 2

2
01. current page topic
Data encryption01
The process of converting original
information (plaintext) into an unreadable
form (ciphertext) to protect data.
Encryption
The process of reverting encrypted
information (ciphertext) back to its original
form (plaintext).
Decryption

## Page 3

3
01. current page topic
Data encryption01
Data encryption
The process of converting data into an encrypted, or
unreadable, form to protect sensitive information.
It is done using an encryption key, and the converted data
(ciphertext) is unreadable by anyone who does not know
the actual content of the original data (plaintext).The main
purpose is to ensure the confidentiality of data.

## Page 4

4
01. current page topic
Data encryption01
The same key is used to encrypt and decrypt data.
Symmetric-key encryption is fast and suitable for handling
large amounts of data, but key management and secure key
exchange methods are important.
Uses two keys. One is used to encrypt the data with the public key,
and the other is used to decrypt the data with the secret key. The
public key is accessible to anyone, but the secret key must be
known only to the recipient of the data. This method provides easy
key management and is highly secure, but is slower to process
than symmetric key encryption.
Symmetric key encryption Asymmetric key encryption

## Page 5

5
01. current page topic
Data encryption01
Full disk encryption uses symmetric key encryption. The user is required to enter a password, PIN, or key (such as a key stored on
a USB drive) when starting the system. This credential is used to decrypt the key that encrypted the disk, which is then usedto
decrypt all data within the system.
Full disk encryption
A technology that encrypts all data stored on a computer's hard drive or
solid-state drive (SSD).
How it works
When the system boots up, it requires some form of authentication from the user, such as a
password, PIN, or security token. Once the correct credentials are provided, the encrypted drive
is decrypted and available for normal use. When the system shuts down, the data is
automatically encrypted and protected from physical access or hacking attempts.
Key benefits
Data protection. Compliance, universal security.
Major drawbacks
Performance degradation, password management
Use cases
Full disk encryption is widely used in enterprise environments as well as by home users. It
is considered an essential measure to enhance data security, especially in the financial,
medical, and legal sectors that deal with sensitive information.

## Page 6

6
01. current page topic
Data encryption01
Decryption process
When the system boots, the user must provide authentication information
(password, PIN, etc.) that can decrypt the encryption key to access the encrypted
disk. If the correct credentials are entered, the internally stored encryption key is
used to decrypt the user's data. The system then boots normally and the user can
access the encrypted data.
How to set up BitLocker
1.Open Control Panel and go to System & Security > BitLocker Drive Encryption
2.Select Turn on BitLocker next to the drive you want to encrypt
3.Select an encryption method, and save the recovery key
4.Once the drive is encrypted, authentication (e.g., password, PIN, USB key, etc.) is
required every time the drive is accessed
Key features and capabilities of BitLocker
Full volume encryption:
BitLocker can encrypt system drives, fixed data drives, and removable data drives
(USB drives). It encrypts all data on the disk, including the operating system itself.
Multi-factor authentication:
Provides an additional layer of security using a Trusted Platform Module (TPM);
users can use a boot password, PIN, or USB key to unencrypt disks
Recovery mechanism:
Provide a recovery key or recovery password, giving users a way to regain access to
their data if the encrypted drive becomes inaccessible.

## Page 7

7
01. current page topic
Data encryption01
File-level encryption
Applies security directly to specific data files or documents, encrypting/decrypting
only those files or folders. File-level encryption requires that each time a user
attempts to access a specific file, they must decrypt it using the encryption key,
and when they are done using the file, it is stored encrypted again.
How it works
File-level encryption allows a unique encryption key to be used for each file or
folder. When a user opens or modifies a file, the encrypted file is automatically
decrypted, and when the user is done and saves the file, it is re-encrypted. This
is transparent to the user, and the user can use the file as normal without any
decryption steps..
Key benefits
Selective protection, security flexibility, and mobility
Major drawbacks
Key management, performance impact
Use cases
Ideal for protecting files or folders containing sensitive data, such as financial
information, personally identifiable information (PII), research materials, and legal
documents. Also used when certain data types need to be encrypted to meet
compliance requirements

## Page 8

8
01. current page topic
Data encryption01
File-level encryption approach
Automatic decryption
Command-line tools
Context menu options
Built-in features of the operating system
Use encryption software

## Page 9

9
01. current page topic
Data encryption01
Dynamic encryption
Data is encrypted and decrypted in real time as it is transmitted or stored. The encryption keys used
in this process can change continuously and are only decrypted at the time the data is used,
increasing the security of the data, especially in cloud computing, big data, and Internet of Things
(IoT) environments.
Key features of dynamic encryption
1.Real-time encryption and decryption : Data is encrypted and decrypted the moment it's created,
transmitted, and accessed, so it's always as secure as possible.
2.Key management : Dynamic encryption is highly secure because it can use different encryption
keys for different data or sessions. Keys change regularly, so even if an attacker steals a key, it
won't be usable for long.
Security based on the state of the data: Encryption is applied not only to data at rest (static data),
but also to data in transit over the network
(dynamic data), not just at rest (static), but also in transit across the network.
3.Increase compliance and security: Applies encryption not only to data at rest (static data), but also
to data in motion (dynamic data) as it travels across the network, ensuring that data remains secure
no matter what state it's in.
Decryption process for dynamic encryption
1.User authentication: Before a user can access data, they must first log into the system or go
through an authentication process, which can be done using a password, smart card, biometric
authentication, etc.
2.Key access and decryption: If authentication is successful, the system accesses the encryption key
from the key management system and decrypts the data. If symmetric key encryption is used, the
same key can be used to decrypt the data. If asymmetric key encryption is used, the data is
decrypted using a private key.
3.Data usage: The decrypted data is provided to the user, who can then perform the necessary
actions.When the user is done, the data is re-encrypted and stored.

## Page 10

10
01. current page topic
Data encryption01
Multi-layer Encryption
This approach encrypts data multiple times, each using a different encryption method or algorithm, and by
doing so, provides a much higher level of security than when using a single encryption layer.Multi-layer
encryption is used when you want to further protect your data, especially when processing or storing sensitive
information.
How it works
Multi-layer encryption involves encrypting data with a first layer, then encrypting the encrypted data again with
another encryption technique, and so on. The encryption keys used for each layer are different, and a user who
wants to access the data must have all the correct keys to decrypt all the encryption layers sequentially.
Pros
Enhanced security, flexibility, and compliance
Identification of encryption layers
The decryption process starts by identifying the layers of encryption applied to the data and the encryption
method used for each layer. This information may be recorded during the encryption process, or it may be
stored in a key management system (KMS).
Decrypt from the outermost layer
Decryption is performed sequentially, starting with the outermost layer and decrypting each layer in turn, in the
reverse order in which they were applied. The user or system must provide the appropriate decryption key to
decrypt each layer.
Use of decryption keys
Decrypting each layer requires either the same key as the key used to encrypt that layer (for symmetric-key
encryption) or a secret key paired with that key (for asymmetric-key encryption). Decryption keys are managed
in a secure manner and should only be accessible to authorized users or systems.t
Sequential decryption
Decryption proceeds from the outermost layer to the inner layers, with each step restoring the encrypted data to
its previous plaintext state Once all encryption layers have been successfully removed, the original data is finally
restored.
Validate your data
After decryption is complete, it may be necessary to verify the integrity and accuracy of the data.
This is to ensure that the data has not been corrupted during the decryption process.

## Page 11

11
01. current page topic
Data manipulation
Manipulating log files
Contains a record of system,
application, and network activity,
which can be a valuable source of
evidence in forensic investigations
Metadata manipulation
Includes information such as the
date and time the file was created,
modified, or accessed, the file
owner, and permission settings.
Timestamp manipulation
Change the timestamps (time
information) of files or system events
to manipulate when certain activities
occurred.
Data scrambling
The process of converting data into
an unreadable form, which can have
a similar effect to encryption.
Data manipulation
02

## Page 12

12
01. current page topic
Data manipulation02
Manipulating log files
The act of altering, deleting, or falsifying log files, which are records of events or activities
that occur on a digital device, to hide or manipulate the actual activity.Because log files play a
critical role in investigating, auditing, and monitoring security incidents on a system,
tampering with them violates security policies and is considered illegal in many cases.
Purpose of log file manipulation
Activity tracking avoidance: Used to erase traces of illegal access, hacking attempts, and
unauthorized access to sensitive data.
Interfering with security investigations: Impede or mislead the investigation of a security
incident, making it difficult to track down the actual attacker.
Audit and compliance violations: Manipulated log files to avoid negative results in a
compliance audit.
How to manipulate log files
Delete logs: Remove evidence of activity by simply deleting logs that occurred during specific
events or times of day.
Altering log contents: Altering or falsifying the content of an event by directly modifying the
data within the log file.
Hide logs: Hide or rename log files so that they are undetectable by common log analysis tools
or procedures.
Fake log generation: Creating and injecting fake logs to mislead security professionals'
investigations.
Countermeasures against log file manipulation
Log integrity verification: Regularly validate the integrity of log files to detect changes, which
can use techniques such as hash value calculation.
Centralized log management: Log data is sent to a centralized server and stored separately,
preventing log manipulation on local systems.
Access control and auditing: Strictly control access to log files and log all access and changes
to log files.
Log encryption: Encrypt log files, preventing unauthorized access to alter or delete logs.
Data manipulation

## Page 13

13
01. current page topic
Data manipulation02
Tripwire
Security and data integrity tools that monitor
changes to files and directories and alert you to
unauthorized changes. Takes snapshots of the
initial state of critical files and settings on your
system and continuously monitors subsequent
changes to ensure their integrity.
LogRhythm , Splunk (log management and analysis tool)
It provides aggregation and analysis of log data, as well as monitoring and alerting of
security-related events. They also enhance security posture by including the ability to verify
the integrity of log files. These programs are used to identify whether log files have been
altered and are essential for maintaining the reliability of log data and the security posture
of the system. Programs that verify the integrity of log files play an important role in
protecting sensitive data and systems when used in conjunction with an organization's
security policies.
Programs that verify the integrity of log files are used to ensure that log files have not been altered or tampered with. These
tools verify integrity by calculating the hash value of a log file and comparing it to previously generated hash values.
Integrity verification tools are an important part of the log management and security audit process.
Programs to verify the integrity of log files
Data manipulation

## Page 14

14
01. current page topic
Data manipulation02
Metadata manipulation
The process of changing, deleting, or adding to a file's metadata, which is structured information
about the file (e.g., creation date, modification date, geolocation, camera settings, etc.)
Privacy
Avoiding digital forensics investigations
Copyright management
Data management
Data manipulation

## Page 15

15
01. current page topic
Data manipulation02
Manipulating timestamps
Data manipulation
The process of artificially altering time information recorded in
other digital data, such as Created, Modified, and Accessed.
You can use PowerShell to make changes to the MAC Time of
the desired file.
# Change the Created time
$(Get-Item "File Path").creationtime = "Date and Time"
# Change the modified time
$(Get-Item "File Path").lastwritetime = "Date and Time"
# Change access time
$(Get-Item "File Path").lastaccesstime = "Date and Time"

## Page 16

16
01. current page topic
Data manipulation02
Data Scrambling
The process of randomly mixing or transforming data to make the original data less
identifiable. This technique is primarily used for the protection of sensitive information, de-
identification of personal information, and secure use of real-world data in test
environments. Data scrambling is a similar concept to data masking, data anonymization,
and data pseudonymization, but each term has subtle differences in scope and
methodology.
The main purpose of data scrambling
Privacy: Transforming real-world data to protect information associated with an individual's
identity.
Enhance data security: Storing or transmitting data in a form different from the actual data
to protect it from illegal external access.
Provide test data: Using scrambled data to protect real user data while creating a test
environment that resembles production.
How data is scrambled
Random Replace: Replacing values in the data with other randomly selected values.For
example, username or address information can be replaced with a random string of
characters.
Rule-based transformations: Applying specific rules or algorithms to transform data. For
example, moving date of birth information to a certain time period,
change some digits in a phone number
Pseudonymization: How to change your real name to a pseudonym to disconnect from
your real data, but still have the form you need to analyze it.
Shaping: Preserving the structure of data but content is filled with fictitious information to
hide the original data.
Data manipulation

## Page 17

17
01. current page topic
Data manipulation02
02 04
03
0501
Substitutions
How to replace each element
in the data with a different
value

Permutations
How to change the order of
elements in your data
Range-based
transformations
How to transform numerical data
based on ranges Date Shift
How to move time-related
data to over a period of time
Pseudonymization
How to prevent individuals
from being directly identifiable
by using pseudonyms instead
of real data
Data manipulation

## Page 18

18
01. current page topic
Data manipulation02
1.Create fictitious dataShaping is the process of manipulating specific data, usually in a
database or dataset, to preserve its shape but mask or change its
actual information. In the case of databases, shaping allows you
to use a data structure in a test environment that resembles
production, while protecting real-world sensitive information.
Shaping focuses on safely transforming the content while
maintaining the structure and integrity of the data.
Shaping lab: Fictional customer database example
This example uses Python to implement a shaping process on a
simple customer database. The example uses the pandas library to
create fictitious customer data, and applies shaping to this data to
transform real names and emails into fictitious information.
Necessary tools
Python, Pandas library-used for data processing
Shaping
Data manipulation

## Page 19

19
01. current page topic
Data manipulation02
2. data shaping: processing names and emails
Create simple fictitious customer data, and
manipulate each customer's name and email to
"CustomerX" and "customerX@example.com"
to hide their real information.
You can safely manipulate the content while
preserving the structure of the data.
Shaping
Data manipulation
