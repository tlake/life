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
        size_1 = random.randint(3, 10)
        size_2 = random.randint(3, 10)
        for i in range(size_1):
            rando_board.append(['0'] * size_2)
        
        self.assertEqual(len(make_next_board(rando_board)), size_1 )
        self.assertEqual(len(make_next_board(rando_board)[0]), size_2)

if __name__ == '__main__':
    unittest.main()

