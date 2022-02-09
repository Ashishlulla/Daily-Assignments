# 1. Write a Python program to find the sum of all items in a dictionary.

# Input : {'a': 100, 'b':200, 'c':300}
# Output : 600
a = {'a': 100, 'b':200, 'c':300}
print(sum(a.values()))


# 2. Write a Python program to merge two dictionaries.

a = {'a':100, 'b':200, 'c':300}
b = {'d':400, 'e':500, 'f':600}
a.update(b)
print(a)
# 3. Write a Python program to check if a substring is present in a given string.,

# Sample Input : str1='Hello, World' str2='World'

# Sample Output : Yes
str1='Hello, World' 
str2='World'
if str2 in str1:
    print("Yes")
else:
    print("No")
