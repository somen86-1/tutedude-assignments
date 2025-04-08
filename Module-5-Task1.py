
# Module 5: Files, Exceptions, and Errors in Python

# Task 1 - Read a File and Handle Errors - Write a Python program that opens and reads a text file named sample.txt, prints its content line by line and handles errors gracefully if the file does not exist.

try:
    with open('sample.txt','r') as file1:
        lines = file1.readlines()
		print("Reading file content:")
        for i, (line) in enumerate(lines):
            print(f"Line {(i+1)}: {line}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")