"""
[参照] https://web.stanford.edu/class/cs9/lectures/RecursionProbSetA_soln.pdf

"""
import unittest
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


def check_validity(sofar):

    if not len(sofar):
        return False

    if sofar[0] == ')' or sofar[-1] == '(':
        return False

    left_num = 0
    right_num = 0
    for s in sofar:
        if s == '(':
            left_num += 1
        elif s == ')':
            right_num += 1
        else:
            raise ValueError(f'check_validity: something wrong {sofar}')
        if left_num < right_num:
            return False

    return True


def allbalancedstringrec(lst, numopensleft, numcloseleft, sofar):
    logger.debug(f'1, {numopensleft}, {numcloseleft}, {sofar}')
    if numopensleft == 0 and numcloseleft == 0 and check_validity(sofar):
        logger.debug(f'sofar:{sofar}')
        lst.append(sofar)
        pass
    else:
        if numopensleft > 0:
            logger.debug(
                f'2, left:{numopensleft}, right:{numcloseleft}, sofar:{sofar}')
            allbalancedstringrec(
                lst,
                numopensleft - 1,
                numcloseleft,
                sofar + '(')
        if numcloseleft > 0:
            logger.debug(
                f'3, left:{numopensleft}, right:{numcloseleft}, sofar:{sofar}')
            allbalancedstringrec(
                lst,
                numopensleft,
                numcloseleft - 1,
                sofar + ')')


class Parentheses(object):

    def find_pair(self, num_pairs):
        # TODO: implement me
        # pass

        if num_pairs is None:
            raise TypeError(f'Parentheses.find_pair: arg error {num_pairs}')

        if num_pairs < 0:
            raise ValueError(f'Parentheses.find_pair: arg error {num_pairs}')

        lst = []
        allbalancedstringrec(lst, num_pairs, num_pairs, '')

        return lst


class TestPairParentheses(unittest.TestCase):

    def test_pair_parentheses(self):
        parentheses = Parentheses()
        self.assertRaises(TypeError, parentheses.find_pair, None)
        self.assertRaises(ValueError, parentheses.find_pair, -1)
        self.assertEqual(parentheses.find_pair(0), [])
        self.assertEqual(parentheses.find_pair(1), ['()'])
        self.assertEqual(parentheses.find_pair(2), ['(())',
                                                    '()()'])
        self.assertEqual(parentheses.find_pair(3), ['((()))',
                                                    '(()())',
                                                    '(())()',
                                                    '()(())',
                                                    '()()()'])
        print('Success: test_pair_parentheses')


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses()


if __name__ == '__main__':
    main()
