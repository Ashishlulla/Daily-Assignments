# 1. Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:
# Input lengths of the triangle sides:
# x: 6
# y: 8
# z: 12
# Scalene triangle

x, y, z = map(int, input("Enter the values separated by comma: ").split(","))
if x == y and y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# 2. Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:
# Input a number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60

number = int(input("Enter the Number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 3. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three
# times of their sum.

a, b, c = map(int, input("Enter the three number separated by comma: ").split(","))
sum = a + b + c
if a == b == c:
    print(sum*3)
else:
    print(sum)


