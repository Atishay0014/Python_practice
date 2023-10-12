import math
# Solution 1 by using exponential operator 

num  = int(input("Enter a number to find a square root : - "))
num = num**0.5
print("Solution 1", num)

# Solution 2 by using square root function in math module in python
num = int(input("Enter a number to find a square root: - "))

num = math.sqrt(num)
print("Solution 2", num)
