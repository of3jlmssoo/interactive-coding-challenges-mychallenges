import unittest


class TestFindDiff(unittest.TestCase):

    def test_find_diff(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None)
        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        self.assertEqual(solution.find_diff_xor('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff_xor('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff_xor('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


class MyTest(unittest.TestCase):

    def test_find_diff(self):
        print(f'start of MyTest')
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None, None)
        # self.assertRaises(ValueError, solution.two_sum, [], 0)
        print(f'end of MyTest')

    
class Solution():

    def find_diff(self, str1: str, str2: str) -> str:
        """find_diff 違いは一文字に限定されている。str1が長いケースも短いケースもある。ただし長さの差は必ず１になる(べき)。

        Args:
            str1 (str): Is case important? The strings are lower case
            str2 (str): Is case important? The strings are lower case

        Returns:
            str: 一文字の異なるキャラクター

        TestCases:
            None input -> TypeError
            'ab', 'aab' -> 'a'
            'aab', 'ab' -> 'a'
            'abcd', 'abcde' -> 'e'
            'aaabbcdd', 'abdbacade' -> 'e'
        """
        if str1 == None or str2 == None:
            raise TypeError('TypeError : None specified in str1 or str2')

def main():
    pass
    # test = TestFindDiff()
    # test.test_find_diff()


if __name__ == '__main__':
    # main()
    test = MyTest()
    test.test_find_diff()

