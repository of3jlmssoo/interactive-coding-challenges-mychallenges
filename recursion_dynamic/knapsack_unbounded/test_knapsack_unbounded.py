"""
[前提]
Can we replace the items once they are placed in the knapsack?
Yes, this is the unbounded knapsack problem

[参照]
https://www.cs.colostate.edu/~cs475/f15/more_progress/Lec04Knapsack.pdf

- knapsack_01は01なので再利用は無しの前提
- 今回はunboundedなので再利用可の前提
- 再利用のチャンスは参照URLのp10の以下のelseの際
    M[i,w] = max (M[i-1, w], v(i)+M[i-1, w-w(i)])
                                  --------------
- 下線は01のため再利用できず行をi-1でマイナス１している
- 再利用の場合ここをiとすることで同じ行(同じW)での再利用となる(はず)

- self.assertEqual(results, expected_value)が１つ足りないようなので追加する

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
        return result[-1][-1]

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
                                  #   W[i - 1][w - weights[i - 1]])
                                  W[i][w - weights[i - 1]])
                    if W[i][w] == W[i - 1][w]:
                        X[i][w].append(W[i - 1][w])
                    else:
                        X[i][w].append(profits[i - 1])
                        X[i][w].append(W[i - 1][w - weights[i - 1]])

        checkLogStatus(f'W(1)             {W}')
        checkLogStatus(
            f'before return len(profits:{len(profits)}, capacity:{capacity} W[len(profits)][capacity]:{W[len(profits)][capacity]}\n')
        # return W[len(profits)][capacity]
        return W


class TestKnapsack(unittest.TestCase):

    def test_knapsack(self):
        knapsack = Knapsack()
        self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=1, weight=1))
        items.append(Item(label='b', value=3, weight=2))
        items.append(Item(label='c', value=7, weight=4))
        total_weight = 8
        expected_value = 14
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results, expected_value)  # added

        total_weight = 7
        expected_value = 11
        results = knapsack.fill_knapsack(items, total_weight)
        self.assertEqual(results, expected_value)
        print('Success: test_knapsack')


def main():
    test = TestKnapsack()
    test.test_knapsack()


if __name__ == '__main__':
    main()
