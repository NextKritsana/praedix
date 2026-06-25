---
title: "24강_Simple automation_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\24강_Simple automation_v1.2.pdf"
source_size_bytes: 561610
source_modified: 2025-11-12T12:48:22
imported_at: 2026-06-14T14:26:41
tags:
  - acs
  - acs-advanced
  - imported
---

# 24강_Simple automation_v1.2

- Source: [24강_Simple automation_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/24%EA%B0%95_Simple%20automation_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Simple automation
• WHY?
• Output service status
• Output drive status
• USB Connect, Disconnect
• Make it a module and run it
24
1

## Page 2

WHY?01
Benefits of Powershell automation
System management and automation
• Automate admini tasks like managing user accounts,
configuring services, monitoring event logs, and more
with PowerShell scripts
Simplification of repetitive tasks
• Scripting and automating repetitive tasks can save you
time
• Use PowerShell to automate tasks such as moving files or
periodically cleaning up files in a specific folder
Provide a scriptable interface
• PowerShell is integrated with the .NET framework,
providing powerful scripting capabilities to handle
complex tasks and interact with a variety of systems
Caveats
Security issue
• Powershell scripts have a powerful impact on your
system
• There is a possibility that a malicious user could use a
PowerShell script to attack you, so you need to be careful
from a security perspective
Resource consumption
• PowerShell scripts can consume system resources while
running
• Especially when performing large automated or
repetitive tasks, put a strain on the system.
Dependency management
• PowerShell script depends on external resources, libraries,
or a specific version of PowerShell
• Need to manage dependencies on an ongoing basis
2

## Page 3

Output service status02
What is a service?
• A process is a running instance of a program
• A process runs with the permission of the user
running it
• Services are a special type of application that
primarily runs in the background on Windows
systems.
Difference from processes
Automation tool that takes a service name as
an argument and prints out information about
that service
Error codes for user-intended errors are printed
in the output X
What to make
Each service runs as an independent process
Manage the resources they need to perform
specific functions
Features
A background process that runs on Window
operating systems that starts automatically
when the system boots and runs even when
the user is not logged in
Service role
3

## Page 4

Output service status02
Service Name is used to identify the service
Service Status indicates whether the service is automatically
started, manually started, or not started automatically
Service Type helps you manage system resources
You can monitor the status of running services and optimize
resource usage by considering the type of services that are
automatically launched.
Define the name of the function as Get-ServiceStatus, add Mandatory as a Parameter property and enter the variable $ServiceName as
a String, with the target of output Service Name, Service Status, and Service Type
Output service status and information
function Get-ServiceStatus {
    param (
        [Parameter(Mandatory=$True)]
        [string]$serviceName
    )
}
Name Status Type
$serviceStatus = $serviceInfo | Select-Object DisplayName, Status, StartType
4

## Page 5

function Get-ServiceStatus {
    param (
        [Parameter(Mandatory=$True)]
        [string]$serviceName
    )
$serviceInfo = Get-Service -Name $serviceName
if ($serviceInfo) {
        $serviceStatus = $serviceInfo | Select-Object DisplayName, Status, StartType
        Write-Host "Service Name   : $($serviceStatus.DisplayName)"
        Write-Host "Status         : $($serviceStatus.Status)"
        Write-Host "Start Type     : $($serviceStatus.StartType)"
} else {
        Write-Host "Service '$serviceName' not found."
    }
}
Output
Output service status02
Description
Gets the DisplayNmae, Status, and StartType information in the variable $ServiceInfo, and then outputs the DisplayName, Status, and StatrtType of the ServiceStatus,
If the given service does not exist, output a message that the service does not exist
5

## Page 6

1. N o r m a l  O u t p u t
Normal result output
2. A b n o r m a l
o u t p u t
Output error messages
1 2
Error?
An error that occurs when you specify the name or alias of the service you want to find using the "Get-Service" command
and the service is not found
Normal output
The ServiceName, Status, and Start Type are output
Output service status02
6

## Page 7

function Get-ServiceStatus {
    param (
        [Parameter(Mandatory=$True)]
        [string]$serviceName
    )
$originalErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
$serviceInfo = Get-Service -Name $serviceName
$ErrorActionPreference = $originalErrorActionPreference
if ($serviceInfo) {
        $serviceStatus = $serviceInfo | Select-Object DisplayName, Status, StartType
        Write-Host "Service Name   : $($serviceStatus.DisplayName)"
        Write-Host "Status         : $($serviceStatus.Status)"
        Write-Host "Start Type     : $($serviceStatus.StartType)"
} else {
        Write-Host "Service '$serviceName' not found."
    }
}
Saving error messages
Turn off error messages
Get process name
Error message on
Output service status02
Variables that Control Error Handling Behavior in the PowerShell
Environment
SilentlyContinue: When an error occurs, proceed without displaying an error
message.
Stop: When an error occurs, the script or command stops immediately.
Continue: If an error occurs, display an error message and proceed (default)
Inquire: Prompt the user if an error occurs and ask if they want to continue
Ignore: ignore the error and proceed
$ErrorActionPreference
• Create an originalErrorActionPreference and store
$ErrorActionPreference in that variable
• Set the value of $originalErrorActionPreference to
SilentlyContinue
• Finally, change the Error Message back to its original value
to keep the default state
Output error message X
The result
7

## Page 8

Output drive status03
Total Drive Capacity
Capacity in use
Free space
Allocated characters
Output Drive Status
See which drives are running low
on storage and how much
capacity they have left
Purpose
The result
Output Drive Status
8

## Page 9

See which drives are on your computer
Check Drive
Calculated based on total and in-use capacity
Calculate remaining capacity
Save to the path C:\, the system drive
Space to store
function Get-DiskSpace {
    param (
    )
}
Output drive status03
9

## Page 10

function Get-DiskSpace {
    param (
)
  $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  $diskSpace = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 }
| Select-Object DeviceID, FreeSpace, Size
    foreach ($disk in $diskSpace) {
        $usedPercentage = ($disk.Size - $disk.FreeSpace) / $disk.Size * 100
       $message = "$timestamp - $($disk.DeviceID): $($usedPercentage)% used"
        Write-Host $message
    }
}
• WMI Declarations and Selecting and Storing Objects in
Variables
• Win32_LogicalDisk provides information about the logical
disks (drives) in the system in the Windows operating system
Red box description
• The DeviceID is a string Type and serves to identify the logical disk
• FreeSpace has a Type of uint64. Represents the free space on the disk in bytes
• Size is also of type uint64 and represents the total size of the disk in bytes
• The Type of Volume Name is a string and represents the name of the volume on the disk
• Type of FileSystem is a string and indicates the filesystem used on the disk in bytes
Output drive status03
10

