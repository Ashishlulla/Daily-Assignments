# 1. Write a Python program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Data : green-red-yellow-black-white
# Expected Output : black-green-red-white-yellow

a = input("Enter the colors separated by hyphen: ").split("-")
print("-".join(sorted(a)))

# 2. Write a Python program to find the values of length six in a given list using lambda.
# Sample List : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Sample Output :
# [Monday, Friday, Sunday]
a = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list(filter(lambda x: len(x) == 6, a)))

# 3. Write a Python program to find palindromes in a given list of strings using lambda.
# Orginal list of strings : ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes  : ['php', 'aaa']

a = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print(list(filter(lambda x: x == x[::-1], a)))
