# Sudoku
'''
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board.
The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

row_list = [
    "195743862",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "254938671",
]
'''

row_list = []  # A list where the rows of number will be stored
is_ok = False
num_list = [x for x in range(1, 10)]    # Will be used to check if there is no copy in the rows, columns, and 3x3 grid of the list of strings

# Function for checking the rows, cols, and 3x3 grid of the sudoku
def checklist(lst):
    lst.sort()
    if lst == num_list:
        return True
    else:
        return False
    
# Prompt the user for the rows of numbers
for row in range(9):    # Ask the user nine times
    is_valid = False    # False until user inputs a valid row of numbers
    while not is_valid: # Keep asking the user for a row of number until the input is valid
        string = input("Enter a string of numbers: ")
        if not string.split():  # If the user input is empty
            print("Please enter a string of numbers!")
        elif len(string) != 9:  # If the user input's length is not correct
            print("It should be 9 numbers (from 1-9)!")
        else:
            row_list.append(string)  # If valid, add it to the list of rows
            is_valid = True
            
# Check if it the rows, cols, and 3x3 grid is okay
is_copy = False     # Will turn true if it found a copy in its row or column position
if not is_copy:
    # Checking the rows
    for row in row_list: 
        tmp_list = list(map(int, row))   # Temporary list variable to store each digits by row
        if not checklist(tmp_list):
            is_copy = True   
if not is_copy:
    # Checking the columns
    for col in range(9):
        tmp_list = []   # Temporary list variable to store each digits by column
        for row in range(9):
            tmp_list.append(int(row_list[row][col]))
        if not checklist(tmp_list):
            is_copy = True
if not is_copy:
    # Check the 3x3 grid of the string of words
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            # This will be used to access the 3x3 sublist in the main list
            # Range of indices for rows
            start_row_index = row
            end_row_index = row + 3
            
            # Range of indices for cols
            start_col_index = col
            end_col_index = col + 3
            
            tmp_list = []   # Temporary list variable to store each digits by column
            for row_index in range(start_row_index, end_row_index):
                for col_index in range(start_col_index, end_col_index):
                    tmp_list.append(int(row_list[row_index][col_index]))
            if not checklist(tmp_list):
                is_copy = True

# Output the result
if not is_copy:
    print("Yes")
else:
    print("No")