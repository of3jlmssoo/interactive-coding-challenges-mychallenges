"""
[参照]
(1) https://en.wikipedia.org/wiki/Knapsack_problem
(2) https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
(3) https://www.cs.colostate.edu/~cs475/f15/more_progress/Lec04Knapsack.pdf

- (2)のjavaのコードを参考にbasic、top-downを各々basicsol.py、topdown.pyでpython化
- bottom-upについては(3)のpseudocodeをpython化

- topdown.py、bottomup.pyのロジックをポーティング
- まずトップダウンをテストして次にボトムアップをテストする
- bottom upについては、total valueを最大化するitemsをリスト形式で返すように修正が必要
    - Wを更新する際Xの同じ位置にアペンドする

          w
          0  1  2  3  4  5  6    7  8
 [ P W i 0 [0, 0, 0, 0, 0, 0, 0,   0, 0],
i  2 2 0 1 [0, 0, 2, 2, 2, 2, 2,   2, 2],
   4 2 1 2 [0, 0, 4, 4, 6, 6, 6,   6, 6],
   6 4 2 3 [0, 0, 4, 4, 6, 6, 10, 10, 12],
   9 5 3 4 [0, 0, 4, 4, 6, 9, 10, 13, 13]]

i=4 & w=8
    else max(
        W[3][8]                     12


        profits[i-1] + W[i-1][w-weights[i-1]]
        profits[4-1]
        profits[3] = 9
                        W[4-1][8-weights[4-1]]
                        W[3][8-weights[3]]
                        W[3][8-5]
                        W[3][3] = 4
                    9 + 4 =13


    )

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


class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


def checkLogStatus(logmsg, opt=''):
    if not logger.disabled:
        if opt == 'end':
            print(logmsg, end='')
        else:
            print(logmsg)


class KnapsackTopDown(object):

    def fill_knapsack(self, input_items, total_weight):
        # TODO: Implement me
        # pass
        argscheck1 = [input_items is None and total_weight is None]
        if any(argscheck1):
            raise TypeError(
                f'Knapsack.fill_kanpsack. arg error. {input_items} {total_weight} ')

        argscheck2 = [input_items == 0, total_weight == 0]
        if any(argscheck2):
            return 0

        profits = [i.value for i in input_items]
        weights = [i.weight for i in input_items]
        # print(profits,weights,total_weight)
        return self.solveks(profits, weights, total_weight)

    def solveks(self, profits, weights, capacity):
        dp = [[None for j in range(capacity + 1)]
              for i in range(len(profits) + 1)]
        return self.ksr(dp, profits, weights, capacity, 0)

    def ksr(self, dp, profits, weights, capacity, currentindex):
        if capacity <= 0 or currentindex >= len(profits):
            return 0
        if(dp[currentindex][capacity] is not None):
            return dp[currentindex][capacity]
        result1 = 0
        if (weights[currentindex] <= capacity):
            result1 = profits[currentindex] + self.ksr(
                dp, profits, weights, capacity - weights[currentindex], currentindex + 1)
        result2 = self.ksr(dp, profits, weights, capacity, currentindex + 1)

        dp[currentindex][capacity] = max(result1, result2)

        # print(f'will return {dp[currentindex][capacity]}')
        checkLogStatus(f'will return {dp[currentindex][capacity]}')
        return dp[currentindex][capacity]


class Knapsack(object):

    def fill_knapsack(self, input_items, total_weight):
        # TODO: Implement me
        # pass
        argscheck1 = [input_items is None and total_weight is None]
        if any(argscheck1):
            raise TypeError(
                f'Knapsack.fill_kanpsack. arg error. {input_items} {total_weight} ')

        argscheck2 = [input_items == 0, total_weight == 0]
        if any(argscheck2):
            return 0

        profits = [i.value for i in input_items]
        weights = [i.weight for i in input_items]
        # return self.solveksbu(profits, weights, total_weight)
        result = self.solveksbu(profits, weights, total_weight)
        checkLogStatus(
            f'result from self.solveksbu {result}\n{result[-1][-1]}')
        # return result[-1][-1]
        return self.findItemfromvalue(input_items, result[-1][-1])
        # print(result[0].label)
        # print(result[1].label)

    def findItemfromvalue(self, input_items, lst):
        # result = []
        # for l in lst:
        #     for i in input_items:
        #         if l == i.value:
        #             result.append(i)
        #             continue
        # return result
        result2 = [v for v in input_items[::-1] if v.value in lst]
        # print(result, result2)
        return result2

    def solveksbu(self, profits, weights, capacity):
        checkLogStatus(
            f'solveksbu() args: P: {profits}, W: {weights}, C: {capacity}')
        if (capacity <= 0 or len(profits) == 0 or len(weights) != len(profits)):
            return 0

        W = [[None for j in range(capacity + 1)]
             for i in range(len(profits) + 1)]
        X = [[[] for j in range(capacity + 1)]
             for i in range(len(profits) + 1)]
        # print('W(0) ', W)
        # print('X(0) ', X)
        checkLogStatus(f'W(0) initialized:{W}\n')
        checkLogStatus(f'X(0) initialized:{X}\n')

        for w in range(capacity + 1):
            W[0][w] = 0
        checkLogStatus(f'W[0][x] updated :{W}\n')

        for i in range(1, len(profits) + 1):
            for w in range(capacity + 1):
                checkLogStatus(
                    f'second loop started. i:{i}, w:{w} --- ', 'end')
                if weights[i - 1] > w:
                    checkLogStatus(
                        f'then: weights[i-1]:{weights[i-1]} > w:{w} --- ', 'end')
                    checkLogStatus(f'W[{i}][{w}] = W[{i-1}][{w}]')
                    W[i][w] = W[i - 1][w]
                    X[i][w].append(W[i - 1][w])
                else:
                    checkLogStatus(
                        f'else:                          W[{i}][{w}] = max(W[{i-1}][{w}], profits[{i-1}]+W[{i-1}][{w}-weights[{i-1}]]) --- max( {W[i-1][w]}, {profits[i-1]}+{W[i-1][w-weights[i-1]]} ) ')
                    W[i][w] = max(W[i - 1][w], profits[i - 1] +
                                  W[i - 1][w - weights[i - 1]])
                    if W[i][w] == W[i - 1][w]:
                        X[i][w].append(W[i - 1][w])
                    else:
                        X[i][w].append(profits[i - 1])
                        X[i][w].append(W[i - 1][w - weights[i - 1]])

        checkLogStatus(f'W(1)             {W}')
        checkLogStatus(
            f'before return len(profits:{len(profits)}, capacity:{capacity} W[len(profits)][capacity]:{W[len(profits)][capacity]}\n')
        # return W[len(profits)][capacity]
        return X


class TestKnapsack(unittest.TestCase):

    def test_knapsack_bottom_up(self):
        knapsack = Knapsack()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results[0].label, 'd')
        self.assertEqual(results[1].label, 'b')
        total_value = 0
        for item in results:
            total_value += item.value
        self.assertEqual(total_value, expected_value)
        print('Success: test_knapsack_bottom_up')

    def test_knapsack_top_down(self):
        knapsack = KnapsackTopDown()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        self.assertEqual(
            knapsack.fill_knapsack(
                items,
                total_weight),
            expected_value)
        print('Success: test_knapsack_top_down')


def main():
    test = TestKnapsack()
    test.test_knapsack_bottom_up()
    test.test_knapsack_top_down()


if __name__ == '__main__':
    main()
