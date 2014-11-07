import unittest
import random
from butt import *

def one_or_zero():
    return random.randint(0, 1)

starting_board_0 = [
    ['1','0','0'],
    ['0','1','0'],
    ['0','0','1']
]
starting_board_1 = [
    ['1','0','1'],
    ['0','1','0'],
    ['1','0','1']
]
starting_board_2 = [
    ['1','1','0'],
    ['0','0','0'],
    ['0','0','1']
]
starting_board_3 = [
    ['0','0','0'],
    ['0','1','0'],
    ['0','0','0']
]
starting_board_4 = [
    ['0','0','0','1','0'],
    ['0','1','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['1','1','1','1','1']
]

print "Stephanie's a big ol' butt."

ending_board_4 = [
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','1','1','1','0']
]
ending_board_0 = [
    ['0','0','0'],
    ['0','1','0'],
    ['0','0','0']
]
ending_board_1 = [
    ['0','0','0'],
    ['0','0','0'],
    ['0','0','0']
]
ending_board_2 = [
    ['0','0','0'],
    ['0','1','0'],
    ['0','0','0']
]
ending_board_3 = [
    ['0','0','0'],
    ['0','0','0'],
    ['0','0','0']
]

# SHAPES/FOOTPRINTS
# this is the footprint for a 2x2 shape (with 4x4 footprint)
footprint_square = [
    ['0','0','0','0'],
    ['0','1','1','0'],
    ['0','1','1','0'],
    ['0','0','0','0']
]       


class MyTest(unittest.TestCase):
    def test(self):
        # make_next_board() with 3x3 boards
        self.assertEqual(make_next_board(starting_board_0), ending_board_0)
        self.assertEqual(make_next_board(starting_board_1), ending_board_1)
        self.assertEqual(make_next_board(starting_board_2), ending_board_2)
        self.assertEqual(make_next_board(starting_board_3), ending_board_3)

        # make_next_board() with 5x5 board
        self.assertEqual(make_next_board(starting_board_4), ending_board_4)

        # make a randomly-sized board
        rando_board = []
        num_rows = random.randint(8, 20)
        num_cols = random.randint(8, 20)
        for i in range(num_rows):
            rando_board.append(['0'] * num_cols)
        # test for randomly-sized boards
        self.assertEqual(len(make_next_board(rando_board)), num_rows)
        self.assertEqual(len(make_next_board(rando_board)[0]), num_cols)

        # randomly select a start location for a 2x2 immortal shape
        # (this has a 4x4 footprint)
        start_row = random.randint(0, num_rows - 4)
        start_col = random.randint(0, num_cols - 4)
        # insert a 2x2 square somewhere in the board
        for row in range(len(footprint_square)):
            for cell in range(len(footprint_square[row])):
                rando_board[start_row + row][start_col + col] \
                    = footprint_square[row][col]
        # test that the randomly-located 2x2 is in the same
        # spot after the next board has been generated
        for row in range(1, 3):
            for col in range(1, 3):
                self.assertEqual(make_next_board(rando_board)[start_row \
                    + row][start_col + col], '1')
        

if __name__ == '__main__':
    unittest.main()



