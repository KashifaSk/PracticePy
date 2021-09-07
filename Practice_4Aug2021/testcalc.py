import unittest

import calc


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10,calc.add(5, 5))  # add assertion here
    def test_substract(self):
        self.assertEqual(0,calc.substract(5, 5))

if __name__ == '__main__':
   unittest.main()
