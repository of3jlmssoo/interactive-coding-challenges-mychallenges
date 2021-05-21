import unittest

""" 以下のサイトを参考にする。
https://ja.wikipedia.org/wiki/In-place%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
"""

class ReverseString(object):
    def reverse(self,chars):
        # pass
        if chars == None: return None
        if chars == ['']: return ['']

        for i in range(len(chars)//2):
            chars[i], chars[len(chars)-i-1] = chars[len(chars)-i-1], chars[i]
        
        return chars    

class TestReverse(unittest.TestCase):

    def test_reverse(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(['']), [''])
        self.assertEqual(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self, func):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func(target_list)
        self.assertEqual(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    reverse_string = ReverseString()
    test.test_reverse(reverse_string.reverse)
    test.test_reverse_inplace(reverse_string.reverse)


if __name__ == '__main__':
    main()
