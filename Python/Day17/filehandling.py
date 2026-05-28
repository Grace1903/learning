# Day 17 - File Handling

# Open and read file
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

# Read line by line
file = open("sample.txt", "r")

for line in file:
    print(line)

file.close()

# Write to file
file = open("write.txt", "w")

file.write("Hello World\n")
file.write("Python File Handling")

file.close()

# Append to file
file = open("write.txt", "a")

file.write("\nNew line added")

file.close()

# Using with (BEST METHOD)
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Read only first characters
with open("sample.txt", "r") as file:
    print(file.read(5))

# readline()
with open("sample.txt", "r") as file:
    print(file.readline())

# readlines()
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Check file exists
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File does not exist")

# Remove file
# os.remove("write.txt")
"""
"r"	read
"w"	write
"a"	append
"x"	create
"w"	replace content
"a"	add content at end
"""