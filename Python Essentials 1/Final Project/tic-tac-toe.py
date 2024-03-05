from random import randrange

# Size of the board template
row = 3
column = 3

# Create the board template
board = []
sign = ''           # This will display the winner
no_victor = True    # The game ends if False/A winner or draw is declared
num = 0
for rows in range(row):
    inner = []
    for cols in range(column):
        num += 1
        inner.append(num)
    board.append(inner)
    
# Set the X's and O's list to false
# This will be used for comparing the values to the possible win outcomes
X = []
O = []

# For X's
for rows in range(row):
    inner = []
    for cols in range(column):
        inner.append(False)
    X.append(inner)
# For O's
for rows in range(row):
    inner = []
    for cols in range(column):
        inner.append(False)
    O.append(inner)

# Initialize the possible win outcomes
possible_outcome = (
    [
        [0, 0], [0, 1], [0, 2]  # 1st row horizontal
    ],
    [
        [1, 0], [1, 1], [1, 2]  # 2nd row horizontal
    ],
    [
        [2, 0], [2, 1], [2, 2]  # 3rd row horizontal
    ],
    [
        [0, 0], [1, 0], [2, 0]  # 1st column vertical
    ],
    [
        [0, 1], [1, 1], [2, 1]  # 2nd column vertical
    ],
    [
        [0, 2], [1, 2], [2, 2]  # 3rd column vertical
    ],
    [
        [0, 0], [1, 1], [2, 2]  # Diagonal from 1st row, 1st column to 3rd row, 3rd column
    ],
    [
        [0, 2], [1, 1], [2, 0]  # Diagonal from 1st row, 3rd column to 3rd row, 1st column
    ],
)


def main():
    # Keep the game going until there is a victor
    while no_victor:
        draw_move(board)
        display_board(board)
        victory_for(board)
        if no_victor == False:  # To stop the loop when computer won
            break
        enter_move(board)
        display_board(board)
        victory_for(board)
    if no_victor == False:
        print(sign)


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0],board[0][1],board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0],board[1][1],board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0],board[2][1],board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    not_exist = True
    while not_exist:
        try:
            move = int(input("Enter your move: "))
            if move > 0 and move < 10:
                for rows in range(row):
                    for cols in range(column):
                        if move == board[rows][cols]:
                            board[rows][cols] = 'O'
                            not_exist = False
                if not_exist:
                    print("Your move is invalid!")
            else:
                print("Usage: integer that is greater than 0 AND less than 10!")
        except ValueError:
            print("Not an integer!")
            

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for rows in range(row):
        inner = ()
        for cols in range(column):
            if board[rows][cols] != 'O' and board[rows][cols] != 'X':
                inner = (rows, cols)
                free_fields.append(inner)
    return free_fields
                

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # Set the X's and O's table to true if there's a match in the board
    for rows in range(row):
        for cols in range(column):
            if board[rows][cols] == 'O' and O[rows][cols] == False:    # For O's
                O[rows][cols] = True
            if board[rows][cols] == 'X' and X[rows][cols] == False:    # For X's
                X[rows][cols] = True
    
    # To update global variables
    global no_victor
    global sign

    # Check possible outcome if there's a match
    for rows in possible_outcome:
        X_true_count = 0    # Count the X's truth value for each set of possible outcome
        O_true_count = 0    # Count the O's truth value for each set of possible outcome
        for cols in rows:
            pos_row = cols[0]
            pos_col = cols[1]
            if X[pos_row][pos_col] == True:
                X_true_count += 1
            if O[pos_row][pos_col] == True:
                O_true_count += 1

        # Check if there is a winner or there is a draw
        if X_true_count == 3:
            sign = 'Computer won!'
            no_victor = False
            return
        elif O_true_count == 3:
            sign = 'You won!'
            no_victor = False
            return
        elif make_list_of_free_fields(board) == []:
            sign = "Game draw!"
            no_victor = False
            return
    return


def draw_move(board):
    # The function draws the computer's move and updates the board.
    not_exist = True
    while not_exist:
        move = randrange(1,10)
        for rows in range(row):
            for cols in range(column):
                if move == board[rows][cols]:
                    board[rows][cols] = 'X'
                    not_exist = False


main()