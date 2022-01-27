# 1. Write a Python program to replace the last element in a list with another list.
# Sample Data : [1,3,5,7,9,10], [2,4,6,8]
# Expected Output: [1,3,5,7,9,2,4,6,8]

a, b = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
a[-1:] = b
print(a)

# 2. Write a Python program to insert a given string at the beginning of all items in a list.
#
# Sample List : [1,2,3,4] , string : 'emp'
# Expected Output : ['emp1', 'emp2', 'emp3', 'emp4']

a = [1, 2, 3, 4]
string = 'emp'
print([string + str(i) for i in a])

# 3. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original List:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list:
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])

a = [1, 1, 2, 3, 4, 4, 5, 1]
n = int(input("length of 1st part : "))
b = [a[:n]]
b.append(a[n:])
print(b)
