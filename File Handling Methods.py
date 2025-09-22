# File Handling Methods

# readline()
f = open("demo.txt", "r")
print(f.readline())   # Reads first line
print(f.readline())   # Reads second line
f.close()


# readlines()
f = open("demo.txt", "r")
lines = f.readlines()
print(lines)   # ['Hello Python World!\n', 'This is new line.\n']
f.close()


# Using with open() (Context Manager)
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)


# Checking if File Exists (os module)
import os
if os.path.exists("demo.txt"):
    print("File exists")
else:
    print("File not found")

"""Practice Programs
Q1: Write a program to read a file line by line and print each line with line number.

Expected Output:
Line 1: Hello World
Line 2: This is Python
Line 3: File Handling Example

 Q2: Write a program to ask user for input and save it permanently in a file called notes.txt.

Example Run:
Enter your note: Python is amazing!


File notes.txt will contain:
Python is amazing!"""