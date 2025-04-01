# Task 1 - Check if a Number is Even or Odd - Takes an integer input from the user. Check whether the number is even or odd using an if-else statement and display the result.

num = int(input("Enter a number: "))
if (num%2) == 0:
	print(num, "is an even number.")
else:
	print(num, "is an odd number.")