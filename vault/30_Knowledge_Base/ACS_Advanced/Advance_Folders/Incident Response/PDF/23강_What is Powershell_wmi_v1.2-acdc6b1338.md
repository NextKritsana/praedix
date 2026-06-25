---
title: "23강_What is Powershell_wmi_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\23강_What is Powershell_wmi_v1.2.pdf"
source_size_bytes: 868519
source_modified: 2025-11-12T12:46:28
imported_at: 2026-06-14T14:26:39
tags:
  - acs
  - acs-advanced
  - imported
---

# 23강_What is Powershell_wmi_v1.2

- Source: [23강_What is Powershell_wmi_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/23%EA%B0%95_What%20is%20Powershell_wmi_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Powershell WMI
• Introduction to WMI
• What are WMI Events?
23
1

## Page 2

WMI01
Windows Management Instrumentation
WMI
C++, VBS, WMIC
Before Powershell...
A standard set of interfaces and tools for system
and network management on Microsoft Windows
operating systems
WMI?
Used to query and control information about many
aspects of the operating system and control aspects
of the operating system
Roles
2

## Page 3

WMI01
Components
In WMI
Provider
• Provides access to specific data or functionality to help external applications,
scripts, or tools access and control that information
• Components include classes, instances, methods, namespaces, WQL, event
providers, security, and permissions
• WQL allows you to query instances of specific classes, monitor events, and
utilize various WMI functions
Exam
• The class "Win32_Process" has an instance for each running process, and you
define methods for the class to implement actions on objects of that class
Consumer
• Components that get and utilize information from WMI
• Receive and process specific events in WMI when they happen
• Can perform queries on data provided through WMI to get the
information you want
• Execute various actions and take control of the system
• Perform custom actions on events or data, allowing system administrators
or developers to collect and control a variety of operating system and
hardware information
Implement data and behaviors
provided through WMI services
Provider
An application or service that
consumes and utilizes events or
data from WMI
Consumer
3

## Page 4

WMI01
WinRM
An acronym for Windows Remote Management,
a protocol and service for remote management
and automation in the Windows operating system
DCOM
Short for Distributed Component Object Model, a
technology based on COM, an object-oriented
programming model developed by Microsoft
WMI
Objects
Distributed object
orientation
Manage remote
systems
4

## Page 5

WMI01
DCOM
• Extends COM to support object-to-object communication in a distributed environment and allows
remote, non-local systems to call COM objects via remote procedure calls (RPC)
• Plays a key role in enabling distributed environments to communicate effectively with objects
located on other computers
Providing Object Activation
DCOM can create and invoke objects when needed, and automatically terminate
them when they are finished using them, enabling efficient management of
resources
This effectively enables DCOM to support object-oriented programming in a
distributed environment and facilitates communication between local and remote
systems
Communication
DCOM uses Remote Procedure Calls (RPCs) to communicate between objects, and RPCs communicate over TCP/IP
Use 2 ports by default
• 135 Port: First ask RPC Endpoint Mapper for RPC endpoint information of the remote server
• Random Port: Once the client receives the server's endpoint information from RPC Endpoint Mapper, the rest of the communication takes place in the
dynamic port range
• Dynamic ports use dynamically assigned ports from 1024 to 65535
Features
Features Commonly used by Microsoft Windows operating systems
and integrated with technologies such as COM+ to develop
business applications and services
Complex depending on security settings and environment
configuration, and more recently, simpler, standardized
technologies such as web services have replaced the use of DCOM
5

## Page 6

WMI01
WinRM
• Short for Windows Remote Management, a protocol and service for remote management and automation
in Windows
• Primarily used to support PowerShell Remoting, which enables secure communication with remote systems
• WinRM is enabled by default in Windows Server 2008 and later versions
How to use
WinRM must be enabled on the remote system when using WinRM
Easily enabled using the Enable-PSRemoting command
You can use Enter-PSSession to open a PowerShell session on the remote
and Invoke-Command to run PowerShell commands on the remote
system
Communication
• It uses the HTTPS protocol to encrypt data and provides secure communication over port 5986 by default
• PowerShell Remoting lets you run PowerShell commands on remote systems, manage remote sessions, and perform
a variety of remote management tasks, including file transfers, events, and more
Features
Features Powerful tools for remote management
One of the key technologies for effectively managing and automating
remote systems, especially in large environments

Used to retrieve data, change settings, and perform administrative
tasks on remote systems
HTTPS
6

## Page 7

WMI01
How to use
Get-WmiObject
• By default, using wmi starts with getting wmiobjects
with Get rather than creating them with New
• You can retrieve wmiobjects via Get-wmiobject –list
• There are two ways to use it: using a class or using a
query
How to use
7

## Page 8

WMI01
Specific process output
01
02
Query
$wqlQuery = "SELECT * FROM Win32_Process WHERE Name='explorer.exe'"
Get-WmiObject -Query $wqlQuery | Select-Object Name, ProcessId,
CommandLine | Format-Table
Class
• $Filter = "Name='explorer.exe'"
• Get-WmiObject Win32_Process -Filter $Filter | Select-Object Name,
ProcessId, CommandLine | Format-Table
• Create a $Filter variable and use Name='explorer.exe' to
filter instances of the Win32_Process class
• Using the Get-WmiObject Cmdlet to Get Instances of the
Win32_Process Class
• Use the $Filter variable to apply filtering to get information
only for the explorer.exe process
• Pass that information into the pipeline and use Select-
Object to select only the properties that you need from the
instances that you get
• Finally, use the pipeline to output in a table format
Using Classes
• Create the $wqlQuery variable
• The WQL query used here selects instances of the
Win32_Process class named "explorer.exe“
• Using the Get-WmiObject Cmdlet to Get an Instance of
the Win32_Process Class through WMI
• Use the $wqlQuery variable to apply a WMI query to get
information specific to the explorer.exe process
• After this, the same as Class
Using Query
1,2 Output value
8

## Page 9

WMI01
Querying WMI Events
WMI event queries are queries that are used to detect and respond to specific events as they occur using WMI, and can provide real-time monitoring of information about
system and application events
Event queries are used to define scripts or actions that run when specific events occur, and to apply filters to detect only the desired events
When the specified event occurs, the registered script or action is executed, allowing the user to perform the desired action
Some malware uses this WMI event query to gain persistence, which allows the malware to run itself on a system over and over again
Examples include malware that uses WMI to download a malware called Mainbot and malware from the SEADADDY family
Caveats
Classes that are the target of WMI event queries are primarily defined in the root\cimv2
namespace
Typical WMI event query targets are within the root\cimv2 namespace
Exam
To detect events about the creation or modification of the Win32_Process class, set the
target to root\cimv2, the namespace in which the class is defined
Definition root
cimv2
9

## Page 10

WMI01
1 . T e m p o r a r y  E v e n t
C o n s u m e r
• Transient consumers that receive and process
events
• A script or application is registered to process
a specific event
• Used primarily to perform one-time actions
that are required only at the time the event is
triggered
• Disappears when the computer reboots
2 . P e r s i s t e n t  E v e n t
C o n s u m e r s
• Consumers that continuously receive and process
events
• Used when continuous monitoring is required, such as
a system service or monitoring tool
• It is registered with the system and continuously
operates, and when it receives events, it can
continuously process them
• Mainly used to implement functions such as
continuous monitoring of system status, logging, and
alert generation
Temporary Permanent
10

## Page 11

WMI01
Windows Management Instrumentation Tester
How to run
In the Run window, type wbemtest and when it runs, the Windows Management Instrumentation Tester GUI displays
On that screen, click the connect button on the top right and connect to root\cimv2 to see various objects
• A tool provided with the Windows operating
system that is used to test and debug WMI
• WBEMTest allows you to run WMI queries, view
information about the WMI namespace, and more
• With it, you can check the Object in WMI
Windows Management
Instrumentation Tester
11

## Page 12

WMI01
Progress flow
When Cimv2 is connected, click open Class and a window appears to enter a class name
Enter Win32_LogicalDisk in the window and click OK to see Win32_LogicalDisk's information, properties, and methods
Click "Instances" button to see a list of instances of Win32_LogicalDisk class
12

## Page 13

WMI01
WMI Explorer.exe
• A graphical user interface tool used to explore and manage WMI namespaces and classes
• Provides a visual and easy way to find information about WMI and allows users to explore the classes, properties, methods, instances, and
more that they are looking for
• Represents the various namespaces and classes in a hierarchical structure for easy navigation and to drill down into the properties, methods,
and instances of selected classes
Download PATH
https://www.majorgeeks.com/mg/getmirror/wmi_explorer,1.html
• View instance data for specific classes and
review property values, and explore system-wide
WMI information with support for all system
and custom WMI namespaces
• Useful tool for IT professionals, system
administrators, developers, and others to use
and debug WMI
• Visually explore a wide range of system and
network information without the need for a
command line interface
Utilization
13

## Page 14

What are WMI events02
~When ~Do itevent Action
Register-WmiEvent -Query $Query -SourceIdentifier 'Name' -Action $Action
Ephemeral Event Consumers
Used to register PowerShell events for WMI events
If the given WMI query is satisfied, the specified action will run
Register-WmiEvent
Specifying specific conditions to raise an event
You can register a WQL query statement in the $Query variable by
using the -query option
Query
Identifier of the registered event
Used to represent an event, and when an event occurs,
PowerShell uses this identifier to identify it
-SourceIdentifier
Actions to take when a WMI event occurs
Action
14

## Page 15

What are WMI events02
HANDS-ON
 PRINT A MESSAGE BOX IF USB IS RECOGNIZED + SHUT DOWN PC
AFTER 9999 SECONDS
01
STEP
03
STEP
05
STEP02
STEP
04
STEP
Create a Batch Script to run Run Delete the event
Unshut down your
computer
Create a temporary event
consumer
15

## Page 16

What are WMI events02
Batch Script
Output a message window that says TEST!!!
msg * TEST!!
Shut down the PC after 9999 seconds
shutdown -s -t 9999
Action
When we create an event, we'll include the path to this batch script in the Action so that it can be executed
Save that batch file to your desktop
16

## Page 17

$MyAction = {Invoke-WmiMethod Win32_process -name Create -Argumentlist 'C:\Users\kusti\Desktop\test.bat'}
$Detect_USB = "SELECT * from Win32_VolumeChangeEvent WITHIN 3"
Register-WmiEvent -Query $Detect_USB -SourceIdentifier 'USB_DOWN' -Action $MyAction
What are WMI events02
Create a temporary event consumer
Variables that define what to do when a USB event occurs
Contains a command that uses Invoke-WmiMethod to invoke the Create method of the Win32_Process class
This method runs a batch file in the specified path.
$MyAction
Variable defining the WMI query to detect USB events, WITHIN checking for events for 3 seconds
Win32_VolumeChangeEvent is a WMI class used to detect volume change events that occur in a Windows environment.
• Detect changes such as new volumes added to the system or existing volumes removed
$Detect_USB
Use $Detect_USB query for USB event detection using Register-WmiEvent, with USB_DOWN as the identifier
The action to run for the event that occurred is the action defined in the $MyAction variable
Register_WmiEvent
17

## Page 18

What are WMI events02
Run
kusti
Unshut down your PC
shutdown -a
• cmd
• powershell
Status window output for USB_DOWN
if the command runs successfully
Run
Plug in the USB and see a pop-up
message saying TEST and warning
that the computer will turn off in
9999 seconds
What if I plug in a USB?
18

## Page 19

What are WMI events02
View, delete events
Verify operation after execution (Get-Job)
End the task
Verify that State has changed to Stopped (Get-Job)
19

## Page 20

Whenever there is a change in the service, save the event to C:\test.log.
"SELECT * from __instanceModificationEvent WITHIN 5 where targetInstance isa 'win32_service'"
What are WMI events02
Persistent Events
Generated when an instance changes in a namespace
__instanceModificationEvent
Instances where changes occurred in WMI events
targetInstance
Requests event notification to all layers of the class if the syntax is included in the Where clause
isa
Query
20

## Page 21

What are WMI events02
$Query = "SELECT * from __instanceModificationEvent WITHIN 5 where targetInstance isa 'win32_service'"
$Service_name_filter = "MyServiceFilter"
$Service_name_consumer = "MyServiceConsumer"
$WmiEvtFilter = Set-WmiInstance -Namespace 'root\subscription' -Class '__EventFilter' -Arguments @{
    Name = $Service_name_filter
    EventNamespace = 'root\cimv2'
    QueryLanguage = "WQL"
    Query = $Query
}
$WmiEvtConsumer = Set-WmiInstance -Namespace 'root\subscription' -Class 'LogFileEventConsumer' -Arguments @{
    Name = $Service_name_consumer
    Filename = "c:\test.log"
    Text = "A change has occurred on the service: %TargetInstance.DisplayName%"
}
Set-WmiInstance -Namespace 'root\subscription' -Class '__FilterToConsumerBinding' -Arguments @{
    Filter = $WmiEvtFilter
    Consumer = $WmiEvtConsumer
}
Exam2
Description
• Name the event filter 'MyServiceFilter' and the event consumer 'MyServiceConsumer'
• $WmiEvtFilter: sets an instance of the '__EventFilter' class in the 'root\subscription' namespace, which will filter events using the query defined above
• $WmiEvtConsumer: Set a 'LogFileEventConsumer' class instance in the 'root\subscription' namespace to write event information to a log file ("c:\test.log") whenever an
event occurs
• Set-WmiInstance: sets an instance of the '__FilterToConsumerBinding' class that binds the event filter to the event consumer, so that the events found are handled by the
event consumer
21

## Page 22

What are WMI events02
Deliverables
Why?
Logging changes in the state of a service can help you diagnose problems or monitor the health of your system
If a service goes down unexpectedly, event logs help you understand when and why it went down
It also helps detect security threats or illegal activity on your system
By monitoring changes in the health of a service, you can determine if it's been taken down due to illegal activity
22
