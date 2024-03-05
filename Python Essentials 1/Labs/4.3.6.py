# Day of the year: writing and using your own functions
'''
Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month)
and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

Use the previously written and tested functions.
Add your own test cases to the code.
'''
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if is_year_leap(year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[month - 1]      
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[month - 1]

def day_of_year(year, month, day):
    days = 0
    i = 0
    for months in range(1, month):
        days += days_in_month(year, months)
    return days + day

print(day_of_year(2000, 12, 31))
