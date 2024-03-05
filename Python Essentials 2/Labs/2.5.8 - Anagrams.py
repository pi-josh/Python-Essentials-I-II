# Anagrams
'''
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.
For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent
'''

import sys

# Prompt the user for a string
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if it is empty or contains spaces-only
# If not, set the strings to lowercase
if ((not string1.split() or len(string1) < 0)
    and (not string2.split() or len(string2) < 0)):
    print("is not an anagram")
    sys.exit(1)
else:
    string1 = string1.lower()
    string2 = string2.lower()

# Convert the strings into a list ignoring characters that are not alphabetic
string_list1 = []
for char in string1:
    if char.isalpha():
        string_list1 += char
        
string_list2 = []
for char in string2:
    if char.isalpha():
        string_list2 += char

# Arrange the lists
string_list1.sort()
string_list2.sort()

# Compare the two lists
if string_list1 == string_list2:
    print("is an anagram")
else:
    print("is not an anagram")