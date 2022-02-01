# 1. Write a Python program to count the elements in a list until an element is a tuple.
# Sample Input : [10,20,30,(10,20),40]
# Expected Output : 3

a = [10, 20, 30, (10, 20), 40]
count = 0
for i in a:
    if type(i) == tuple:
        break
    else:
        count += 1
print(count)

# 2. Write a Python program to compute element-wise sum of given tuples.
#
# Original Lists:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

a = (1, 2, 3, 4)
b = (3, 5, 2, 1)
c = (2, 2, 3, 1)
print(tuple(map(lambda x, y, z: x + y + z, a, b, c)))

# 3. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers
# using lambda function.
# Original List: [2,4,-6,-9,11,-12,14,-5,17]
# Sum of the negative numbers: -32
# Sum of the positive numbers: 48

a = [2, 4, -6, -9, 11, -12, 14, -5, 17]
positive = 0
negative = 0
for i in a:
    if i < 0:
        negative += i
    else:
        positive += i

print(negative)
print(positive)
