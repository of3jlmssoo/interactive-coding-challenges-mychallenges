"""
[参照]
https://algorithms.tutorialhorizon.com/magic-index-find-index-in-sorted-array-such-that-ai-i/

とはいえ、magic indexをindexの低い方から1つ見つければ良いという課題のため、インデックス0から順に処理する形態で済ますことにする。

"""
import unittest


class MagicIndex(object):

    def find_magic_index(self, array):
        # TODO: Implement me
        # pass
        argcheck = [array is None, array == []]
        if any(argcheck):
            return -1

        """ 内包表記で1個選んだらbreakの処理をかけなかったので。。。
        """
        for i, n in enumerate(array):
            if i == n:
                return n
        return -1


class TestFindMagicIndex(unittest.TestCase):

    def test_find_magic_index(self):
        magic_index = MagicIndex()
        self.assertEqual(magic_index.find_magic_index(None), -1)
        self.assertEqual(magic_index.find_magic_index([]), -1)
        array = [-4, -2, 2, 6, 6, 6, 6, 10]
        self.assertEqual(magic_index.find_magic_index(array), 2)
        array = [-4, -2, 1, 6, 6, 6, 6, 10]
        self.assertEqual(magic_index.find_magic_index(array), 6)
        array = [-4, -2, 1, 6, 6, 6, 7, 10]
        self.assertEqual(magic_index.find_magic_index(array), -1)
        print('Success: test_find_magic')


def main():
    test = TestFindMagicIndex()
    test.test_find_magic_index()


if __name__ == '__main__':
    main()
