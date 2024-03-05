# The continue statement - the Pretty Vowel Eater
'''
Scenario
Your task here is even more special than before:
you must redesign the (ugly) vowel eater from the previous lab and create a better, 
upgraded (pretty) vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case;
we'll talk about string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it.
Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns,
and assign it to the word_without_vowels variable.
'''
word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the loop.
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)