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
        self.assertEqual(solution.find_diff('ab', 'aab'), 'a')
        self.assertEqual(solution.find_diff_xor('ab', 'aab'), 'a')
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

        str1 = self.str2list(str1)
        str2 = self.str2list(str2)
        
        short_str, long_str = self.set_short_long(str1, str2)

        for c in short_str:
            try:
                long_str.remove(c)
            except ValueError:
                print('Error with preset condition')
        if len(long_str) != 1:
            print("something wrong")

        return long_str[0]

    def find_diff_xor(self, str1: str, str2: str) -> str:
        """find_diff_xor ギブアップ。solutionを参考にする。
        === str1 === char:a, ord(char):97, result:97, bin(ord(char):0b1100001,  bin(result):0b1100001
        === str1 === char:b, ord(char):98, result:3,  bin(ord(char):0b1100010,  bin(result):0b11
        === between str1 and str2 === result:3, bin(result):0b11
        === str2 === char:a, ord(char):97, result:98, bin(ord(char):0b1100001,  bin(result):0b1100010
        === str2 === char:a, ord(char):97, result:3,  bin(ord(char):0b1100001,  bin(result):0b11
        === str2 === char:b, ord(char):98, result:97, bin(ord(char):0b1100010,  bin(result):0b1100001
        === before return === result:97, chr(result):a
        a
        =============================
        === str1 === char:a, ord(char):97, result:97, bin(ord(char):0b1100001,  bin(result):0b1100001
        === str1 === char:a, ord(char):97, result:0,  bin(ord(char):0b1100001,  bin(result):0b0
        === str1 === char:b, ord(char):98, result:98, bin(ord(char):0b1100010,  bin(result):0b1100010
        === between str1 and str2 === result:98, bin(result):0b1100010
        === str2 === char:a, ord(char):97, result:3,  bin(ord(char):0b1100001,  bin(result):0b11
        === str2 === char:b, ord(char):98, result:97, bin(ord(char):0b1100010,  bin(result):0b1100001
        === before return === result:97, chr(result):a
        a
        =============================
        === str1 === char:a, ord(char):97, result:97, bin(ord(char):0b1100001,  bin(result):0b1100001
        === str1 === char:b, ord(char):98, result:3,  bin(ord(char):0b1100010,  bin(result):0b11
        === str1 === char:c, ord(char):99, result:96, bin(ord(char):0b1100011,  bin(result):0b1100000
        === str1 === char:d, ord(char):100, result:4, bin(ord(char):0b1100100,  bin(result):0b100
        === between str1 and str2 === result:4, bin(result):0b100
        === str2 === char:a, ord(char):97, result:101, bin(ord(char):0b1100001,  bin(result):0b1100101
        === str2 === char:b, ord(char):98, result:7,   bin(ord(char):0b1100010,  bin(result):0b111
        === str2 === char:c, ord(char):99, result:100, bin(ord(char):0b1100011,  bin(result):0b1100100
        === str2 === char:d, ord(char):100, result:0,  bin(ord(char):0b1100100,  bin(result):0b0
        === str2 === char:e, ord(char):101, result:101,bin(ord(char):0b1100101,  bin(result):0b1100101
        === before return === result:101, chr(result):e
        e
        =============================
        === str1 === char:a, ord(char):97, result:97,   bin(ord(char):0b1100001,  bin(result):0b1100001
        === str1 === char:a, ord(char):97, result:0,    bin(ord(char):0b1100001,  bin(result):0b0
        === str1 === char:a, ord(char):97, result:97,   bin(ord(char):0b1100001,  bin(result):0b1100001
        === str1 === char:b, ord(char):98, result:3,    bin(ord(char):0b1100010,  bin(result):0b11
        === str1 === char:b, ord(char):98, result:97,   bin(ord(char):0b1100010,  bin(result):0b1100001
        === str1 === char:c, ord(char):99, result:2,    bin(ord(char):0b1100011,  bin(result):0b10
        === str1 === char:d, ord(char):100, result:102, bin(ord(char):0b1100100,  bin(result):0b1100110
        === str1 === char:d, ord(char):100, result:2,   bin(ord(char):0b1100100,  bin(result):0b10
        === between str1 and str2 === result:2, bin(result):0b10
        === str2 === char:a, ord(char):97, result:99,   bin(ord(char):0b1100001,  bin(result):0b1100011
        === str2 === char:b, ord(char):98, result:1,    bin(ord(char):0b1100010,  bin(result):0b1
        === str2 === char:d, ord(char):100, result:101, bin(ord(char):0b1100100,  bin(result):0b1100101
        === str2 === char:b, ord(char):98, result:7,    bin(ord(char):0b1100010,  bin(result):0b111
        === str2 === char:a, ord(char):97, result:102,  bin(ord(char):0b1100001,  bin(result):0b1100110
        === str2 === char:c, ord(char):99, result:5,    bin(ord(char):0b1100011,  bin(result):0b101
        === str2 === char:a, ord(char):97, result:100,  bin(ord(char):0b1100001,  bin(result):0b1100100
        === str2 === char:d, ord(char):100, result:0,   bin(ord(char):0b1100100,  bin(result):0b0
        === str2 === char:e, ord(char):101, result:101, bin(ord(char):0b1100101,  bin(result):0b1100101
        === before return === result:101, chr(result):e
        """
        result = 0
        for char in str1:
            result ^= ord(char)
            # print(f"=== str1 === char:{char}, ord(char):{ord(char)}, result:{result}, bin(ord(char):{bin(ord(char))},  bin(result):{bin(result)}")

        # print(f"=== between str1 and str2 === result:{result}, bin(result):{bin(result)}")
        
        for char in str2:
            result ^= ord(char)
            # print(f"=== str2 === char:{char}, ord(char):{ord(char)}, result:{result}, bin(ord(char):{bin(ord(char))},  bin(result):{bin(result)}")

        # print(f"=== before return === result:{result}, chr(result):{chr(result)}")
        return chr(result)

    def str2list(self, string: str) -> list:
        return [char for char in string]

    def set_short_long(self, str1: str, str2: str) -> list:
        if len(str1) > len(str2):
            return str2, str1
        elif len(str1) < len(str2):
            return str1, str2
        else:
            print("len(str1) == len(str2)")


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()
    test = MyTest()
    test.test_find_diff()

