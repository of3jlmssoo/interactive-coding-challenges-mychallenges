from typing import Type
import unittest
import math
import copy
import logging

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = True


class Solution(object):

    def mult_other_numbers(self, array):
        # TODO: Implement me
        # pass

        if array is None:
            raise TypeError(f'Solution.mult_other_numbers: array is None')

        if len(array) == 1:
            return []

        if len(array) == 2:
            return [array[1], array[0]]

        result = [None] * len(array)
        for i, n in enumerate(array):
            others = copy.deepcopy(array)
            others.pop(i)
            result[i] = math.prod(others)
        return result


class TestMultOtherNumbers(unittest.TestCase):

    def test_mult_other_numbers(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.mult_other_numbers, None)
        self.assertEqual(solution.mult_other_numbers([0]), [])
        self.assertEqual(solution.mult_other_numbers([0, 1]), [1, 0])
        self.assertEqual(solution.mult_other_numbers([0, 1, 2]), [2, 0, 0])
        self.assertEqual(solution.mult_other_numbers(
            [1, 2, 3, 4]), [24, 12, 8, 6])
        print('Success: test_mult_other_numbers')


def main():
    test = TestMultOtherNumbers()
    test.test_mult_other_numbers()


if __name__ == '__main__':
    main()
