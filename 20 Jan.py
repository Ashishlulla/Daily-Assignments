# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : 'w'
# Expected Result : ''

string = input("Enter the String: ")
if len(string) > 2:
    print(string[:2]+string[-2:])
elif len(string) == 2:
    print(string*2)
else:
    print("Empty String")

# 2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
# string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

string = input("Enter the String: ")
if  len(string)>=3 and string.endswith("ing"):
    string+="ly"
    print(string)
elif len(string)>=3:
    string+="ing"
    print(string)
else:
    print(string)

# 3. Write a Python program to get a single string from two given strings, separated by a space and swap the
# first two characters of each string.

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

string1, string2 = input("Enter the two Strings separated by space: ").split(" ")
print(string2[:2]+string1[2:]+" "+string1[:2]+string2[2:])

