# How many days: writing and using your own functions
'''
our task is to write and test a function which takes two arguments (a year and a month)
and returns the number of days for the given year-month pair (while only February is sensitive to the year value, 
your function should be universal).

The initial part of the function is ready.
Now, convince the function to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6).
It may be very helpful. We encourage you to use a list filled with the months' lengths.
You can create it inside the function - this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases.
'''
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100:
        return True
    elif year % 400:
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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
