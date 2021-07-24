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
logger.disabled = False


class Solution(object):

    def add_digits(self, val):
        # TODO: Implement me
        pass

        logger.debug(f'Solution.add_digits: called. {val}')
        """ None input -> TypeError """
        if val is None:
            raise TypeError(f'Solution.add_digits: val == None')
        """ negative input -> ValueError """
        if val < 0:
            raise ValueError(f'Solution.add_digits: val < 0')
        """ 9 -> 9 """
        if val < 10:
            return val
        """ 138 -> 3 """
        """ 65536 -> 7 """
        while self.isTwoDigits(val):
            val = self.transform(val)
        return val

    def isTwoDigits(self, val):
        logger.debug(f'Solution.isTwoDigits: {val}')
        return len(list(str(val))) > 1

    def transform(self, val):

        result = 0
        for idx in reversed(list(str(val))):
            result = result + int(idx)
        logger.debug(f'Solution.transform: {result}')
        return result


class TestAddDigits(unittest.TestCase):

    def test_add_digits(self, func):
        self.assertRaises(TypeError, func, None)
        self.assertRaises(ValueError, func, -1)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(9), 9)
        self.assertEqual(func(138), 3)
        self.assertEqual(func(65536), 7)
        print('Success: test_add_digits')


def main():
    test = TestAddDigits()
    solution = Solution()
    test.test_add_digits(solution.add_digits)
    try:
        test.test_add_digits(solution.add_digits_optimized)
    except AttributeError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
