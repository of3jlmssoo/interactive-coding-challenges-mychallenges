"""
久しぶりにpandasを使ってみる。in O(1)は気にしない。。。

"""
from typing import Type
import unittest
import pandas as pd


class Solution(object):

    def __init__(self, upper_limit=100):
        # TODO: Implement me
        # pass
        self.max = None
        self.min = None
        self.mean = None
        self.mode = None

        self.ps = pd.Series([], dtype='float64')

    def insert(self, val):
        # TODO: Implement me
        # pass
        if val is None:
            raise Type(f'Solution.insert: val == None')

        self.ps = self.ps.append(pd.Series([val]))

        self.update_max()
        self.update_min()
        self.update_mean()
        self.update_mode()

    def update_max(self):
        self.max = self.ps.max()

    def update_min(self):
        self.min = self.ps.min()

    def update_mean(self):
        self.mean = self.ps.mean(axis=0)

    def update_mode(self):
        s = pd.Series(list(self.ps))
        self.mode = s.mode()[0]


class TestMathOps(unittest.TestCase):

    def test_math_ops(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.insert, None)
        solution.insert(5)
        solution.insert(2)
        solution.insert(7)
        solution.insert(9)
        solution.insert(9)
        solution.insert(2)
        solution.insert(9)
        solution.insert(4)
        solution.insert(3)
        solution.insert(3)
        solution.insert(2)
        self.assertEqual(solution.max, 9)
        self.assertEqual(solution.min, 2)
        self.assertEqual(solution.mean, 5)
        self.assertTrue(solution.mode in (2, 9))
        print('Success: test_math_ops')


def main():
    test = TestMathOps()
    test.test_math_ops()


if __name__ == '__main__':
    main()
