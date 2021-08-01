"""
一度に取れるのは3枚
最後に取った方が勝ち
1 勝ち
2 勝ち
3 勝ち
4 負け  1枚取る -> 3枚残りで相手全部取り
    　  2枚取る -> 2枚残りで相手全部取り
    　  3枚取る -> 1枚残りで相手全部取り
5 勝ち  1枚取る -> 相手が4枚
6 勝ち  2枚取る -> 相手が4枚
7 勝ち  3枚取る -> 相手が4枚
8 負け  1枚取る -> 7枚残りで相手
    　  2枚取る -> 6枚残りで相手
    　  3枚取る -> 5枚残りで相手
9 勝ち  1枚取る -> 相手が8枚
10勝ち  2枚取る -> 相手が8枚
11勝ち  3枚取る -> 相手が8枚

=> 4の倍数かどうか。
    倍数    負け
    以外    勝ち

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

    def can_win_nim(self, num_stones_left):
        # TODO: Implement me
        pass

        if num_stones_left is None:
            raise TypeError(f'Solution.can_win_nim: num_stones_left is none')

        if num_stones_left % 4:
            return True
        else:
            return False


class TestSolution(unittest.TestCase):

    def test_can_win_nim(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.can_win_nim, None)
        self.assertEqual(solution.can_win_nim(1), True)
        self.assertEqual(solution.can_win_nim(2), True)
        self.assertEqual(solution.can_win_nim(3), True)
        self.assertEqual(solution.can_win_nim(4), False)
        self.assertEqual(solution.can_win_nim(7), True)
        self.assertEqual(solution.can_win_nim(40), False)
        print('Success: test_can_win_nim')


def main():
    test = TestSolution()
    test.test_can_win_nim()


if __name__ == '__main__':
    main()
