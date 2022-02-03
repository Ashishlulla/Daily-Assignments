# 1. Write a Python program to check if there are duplicate values in a given flat list.
#
# Sample Output:
# Original List:[1,2,3,4,5,6,7]
# Check if there are duplicate values in the said given flat list : False
#
# Original List:[1,2,3,3,4,5,5,6,7]
# Check if there are duplicate values in the said given flat list : True

def check_duplicates(lst):
    flag = 0
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False

a = [1,2,3,3,4,5,5,6,7]
print(check_duplicates(a))


# 2. Write a Python program to convert a given number (integer) to a list of digits.
#
# Sample Input : 123
# Sample Output : [1,2,3]
a = 123
print(list(map(int, str(a))))

# 3. Write a Python program to remove all the values except integer values from a given array of mixed values.
#
# Original List: [34.67, 12, -94.89, 'Python', 0, 'C#']
#
# After removing all the values except integer values from the said array of mixed values: [12, 0]

a = [34.67, 12, -94.89, 'Python', 0, 'C#']
print([i for i in a if type(i) == int])
