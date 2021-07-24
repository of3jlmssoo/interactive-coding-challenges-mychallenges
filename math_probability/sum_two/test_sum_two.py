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
    """
    ちょっと違う気もするし、sub_twoどうしようはあるが+も-も使っていないことに間違い無し。。。
    """

    def sum_two(self, val1, val2):
        # TODO: Implement me
        # pass
        logger.debug(f'Solution.sum_two: {val1} {val2}')
        if val1 is None or val2 is None:
            raise TypeError(f'Solution.sum_two: val == None')
        lst = []
        lst.append(val1)
        lst.append(val2)
        return sum(lst)


class TestSumTwo(unittest.TestCase):

    def test_sum_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.sum_two, None)
        self.assertEqual(solution.sum_two(5, 7), 12)
        self.assertEqual(solution.sum_two(-5, -7), -12)
        self.assertEqual(solution.sum_two(5, -7), -2)
        print('Success: test_sum_two')


def main():
    test = TestSumTwo()
    test.test_sum_two()


if __name__ == '__main__':
    main()
