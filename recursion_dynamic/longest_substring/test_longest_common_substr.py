"""
test_longest_common_subseq.pyと同じ内容。

"""
import unittest
from test_longest_common_subseq import StringCompare


# class StringCompare(object):
class StringCompare(StringCompare):

    def longest_common_substr(self, str0, str1):
        # TODO: Implement me
        # pass
        print(str0, str1)
        return super().longest_common_subseq(str0, str1)


class TestLongestCommonSubstr(unittest.TestCase):

    def test_longest_common_substr(self):
        str_comp = StringCompare()
        self.assertRaises(
            TypeError,
            str_comp.longest_common_substr,
            None,
            None)
        self.assertEqual(str_comp.longest_common_substr('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        self.assertEqual(str_comp.longest_common_substr(str0, str1), expected)
        print('Success: test_longest_common_substr')


def main():
    test = TestLongestCommonSubstr()
    test.test_longest_common_substr()


if __name__ == '__main__':
    main()
