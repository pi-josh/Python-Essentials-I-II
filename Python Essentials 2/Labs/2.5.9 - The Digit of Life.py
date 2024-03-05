# The Digit of Life
'''
Some say that the Digit of Life is a digit evaluated using somebody's birthday.
It's simple - you just need to sum all the digits of the date.
If the result contains more than one digit, you have to repeat the addition until you get exactly one digit.
For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually,
the order of the digits doesn't matter)
outputs the Digit of Life for the date.
'''

'''
# Prompt the user for their birthday
is_birthday = False
while not is_birthday:
    birthdate = input("Enter your birthday: ")
    if len(birthdate) != 8:
        print("Incorrect length (it should be 8 digits in any format | YYYYMMDD | YYYYDDMM | MMDDYYYY)")
    elif not birthdate.isdigit():
        print("Format should only include digits!")
    else:
        is_birthday = True

# Add each digit (until there is exactly one digit)
sum_digit = 0
for char in birthdate:
    sum_digit += int(char)
    while sum_digit > 9:
        birthdate = str(sum_digit)
        sum_digit = 0
        for char in birthdate:
            sum_digit += int(char)
            
# Output the Digit of Life for the date
print(sum_digit)
'''

# Prompt the user for their birthday
is_birthday = False
while not is_birthday:
    birthdate = input("Enter your birthday: ")
    if len(birthdate) != 8:
        print("Incorrect length (it should be 8 digits in any format | YYYYMMDD | YYYYDDMM | MMDDYYYY)")
    elif not birthdate.isdigit():
        print("Format should only include digits!")
    else:
        is_birthday = True

# Convert the string into a list of integers
list_of_digits = list(map(int, birthdate))

# Use the sum method to get the sum of the digits
sum_of_digits = sum(list_of_digits)

# Repeat Step 2 and Step 3 until there is only one digit
while sum_of_digits > 9:
    list_of_digits = list(map(int, str(sum_of_digits)))
    sum_of_digits = sum(list_of_digits)
    
# Output the Digit of Life
print(sum_of_digits)