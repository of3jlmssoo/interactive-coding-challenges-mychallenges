"""
[追記]
Problem: Counting Ways of Making ChangeとDetermine the total number of unique ways to make n cents, 
given coins of denominations less than n centsのproblemが同じように思える。
そのため、ここであわせて処理してしまう。


[参照]
https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/

waysは0からNまで
way[0]は1とする(0を満たすのは0の一つのみ)
    => テストの1つ目と考え方が違うがここでは良しとする
    => 狭義の目的はways[N]での数だが、分割するのでways[N-1]以下も考える
コイン1を使って満たせるか？ways[1]-ways[N]
    コインがindexを超えない範囲。コイン1では全インデックスが対象となる
         0 1 2 3 4 5 6 7 8 9 0 1 2
    ways[1,0,0,0,0,0,0,0,0,0,0,0,0]
    ways[1,1,1,1,1,1,1,1,1,1,1,1,1]
    ways[0] = 1 (固定)
    ways[1] = ways[1-1] + ways[1] = 1
    ways[2] = ways[2-1] + ways[2] = 1   コイン合計2を満たすためにコイン1を一枚使う。足りない分をways[2-1]で補足する。
                                        ways[2-1はは一方法しかない。
    ways[12] = ways[12-1] + ways[12] = 1

コイン5を使って満たせるか？ways[1]-ways[N]
    コインがindexを超えない範囲。コイン5では矢印範囲が対象となる。
         0 1 2 3 4 5 6 7 8 9 0 1 2
    ways[1,1,1,1,1,1,1,1,1,1,1,1,1]
                   <------------->
    
    ways[2] = ways[2-1] + ways[2] = 1       1x2

    ways[5] = ways[5-5] + ways[5] = 2
    ways[6] = ways[6-5] + ways[6] = 2
    ways[7] = ways[7-5] + ways[7] = 2       1x7(繰りこし), 1x2(ways[2]+5x1)
    ways[8] = ways[8-5] + ways[8] = 2
    ways[9] = ways[9-5] + ways[9] = 2
    ways[10] = ways[10-5] + ways[10] = 3
    ways[11] = ways[11-5] + ways[11] = 3
    ways[12] = ways[12-5] + ways[12] = 3    ways[12] = 1通り
                                            ways[12-5] = ways[7] => 2通り
                                                            ways[7]
                                                                ways[7] (元々)     => 1 (1x7)
                                                                ways[7-5]= ways[2] => 1 (1x2) 5を1枚使って残り2を満たすのは一通りのみ




        12を満たすためにコイン5を使う
        残りは7
        7を満たすためにコイン5を使う         A 1x2 + 5x1
        残りは2                              A 1x2

         0 1 2 3 4 5 6 7 8 9 0 1 2
    ways[1,1,1,1,1,2,2,2,2,2,3,3,3]


coin 5を処理した時点でcoins[10]がなぜ3か

    10(index)-5(coin)は5。j-c
    10のうち5(coin)が満たされたので残り5。
    ways[5]=2 
    coin 5を前提に2つ方法があるので2を足す

N=12
coins = [1,5,10]
ways = [1] + [0]*N
print(ways)
for c in coins:
    for j in range(1,N+1):
        if c <= j:
            ways[j] = ways[j-c] + ways[j]
    print(f'--- ',ways)
print(ways)

1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 5
1 1 5 5
1 1 10

"""
import unittest

class CoinChanger(object):

    def make_change(self, coins, total):
        # TODO: Implement me

        if total == 0:
            return 0

        ways = [1] + [0]*total
        # print(ways)
        for c in coins:
            for j in range(1,total+1):
                if c <= j:
                    ways[j] = ways[j-c] + ways[j]
        #     print(f'--- ',ways)
        # print(ways)

        n=ways[-1]

        return n

class Challenge(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        self.assertEqual(coin_changer.make_change([1, 2], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 5)
        self.assertEqual(coin_changer.make_change([1, 5, 25, 50], 10), 3)

        """ Problem: Counting Ways of Making Change """
        self.assertEqual(coin_changer.make_change([1, 2], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 100), 884)
        self.assertEqual(coin_changer.make_change(range(1,101), 1000),15658181104580771094597751280645)

        print('Success: test_coin_change')


def main():
    test = Challenge()
    test.test_coin_change()


if __name__ == '__main__':
    main()
