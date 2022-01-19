# 1. Write a Python program to calculate the length of a string without using built-in function.

string = "Ashish Lulla"
count = 0
for i in string:
    count +=1
print(count)


# 2. Write a Python function to reverses a string if it's length is a multiple of 4
# without using built-in function.
string = "Ashish Lulla"
if len(string) % 4 == 0:
    print(string[::-1])
else:
    print(string)

# 3. Write a Python program to print the index of the character in a string.

# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

a = 'w3resource'
for i in range(len(a)):
    print(f"Current character {a[i]} position at {i}") 
