
# Module 6: Data Structures and Strings in Python

# Task 1 - Create a Dictionary of Student Marks - Creates a dictionary where student names are keys and their marks are values. Asks the user to input a student's name and display their corresponding marks. If the student's name is not found, display an appropriate message.

student_marks = {"alice" : 85, "steve" : 75, "bob" : 70, "rohan" : 85, "smith" : 65}

name = input("Enter the student's name: ").strip().lower()

marks = student_marks.get(name)

if marks is not None:
	print(f"{name.capitalize()}'s marks: {marks}")
else:
	print("Student not found.")