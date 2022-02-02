# 1. Write a Python program to create string consisting of the non-negative integers up to n inclusive.
# Input : 4
# Output : 0 1 2 3 4
# Input : 15
# Output : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

n = int(input("Enter the Number"))
print(" ".join([str(i) for i in range(n + 1)]))

# 2. Write a Python program to generate a list, containing the fibonacci sequence, up until the nth term.
# Sample Output:
# First 6 fibonacci numbers: [0, 1, 1, 2, 3, 5]

n = int(input("Enter nth term: "))
n1, n2 = 0, 1
count = 0
if n <= 0:
    print("Enter a positive integer")
elif n == 1:
    print(f"First fibonacci number: {n1}")
else:
    lst = []
    while count < n:
        lst.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(f"First {n} fibonacci numbers: {lst}")


# 3. Write a Python program to check if all the elements of a list are included in another given list.
# Sample Input :
# test_includes_all([10, 20, 30, 40, 50, 60], [20, 40]))
# test_includes_all([10, 20, 30, 40, 50, 60], [20, 80]))
# Sample Output:
# True
# False

def test_includes_all(l1, l2):
    return all(i in l1 for i in l2)


print(test_includes_all([10, 20, 30, 40, 50, 60], [20, 40]))
