# 1. Write a Python program to get the largest number from a list without using built-in function.
# Sample Input : [1, 5, -8, 0, -2]
# Expected Output : 5

def get_max(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                pass
    return lst[-1]


print(get_max([1, 5, -8, 0, -2]))


# 2. Write a Python program to get the smallest number from a list without using built-in function.
#
# Sample Input : [1, 5, -8, 0, -2]
# Expected Output : -8
def get_min(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                pass
    return lst[-1]


print(get_min([1, 5, -8, 0, -2]))
#
# 3. Write a Python program to unzip a list of tuples into individual lists.
#
# Sample Input : [(1,2), (3,4), (8,9)]
# Expected Output : [(1, 3, 8), (2, 4, 9)]

a = [(1, 2), (3, 4), (8, 9)]
print([tuple([i[0] for i in a]), tuple([i[1] for i in a])])


