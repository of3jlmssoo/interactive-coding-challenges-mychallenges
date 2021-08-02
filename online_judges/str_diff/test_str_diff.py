"""
[参照]
See the LeetCode problem page.とあるので
https://leetcode.com/problems/find-the-difference/

tはsにランダムに生成した一文字を追加したもの。
ということは、sで使われている文字のケースもあれば使われていなケースもある

'aaabbcdd', 'abdbacade'), 'e')
 aaabbcdde

"""
import unittest
import copy


class Solution(object):

    """ tにデフォルト値追加。assertRaises対応のため """
    def find_diff(self, s, t=''):
        # TODO: Implement me
        # pass

        if s is None or t is None:
            raise TypeError(f'Solution.find_diff. str is None or t is None')

        if s == '' and len(t) == 1:
            return t

        copied_t = copy.deepcopy(list(t))
        for c in s:
            copied_t.remove(c)

        # print(f'copied_t:{copied_t}')
        return copied_t[0]
        

class TestFindDiff(unittest.TestCase):

    def test_find_diff(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None)
        self.assertEqual(solution.find_diff('', 'y'), 'y')
        self.assertEqual(solution.find_diff('a', 'aa'), 'a')
        self.assertEqual(solution.find_diff('ae', 'aea'), 'a')
        self.assertEqual(solution.find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()
