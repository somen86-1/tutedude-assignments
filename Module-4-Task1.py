# Task 1 - Calculate Factorial Using a Function - Write a Python program that takes a number as an argument and calculates its factorial using a loop or recursion and returns the calculated factorial.

#Using Recursion
def factorial_1(num):
	if num < 2:
		return 1
	else:
		return num * factorial_1(num-1)
num = 5
print(f"Factorial of {num} is: ", factorial_1(num))


#Using Loop/Iteration
def factorial_2(num):
	fact = 1
	for n in range(num, 0, -1):
		fact*=n
	return fact

num = 5
print(f"Factorial of {num} is: ", factorial_2(num))