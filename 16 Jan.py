# 1. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

a = 'w3resource'
dic_1 = {}
for i in a:
    dic_1[i] = a.count(i)
print(dic_1)

# 2. Write a Python program to sort a list alphabetically in a dictionary.
# Sample dictionary:{'n1': [2, 3, 1], 'n2': [5,1,2], 'n3': [3, 2, 4]}

# Sample Output :- {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

a = {'n1': [2, 3, 1], 'n2': [5,1,2], 'n3': [3, 2, 4]}
print(sorted(a.items(), key=lambda x: x[1]))


# 3. Write a Python program to combine two lists into a dictionary.
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1, 2, 3, 4, 5]
print(dict(zip(a, b)))

