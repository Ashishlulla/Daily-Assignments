# 1. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
# Sample Input : 5
# Expected Output : 120
def my_factorial(num):
    fact = 1
    if num == 0 and num == 1:
        return 1
    else:
        while num > 0:
            fact =fact * num
            num -= 1
    return fact

print(my_factorial(5))

# 2. Write a Python function that takes a list and returns a new list with unique elements of the first list without using set().
#
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

a = [1, 2, 3, 3, 3, 4, 5]
b = []
for i in a:
    if i not in b:
        b.append(i)

print(b)

# 3. Write a Python function that checks whether a passed string is palindrome or not.
# The function should return true if it is a palindrome it should return false.
#
# Sample Input : 'Wow'
# Expected Output : True

def my_palindrome(string):
    a=  string.lower()
    if a == a[::-1]:
        return True
    else:
        return False

print(my_palindrome("Wow"))
