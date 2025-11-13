# Task 1: Calculate Factorial Using a Function
#
# Problem Statement: Write a Python program that:
#
# 1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2. Returns the calculated factorial.
# 3. Calls the function with a sample number and prints the output.

def fectorial_fun(n):
    if n == 0:
        return 1
    else:
        return n * fectorial_fun(n - 1)

num = int(input("Enter a number: "))
result = fectorial_fun(num)

print(f"Factorial of {num} is {result}")



