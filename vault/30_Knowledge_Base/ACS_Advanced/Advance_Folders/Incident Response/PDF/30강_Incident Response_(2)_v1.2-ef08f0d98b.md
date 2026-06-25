---
title: "30강_Incident Response_(2)_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\30강_Incident Response_(2)_v1.2.pdf"
source_size_bytes: 1129328
source_modified: 2025-11-12T13:25:53
imported_at: 2026-06-14T14:26:49
tags:
  - acs
  - acs-advanced
  - imported
---

# 30강_Incident Response_(2)_v1.2

- Source: [30강_Incident Response_(2)_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/30%EA%B0%95_Incident%20Response_%282%29_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Incident Response (2)
• Network
• Firewall
30
1

## Page 2

Network01
Firewall
Check your firewall configuration
Add a firewall
Delete a firewall
Network
Open Ports
Identify the processes using the
port
Ending a process
2

## Page 3

Infringement Continuance
Act01
Network
Open Port
• A network port is a virtual communication endpoint used to
transfer data in communications between a computer and a
network
• Port numbers are used to identify specific processes or services
running within a particular computer
• Ports are managed by transport layer protocols such as TCP or
UDP, each of which holds a different port space
• Ports from 0 to 1023 are the well-known ports
What is Port?
What is Open port
Open port
A few ports to keep
an eye on

Major ports
• If unnecessary ports are open, they pose a security threat
• Attackers can use these ports to perform malicious actions, such as
breaking into your system or stealing sensitive information
• It is important to periodically check which ports are open on your
system and close those that are not needed
• This will improve the security posture of your system and protect it
from potential threats
Open Port?
Network
3

## Page 4

Infringement Continuation
Law01
23
Telnet is a protocol for controlling a computer
remotely
Unlike SSH, Telnet uses plain text communication,
which makes it vulnerable to packet sniffing attacks
Vulnerable to packet sniffing attacks
By accessing a system remotely via Telnet, the system
is potentially exposed to various attacks such as brute
force attacks and dictionary attacks
20, 21
A port associated with the File Transfer Protocol (FTP),
which is a protocol for transferring files
FTP transmits usernames and passwords in plain text,
which is vulnerable to an attack technique called 'packet
sniffing’.
Because FTP does not provide encryption, an attacker can
steal FTP commands or file data through a man-in-the-
middle attack
Network
4

## Page 5

Infringement Continuation
Law01
53 Port
• Port 53 is associated with the Domain Name System (DNS) service, which is responsible for translating a website's domain name into the IP
address of that site, which is important for internet communication
• Abuse of this feature has the potential to cause a variety of security issues
• DNS spoofing is an attack in which an attacker
manipulates the responses of a DNS server, causing users
to be directed to a different IP address instead of the
desired website
• This allows the attacker to direct you to a dangerous site
or potentially intercept sensitive information
DNS spoofing
• How DNS requests and responses can be used to send data
covertly
• This allows attackers to bypass firewalls, exfiltrate data, or
send commands to control systems remotely
• DNS services must be set up correctly and checked periodically
for security
DNS tunneling
Network
5

## Page 6

Infringement Continuation
Law01
443
It uses port 443 and uses encrypted communication,
which provides protection against most of the
attacks mentioned for HTTP
Possibility for attackers to create fake HTTPS sites to
trick users
Attacks using vulnerabilities in TLS/SSL protocols
If authentication is weak, attacks can enter through
this port
80
HTTP uses port 80 and exchanges information
between the browser and web server
Because HTTP uses unencrypted communication, it is
vulnerable to "packet sniffing" attacks that intercept
data in the middle
Vulnerable to man-in-the-middle attacks
Network
6

## Page 7

Infringement Continuation
Law01
$ports = @(20,21,22,53,80,443,3389)
foreach ($port in $ports) {
    $portStatus = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
    if ($portStatus) { Write-Output "Port $port is open." }
    else { Write-Output "Port $port is closed." }
}
Description
•$port: This part defines an array of port numbers you want to check, in this case we set to check ports 20, 21, 23, 53, 80, 4 43, 3389
•Iterator : Iterator to process the port numbers defined above in order
•$portStatus: Use the Get-NetTCPConnection cmdlet to determine the status of each port and store it in the $portStatus variable
•The -ErrorAction SilentlyContinue option allows the script to continue running even if an error occurs while getting information about the
port
•Conditional statement: check if the $portStatus variable exists, i.e. if the port is open, and if $portStatus is True, print Port is open, and if
it is False, print Port is closed
Network
7

## Page 8

Infringement continuation
techniques01
3389 Port
•Port 3389 is used for Remote Desktop Protocol (RDP)
•RDP is a protocol for remotely controlling a computer's desktop, primarily used on Windows operating systems
• When you access a system remotely through RDP, you
can use the computer as if you were physically in front of
it
• Useful for system administrators to manage systems
remotely, or for users to use their computers remotely
DNS spoofing
• If this port is open, an attacker can gain access to the system
through a vulnerability in RDP or by obtaining a weak
password via brute force
Caveats
Network
8

## Page 9

Infringement Continuation
Law01
Port 20 is closed.
Port 21 is closed.
Port 23 is closed.
Port 53 is closed.
Port 80 is closed.
Port 443 is closed.
Port 3389 is open.
Run Result
Network
9

## Page 10

Infringement Continuation
Law01
$port = 3389
$processID = (Get-NetTCPConnection -LocalPort $port).OwningProcess
$process = Get-Process -Id $processID -ErrorAction SilentlyContinue
if ($process) {
    Write-Output "Port $port is used by the following service:"
    Write-Output ("Process Name: " + $process.Name)
    Write-Output ("Process ID: " + $process.Id)
} else { Write-Output "No service is using port $port." }
Description.
• $processID: Uses the Get-NetTCPConnection cmdlet to find the TCP connection that is using the specified local port (in this case, 3389) and stores
the ID of the process that owns the connection in the $processID variable
• Get-NetTCPConnection: This command shows the status of the TCP connections that are currently active on the system. This cmdlet is useful for
network diagnostics and monitoring. It is also often used to find the process that is using a particular port. OwningProcess displays the ID of the
process that owns the TCP connection
• The $process: variable uses the Get-Process cmdlet to find the process with the process ID stored in $processID; if it does not find a process with that
ID, it proceeds without printing an error
• Conditional statement: If $process is non-null, that is, if a process with that ID is found, the name and ID of the process are displayed; if $process is
null, that is, if a process with that ID is not found, "No service is using port $port." is displayed
Network
10

## Page 11

Infringement Continuation
Law01
Port 3389 is used by the following service:
Process Name: svchost
Process ID: 47656
Run Result
Network
11

## Page 12

Infringement Continuation
Law01
$port = 3389
$processID = (Get-NetTCPConnection -LocalPort $port).OwningProcess
if ($processID) {
    Stop-Process -Id $processID -Force
    Write-Output "Process $processID has been stopped."
} else { Write-Output "No process is using port $port." }
Description.
• Conditional statement: If $processID is not null, use the Stop-Process cmdlet to force the process to stop, displaying "Process $processID has been
stopped." If $processID is null, display "No process is using port $port."
Network
12

## Page 13

Infringement Continuation
Law01
Process 3389 has been stopped
Result
Network
13

## Page 14

Firewall02
• Windows Firewall is an important tool for protecting your computer
• It controls communication between your computer and the internet to prevent
malicious software from entering and sensitive information from being leaked
What is Firewall
Inbound
• Inbound traffic is communication coming into a computer from an
external network (such as the Internet)
• You can control inbound traffic to prevent malicious software from
entering your computer
• For example, you can block traffic from known malicious IP addresses,
traffic through specific ports, etc.
Outbound
• Outbound traffic is communication that leaves your computer to an
external network
• Windows Firewall can control this outbound traffic to prevent the leakage
of sensitive information
• For example, it can block malicious programs when they try to send data
outward
Features
14

## Page 15

Programmatic traffic control
• Windows Firewall can allow or block certain programs from accessing the Internet
• This can prevent certain programs from accessing the internet unnecessarily
• The program-specific traffic control feature in Windows Firewall is used to allow or block certain programs from accessing the network
• This feature is effective in preventing malicious software from leaking information over the network or downloading additional malicious
code
If a known malicious programme is installed on your computer
and tries to access your network, you can block it to prevent
further damage
Conversely, if a particular programme requires network access to
function properly, you can whitelist it to allow it to access the
network
Exam
Firewall02
15

## Page 16

Infringement Continuation
Law01
• Windows Firewall allows you to set security levels to tighten or loosen security for network traffic
• This is used to determine the policy by which the firewall automatically allows or blocks traffic
• Increasing the security level can provide more security because more traffic is blocked, but the
trade-off is that some legitimate traffic may be blocked
• Conversely, lowering the security level allows more traffic to be allowed, which can provide more
connectivity, but has the disadvantage of increasing the likelihood of malicious traffic gaining access
to the system
Setting security levels
• Windows Firewall can allow or block traffic through specific ports
• This allows you to control access to specific services
• For example, if you run a web server, you need to open port 80 to receive HTTP traffic
• Conversely, if you don't want to allow access through a specific port, you can block that port by
using the
Controlling traffic by port
Firewall02
16

## Page 17

Infringement continuation
techniques01
New-NetFirewallRule -DisplayName "My Inbound Rule" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow
command
Create a new inbound firewall rule named My Inbound Rule
New-NetFirewallRule is one of the cmdlets in PowerShell,
used to add new rules to the Windows Firewall
• DisplayName "My Inbound Rule" means that you want to name the
firewall rule "My Inbound Rule"
• Direction Inbound means to set the direction of traffic to which the
rule applies to inbound
• LocalPort -LocalPort means to set the local port number to which
this rule applies to 80
• Protocol -TCP sets the protocol to which this rule applies to
TCPAction allow means allow inbound traffic according to this rule
Description.
Firewall02
17

## Page 18

Infringement Continuation
Law01
• Remoteport refers to the port number of the remote
system
• Create a firewall rule to allow outbound traffic to TCP
port 80
• Rules are used to allow traffic needed to provide
services, such as web servers, to the outside world
Description.
New-NetFirewallRule -DisplayName "My Outbound Rule" -Direction Outbound -RemotePort 80 -Protocol TCP -Action Allow
command
Firewall02
18

## Page 19

Infringement Continuation
Law01
A firewall rule is created that blocks incoming TCP traffic
through port 80
This allows you to block unnecessary access to services that
use port 80, such as web servers
Description.
New-NetFirewallRule -DisplayName "Block Inbound Port 80" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Block
command
Firewall02
19

## Page 20

Infringement Continuation
Law01
See the firewall rules you've set up
Description.
• Used to get all rules in Windows Firewall
• Useful for managing network security settings and finding or
analysing specific firewall rules
• Returns an object that provides a variety of information about the
firewall rule
• Includes the rule's name, description, active status, action, direction
protocol, etc.
Get-NetFirewallRule
Get-NetFirewallRule | Format-Table -Property DisplayName, Direction, Action
command
Firewall02
20

## Page 21

Infringement Continuance
Act01
Remove-NetFirewallRule -DisplayName "My Inbound Rule"
Remove-NetFirewallRule -DisplayName "My Outbound Rule"
Remove-NetFirewallRule -DisplayName "Block Inbound Port 80"
command
Remove a firewall rule you set up
Description.
•Used to remove Windows Firewall rules
•Helpful for managing network security settings
•If malware has added a specific firewall rule, you can
delete it with this command
Remove-NetFirewallRule
Firewall02
21

## Page 22

Infringement Continuance
Act01
Get-NetFirewallRule | Where-Object {$_.Action -eq 'Allow'} | Get-NetFirewallPortFilter |
Where-Object { $_.LocalPort -ge 100 -and $_.LocalPort -le 8000 } | Format-Table
Abbreviations for Get-NetFirewallRule
Gets all network firewall rules currently set on the system
Get-NetFirewallRule
Gets port filtering information for selected rules
This information includes the port range that each
rule applies to, etc.
Get-NetFirewallPortFilter
Output the final selected rules in a table format
Format-Table
Command
Query for firewall rules that allow traffic with local port numbers between 100 and 8000, and output the results in a table format
Easily identify firewall rules that meet specific conditions
Firewall02
22

## Page 23

Infringement continuation
techniques01
Results screen
The table on the left outputs information about the firewall's port filter settings
Protocol indicates the protocol used, Local Port indicates the port number used on the local system, and Remote Port indicates the port number used on the
remote system
ICMP Type indicates the message type of the Internet Control Message Protocol, and Dynamic Target is used to specify the target to which the firewall rule is
dynamically updated
Looking at the first line, we can see that local port 445, which uses the TCP protocol, is set to allow traffic from all remote ports
Firewall02
23
