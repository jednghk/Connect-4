board_config = {(row, column): ' ' for row in range(1, 7) for column in range(1, 8)}

def generateBoard():
    for i in range (1, 8):
        print(' {}'.format(i), end = '')
    print ('')
    for row in range(6, 0, -1):
        for column in range(1, 8):
            print ('|' + board_config[(row, column)], end = '')
        print("|")

def next_avail_space(column):
    """checks the next available space in a column and returns its tuple"""
    for row in range (1, 7):
        if board_config[(row, column)] == ' ':
            return (row, column)
        else:
            pass
    return None #User tries to put chip in a full column

#Creates plaintext board with each blank space representing tuple (row,column) in board_config dictionary

def check_for_4_E(position, symbol):
    """checks to the right"""
    row = position[0]
    column = position [1]
    """takes in the position (tuple) and returns if win or not"""
    for i in range(1,4): #checks horizontally to the right
        if board_config.get((row, column + i)) == symbol: #if outside board, will return none, if not occupied, will return ' '
            continue
        else: #if slot is not occupied, it either is unoccupied or outside the board, so return False
            return False
    return True  # if loops are completed without returning False, return True

def check_for_4_N(position, symbol):
    """checks N"""
    row = position[0]
    column = position[1]
    for i in range(1,4):
        if board_config.get((row + i, column)) == symbol: #if outside board, will return none, if not occupied, will return ' '
            continue
        else: #if slot is not occupied, it either is unoccupied or outside the board, so return False
            return False
    return True #if loops are completed without returning False, return True

def check_for_4_NE(position, symbol):
    """checks E"""
    row = position[0]
    column = position[1]
    for i in range(1,4):
        if board_config.get((row + i, column + i)) == symbol: #if outside board, will return none, if not occupied, will return ' '
            continue
        else: #if slot is not occupied, it either is unoccupied or outside the board, so return False
            return False
    return True #if loops are completed without returning False, return True

def check_for_4_NW(position, symbol):
    """checks NW"""
    row = position[0]
    column = position[1]
    for i in range(1,4):
        if board_config.get((row + i, column - i)) == symbol: #if outside board, will return none, if not occupied, will return ' '
            continue
        else: #if slot is not occupied, it either is unoccupied or outside the board, so return False
            return False
    return True #if loops are completed without returning False, return True

def check_win_status (board, symbol):
    """iterates through each space in the board and runs check_for_4 function. Returns True if """
    win_status = False
    for row in range(1, 7):
        for column in range(1, 8):
            if board[(row, column)] == symbol:
                if check_for_4_N((row, column), symbol) or check_for_4_E((row, column), symbol) or check_for_4_NW((row, column), symbol) or check_for_4_NE((row, column), symbol):
                    return True
    return win_status
