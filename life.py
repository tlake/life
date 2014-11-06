# RULES:
# if cell is live and has 4+, it dies to overcrowding
# if cell is live and has 1-, it dies to being forever alone
# if cell is live and has 2-3 friends, it stays alive
# if cell is dead and has =3 living neighbors, it rises from the dead
# (otherwise it stays dead)
#
# there will be three boards:
# a reading board (rb), a padded board (pb),
# and a writing board (wb).

# it will be nice to be able to track how the board progresses
# at a reasonable speed
import time

# global variables! so everybody can play!
rb = []
pb = []
wb = []

def testing_worldgen():
    rb = [
    ['0', '0', '1', '1', '0', '1', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '0', '1', '0', '1', '0'],
    ['0', '1', '1', '1', '0', '0', '0', '1', '0', '0'],
    ['0', '0', '1', '1', '0', '0', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '1', '1', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '0', '0', '0', '1', '0'],
    ['1', '0', '1', '1', '0', '0', '0', '1', '0', '1'],
    ['0', '0', '1', '1', '0', '0', '0', '0', '1', '0'],
    ['0', '0', '1', '1', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '1', '1', '0', '0', '0', '0', '0', '0']
    ]
    pb = spawn_padded_board(rb)
    wb = spawn_board(10, '0')


def spawn_board(size, value):
    board = []
    for i in range(size):
        board.append([str(value)] * size)
    return board

def print_board(the_board):
    for row in the_board:
        print " ".join(row)

# takes an existing board and returns a copy of it, with an additional
# row of 0's all around it
def spawn_padded_board(source_board):
    padded_board = []
    padded_board.append(['0'] * (len(source_board) + 2))
    for i in range(len(source_board)):
        padded_board.append(['0'] + source_board[i] + ['0'])
    padded_board.append(['0'] * (len(source_board) + 2))
    return padded_board

# for a given cell (at board[row][col]), returns the result of 
# adding the values of all eight cells surrounding it
def sum_neighbors(board, row, col):
    row = int(row)
    col = int(col)
    return int(board[row - 1][col - 1]) + int(board[row - 1][col]) + \
        int(board[row - 1][col + 1]) + int(board[row][col - 1]) + \
        int(board[row][col + 1]) + int(board[row + 1][col - 1]) + \
        int(board[row + 1][col]) + int(board[row + 1][col + 1])

# returns what the next step ought to be for the given
# cell (at board[row][col]) based on the status of its neighbors
def decide_fate(board, row, col):
    row = int(row)
    col = int(col)
    sum_num = sum_neighbors(board, row, col)
    if (board[row][col] == '1' and sum_num == 2) or sum_num == 3:
        return '1'
    else:
        return '0'

# when given a cell (at padded_board[padded_row][padded_col]), this
# will decide_fate(that-cell) and then apply that result to the
# proper cell on the next-step board (dest_board); it should be
# apparent from the variables, but apply_judgement() must be called
# upon a cell on the padded board
def apply_judgement(padded_board, padded_row, padded_col, dest_board):
    padded_row = int(padded_row)
    padded_col = int(padded_col)
#    print "wb[%s][%s] = " % (padded_row - 1, padded_col - 1), \
#    decide_fate(padded_board, padded_row, padded_col)
# (just debugging code)
    dest_board[padded_row - 1][padded_col - 1] = \
    decide_fate(padded_board, padded_row, padded_col)

# here we call apply_judgement() on each cell in the padded board
# (which of course was populated from the reading board); we need
# to pass in all three boards: update_world() will figure out which
# cells upon which to act from information in the reading board,
# then it will pass the padded and writing boards through to
# apply_judgement(). 
def update_world(reading_board, padded_board, writing_board):
    for row in range(1, len(reading_board) + 1):
        for col in range(1, len(reading_board[row - 1]) + 1):
            apply_judgement(padded_board, row, col, writing_board)

def main():
    # oh man! all the hard work of defining the functions is done!
    # now i just have to work out the order in which things play
    # out here in the main() function!
    rb = []
    pb = []
    wb = []

    # we need to run an initial world setup to generate the boards.
    # this means initial conditions in rb, a padded rb livin in pb,
    # and a blank wb
    testing_worldgen()

    # let's print the initial board condition
    print_board(rb)

    # probably as long as there is at least one living cell, we 
    # should run the game. put a while loop in here.
    # it's dependent upon y_l being True
    y_l = True

    # (get it? the variable for the while loop is y_l?)
    # (no? try saying the letters of the variable name out loud.)
    # (... 'while', 'y_l' ... they're almost homophones!)

    # TOP OF WHILE LOOP
    while y_l == True:

        # we should update_world()
            # this will call apply_judgement() on each non-edge cell in
            # the padded board
                # which will call decide_fate()
                    # which will call sum_neighbors()
                        # which will return how many neigbors are alive
                # based on sum_neighbors(), decide_fate() will return 
                # '1' or '0' to apply_judgement()
            # based on decide_fate(), apply_judgement() will write the
            # next state of each cell to the writing board
        update_world(rb, pb, wb)

        # at this point, we should have a whole new world state held
        # inside wb. now we need to store wb inside of rb, and then
        # make a new padded version of rb stored inside of pb.
        rb = wb
        pb = spawn_padded_board(rb)

        # with our boards all updated, we should print the newly-made
        # reading board for the player, then let them appreciate it.
        print_board(rb)
        time.sleep(3)
    
        # we should now see if there are still living cells on the board
        # if so, let's set the variable y_l to True; otherwise,
        # it gets set to False. we'll hit the end of the while loop and
        # as long as y_l == True, we'll jump back to the start of
        # the while loop.
        for row in range(len(rb)):
            for col in range(len(rb[row])):
                if rb[row][col] == '1':
                    y_l = True
                    break
                else:
                    y_l = False
                break
            break

        # END OF WHILE LOOP

    # we should probably have an end-of-game message here
    print "Congratulations! You made everything die."