## Page 11

function Get-DiskSpace {
    param (
)
  $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  $diskSpace = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 }
| Select-Object DeviceID, FreeSpace, Size
    foreach ($disk in $diskSpace) {
        $usedPercentage = ($disk.Size - $disk.FreeSpace) / $disk.Size * 100
       $message = "$timestamp - $($disk.DeviceID): $($usedPercentage)% used"
        Write-Host $message
    }
}
• Repeating the values stored in diskSpace and calculating and printing their
size
• $_.DriveType -eq 3 means the DriveType property of the current object is 3
• Use Select-object to select DeviceID, FreeSpace, and Size
• Calculate the percentage of utilization for each disk and store it in the
$usedPercentage variable
• Declare a variable called $message and output the Timestamp variable
followed by the Drive ID and the value of the $UsedPercentage variable
Green box description
The result
Output drive status03
11

## Page 12

• Add a script to save $message to $logFilePath by setting the PATH
to be saved in Parameter and using Write-Host with the Add-
Content and -value options
• Save the file DiskSpaceLog.txt in the path C:\.
Blue box description
function Get-DiskSpace {
    param (
        [string]$logFilePath = "C:\DiskSpaceLog.txt"
    )
 $diskSpace = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 }
| Select-Object DeviceID, FreeSpace, Size
    foreach ($disk in $diskSpace) {
        $usedPercentage = ($disk.Size - $disk.FreeSpace) / $disk.Size * 100
        $message = "$timestamp - $($disk.DeviceID): $($usedPercentage)% used"
        Add-Content -Path $logFilePath -Value $message
        Write-Host $message
    }
}
Output drive status03
12

## Page 13

Why?
• Monitor USB connect and disconnect events to detect security incidents
• Detect USB devices with sensitive data or to prevent illegal data movement, and it can be used for asset management in your
organization by logging USB connect and disconnect events
• Understand the health of your IT assets by tracking which devices were connected and when
• Useful when investigating security incidents or data breaches
Print simple information about a USB
Print the time the USB was connected
Check USB information
• Events should run when the USB is connected
• The USB is recognized as a drive and the drive is
added to the computer when it is recognized
Check the USB connection
Use event subscriptions to increase persistence
Event subscription features
USB Connect, Disconnect04
13

## Page 14

