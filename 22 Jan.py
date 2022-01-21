# 1. Write a Python program to reverse a string without using any built-in function and slicing.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"

a = "1234abcd"
string = ""
for i in a:
    string = i + string

print(string)

# 2. Write a Python program to convert a list of characters into a string.
# Sample List : ['a', 'b', 'c', 'd']
# Expected Output : abcd

a = ['a', 'b', 'c', 'd']
string = ""
for i in a:
    string += i

print(string)


# 3. Write a Python program calculate the product, multiplying all the numbers of a given tuple.
#
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648

def multiply(tpl):
    product = 1
    for i in tpl:
        product *= i

    return product


a = (2, 4, 8, 8, 3, 2, 9)
print(multiply(a))
