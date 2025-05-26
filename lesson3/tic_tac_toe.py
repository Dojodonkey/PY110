'''
Problem Statement:
Tic Tac Toe is a 2-player game played on a 3x3 grid called the board.
Each player takes a turn and marks a square on the board.
The first player to get 3 squares in a row -- horizontally, vertically, or diagonally -- wins.
If all 9 squares are filled and neither player has 3 in a row, the game ends in a tie.

Algorithm:

1. Display the initial empty 3x3 board.
2. Ask the user to mark a square.
3. Computer marks a square.
4. Display the updated board state.
5. If it's a winning board, display the winner.
6. If the board is full, display tie.
7. If neither player won and the board is not full, go to #2
8. Play again?
9. If yes, go to #1
10. Goodbye!

- An outer loop between steps #1 and #9 that repeats as long as the player wants to keep playing.
- An inner loop between steps #2 and #7 that repeats as long as there is no winner and the board isn't full.
'''
import os
import random

# Magic chars
INIT_MARKER = ' '
PLAYER_MARKER = 'X'
COMP_MARKER = 'O'

# To begin game
def initialize_board():
    return {square: INIT_MARKER for square in range(1, 10)}

# Game board
def display_board(board):
    os.system('clear')

    print('P1 - "X" ||||||| Computer - "O"')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')

# Asking for input
def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items() if value == INIT_MARKER]

def join_or(lst, sep=',', fin_sep='or'):
    result_lst = []
    for i in range(len(lst) - 1):
        result_lst.append(f'{str(lst[i]) + sep}')
    if len(lst) > 1:
        result_lst.append(fin_sep + ' ' + str(lst[-1]))
        result_lst[-2] = str(lst[-2])
    else:
        #index out of range when only one available square is left.
    return ' '.join(result_lst)

def player_choice(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Pick a square ({join_or(valid_choices)}): ')
        choice = input().strip()
        if choice in valid_choices:
            break

        print('Invalid choice, pick again..')
    board[int(choice)] = PLAYER_MARKER

def computer_choice(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMP_MARKER

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], #horizontal lines
        [1, 4, 7], [2, 5, 8], [3, 6, 9], #vertical lines
        [1, 5, 9], [3, 5, 7],            #diagnol lines
    ]
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == PLAYER_MARKER and
        board[sq2] == PLAYER_MARKER and
        board[sq3] == PLAYER_MARKER):
            return 'P1'
        elif (board[sq1] == COMP_MARKER and
        board[sq2] == COMP_MARKER and
        board[sq3] == COMP_MARKER):
            return 'Computer'

    return None

def board_is_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def board_checker(board):
    return board_is_full(board) or someone_won(board)

def score_board(board, player_score, computer_score):
    # scoreboard for best of 5 game
    BEST_OF = 5
    first_to_five = True
    if detect_winner(board) is 'P1':
        player_score += 1
    if detect_winner(board) is 'Computer':
        computer_score += 1
    if computer_score >= BEST_OF or player_score >= BEST_OF:
        if computer_score >= BEST_OF:
            prompt('Computer wins best of 5!')
        else:
            prompt('Player 1 wins best of 5!')
        # best of five is complete and loop needs to break
        global match_5
        match_5 = False
    prompt(f'-SCOREBOARD-\n P1: {player_score} -+- Computer: {computer_score}')
    return first_to_five



player_score = 0
computer_score = 0
# Start Game
def tic_tac_toe():
    #play best of five
    match_5 = True
    while match_5:
        #play round of game
        while True:
            board = initialize_board()
            # Main Loop
            while True:
                display_board(board) # Display board after each turn
                player_choice(board)
                if board_checker(board):
                    break
                computer_choice(board)
                if board_checker(board):
                    break
            # Display final board
            display_board(board)
            # Determine winner/draw
            if someone_won(board):
                prompt(f'{detect_winner(board)} WINS!')
            else:
                prompt(f'{"It's a draw!".upper()}')
            # Display scoreboard
            score_board(board, player_score, computer_score)
            # Play again?
            prompt('Play again? (y/n):')
            answer = input()
            if answer != 'y':
                match_5 = False
                break
        prompt('Thanks for playing!')

tic_tac_toe()