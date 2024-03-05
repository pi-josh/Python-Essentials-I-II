# Find a word!
'''
Let's play a game. We will give you two strings:
one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question:
are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas",
the answer is no (as the letters "d", "o", or "g" don't appear in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
'''

# Prompt the user for a word
is_word = False
while not is_word:
    word = input("Enter a word: ")
    if not word.split() or len(word) < 0:
        print("Input one or more character!")
    elif not word.isalpha():
        if ' ' in word:
            print("Word should not contain any spaces")
        else:
            print("Word should only contain alphabet character!")
    else:
        # If it is in the correct format, make it case-insensitive for smooth comparing
        word = word.lower()
        is_word = True

# Prompt the user for a combination to be used
is_combination = False
while not is_combination:
    combination = input("Enter a combination of characters: ")
    if not combination.split() or len(combination) < 0:
        print("Input one or more character!")
    elif not combination.isalpha():
        if ' ' in combination:
            print("Word should not contain any spaces")
        else:
            print("Word should only contain alphabet character!")
    else:
        # If it is in the correct format, make it case-insensitive for smooth comparing
        combination = combination.lower()
        is_combination = True

# Check if word can be found in the combination
is_found = False
while not is_found:
    if word in combination:
        is_found = True
    else:
        current_index = 0       # This will be the starting point at each iteration
        found_count = 0         # This will keep track of the times the character in word has been found in the combination respectively.
        max_count = len(word)   # If found_count is equal to the maximum count then the word is found
        while not is_found:
            for word_index in range(len(word)):
                for combi_index in range(current_index, len(combination)):
                    if word[word_index] == combination[combi_index]:
                        current_index = combi_index + 1    # Set the current index to the index (increment 1) where the character is found so it won't check the previous and current character in combination
                        found_count += 1
            if found_count == max_count:
                is_found = True
            else:
                break   # Exit out of this loop if it is not found
        if not is_found:
            break   # Exit out of this loop if it is not found
                
# Output the result
if is_found:
    print("yes")
else:
    print("no")