"""
- インプットとなるリスト[8, 5, 3, 2, 1]の値は株価
- インデックス0から時系列になっている
- まず買い。その後売りの順。空売りは考えなくて良い。手数料も。
"""
from typing import Type
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


class Solution(object):

    def find_max_profit(self, prices):
        # TODO: Implement me
        # pass

        if prices is None:
            raise TypeError(f'Solution.find_max_profit: prices is None')
        if prices == []:
            raise ValueError(f'Solution.find_max_profit: prices is []')

        """ forループで順に処理。pricesの場合時系列データで、このデータに対し買いと売りが発生するため
            [8, 5, 3, 2, 1]の場合4回のループになる。
            maxesには各ループでの最大値(max profit)を納め、return max(maxes)する

            lambdaで利益を算出
            yの内包表記で8(買い)の場合5以降で売りとなるためprices[prices.index(k) + 1:]

        """
        maxes = []
        for k in prices[:-1]:
            maxes.append(max(list(map(lambda x: x - k,
                                      [y for y in prices[prices.index(k) + 1:]]))))
            if not logger.disabled:
                print((list(map(lambda x: x - k,
                            [y for y in prices[prices.index(k) + 1:]]))))
        return max(maxes)


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_max_profit, None)
        self.assertRaises(ValueError, solution.find_max_profit, [])
        self.assertEqual(solution.find_max_profit([8, 5, 3, 2, 1]), -1)
        self.assertEqual(solution.find_max_profit([5, 3, 7, 4, 2, 6, 9]), 7)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()