function Monitor-USBConnection {
    $Detect_USB = "SELECT * from Win32_VolumeChangeEvent WITHIN 3"
    Register-WmiEvent -Query $Detect_USB -SourceIdentifier 'USB_MONITOR' -Action {
        $usbDevice = $event.SourceEventArgs.NewEvent.TargetInstance
        $message = "USB device connect or disconnect"
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Write-Host $message at $timestamp
    }
    Write-Host "USB connection monitoring started..."
}
Monitor-USBConnection
• Enable detection of USB connect and disconnect events using the $Detect_USB
query
• Set the event identifier to USB_MONITOR
• Accessing the event's arguments via .SourceEventArgs
• The following .NewEvent property holds information about the new event
• The .TargetInstance property represents the data of the actual changed instance
among the information obtained
Subscribe to events
• Saving a WMI Query to Detect USB Connect and Disconnect Events in
the $Detect_USB Variable
• The Win32_VolumeChangeEvent class detects volume change events
• WITHIN 3 option to detect events that changed within 3 seconds
Query
USB Connect, Disconnect04
14

## Page 15

function Monitor-USBConnection {
    $usbConnectionQuery =
    Register-WmiEvent -Query $usbConnectionQuery -SourceIdentifier 'USB_NAME' -Action {

    }
    Write-Host "USB connection monitoring started..."
}
Monitor-USBConnection
Query
Action
Want
USB Connect, Disconnect04
15

## Page 16

$usbConnectionQuery = "SELECT * FROM __InstanceCreationEvent WITHIN 3 WHERE TargetInstance ISA
'Win32_PnPEntity' AND TargetInstance.DeviceID LIKE '%USB%'"
Query description
• The __InstanceCreationEvent class fires an event when a new instance (device) is created
• This class is a type of WMI event that occurs when an object is created
• When the WITHIN clause is used in an event query, only events that occurred during that time interval are detected
• ISA stands for "Is A", an operator that checks whether an object is an instance of a specified class
• TargetInstance ISA 'Win32_PnPEntity' is a syntax that checks whether the TargetInstance is an instance of the Win32_PnPEntityclass
• Win32_PnPEntity is a class used in WMI to represent Plug and Play (PnP) devices
• TargetInstance ISA 'Win32_PnPEntity' ensures that object returned from that event is an instance of the Win32_PnPEntity class
• TargetInstance.DeviceID LIKE '%USB%' specifies that only devices are selected if the device's identifier (DeviceID) contains 'USB'
Query
USB Connect, Disconnect04
16

## Page 17

Register-WmiEvent -Query $usbConnectionQuery -SourceIdentifier 'USB_NAME' -Action {
        $usbDevice = $event.SourceEventArgs.NewEvent.TargetInstance
        $message = "USB device connected: $($usbDevice.Description) (Device ID: $($usbDevice.DeviceID))"
        Write-Host $message
    }
Use a WMI query to detect USB connection events
and register an action to run when they occur
Use the -SourceIdentifier to use an identifier named
USB_NAME
Register-WmiEvent
Assign information about the USB device to the $usbDevice
variableCreate a message in $message indicating the
connection of the USB device
The USB device's Description and DeviceID properties to
configure the message
ADD TEXT
USB Connect, Disconnect04
17

## Page 18

function Monitor-USBConnection {
    $usbConnectionQuery = "SELECT * FROM __InstanceCreationEvent WITHIN 3 WHERE TargetInstance
ISA 'Win32_PnPEntity' AND TargetInstance.DeviceID LIKE '%USB%'"
 Register-WmiEvent -Query $usbConnectionQuery -SourceIdentifier 'USB_NAME' -Action {
        $usbDevice = $event.SourceEventArgs.NewEvent.TargetInstance
        $message = "USB device connected: $($usbDevice.Description) (Device ID: $($usbDevice.DeviceID))"
        Write-Host $message
    }
    Write-Host "USB connection monitoring started..."
}
Module05
18

## Page 19

Module05
Check subscriptions
Get-EventSubscriber
Delete subscriptions
Unregister-Event
Example : Unregister-Event -SourceIdentifier 'USB_NAME'
• Most events disappear when you turn your computer off and on, but sometimes you
don't turn your computer off and the event is hogging your computer's resources
• In this case, you can manually delete them
Why?
• You can also use a pipeline to delete all WMI events at once.
• Example: Get-EventSubscriber | Unregister-Event
Tip
19

## Page 20

모듈04
Make Module & SAVE
Get-ServiceStatus
Displays the name, type, and status of a service
Get-DiskSpace
Output the remaining space on the drive, filesystem
type, Type, Volume Name, etc.
Monitor-USBConnection
Use Timestamp to represent time values and
Win32_VolumeChangeEvent to detect USB
connections and disconnections
Module
Module05
20

## Page 21

모듈04
Import Module
Get-DiskSpace
Get-ServiceStatus
Monitor-USBConnection
Module05
21
