"""
- n_pairs_parenthesesを参考にする
- find_permutations()でリターンする配列の順序については考慮していないがexpectedと同じになったので良しとする
"""
import unittest
import copy
import logging


logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = True


class Permutations(object):

    def find_permutations(self, string):
        # TODO: Implement me
        # pass

        argchecks = [string is None, string == '']

        if any(argchecks):
            return string

        n = len(string)
        work_str = []
        lst = []
        _make_permutations(list(string), n, work_str, '', lst)
        logger.debug(f'lst: {lst}')
        return lst


def _make_permutations(str, n, work_str, sofar, lst):
    logger.debug(f'_make_permutations called str:{str}, \
         n:{n}, work_str:{work_str}, sofar:{sofar}, lst:{lst}')

    if n == 0:
        if sofar not in lst:
            lst.append(sofar)
        return

    else:
        for s in range(n):
            work_str = copy.deepcopy(str)
            work_str.remove(str[s])
            _make_permutations(work_str, n - 1, work_str, sofar + str[s], lst)


class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        permutations = Permutations()
        self.assertEqual(permutations.find_permutations(None), None)
        self.assertEqual(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        self.assertEqual(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


def main():
    test = TestPermutations()
    test.test_permutations()


if __name__ == '__main__':
    main()
