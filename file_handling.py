# file=open("students.txt","r")
# content=file.read()
# print(content)
# file.close() 

#types of read():
#1. read() 
# file=open("students.txt","r")
# content=file.read()
# print(content)
# file.close() 

#2. readline() 
# file=open("students.txt","r")
# content=file.readline()
# content1=file.readline()
# content2=file.readline()
# print(content)
# print(content1)
# print(content2)
# file.close() 

#3. readlines()
# file=open("students.txt","r") 
# content=file.readlines()
# print(content)
# file.close()

file=open("student.txt","a")
#write,writelines
file.write("hello c++\n")
file.close()


File Handling in Python

Introduction to Files
 A file is a collection of data stored on a computer’s hard drive (permanent storage).
 When you run a program, data is stored in RAM (temporary memory) and lost when the
program ends.
 Files allow us to store data permanently for future use.
File Handling
File handling in Python means working with files (creating, opening, reading, writing, updating,
and closing) so that data is stored permanently instead of being lost when the program ends.
👉Example:
 Notes app saves your text in a file.
 A game saves your progress in a file.
 Banking software stores account records in files/databases.
Types of Files
In Python, there are two types of files:
1. Text Files (.txt, .csv, .log)
o Store data in human-readable format (characters).
o Each line ends with \n.
o Example:
o Nandan - 90
o Aarav - 85
o Priya - 92
2. Binary Files (.bin, .jpg, .exe, .mp3)
o Store data in 0s and 1s (machine-readable).
o Example: images, videos, executables.
o Not directly readable in Notepad.

Explain the Basics
File Operations in Python:
There are four main operations on files:
1. Open → Open the file for use
2. Read → Get data from the file
3. Write → Put data into the file
4. Close → Close the file after work
📌Python uses the open() function:
open("filename", "mode")
Access Modes in Python
When opening a file, we specify a mode (what we want to do with it).
📌Syntax:
file = open("filename", "mode")
Mode Meaning Example Use
"r" Read (default) Opens file for reading. Error if file doesn’t exist.
"w" Write Creates a new file OR overwrites existing content.
"a" Append Opens file for writing. Adds new data at the end.
"rb" Read Binary For binary files (images, videos).
"wb" Write Binary Write to binary file.
"r+" Read + Write Can read and write, file must exist.
"w+" Write + Read Creates new file, can read/write. Old content deleted.
1. Opening a File
Opening a file means using the open() function to access a file in a specific mode (read, write,
append, etc.) before working with it.

📌Syntax:
file = open("filename", "mode")
 "filename" → Name of the file (e.g., "data.txt")
 "mode" → What you want to do with the file
2. Closing a File
 Closing a file means using the close() function to end the connection with the file and
save changes safely.
 After working with a file, you must close it to save changes and free memory.
file.close()

3. Writing to a File
Writing to a file means storing new data into a file and removes the old data using write() or
writelines().
file = open("students.txt", "w") # open in write mode
file.write("Hello Students!\n")
file.write("Welcome to File Handling.\n")
file.close()
print("Data written successfully!")
3.1 Writing multiple lines with writelines()
# Writing multiple student names into a file
lines = ["Nandan\n", "Aarav\n", "Priya\n"]
file = open("students.txt", "w")
file.writelines(lines)
file.close()
print("Data written successfully!")
👉This creates a file students.txt with the given content.
⚠️If file already exists, old content will be erased.

4. Appending to a File
Appending to a file means adding new data at the end of the file without deleting the existing
content.
file = open("students.txt", "a") # open in append mode
file.write("This line is added later.\n")
file.close()
👉New content is added without removing old data.
5. Reading from a File
Reading from a file means getting data from a file into the program using read(), readline(), or
readlines().
file = open("students.txt", "r") # open in read mode
content = file.read() # read whole file
print("File Content:\n", content)
file.close()
5.1 Different Read Methods
Python provides multiple ways to read a file:
a. readline() → Reads one line at a time.
f = open("students.txt", "r")
print(f.readline()) # first line
print(f.readline()) # second line
f.close()
b. readlines() → Reads all lines and returns a list.
f = open("students.txt", "r")
lines = f.readlines()
print(lines)
f.close()

6. Reading Line by Line
Reading line by line means accessing the file content one line at a time, usually using a loop.
file = open("students.txt", "r")
for line in file:
print(line.strip()) # strip() removes extra spaces/newline
file.close()
👉Useful when reading large files.
7. Using with Statement
 Normally, we must call close() after file operations.
 But with with, the file closes automatically after use.
with open("students.txt", "r") as f:
data = f.read()
print(data)
8. Practical Example
Storing Student Marks
# Writing student data into a file
with open("marks.txt", "w") as f:
f.write("Nandan - 90\n")
f.write("Aarav - 85\n")
f.write("Anurag - 92\n")

# Reading back student data
with open("marks.txt", "r") as f:
print("Student Marks:")
for line in f:
print(line.strip())

📌Output:
Student Marks:
Nandan - 90
Aarav - 85
Anurag - 92
9. Why is File Handling Important?
 Data is stored permanently.
 Helps in creating real-world applications:
o Saving notes in an app
o Recording marks or employee details
o Logging activities (log files)
o Reading and analyzing large datasets

👉Without file handling, data is lost when the program ends.
10. File Handling Practice Problems
1. Write a program to create a new file called student.txt.
2. Write a program to write the text "Hello Students!" into a file.
3. Write a program to read and display the contents of a file named info.txt.
4. Write a program to append "Good Luck!" to the existing file student.txt.
5. Write a program to read a file line by line and print each line.
6. Write a program to write 5 lines (entered by the user) into a file called notes.txt.
7. Write a program to count the number of lines in a file called data.txt.
8. Write a program to copy the contents of one file (source.txt) to another file
(destination.txt).
9. Write a program to write a list of fruits ["Apple", "Banana", "Mango"] to a file using
writelines().
10. Write a program to read the first 20 characters of a file using the read() method.





