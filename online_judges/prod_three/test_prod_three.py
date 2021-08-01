import unittest
import itertools
import math


class Solution(object):

    def max_prod_three(self, array):
        # TODO: Implement me
        # pass

        if array is None:
            raise TypeError(
                f'Solution.max_prod_three: num_stones_left is none')

        if len(array) < 3:
            raise ValueError(f'Solution.max_prod_three: len(array)<3')

        return(
            max([math.prod(v) for v in itertools.combinations(array, 3)])
        )


class TestProdThree(unittest.TestCase):

    def test_prod_three(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.max_prod_three, None)
        self.assertRaises(ValueError, solution.max_prod_three, [1, 2])
        # self.assertEqual(solution.max_prod_three([5, -2, 3]), -30)
        self.assertEqual(solution.max_prod_three([5, -2, 3, 1, -1, 4]), 60)
        print('Success: test_prod_three')


def main():
    test = TestProdThree()
    test.test_prod_three()


if __name__ == '__main__':
    main()
