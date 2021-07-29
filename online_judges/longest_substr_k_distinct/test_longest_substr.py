"""
self.assertEqual(solution.longest_substr('abcabcdefgghiij', k=3), 6)
abcabc defgghiij abcのk=3 charactersで6桁

self.assertEqual(solution.longest_substr('abcabcdefgghighij', k=3), 7)
abcabcdef　gghighi j 	ghiで最大7桁
"""
import unittest


class Solution(object):

    def longest_substr(self, string, k):
        # TODO: Implement me
        pass


class TestSolution(unittest.TestCase):

    def test_longest_substr(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.longest_substr, None)
        self.assertEqual(solution.longest_substr('', k=3), 0)
        self.assertEqual(solution.longest_substr('abcabcdefgghiij', k=3), 6)
        self.assertEqual(solution.longest_substr('abcabcdefgghighij', k=3), 7)
        print('Success: test_longest_substr')


def main():
    test = TestSolution()
    test.test_longest_substr()


if __name__ == '__main__':
    main()
