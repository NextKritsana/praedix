---
title: "20강_Powershell Conditions and Controls_v1.2"
type: "acs-advance-pdf"
course: "ACS Advanced"
course_folder: "Incident Response"
source_path: "E:\\ProJect\\ACS File\\advance\\Incident Response\\20강_Powershell Conditions and Controls_v1.2.pdf"
source_size_bytes: 773451
source_modified: 2025-11-12T12:44:50
imported_at: 2026-06-14T14:26:36
tags:
  - acs
  - acs-advanced
  - imported
---

# 20강_Powershell Conditions and Controls_v1.2

- Source: [20강_Powershell Conditions and Controls_v1.2.pdf](file:///E:/ProJect/ACS%20File/advance/Incident%20Response/20%EA%B0%95_Powershell%20Conditions%20and%20Controls_v1.2.pdf)

> Imported from PDF for Obsidian search. Verify formatting against the original file when exact layout matters.

## Page 1

Powershell Conditions
and Controls
• Conditions and controls
• Get more out of it
20
1

## Page 2

01 Conditions and controls
Operators
Arithmetic
+, -, /, *, =, %, ...
Compare
-eq, -match, -gt, -lt, -contain, ...
Logical, Other
-and, -or, -xor, !, -replace, -join, -split
Used to check a string for a match to a pattern
Returns True or False if the string matches the regular expression
pattern
-match
Determining whether a specific item exists in an array
match checks for a match in a string, and conatin indicates
presence in an array
-contain
Greater than and less than are short for check if the left value
is greater than the right value and check if the right value is
greater than the left value, respectively
-gt, -lt
2

## Page 3

01 Conditions and controls
-join
+Β
$str1 = "THIS"
$str2 = "is"
$str3 = "STR"
$plus = $str1 + $str2 + $str3
$words = "This", "is", "STR"
$plus = $words
$join = $words -join " "
THISisSTR
THIS is STR
Tips
When you combine strings with the + operator, the two strings are merged together to create a new string
You can see that THISisSTR is just concatenated with no spaces because it's just a concatenation
Tips
Used to concatenate items in an array to a specific string
This operator is primarily used to combine elements of an array of strings to create a new string
In the second box, you can see that items in the array called $words are concatenated with a space when concatenated
3

## Page 4

01 Conditions and controls
-split
-replace
$words = "This", "is", "STR"
$plus = $words
$join = $words -join " "
$replace = $join -replace "STR","ACS"
$words = "This", "is", "STR"
$plus = $words
$join = $words -join " "
$split = $join -split
THIS is ACS
THIS
is
STR
Tips
The -replace operator is used in PowerShell to replace a matching part of a string with another string
Perform replacement actions based on regular expressions or simple string matching
The result of join is THIS is STR, and $replace replaces STR with ACS
Tips
The -split operator is used to separate strings based on the specified delimiter and return them as an array
Useful when you want to split a string based on a specific pattern or string of characters
Notice that the join splits the string THIS is STR, which was joined by a space, back to a space-based split\
4

## Page 5

Conditional statements
If, else, switch
Looping statements
While, do while, do until, for, foreach (%)
• Structures that perform a specific behavior when a given
condition is true
• If the condition is true, the block is executed; if false, the
next condition is checked or the else block is executed
Conditional statements
• Repeatedly execute code within a block when a given condition is
true
• Many of you may have never seen foreach before, which will be
explained in a moment
Looping statements
01 Conditions and controls
5

## Page 6

One of the comparison operators used in PowerShell,
used to determine whether a string matches a regular
expression
match
Outputs Correct if $str1 contains the string ACS, and Not
Correct if it does not
if
Output results
Because the value of that conditional statement is True, Correct is the output
01 Conditions and controls
6

## Page 7

01 Conditions and controls
for ($i = 1; $i -le 5; $i++) {
  Write-Output "Number: $i"
}1
$counter = 1
do {
  Write-Output "Now value: $counter"
  $counter++
} while ($counter -le 5)
2
$counter = 1
while ($counter -le 5) {
  Write-Output "Now value: $counter"
  $counter++
}
3
$counter = 1
do {
  Write-Output "Now value: $counter"
  $counter++
} until ($counter -gt 5)
4
• Initial value is the starting value of the iteration variablei
• $i -lt 5 is the condition to keep the loop running, $i++ is to increment the
iteration variable
• Print the value of $i via Write-Output
1, for
• The $counter is a looping variable
• do { ... } while ($counter -le 5) executes the code first, then
checks the $counter -le 5 condition and executes the block of
code again if true
2, do while
• The while ($counter -le 5) syntax executes the following code block
repeatedly until $counter is equal to or less than 5
• Write-Output "Now value: $counter" outputs the current value of
$counter
3 times, while
• The do { ... } until ($counter -gt 5) syntax executes the code
block below once and then iterates over it until $counter is
greater than 5
• If $counter -gt 5 is true, the iteration ends
4, do until
7

## Page 8

01 Conditions and controls
foreach
A type of iteration statement that performs an operation on each element
of a collection by sequentially substituting for it
Can iterate over collections such as lists and arrays
$height = 5: Set the variable representing the height of the
triangle to 5
height
External for statements
Row representation for overall height ($height)
Internal for statements
Represent whitespace in each row
Outputs the height of the current row minus $i, plus as many
spaces as there are in it
for statement
Representation of stars in each row
Output ($i * 2 - 1) stars based on the height of the current row
($i)
foreach
$height = 5
for ($i = 1; $i -le $height; $i++) {
 for ($j = 1; $j -le ($height - $i); $j++) {
  Write-Host -NoNewline " "
 }
 foreach ($k in 1..($i * 2 - 1)) {
  Write-Host -NoNewline "*"
 }
 Write-Host ""
}
Output
8

## Page 9

01 Conditions and controls
Command
Command
$colors = "Red", "Green", "Blue", "Yellow"
foreach ($color in $colors) {
    Write-Output "Color: $color"
}
$files = Get-ChildItem
foreach ($file in $files) {
    Write-Output "File: $($file.Name)"
}
Exam 1
• $colors is an array with string elements
• foreach ($color in $colors) { ... } assigns each element of the
array to the $color variable, and outputs that element within
the code block
Exam 2
• foreach ($file in $files) { ... } for each file, assigning it to the
$file variable, and outputting the name of that file
• In the code above, $file is the variable used in each iteration,
where the items being processed in the current iteration are
assigned to it, and $files is the collection to iterate over
9

## Page 10

01 Conditions and controls
$people = @(
    @{
        "Name" = "Kusti"
        "Age" = 26
        "Occupation" = "Engineer"
    },
    @{
        "Name" = "Deb"
        "Age" = 25
        "Occupation" = "Designer"
    },
    @{
        "Name" = "Ug"
        "Age" = 35
        "Occupation" = "Manager"
    }
)
foreach ($person in $people) {
    Write-Output "Name: $($person.Name), Age: $($person.Age), Occupation:
$($person.Occupation)"
}
Exam 3
• Example of using a foreach loop to process a complex data structure, an
array of objects
• Let $people be an array of objects, each object an associative array
containing name, age, and occupation information
• Iterate over the array of objects using foreach ($person in $people) { ... },
assigning each object to the $person variable, and run the following block
of code
• Write-Output "Name: $($person.Name), Age: $($person.Age), Occupation:
$($person.Occupation)" to print the values of the current object's
properties
• When getting a property value, such as $($person.Name), use $() to
enclose a variable or property name
Output
10

## Page 11

c o m m a n d
Conditions and controls01
$commands = @(
 (get-command),
 (get-help about_comparison_operators),
 (get-help get-command)
)
foreach ($command in $commands) {
 $command.gettype()
}
Description
• Using foreach to determine the Type of each variable
• Define the $commands array
• This array holds information about three commands, and we use a
foreach loop to process each item in the $commands array
• Then, for each command, we call the gettype() method to print
out the type of the command
• The result is the Type value of the above commands.
11

## Page 12

M o r e
Get-help about_comparison_operators
Conditions and controls01
2 -eq 2 # Output: True
 2 -eq 3 # Output: False
 "abc" -eq "abc" # Output: True
 "abc" -eq "abc", "def" # Output: False
 "abc" -ne "def" # Output: True
 "abc" -ne "abc" # Output: False
 "abc" -ne "abc", "def" # Output: True
More Example
Description.
• Use the Get-Help command to get more information about the operator
• For help with comparison operators, use the Get-Help about_comparison_operators command
• This article provides a detailed description of the comparison operator in PowerShell, with examples, caveats, and more
12

## Page 13

Get more out of it02
Description
• Store the command get-help about_comparison_operators in the
variable $command2
• Verify that $command2 has a type of Stirng
• Check for the existence of the string compare with the -match
operator, returning True
• This means that the values stored in the variable $command2 all
represent strings
BASE TYPE : SYSTEM.OBJECT - STRING
13

## Page 14

02
BASE TYPE : CUSTOM OBJECT
Description
• Save the result of get-help get-command to $command3
• Verify that the result of Gettype() is PS Custom Object
• Using the -match operator, the string SYSNOPSIS is checked for
True
• Check for the string other sessions below and get False
• You can see that SYSNOPSIS is a string and the value under
DESCRIPTION is not a string
Get more out of it02
14

## Page 15

Get more out of it02
BASE TYPE : ARRAY
Keyword
When you substitute the value of get-command into $command1, you can see that it is an Object with a BaseType of System.Array when you check the type with
Gettype()
Check if $command1 contains the string Computer, and the result is not a Boolean, but an enumerated list
In this example, we can see that if the Type is an array, it outputs a list of matches instead of True and False values
15

## Page 16

Get more out of it02
Incident perspective
• Processes with high memory occupancy can indicate a number of suspicious situations
• If a process with a high memory occupancy is associated with the execution of
malware, it is likely that malware is active on the system
• Additionally, if a process with a high memory occupancy is accessing other system
resources or exhibiting suspicious behavior, this can be considered a sign of a cyber
security incident
High memory occupancy can cause the system to run out of physical random access memory (RAM), which can make it difficult to allocate memory for other processes or
applications to run, potentially reducing overall system performance
Identify the 10 processes with the highest memory
occupancy
Get-Process
Sort-Object -Property WorkingSet -Descending
Select-Object -First 10
Used to sort data by an object's properties
DescendingSelect a property
Select the top 10Commands to use
• Get-Process: Gets information about the processes that are currently running in PowerShell
• Sort-Object: Lets you sort objects in ascending or descending order based on their properties
• Select-Object: Lets you keep some of the properties of an object or add new properties to get the output in the
format you want
16

## Page 17

Get more out of it02
Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 10
Pipe Line
Used when passing the result of the preceding result to the following
Command
Deliverables
• A command to sort the values of the WorkingSet property in
descending order from the result of get-Process and print the top
10 values from the result
• Checking the WS(WorkingSet) property shows the 10 values
sorted in descending order
Description
17

## Page 18

Get more out of it02
Format-list
CMDlets that display the properties of an output object in a list format
Format-List is used primarily by developers and system administrators for debugging and for viewing the structure of objects
Because Format-List turns the output into text and does not preserve the format of the object, it is best to avoid formatting
data before passing it through a pipeline to other cmdlets whenever possible
Tips
Usage can be verified with the command get-command *format-list* | get-help
Type Format-list -property * to see all the information
Example
• Example : Get-Process | Format-List Name, WorkingSet
• Gets information about running processes, selecting the Name and
WorkingSet properties to output in list format

Command
18

## Page 19

Get more out of it02
$p_top3 = Get-Process | Sort-Object -Property WorkingSet -Descending | Select-Object -First 3
$p_top3 | format-list
Command
$p_top3 | format-list $p_top3
Output WS only
• $p_top3 | format-list -property ws
Command
19

## Page 20

Get more out of it02
Format table
• The Format-Table Cmdlet is used to format and print the properties of an object in PowerShell in a table format
• Displays the properties of selected objects in a horizontal, tabular format for better readability
• It is useful when you want to visually compare the properties of multiple objects, or when you want to highlight certain properties
• When used like Format-list, the output turns to text and does not preserve the formatting of the objects, so it is best to avoid formatting data
before passing it through a pipeline to other cmdlets
example
• Get-process | format-table name, ws, si
• Output only Name, WS, and SI values in a tabular format
Command
20

## Page 21

Get more out of it02
• Output ID, Name, WS, and Company information in table format
• WS is output in MB
About us
Use $p_top3 | table-list -property * to see the value of the property named
company
Why?
When the malware is running as a process, there is a possibility that the
company value has a space in it or contains a strange string

21

## Page 22

Get more out of it02
Create a column
Represents the WS value as an
integer MB
Label Name:
WS(M)
Left Align
$p_top3 | format-table "id", "name", @{Label="WS(M)"; Expression={[math]::Round(($_.WS/1MB), 0)}; align="left"}, "company"
WS to MB
Create as variable and add
$col1 = "id", "name", @{Label="WS(M)"; Expression={[math]::Round(($_.WS/1MB), 0)}; align="left"}, "company"
$p_top3 | format-table $col1
• Checking values through $p_top3 | format-table $col1
shows values of ID, Name, WS(M), Company
• Memory Compression is used to compress the original
Company value X
Check the result with Format list
22
