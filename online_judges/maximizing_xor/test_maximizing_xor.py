"""
[参照]
See the HackerRank problem page.とあるので見てみる。
"""
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

    def max_xor(self, lower, upper):
        # TODO: Implement me
        # pass

        maxes = []
        vals = range(lower, upper + 1)
        for l in vals:
            maxes.append(max(list(map(lambda x: x ^ l, vals))))
            logger.debug(
                f'Solution.max_or 1: {list(map(lambda x: x ^ l, vals))}')

        logger.debug(f'Solution.max_or 2: {maxes}')

        return max(maxes)


class TestMaximizingXor(unittest.TestCase):

    def test_maximizing_xor(self):
        solution = Solution()
        self.assertEqual(solution.max_xor(10, 15), 7)
        print('Success: test_maximizing_xor')

        """ [参照]ページに記載された例で確認 """
        # self.assertEqual(11 ^ 11, 0)
        # self.assertEqual(11 ^ 12, 7)
        # self.assertEqual(12 ^ 12, 0)


def main():
    test = TestMaximizingXor()
    test.test_maximizing_xor()


if __name__ == '__main__':
    main()
