import unittest
from butt import *

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(4, 4)
        a = sum_neighbors([['1','1','0'],['0','0','0'],['0','0','0']], 1, 1)
        self.assertEqual(a, 2)

if __name__ == '__main__':
    unittest.main()




