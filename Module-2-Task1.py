# Task 1 - Takes two numbers as input from the user and performs basic mathematical operations on these two numbers i.e. Addition, Subtraction, Multiplication and Division and displays the results of each operation on the screen at the end.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
dvd = num1 / num2

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", dvd)