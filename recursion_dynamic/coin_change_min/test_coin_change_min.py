"""

[参照]
https://trykv.medium.com/how-to-solve-minimum-coin-change-f96a758ccade

coin change関連では一番読みやすく理解しやすいと感じた。

test_coin_change.pyとの関係
    test_coin_change.py     +
    test_coin_change_min.py -

リストを初期化。サイズはN+1。初期値はinfinity。インデックス0を0に
コイン毎ループ
    0からN+1までループ
    if (リストのインデックス - coin) >= 0
        リスト[リストのインデックス] = math.min(リスト[リストのインデックス], リスト[リストのインデックス-coin]+1)

return リスト[N] if not infinity otherwise return -1

"""
import unittest
import sys

class CoinChanger(object):

    def make_change(self, coins, total):
        # TODO: Implement me
        # pass

        if coins == None or total == None:
            raise TypeError(f'CoinChanger.object.make_change: coins == None or total == None')

        if coins == [] or total==0:
            return 0

        min_coins = [sys.maxsize] * (total+1)
        min_coins[0] = 0

        for c in coins:
            for i in range(total+1):
                if i-c>=0:
                    min_coins[i] = min(min_coins[i], min_coins[i-c]+1)

        # print(min_coins[total])
        return min_coins[total]


class TestCoinChange(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        self.assertRaises(TypeError, coin_changer.make_change, None, None)
        self.assertEqual(coin_changer.make_change([], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 2)
        self.assertEqual(coin_changer.make_change([3, 2, 1], 5), 2)
        self.assertEqual(coin_changer.make_change([3, 2, 1], 8), 3)
        print('Success: test_coin_change')


def main():
    test = TestCoinChange()
    test.test_coin_change()


if __name__ == '__main__':
    main()
