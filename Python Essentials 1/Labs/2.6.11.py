# Operators and expressions - 2
'''
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time,
given as a number of minutes (it could be arbitrarily large).
The start time is given as a pair of hours (0..23) and minutes (0..59).
The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code 
- it's okay if it accepts an invalid time 
- the most important thing is that the code produces valid results for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.
'''

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
rem = (mins + dura) % 60
hour += ((mins + dura) // 59)
mins = rem

print(str(hour) + ":" + str(mins))
