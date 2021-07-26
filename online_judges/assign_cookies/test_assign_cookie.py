
"""
[目的]
Your goal is to maximize the number of your content children and output the maximum number.
your content childrenの数を最大化すること


"""
import logging
import unittest

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

    def find_content_children(self, g, s):
        # TODO: Implement me
        # pass
        if g == None or s == None:
            raise TypeError(f'Solution.find_content_children: argments == None {g} {s}')

        result = 0
        """ 子供情報(欲しい大きさ)を一つずつ処理 """
        for i in g:
        # for i in reversed(g):
            logger.debug(f'Solution.find_content_children: i:{i}, s:{s}')
            """ 子供の要望を満たすサイズのクッキー(i)があれば
                remove(i)する(remove()なので一つだけ削除される)
            """
            if [j for j in s if j>=i]:  # 子供のサイズ要望を満たすクッキーがある場合
                k=i                     # 子供要望サイズ < 提供可能なクッキーサイズに対応
                if k in s:              # 子供要望サイズ in 提供可能なクッキーサイズであれば
                    s.remove(k)         # 提供可能クッキーからその分を削除し
                    result += 1         # 提供事例をプラス1
                else:                   # 子供要望サイズをプラス1
                    k = k +1

        return result
class TestAssignCookie(unittest.TestCase):

    def test_assign_cookie(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_content_children, None, None)
        self.assertEqual(solution.find_content_children([1, 2, 3], 
                                                    [1, 1]), 1)
        self.assertEqual(solution.find_content_children([1, 2], 
                                                    [1, 2, 3]), 2)
        self.assertEqual(solution.find_content_children([7, 8, 9, 10], 
                                                    [5, 6, 7, 8]), 2)
        print('Success: test_find_content_children')

        # additonal test
        self.assertEqual(solution.find_content_children([7, 8, 9, 10], 
                                                    [8]), 1)

def main():
    test = TestAssignCookie()
    test.test_assign_cookie()


if __name__ == '__main__':
    main()
