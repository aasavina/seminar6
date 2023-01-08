def mult_ij(i, j):
    return i*j

import unittest
class TestMultIJ(unittest.TestCase):
    def testequal(self):
        self.assertEqual(mult_ij(2, 3), 7)
        if __name__ == '__main__':
            unittest.main()