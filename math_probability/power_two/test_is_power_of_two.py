"""
ビット演算が続く。
if power of 2でgoogleして一番上のエントリーを参考にする。
https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2
"""
import unittest


class Solution(object):

    def is_power_of_two(self, val):
        # TODO: Implement me
        # pass

        if val is None:
            raise TypeError(f'Solution.is_power_of_two: val = None')

        return (val != 0) and ((val & (val - 1)) == 0)


class TestSolution(unittest.TestCase):

    def test_is_power_of_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.is_power_of_two, None)
        self.assertEqual(solution.is_power_of_two(0), False)
        self.assertEqual(solution.is_power_of_two(1), True)
        self.assertEqual(solution.is_power_of_two(2), True)
        self.assertEqual(solution.is_power_of_two(15), False)
        self.assertEqual(solution.is_power_of_two(16), True)
        print('Success: test_is_power_of_two')


def main():
    test = TestSolution()
    test.test_is_power_of_two()


if __name__ == '__main__':
    main()
