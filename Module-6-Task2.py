
# Module 6: Data Structures and Strings in Python

# Task 2 - Demonstrate List Slicing - Creates a list of numbers from 1 to 10. Extracts the first five elements from the list and reverse it. Print both the extracted list and the reversed list.

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = num1[:5]

print(f"Original List: {num1}")

print(f"Extracted first five elements: {first_five}")

first_five.reverse()

print(f"Reversed first five elements: {first_five}")