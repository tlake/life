import unittest
from butt import *


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
#        self.assertEqual(4, 4)
        self.assertEqual(make_next_board(starting_board_0), ending_board_0)
        self.assertEqual(make_next_board(starting_board_1), ending_board_1)
        self.assertEqual(make_next_board(starting_board_2), ending_board_2)
        self.assertEqual(make_next_board(starting_board_3), ending_board_3)
        self.assertEqual(make_next_board(starting_board_4), ending_board_4)

if __name__ == '__main__':
    unittest.main()

