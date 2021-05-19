import unittest


class TestFindDiff(unittest.TestCase):

    def test_find_diff(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None)
        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff('aab', 'ab'), 'a')
        self.assertEqual(solution.find_diff('abcd', 'abcde'), 'e')
        self.assertEqual(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        # self.assertEqual(solution.find_diff_xor('ab', 'aab'), 'a')
        # self.assertEqual(solution.find_diff_xor('aab', 'ab'), 'a')
        # self.assertEqual(solution.find_diff_xor('abcd', 'abcde'), 'e')
        # self.assertEqual(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


class MyTest(unittest.TestCase):

    def test_find_diff(self):
        print(f'start of MyTest')
        solution = Solution()
        self.assertRaises(TypeError, solution.find_diff, None, None)
        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')
        # self.assertRaises(ValueError, solution.two_sum, [], 0)
        print(f'end of MyTest')

    
class Solution():
    """Solution find_diff()とfind_diff_xorの2パターンを作成
    
    find_diff() :  1つ目の引数と2つ目の引数のどちらが長いかは決まっていないが、
        短い方のリストから一文字選択
            長い方のリストから該当の一文字を削除
        長い方のリストに一文字残るのでreturn list_name[0]

    find_diff_xor()についてはgoogle python list comparison xorでの検索結果ら得られたsymmetric_difference()を使う


    """

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

        str1 = [char for char in str1]
        str2 = [char for char in str2]
        
        if len(str1) > len(str2):
            short_str = str2
            long_str = str1 
        elif len(str1) < len(str2):
            short_str = str1
            long_str = str2 
        else:
            print("len(str1) == len(str2)")

        for c in short_str:
            try:
                long_str.remove(c)
            except ValueError:
                print('Error with preset condition')
        if len(long_str) != 1:
            print("something wrong")

        return long_str[0]



def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()
    test = MyTest()
    test.test_find_diff()

