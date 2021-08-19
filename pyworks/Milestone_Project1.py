# Create a function that can print out a board. Set up your board as a list
# where each index 1-9 corresponds with a number on a number pad, so you get a 3x3 board representation.
import random


def display_board(board):
    from IPython.display import clear_output
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# Function to take player input and assign their marker as 'X' and 'O'.
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Function that takes in the board list object, a marker('X' or 'O') and a desired position (number 1-9) and assigns it
# to the board
def place_marker(board, marker, position):
    board[position] = marker


# Function takes in a board and a mark(X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    # WIN TIC TAC TOE?

    # ALL ROWS, and check to see if they all share the same marker?
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (
                board[7] == board[8] == board[9] == mark) or
            # ALL COLUMNS, check to see if marker matches
            (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (
                        board[9] == board[6] == board[3] == mark) or
            # 2 diagonals, check to see match
            (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark))


# Function that uses the random module to randomly decide which player goes first.
def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Function returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '


# Function check and return a boolean value if the board is full.
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Function that asks players next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. if it is then return the position for later use.
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9): '))
    return position


# Function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    choice = input('Play again? (y or n): ')
    return choice == 'y'


# Run the game
# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')
while True:
    # Play the game

    ## SET EVERYTHIN UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? (y or n): ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # GAME PLAY
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'

        ### PLAYER ONE TURN

        else:
            if turn == 'Player 2':
                # Show the board
                display_board(the_board)
                # Choose a position
                position = player_choice(the_board)
                # Place the marker on the position
                place_marker(the_board, player2_marker, position)

                # Check if they won
                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('PLAYER 2 HAS WON!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        turn = 'Player 1'

    if not replay():
        break
