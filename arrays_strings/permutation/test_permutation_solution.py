""" 並べ替えか？
- スペースも該当

altについてはXORを使ってみる。
"""
import unittest

class Permutations(object):

    def is_permutation(self, str1, str2):
        # TODO: Implement me
        # pass
        if str1 == None or str2 == None:    return False
        if str1 == '' or str2 == '':    return False
        if sorted([c for c in str1]) != sorted([c for c in str2]):  
            return False 
        else: 
            return True


class TestPermutation(unittest.TestCase):

    def test_permutation(self, func):
        self.assertEqual(func(None, 'foo'), False)
        self.assertEqual(func('foo', None), False)
        self.assertEqual(func('', 'foo'), False)
        self.assertEqual(func('foo', ''), False)
        self.assertEqual(func('Nib', 'bin'), False)
        self.assertEqual(func('act', 'cat'), True)
        self.assertEqual(func('a ct', 'ca t'), True)
        self.assertEqual(func('dog', 'doggo'), False)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
