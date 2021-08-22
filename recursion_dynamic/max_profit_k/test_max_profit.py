"""
[参照]
https://jovian.ai/justcallmerob/max-profit-with-k-transactions

1)  まずmax profitsが10になるコードを作り、この時点ではtransactionsは[]を返す
    2)のため、maxは使わない。
2） その後、transactionsを正しく返すようにする

"""
import sys
import unittest

from enum import Enum  # Python 2 users: Run pip install enum34


class Type(Enum):
    SELL = 0
    BUY = 1


class Transaction(object):

    def __init__(self, type, day, price):
        self.type = type
        self.day = day
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and \
            self.day == other.day and \
            self.price == other.price

    def __repr__(self):
        return str(self.type) + ' day: ' + \
            str(self.day) + ' price: ' + \
            str(self.price)


class StockTrader(object):

    def find_max_profit(self, prices, k):
        # TODO: Implement me
        # pass

        checkargs1 = [prices is None, k is None]
        if any(checkargs1):
            raise TypeError(
                f'StockTrader.find_max_profit: args error prices:s{prices} k:{k}')
        checkargs2 = [prices == [], k == 0]
        if any(checkargs2):
            return []

        self.profits = [[0] * len(prices) for i in range(k + 1)]
        self.combination = [[None] * len(prices) for i in range(k + 1)]
        self.prices = prices
        self.print_profits()

        self.profits[0] = [0] * len(prices)
        self.print_profits()

        for p in self.profits[1:]:
            p[0] = 0
        self.print_profits()

        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                # print(f'i:{i} j:{j}')
                first = self.get_first(i, j)
                second = self.get_second(i, j)
                if first > second:
                    self.profits[i][j] = first
                else:
                    self.profits[i][j] = second
        self.print_profits()

    def get_second(self, i, j):
        result = -sys.maxsize
        for x in range(j):
            if result < (
                    (p1 := -self.prices[x]) + (p2 := self.profits[i - 1][x])):
                result = p1 + p2
        return self.prices[j] + result

    def get_first(self, i, j):
        return self.profits[i][j - 1]

    def print_profits(self):
        # [print(n) for n in self.profits]
        [print(p, c) for p, c in zip(self.profits, self.combination)]
        print('\n')


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        stock_trader = StockTrader()
        self.assertRaises(TypeError, stock_trader.find_max_profit, None, None)
        self.assertEqual(stock_trader.find_max_profit(prices=[], k=0), [])
        # prices = [5, 4, 3, 2, 1]
        k = 3
        # self.assertEqual(stock_trader.find_max_profit(prices, k), (0, []))
        prices = [2, 5, 7, 1, 4, 3, 1, 3]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        # self.assertEqual(profit, 10)
        # self.assertTrue(Transaction(Type.SELL,
        #                             day=7,
        #                             price=3) in transactions)
        # self.assertTrue(Transaction(Type.BUY,
        #                             day=6,
        #                             price=1) in transactions)
        # self.assertTrue(Transaction(Type.SELL,
        #                             day=4,
        #                             price=4) in transactions)
        # self.assertTrue(Transaction(Type.BUY,
        #                             day=3,
        #                             price=1) in transactions)
        # self.assertTrue(Transaction(Type.SELL,
        #                             day=2,
        #                             price=7) in transactions)
        # self.assertTrue(Transaction(Type.BUY,
        #                             day=0,
        #                             price=2) in transactions)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()
