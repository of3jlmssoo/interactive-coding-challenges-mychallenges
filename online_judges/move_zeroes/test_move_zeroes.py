import unittest
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

    def move_zeroes(self, nums):
        """ Is the output a new array of ints?
            No, do this in-place
        """
        # TODO: Implement me
        pass

        if nums is None:
            raise TypeError(f'Solution.move_zeroes: nums is None')

        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(n)

        return nums


class TestMoveZeroes(unittest.TestCase):

    def test_move_zeroes(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.move_zeroes, None)
        array = [0, 1, 0, 3, 12]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 3, 12, 0, 0])

        array = [1, 0]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])

        array = [0, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 0])

        array = [0]
        solution.move_zeroes(array)
        self.assertEqual(array, [0])

        array = [1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1])

        array = [1, 1]
        solution.move_zeroes(array)
        self.assertEqual(array, [1, 1])
        print('Success: test_move_zeroes')


def main():
    test = TestMoveZeroes()
    test.test_move_zeroes()


if __name__ == '__main__':
    main()
