# Solution 1 By using 3rd variable to swap the values of variable 1 and variable 2

a = 5
b = 6

print("Before swapping: - ", a, b)

c = a
a = b
b = c

print("After Swapping: - ",a, b)

# Solution 2 by without using 3rd variable to swap the values of variable 1 and variable 2

a = 5
b = 6

a, b = b, a

print("the value of a ",a)
print("the value of b ",b)