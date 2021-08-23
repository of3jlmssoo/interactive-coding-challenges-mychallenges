"""
[参照]
https://jovian.ai/justcallmerob/max-profit-with-k-transactions

1)  まずmax profitsが10になるコードを作り、この時点ではtransactionsは[]を返す
    2)のため、maxは使わない。
2） その後、transactionsを正しく返すようにする
    必要なデータは
        BUY/SELL
        day
        price
    の3つ
    profits[i][j]=max(①, ②+max(③+④))
    ② price[j] => SELL (day)j (price)prices[j]
    ③ MAX時の-price[x] => BUY (day)x (price)price[x]
    ④ 前のトランザクションでのmax profits

    challangeでのtransactionデータ
    buy day 0 @ 2
    sel day 2 @ 7       profit 5

    buy day 3 @ 1
    sel day 4 @ 4       profit 8

    buy day 6 @ 1
    sel day 7 @ 3       profit 10

self.combination
[None, None, None, None, None, None, None, None]
[None, ['B day', 0, 2, 'S day', 1, 5, 0, 0], ['B day', 0, 2, 'S day', 2, 7, 0, 0], ['B day', 0, 2, 'S day', 3, 1, 0, 0], ['B day', 3, 1, 'S day', 4, 4, 0, 3], ['B day', 3, 1, 'S day', 5, 3, 0, 3], ['B day', 3, 1, 'S day', 6, 1, 0, 3], ['B day', 3, 1, 'S day', 7, 3, 0, 3]]
[None, ['B day', 0, 2, 'S day', 1, 5, 1, 0], ['B day', 0, 2, 'S day', 2, 7, 1, 0], ['B day', 0, 2, 'S day', 3, 1, 1, 0], ['B day', 3, 1, 'S day', 4, 4, 1, 3], ['B day', 3, 1, 'S day', 5, 3, 1, 3], ['B day', 3, 1, 'S day', 6, 1, 1, 3], ['B day', 3, 1, 'S day', 7, 3, 1, 3]]
[None, ['B day', 0, 2, 'S day', 1, 5, 2, 0], ['B day', 0, 2, 'S day', 2, 7, 2, 0], ['B day', 0, 2, 'S day', 3, 1, 2, 0], ['B day', 3, 1, 'S day', 4, 4, 2, 3], ['B day', 3, 1, 'S day', 5, 3, 2, 3], ['B day', 5, 3, 'S day', 6, 1, 2, 5], ['B day', 6, 1, 'S day', 7, 3, 2, 6]]

"""
import sys
import logging
import unittest
from enum import Enum  # Python 2 users: Run pip install enum34

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

        self.prices = prices
        self.k = k

        self.transactions = []

        self.profits = [[0] * len(prices) for i in range(k + 1)]
        self.combination = [
            [None] * len(prices) for i in range(k + 1)
        ]  # tranactionデータを記録する

        self.profits[0] = [0] * len(prices)  # 元々0で作成しているが特定行、特定列を0で明示的に初期化
        for p in self.profits[1:]:
            p[0] = 0
        if not logger.disabled:
            self.print_profits()

        """ 以下の処理を実現
            profits[i][j] = max(profits[i][j-1], prices[j]+max(-prices[x] + profits[i-1][x])) where 0 <= x < j
                                first            second
        """
        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                # print(f'i:{i} j:{j}')
                first = self.get_first(i, j)
                second = self.get_second(i, j)
                """ get_second()内でprofit更新があると上記処理に加えrecord_proc()がコールされてself.combinationに記録する """
                if first > second:
                    self.profits[i][j] = first
                else:
                    self.profits[i][j] = second
        if not logger.disabled:
            self.print_profits()
        """ transactionを作るため register_tx()をコール """
        self.register_tx()
        if not logger.disabled:
            print(f'after search_buy_sell_info  {self.transactions}')
        return self.profits[-1][-1], self.transactions

    def register_tx(self):
        i = self.k
        j = len(self.prices) - 1
        while self.profits[i][j] != 0:
            """ profit=0の状態になるまで繰り返し処理する """
            if not logger.disabled:
                print(f'in while {self.combination[i][j]}')

            """ max profitsの状態から始めてprofit=0まで繰り返す
                class Transaction(object): def __init__(self, type, day, price): """
            self.transactions.append(Transaction(
                self.combination[i][j][0],
                self.combination[i][j][1],
                self.combination[i][j][2]))
            self.transactions.append(Transaction(
                self.combination[i][j][3],
                self.combination[i][j][4],
                self.combination[i][j][5]))

            """ 次の処理すべきデータをセットする """
            i, j = self.search_tx_data(
                self.combination[i][j][6], self.combination[i][j][7])
            # i=self.combination[i][j][6]
            # j=self.combination[i][j][7]

    def search_tx_data(self, i, j):
        """
            0   1   2   3   4   5   6   7
        --+-------------------------------
        0 | 0	0	0	0	0	0	0	0
        1 | 0	3	5	5	5	5	5	5
        2 | 0	3	5	5	8	8	8	8
        3 | 0	3	5	5	8	8	8	10
        上記データの場合、i=3, j=7から始まる
        self.combination[3,7]を見るとi=2, j=6が参照されれている。profitは8。
        この8になった最初の日をindexで探し、その値を新たなjとして返す(i=2,j=4が返される)
        register_tx()ではself.combination[2][4]のデータを処理する。以下同様
        i=1, j=3に行き(profitは5)、次に5になった日を探しi=1, j=2を得る。。。。
        """
        return i, self.profits[i].index(self.profits[i][j])

    def get_second(self, i, j):
        """ 以下の処理のsecondパートを実現
            profits[i][j] = max(profits[i][j-1], prices[j]+max(-prices[x] + profits[i-1][x])) where 0 <= x < j
                                first            second         p1          p2
                                                 prices[j]+result
        """

        result = -sys.maxsize
        for x in range(j):
            if result < (
                    (p1 := -self.prices[x]) + (p2 := self.profits[i - 1][x])):
                self.record_proc(i, j, x)
                result = p1 + p2
        return self.prices[j] + result

    def record_proc(self, i, j, x):
        """ 以下のようなリストを作成する。
            [<Type.BUY: 1>, 6, 1, <Type.SELL: 0>, 7, 3, 2, 6]]

            index
            0 : <Type.BUY: 1>   引き続きのデータがBuyのデータであることｗ表す。無くても順番で処理はできる
            1 : 6               Buyの日付
            2 : 1               Buyのプライス
            3 : <Type.SELL: 0>  引き続きのデータがSellのデータであることｗ表す。無くても順番で処理はできる
            4 : 7               Sellの日付
            5 : 3               Sellのプライス
            6 : 2               前のトランザクションのprofitsのi。以下の④に相当
            7 : 6               前のトランザクションのprofitsのj。以下の④に相当

            profits[i][j]=max(①, ②+max(③+④))
            ② price[j]         => SELL (day)j (price)prices[j]
            ③ MAX時の-price[x] => BUY  (day)x (price)price[x]

        """
        # print(f'---i:{i} j:{j} x:{x} self.combination[i][j]:{self.combination[i][j]} ---')
        # sell_data = [Type.SELL,j,self.prices[j]]
        # buy_data  = [Type.BUY,x,self.prices[x]]
        sell_data = [Type.SELL, j, self.prices[j]]
        buy_data = [Type.BUY, x, self.prices[x]]
        prev_data = [i - 1, x]
        self.combination[i][j] = buy_data + sell_data + prev_data

    def get_first(self, i, j):
        return self.profits[i][j - 1]

    def print_profits(self):
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
        self.assertEqual(profit, 10)
        self.assertTrue(Transaction(Type.SELL,
                                    day=7,
                                    price=3) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                    day=6,
                                    price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                    day=4,
                                    price=4) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                    day=3,
                                    price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                    day=2,
                                    price=7) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                    day=0,
                                    price=2) in transactions)
        print('Success: test_max_profit')

        """ 追加テスト """
        prices = [1, 2, 1, 2, 1, 7]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        self.assertEqual(profit, 8)
        self.assertTrue(Transaction(Type.SELL,
                                    day=1,
                                    price=2) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                    day=0,
                                    price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                    day=3,
                                    price=2) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                    day=2,
                                    price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                    day=5,
                                    price=7) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                    day=4,
                                    price=1) in transactions)

        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()
