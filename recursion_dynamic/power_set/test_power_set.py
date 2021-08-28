"""
[前提]
- 結果のリスト内の順序に意味があるとは思えないので、結果確認のところは修正している(check_result())
- Class SetsはClass Combinatoricにリネーム
- test_power_setもWeb版に変更

[参照]
https://en.wikipedia.org/wiki/Power_set#/media/File:Hasse_diagram_of_powerset_of_3.svg
Power setでは再帰とビットの2つの方法がある。

(1)再帰
再帰に関しては、[参照]の図を見て以下のようにまとめる。

input_str					rest			sofar
xyz
	x				yz			x			1
		y			z			xy			2
			z		'’			xyz			3

	y				xz			y			4
		x			z			yz			5
			z		'’			yzx
	z				xy			z			6
		x			y			zx			7
			y		'’			zxy			and ‘’

- 結果のとり方がこれまでとは異なる。
- 最初xyzがとられなかったが以下で対応
       if len(rest) > 1:
            rest.remove(c)
"""
import copy
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


# class Sets(object):
class Combinatoric(object):

    def find_power_set_iterative(self, input_set):
        # TODO: Implement me
        pass

    def check_result(self, expected, result):
        """ expectedとresultを比較 1)長さ、2)エレメント """
        logger.debug(f'check_result: {expected=} {result=}')
        if len(expected) != len(result):
            return False

        for e in expected:
            if e not in result:
                return False

        return True
        # self.assertEqual(resu

    def find_power_set_recursive(self, input_set):
        # TODO: Implement me
        # pass
        result = []
        input_set = list(input_set)
        rest = copy.deepcopy(input_set)
        self._find_power_set_recursive(
            input_set, len(input_set), rest, '', result)
        return self.find_power_make_return(result)

    def find_power_make_return(self, result):
        """ リスト化 """
        return [[] if r == set() else list(sorted(r)) for r in result]
        # return ['' if r == set() else list(sorted(r)) for r in result]

    def print_vars(self, idx, n, input_set, rest, sofar, result, c=''):
        input_set = ','.join([x for x in input_set])
        rest = ','.join([x for x in rest])
        print(
            f'({idx}) {n=:} {c=:3} {input_set=:10} {rest=:10} {sofar=:10} {result=}')

    def _find_power_set_recursive(self, input_set, n, rest, sofar, result):
        if not logger.debug:
            self.print_vars(1, n, input_set, rest, sofar, result)

        if set(sofar) not in result:
            logger.debug(
                f'{" "*100} set(sofar):{set(sofar)} will be added to result')
            result.append(set(sofar))

        if n == 0:
            logger.debug(f'{" "*100} n==0: result:{result}, sofar:{sofar}')
            # result.append(sofar)
            return

        for c in input_set:
            rest = copy.deepcopy(input_set)
            if len(rest) > 1:
                rest.remove(c)
            if not logger.debug:
                self.print_vars(2, n, input_set, rest, sofar, result, c)
            for d in rest:
                self._find_power_set_recursive(
                    rest, n - 1, rest, sofar + c, result)
            rest = copy.deepcopy(input_set)


class TestPowerSet(unittest.TestCase):

    def test_power_set(self):
        # input_set = ''
        # expected = ['']
        # self.run_test(input_set, expected)
        # input_set = 'a'
        # expected = ['a', '']
        # self.run_test(input_set, expected)
        # input_set = 'ab'
        # expected = ['a', 'ab', 'b', '']
        # self.run_test(input_set, expected)
        # input_set = 'abc'
        # expected = ['a', 'ab', 'abc', 'ac',
        #             'b', 'bc', 'c', '']
        # self.run_test(input_set, expected)
        # input_set = 'aabc'
        # expected = ['a', 'aa', 'aab', 'aabc',
        #             'aac', 'ab', 'abc', 'ac',
        #             'b', 'bc', 'c', '']
        # self.run_test(input_set, expected)
        # print('Success: test_power_set')
        input_set = []
        expected = [[]]
        self.run_test(input_set, expected)
        input_set = ['a']
        expected = [['a'], []]
        self.run_test(input_set, expected)
        input_set = ['a', 'b']
        expected = [['a'], ['a', 'b'], ['b'], []]
        self.run_test(input_set, expected)
        input_set = ['a', 'b', 'c']
        expected = [['a'], ['a', 'b'], ['b'], ['a', 'c'],
                    ['a', 'b', 'c'], ['b', 'c'], ['c'], []]
        self.run_test(input_set, expected)
        print('Success: test_power_set')

    def run_test(self, input_set, expected):
        # combinatoric = Combinatoric()
        # result = combinatoric.find_power_set(input_set)
        # self.assertEqual(result, expected)

        combinatoric = Combinatoric()
        result = combinatoric.find_power_set_recursive(input_set)
        # self.assertEqual(result, expected)
        self.assertEqual(combinatoric.check_result(expected, result), True)
        # result = combinatoric.find_power_set_iterative(input_set)
        # self.assertEqual(result, expected)


def main():
    test = TestPowerSet()
    test.test_power_set()


if __name__ == '__main__':
    main()
