"""
[test_anagrams.py]
- dataの各エレメントをソート
- data自体をnumpyでargsort
- dataにargsortで得られたインデックスを適用

また、resultとexpectedの順番問題あり

[test_anagrams2.py]
https://github.com/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/anagrams/anagrams_challenge.ipynb
には、from collections import OrderedDictがあるのでOrderedDictを使えということなのだろう。

"""
import unittest
import numpy as np
import copy
from collections import OrderedDict


class Anagram(object):

    def group_anagrams(self, items):
        # TODO: Implement me
        # pass

        if items is None:
            raise TypeError(f'Anagram.group_anagrams: arg error {items=}')

        od = OrderedDict()

        for i in items:
            # print(''.join(sorted(i)))
            if (k := ''.join(sorted(i))) not in od:
                od[k] = [i]
            else:
                od[k].append(i)

        # print(od, od.values())
        return [x for row in od.values() for x in row]

    def make_sequence(self, items, data_np):
        data_np_copy = []
        already_processed = []

        for i in items:
            if i not in already_processed:
                idx = list(data_np).index(i)
                data_np_copy.append(data_np[idx])
                data_np_copy.append(data_np[idx + 1])
                already_processed.append(data_np[idx])
                already_processed.append(data_np[idx + 1])
        return data_np_copy


class TestAnagrams(unittest.TestCase):

    def test_group_anagrams(self):
        anagram = Anagram()
        self.assertRaises(TypeError, anagram.group_anagrams, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        self.assertEqual(anagram.group_anagrams(data), expected)

        print('Success: test_group_anagrams')


def main():
    test = TestAnagrams()
    test.test_group_anagrams()


if __name__ == '__main__':
    main()
