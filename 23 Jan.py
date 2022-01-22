# 1. Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', ('c'), 'd']

a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
print([i for i in a if len(i) >= 1])

# 2. Write a Python program to calculate the hypotenuse of a right angled triangle.

side1, side2 = map(int, input("Enter the values of two sides of triangle: ").split(" "))
hypo = (side1**2 + side2**2)**0.5
print(hypo)

# 3. Write a Python program to calculate the sum of the digits in an integer.
#
# Sample Data : 16251
# Expected Output : 15

num = int(input("Enter the number:"))
a = 0
print(sum([int(i) for i in str(num)]))
