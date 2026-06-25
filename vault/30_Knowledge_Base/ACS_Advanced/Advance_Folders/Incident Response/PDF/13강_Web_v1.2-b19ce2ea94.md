---
title: "13강_Web_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\13강_Web_v1.2.pdf"
source_size_bytes: 1436888
source_modified: 2025-11-12T12:24:54
imported_at: 2026-06-14T14:26:29
tags:
  - acs
  - acs-advanced
  - imported
---

# 13강_Web_v1.2

- Source: [13강_Web_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/13%EA%B0%95_Web_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

What is a browser?
• What is a browser?
• Chrome Artifacts
• Edge
13
1

## Page 2

What is a browser?01
• Control the behavior between the interface and
the rendering engine
• Rendering engine parses and displays requested
resources
• Chrome maintains separate rendering engine
instances
• Each tab is treated as an independent process
Engine
• Screens that users interact with most
• The user interface includes configuring the
browser GUI, such as the search bar, undo,
redo, and renew.
User interface
Display the resource the user selected after
requesting it from the server
The address of the requested resource is
determined by the URI
Interprets and displays HTML files according to
HTML and CSS specifications
Main features
Tools to access your site
Web Browser?
2

## Page 3

What is a browser?01
Browser
Artifact
• Traces created by user behavior as
web applications and web
browsers communicate with each
other
• Contains a variety of information
related to web browsing activity
• Can be used to respond to a
breach in the event of a
cybersecurity incident
Track user activity
See what web activity has occurred through traces of
web pages visited, search history, and more
Identify web browsing patterns, targeted web pages,
and more to understand intrusion motives and methods,
and build a response strategy
1
Identify propagation vectors and attack types
Identify information associated with malicious websites
Analyze malicious domains used by the attacker or
malicious files downloaded
Check the history of defenses against attacker attempts
2
ETC..
Traces of download history, browsing history, cache,
access history, etc.
Determine the scope of the cybersecurity incident,
understand the attacker's motives and methods, and
take appropriate response and prevention measures
3
History urls
Download Cache
Keywordvisit
3

## Page 4

What is a browser?01
Check the scope of the damage
• Analyzing web artifacts can reveal how far an attack has spread
• If the sender of the email was an insider, the likelihood that their PC was also
infected
• Estimate the approximate scope of the attack if it occurred within the
company's internal network
Understanding the starting point
When a cybersecurity incident occurs, finding the starting point of the event is key
Web artifact analysis can help you understand what malicious behavior occurred
when a user received a malicious email or visited a specific website
Example
• Spearphishing tricks users into running attachments
• Downloading cracked versions of paid programs from the internet
• Game hacks
4

## Page 5

0
18
35
53
70
88
chrome safari firefox edge
Web browser share
chrome safari firefox edge
What is a browser?01
Keyword
Chrome browser dominates, share of more than 60% and reaching nearly 70%
Edge has been slowly gaining ground since 2020
Highly extensible, fast
Provides a simple interface
Chrome
Synchronizing your devices
Tracker blocking features
Safari
Tracker Blocker Features
Ad social blocking, capture tool support
Firefox
Fewer ads
Window 10 basic installation
Edge
5

## Page 6

What is a browser?01
C
Chrome
Browsers with the highest market share 68%
E
Edge
Windows provides a browser by default4%
C
Performance and speed, user experience and UI
Openness, extensibility, and support for multiple
platforms
Continuous updates from Google
E
Microsoft's own security features
Integration with Microsoft 365
Fewer resources
6

## Page 7

Chrome Artifacts02
A cybersecurity incident perspective
• Determine what web pages were visited along with the time of day when the
intrusion occurred
• It is possible that a user's access to a malicious website is recorded in the web
history, so you can analyze the web history to determine if the user was
unintentionally exposed to a malicious site
• It shows the user's behavior patterns, which can be analyzed to distinguish between
normal and abnormal behavior
• Determine if you've been exposed to phishing sites or social engineering attacks
A system or feature that stores and manages a history of web pages visited by a user through a web browser
Web history tracks a user's browsing activity and records information about previously visited web pages
This history is retained even if the browser is closed and reopened, and is utilized by autocomplete features when a user attempts to revisit a web page in a web
browser
PATH
%UserProfile%AppData\Local\Google\Chrome\User Data\Default\History
History
7

## Page 8

Chrome Artifacts02
Browser
For
SQLite
Chrome
History
Storage method
Chrome stores your web browsing activity in a database file in SQLite format
Stored in a file named History, including the URLs of web pages you visited, the time of visit, page titles, etc.
SQLite
Use the Browser for SQLite tool to open that database
file and extract and visualize the information you want
with SQL Query
8

## Page 9

Chrome Artifacts02
Main tables
Download history
Downloads
Keyword search history
Keyword Search Terms
Manage a user's access URL
urls
Access URL, access time
visits
Web History
9

## Page 10

Chrome Artifacts02
View URLs of web pages users have visited
URL
View titles of webpages you've visited
TITLE
The number of visits to a specific webpage
For Typed_count, it means the number of
times a URL was visited by typing it in the
address bar
Visit count
When the web page was last visited
Chromium Time Stamp
Last Visit Time
10

## Page 11

Chrome Artifacts02
Record the history of web pages users visit
Can provide critical information in cyber security incident
detection and response
visit?
Representing when visits occurred in chromium Time
Determine when a user visited a specific website
visit_time
See how long a visit lasted
duration
Identify patterns and types of user activity
In the event of a cybersecurity incident, this information can be
used to determine the origin of the incident
Composite
visits
11

## Page 12

downloads
Store a record of the files that users download
downloads?
When the file download started
The time the file download finished
Start time, End time
Full path of downloaded files
The location where the downloaded file is stored
full path
Record where the download started
referrer
Chrome Artifacts02
12

## Page 13

Chrome Artifacts02
Web Cache
Data from the sites you visit when you access a website
Web cache should be checked in most cases when the web is used during the course of a cyber security incident
Images, text, icons, HTML, etc.
Must be manually deleted by the user
Storage information
Automatically download data based on page design
Improve webpage loading speeds
Purpose
Can be tampered with and used to access malicious pages
Risks
Index Record with a size of 24 bytes
URL Record information at locations 0x18 through 0x1B
URL Record data starting at 0x 2000
Structure
C:\Users\[User Profile]\AppData\Local\Google\Chrome\User Data\Default\Cache\Cache_Data
PATH
Navigate to that location and you'll see files like data 0, data 1, data 2,
etc.
In addition to these, there are also several files that start with f
13

## Page 14

Web Cache
File Name
Data_0
Data_1
Data_2
Data_3
Index Record of Cache Data is saved
Storing cache data
If cache data is large, store it in F_000(N)
Chrome Artifacts02
14

## Page 15

00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
91 65 EA 3B 05 66 2F 00 91 65 EA 3B 05 66 2F 00
FD 01 00 90 03 00 00 90 02 00 01 A1 00 00 00 00
F2 9F 60 02
Web Cache
Stored in data_1Block Index
0x0002 as the Little Endian value
Block units
• Data_1 = 0x100
• Data_2 = 0x400
• Data_3 = 0x1000Block Index * Block Units + Block Index Start Position
0x0002 * 0x100 + 0x2000 = 0x2200
Chrome Artifacts02
15

## Page 16

Web Cache
Chrome Artifacts02
Metadata
URL
Description
Location 0x2200 in Data_1
See that we have the above 0x50 bytes of metadata and a variable length url
16

## Page 17

00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
73 56 14 B3 00 00 00 00 00 00 00 90 1D 00 00 00
00 00 00 00 00 00 00 00 AC E7 78 5F EF 65 2F 00
D3 00 00 00 00 00 00 00 B0 1F 00 00 5F 00 00 00
00 00 00 00 00 00 00 00 16 0B 03 C1 4B 1F 01 A0
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
URL start position is variable
Web Cache
URL Size: 211 Metadata size: 8112 Data size: 95
Metadata locations Data location and name
Chrome Artifacts02
17

## Page 18

Web Cache
Name Hex Value Dec Value
URL size 0x000000D3 211
Metadata size 0x00001FB0 8112
Data size 0x0000005F 95
Metadata locations 0x160B03C1
Data location 0x4B1F01A0
Metadata location
0x0B16*0x1000+0x2000 = 0xB18000
Data location
0x1F4B*0x100+0x2000 = 0x1F6B00
Chrome Artifacts02
18

## Page 19

Chrome Artifacts02
Start offset
End offset
Select Block
hex dec bin
Start offset
End offset
Select Block
hex dec bin
Incident perspective
If cached data contains sensitive information, you can find the vulnerabilities used to access that information and take remediation action
Analyzing and detecting the presence of malware or malicious scripts propagating through the cache
Analyze cached data to detect unauthorized access to or manipulation of sensitive information to prevent man-in-the-middle or phishing attacks through web caches
1FB0
Metadata Size
5F
Data Size
19

## Page 20

Chrome Artifacts02
Persistent cookies are cookies that remain valid
until a set expiration date, even if the user
closes the browser
Persistent Cookie
• Secure Cookies are only sent over a secure
connection
• HttpOnly Cookie increases security by preventing
JavaScript from accessing the cookie
• SameSite Cookie is set to prevent CSRF attacks
Etc
Session Cookies are cookies that are only valid until
the user closes the browser, and are typically utilized
to maintain the user's session state
Session cookie
Small text file that exchanges and stores
information between a web browser and a
web server
Used to maintain the user's session state
What are cookies?
20

## Page 21

C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\Network\
PATH
SQLite
Use the Browser for SQLite tool to
open that database file and extract
and visualize the information you
want with SQL Query
Put the value of Creation utc into
Dcode to see the time value
Creation utc
Chrome Artifacts02
21

## Page 22

Edge03
WebCacheV01.dat
A WebCacheV01.dat file is a file that stores web cache data associated with Internet Explorer and Microsoft Edge in the Microsoft Windows
operating system
The file is located on the user's local disk and is used by the browser to store some or all of the contents of previously visited web pages
Stores elements such as HTML, CSS,
JavaScript, images, and more from
previously visited web pages
Load web pages faster and save bandwidth
Web page content
Stores authentication information, such as
a user's login state or session information
Users can access web pages without
having to log in again
Cookies and authentication
information
Stores temporary files and cache data used
by web pages
Can be loaded quickly on return visits
Temporary files and cache data
Browser history and log information
Logs and history of web pages
Microsoft
Edge
Considerations
The WebCacheV01.dat file is in the Extensible Storage Engine (ESE) Database Format file structure and unlike other files, it cannot be analyzed directly from the path above
This is because the WebCacheV01.dat file is in use by another process when you try to read access it
22

## Page 23

Edge03
Info
IE10 Analyzer
Name
Originally used to analyze Windows
7 operating systems, this tool can
also analyze WebCacheV01.dat
When
https://github.com/moaistory/IE10Analyzer
Download PATH
ABOUT Tools
23

## Page 24

Edge03
01
02
03
04
Select a file
Start analysis
Analysis complete
Display
analysis results
Start Analysis
IE10Analyzer analyzes the web cache
data based on the selected file
Select the WebCacheV01 file
After running the IE10 Analyzer program,
select the WebCacheV01.dat file you want
to analyze
Displaying analytics results
View analytics results to provide detailed
information about the web pages visited
by users of your web browser and their
activity history
Completing the analysis
When the analysis is complete, the tool
provides information such as web page
visit history, cached resources, cookies, and
more
24

## Page 25

• Create Time
• Modified Time
• Accessed Time
• File Name
• Url
• Etc…
Verifiable information
Edge03
25
