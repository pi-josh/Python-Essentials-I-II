# Palindromes
'''
Do you know what a palindrome is?

It's a word which look the same when read forward and backward.
For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.
Test your code using the data we've provided.

Solution 1: Using the reverse method
Solution 2: Using iteration of character in the string
'''
'''
import sys

# Promp the user for a string
string = input("Enter a string: ")

if not string.split() or len(string) < 0:   # If string is empty or contains space only then output "not a palindrome"
    print("not a palindrome")
    sys.exit(1)
else:                                       # Else, set the string to lowercase to make it case-insensitive
    string = string.lower()

# Turn the string of characters into a list and ignore those that are not alphabetic
main_list = []
for char in string:
    if char.isalpha():
        main_list += char
        
# Reverse the list and store it in another variable
reverse_list = main_list[:]
reverse_list.reverse()

# Compare the original and reversed list
if main_list == reverse_list:
    print("is a palindrome")
else:
    print("is not a palindrome")
'''

import sys

# Prompt the user for a string
string = input("Enter a string: ")

# If the string is empty or contains space only, output "not a palindrome" and exit
# Else, set the string to lowercase to make it case-sensitive
if not string.split() or len(string) < 0:
    print("not a palindrome")
    sys.exit(1)
else:
    string = string.lower()

# Turn the string into a list, ignoring characters that are not alphabetic
string_list = []
for char in string:
    if char.isalpha():
        string_list += char

# Use for loop to iterate from first to middle and last to middle then check if each character is the same
# You can use while loop if more comfortable
last = len(string_list) - 1
for index in range(len(string_list) // 2):
    if string_list[index] != string_list[last]:   # If not equal, output "not a palindrome" and exit the program
        print("not a palindrome")
        sys.exit(0)
    last -= 1
else:   # If all equal, output "is a palindrome"
    print("is a palindrome")






