# user-defined field size?
# (maybe later?)

# make dat array
# there will be three boards:
# a reading board (rb), a background board (bb),
# and a writing board (wb).

rb = []
bb = []
wb = []

def board_spawn(size, value):
    board = []
    for i in range(size):
        board.append([str(value)] * size)
    return board

def print_board(the_board):
    for row in the_board:
        print " ".join(row)

def sum_neighbors(board, row, col):
    return int(board[row - 1][col - 1]) + int(board[row - 1][col]) + \
        int(board[row - 1][col + 1]) + int(board[row][col - 1]) + \
        int(board[row][col + 1]) + int(board[row + 1][col - 1]) + \
        int(board[row + 1][col]) + int(board[row + 1][col + 1])

# instead of all this specific cell nonsense, we should be getting
# rid of the corners. we'll need a background board to work on.

def apply_rules(board, row, col):
    sum_num = sum_neighbors(board, row, col)
    if (board[row][col] == '1' and sum_num == 2) or sum_num == 3:
        return '1'
    else:
        return '0'

# apply rules to each cell, and create a new board onto which
# changes are mapped (otherwise i'll be giving/taking life in
# accordance with the changes i've already made for the current
# board, instead of applying all changes 'at once')

# LOGIC TIME
# for first cell in reading board ( rb[0][0] ), 

def spawn_padded_board(source_board):
    padded_board = []
    padded_board.append(['0'] * (len(source_board) + 2))
    for i in range(len(source_board)):
        padded_board.append(['0'] + source_board[i] + ['0'])
    padded_board.append(['0'] * (len(source_board) + 2))
    return padded_board

# RULES:
# if cell is live and has 4+, it dies to overcrowding
# if cell is live and has 1-, it dies to being forever alone
# if cell is live and has 2-3 friends, it stays alive
# if cell is dead and has =3 living neighbors, it rises from the dead
# (otherwise it stays dead)




