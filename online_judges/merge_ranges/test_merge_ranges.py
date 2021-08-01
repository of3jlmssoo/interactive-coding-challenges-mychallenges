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

    def merge_ranges(self, array):
        # TODO: Implement me
        pass

        if array is None:
            raise TypeError(f'Solution.merge_ranges: array is None')

        if array == []:
            return []

        """
            lower i[0] i[1] upper
            lower i[0]      upper i[1]
            lower           upper i[0] i[1]

            check_data_validity()で以下のパターンは排除している
            i[0] lower(i[0]がlowerより小さい。sortしている)
            i[0] > i[1]
        """

        sorted_array = sorted(array, key=lambda x: (x[0], x[1]))
        logger.debug(f'Solution.merge_ranges: sorted_array:{sorted_array}')

        outarr = []
        lower = None
        upper = None
        for i in sorted_array:
            logger.debug(f'Solution.merge_ranges: for loop: {i[0]}, {i[1]}')
            self.check_data_validity(i, lower)

            if lower is None and upper is None:
                lower = i[0]
                upper = i[1]
                continue
            elif i[0] <= upper and upper < i[1]:
                """ lower i[0]      upper i[1] """
                upper = i[1]
            elif lower <= i[0] and i[1] <= upper:
                """ lower i[0] i[1] upper """
                continue
            # else:
            elif upper <= i[0]:
                """ lower           upper i[0] i[1] """
                outarr.append((lower, upper))
                lower = i[0]
                upper = i[1]
            else:
                raise ValueError(
                    f'Solution.merge_ranges: {i[0]}, {i[1]}, lower:{lower}, upper:{upper}')

        outarr.append((lower, upper))
        return outarr

    def check_data_validity(self, i, lower):
        logger.debug(f'Solution.merge_ranges: i:{i}, lower:{lower}')
        if lower is not None and (i[0] >= i[1] or lower >= i[0]):
            raise ValueError(f'Solution.merge_ranges: ValueEroor i[0] >= i[1]')


class TestMergeRanges(unittest.TestCase):

    def test_merge_ranges(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.merge_ranges, None)
        self.assertEqual(solution.merge_ranges([]), [])

        array = [(2, 3), (7, 9)]
        expected = [(2, 3), (7, 9)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(3, 5), (2, 3), (7, 9), (8, 10)]
        expected = [(2, 5), (7, 10)]
        self.assertEqual(solution.merge_ranges(array), expected)
        array = [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)]
        expected = [(1, 11)]
        self.assertEqual(solution.merge_ranges(array), expected)
        print('Success: test_merge_ranges')


def main():
    test = TestMergeRanges()
    test.test_merge_ranges()


if __name__ == '__main__':
    main()
