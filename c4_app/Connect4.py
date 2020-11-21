from board import *

print('''
Hello! Welcome to the Connect 4 game.
Rules: 
Each player will choose a color (red or yellow) and then take turns dropping colored discs into a seven-column,
six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within 
the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of 
four of one's own discs.
''')

p1_name = input('Once ready, enter the name of Player 1:')
p2_name = input('Enter the name of Player 2:')

turn = 0
symbol = '0'
while not check_win_status(board_config, symbol):
    generateBoard()
    if turn % 2 == 0:
        p1_move = int(input('Your turn {}! Choose the column to place your chip.'.format(p1_name)))
        if p1_move > 7 or p1_move < 1:
            print ("That's not a valid option, try again")
            continue
        slot = next_avail_space(p1_move)
        if slot is not None:
            board_config[slot] = '0'
            turn += 1
            symbol = '0'
        else:
            print("That's not a valid move. Try again.")
            continue
    else:
        p2_move = int(input('Your turn {}! Choose the column to place your chip.'.format(p2_name)))
        if p2_move > 7 or p2_move < 1:
            print ("That's not a valid option, try again")
            continue
        slot = next_avail_space(p2_move)
        if slot is not None:
            board_config[slot] = 'X'
            turn += 1
            symbol = 'X'
        else:
            print("That's not a valid move. Try again.")
            continue

if symbol == 'X':
    print("Congratulations! {} has won!".format(p2_name))
else:
    print("Congratulations! {} has won!".format(p1_name))
