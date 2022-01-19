# 1. WAP to check whether the each word in a string begins with upper letter on not. If all the word begins with Upper letter print True otherwise print false.
# Sample input :-  "I Like Python"
# Output:- True
# Sample Input : "I Like python "
# Output :- False

a = input("Enter the String: ")
print(a.istitle())
# 2. Write a Python Program to print all the duplicates from a given list.(without using set function).
# Sample input: [1,2,2,3,3,4,4,4]
# Sample output:- [2,3,4]

a = [1, 2, 2, 3, 3, 4, 4, 4]
b = []
for i in a:
    if i not in b and a.count(i) > 1:
        b.append(i)

print(b)


# 3. Write a Python Program to print the symmetric difference between two list.

a = [1,2,3,4,5]
b=  [4,5,6,7,8]
print(list(set(a).symmetric_difference(set(b))))
