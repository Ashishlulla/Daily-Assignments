
# 1. Write a Python program to compute average of two given lists. 

# Original Lists:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706

a,b = [1, 1, 3, 4, 4, 5, 6, 7],[0, 1, 2, 3, 4, 4, 5, 7, 8]
print(f"Average of two list is: {(sum(a)+sum(b))/(len(a)+len(b))}")

# 2. Write a Python program to count integer in a given mixed list. 

# Original List:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:6
a = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(len([i for i in a if type(i)==int]))
# 3. Write a Python program to extract a specified column from a given nested list. 

# Original Nested List:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]

a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print([i[0] for i in a])
