
# Module 5: Files, Exceptions, and Errors in Python

# Task 2 - Write and Append Data to a File - Write a Python program that takes user input and writes it to a file named output.txt. Also appends additional data to the same file and reads and displays the final content of the file.

input1 = input("Enter text to write to the file: ")

with open('output.txt', 'w') as file1:
    file1.write(input1+"\n")
    print("Data successfully written to 'output.txt'")

input2 = input("Enter additional text to append: ")

with open('output.txt', 'a') as file1:
    file1.write(input2+"\n")
    print("Data successfully appended.")

with open('output.txt', 'r') as file1:
    lines = file1.readlines()
    print("Final content of 'output.txt':")
    for line in lines:
        print(line.strip())