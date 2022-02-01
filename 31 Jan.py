

# 1. Write a Python program to check if two given sets have no elements in common.
# Sample Output:
# Original set elements:
# {1, 2, 3, 4}
# {4, 5, 6, 7}
# {8}
# Confirm two given sets have no element(s) in common:
# Compare x and y : False
# Compare x and z : True
# Compare y and z : True

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

print(f"Compare x and y : {x.isdisjoint(y)}")
print(f"Compare x and z : {x.isdisjoint(z)}")
print(f"Compare y and z : {y.isdisjoint(z)}")

# 2. Write a Python program to swap two variables.

a = 10
b = 20
print(f"before Swapping A = {a} and B = {b}")
a, b = b, a
print(f"After Swapping A = {a} and B = {b}")

# 3. Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

num = int(input("Enter the Number : "))
if num <= 17:
    print(17-num)
else:
    print(abs((17-num)*2))
