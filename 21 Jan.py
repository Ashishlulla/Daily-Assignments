# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
print([i for i in range(1500, 2701) if i % 7 == 0 and i % 5 == 0])


# 2. Write a Python program that accepts a string and calculate the number of digits and letters.
#
# Sample Data : Python 3.2
# Expected Output :
# Letters : 6
# Digits : 2

def count_letter_digit(string):
    letter_count = 0
    digit_count = 0
    for i in string:
        if i.isalpha():
            letter_count += 1
        elif i.isnumeric():
            digit_count += 1
        else:
            pass
    return f"Letter:{letter_count} \n" \
           f"Digit: {digit_count}"


string = "Python 3.2"
print(count_letter_digit(string))

#
# 3. Write a Python program to convert month name to a number of days.

# Expected Output:
# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of month: February
# Number of days: 28/29 days
month = ("January", "February", " March", "April", 'May', 'June', 'July', ' August', ' September',
         'October', "November", "December")
days = ('31', '28/29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31')
month_day = dict(zip(month, days))
user_input= input("Input the name of Month: ")
if user_input in month_day.keys():
    print(f"Number of Days : {month_day[user_input]} days")
else:
    print('Invalid Month name')
