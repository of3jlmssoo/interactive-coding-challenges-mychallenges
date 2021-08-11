"""
[参照]
(1) https://en.wikipedia.org/wiki/Knapsack_problem
(2) https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
(3) https://www.cs.colostate.edu/~cs475/f15/more_progress/Lec04Knapsack.pdf

- (2)のjavaのコードを参考にbasic、top-down、bottom-upを各々basicsol.py、topdown.pyをpython化
- bottom-upについては(3)のpseudocodeをpython化
- topdown.py、bottomup.pyのロジックをポーティング

- まずトップダウンをテストして次にボトムアップをテストする
"""


import unittest


class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


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

        # print('P:', profits, 'W:', weights, 'C:', total_weight)
        # if (total_weight <= 0 or len(profits) == 0 or len(weights) !=
        # len(profits)):
            return 0
        # print('P:', profits, 'W:', weights, 'C:', total_weight)

        # n = len(profits)
        n = len(input_items)
        print("n iiiisssssss ", n)
        W = [[None for j in range(total_weight + 1)]
             for i in range(len(input_items) + 1)]
        print('W(0) ', W)

        for w in range(total_weight + 1):
            W[0][w] = 0

        print('W(1) ', W)

        for i in range(1, len(input_items) + 1):
            for w in range(total_weight + 1):
                print(f'i:{i}, w:{w} --- ', end='')
                # if weights[i - 1] > w:
                if input_items[i - 1].weight > w:
                    # print(
                    #     f'then: weights[i-1]:{weights[i-1]} > w:{w} --- ',
                    #     end='')
                    print(f'W[{i}][{w}] = W[{i-1}][{w}]')
                    W[i][w] = W[i - 1][w]
                else:
                    # print(
                    # f'else:                          W[{i}][{w}] =
                    # max(W[{i-1}][{w}],
                    # profits[{i-1}]+W[{i-1}][{w}-weights[{i-1}]]) --- max(
                    # {W[i-1][w]}, {profits[i-1]}+{W[i-1][w-weights[i-1]]} ) ')
                    W[i][w] = max(W[i - 1][w], input_items[i - 1].value +
                                  W[i - 1][w - input_items[i - 1].weight])
                    # W[i][w] = max(W[i-1][w], profits[i-1]+W[i][w-weights[i-1]])

        print('W(2) ', W)
        # print(f'{len(profits)}, {total_weight}')
        return W[len(input_items)][total_weight]


class TestKnapsack(unittest.TestCase):

    def test_knapsack_bottom_up(self):
        knapsack = Knapsack()
        # self.assertRaises(TypeError, knapsack.fill_knapsack, None, None)
        # self.assertEqual(knapsack.fill_knapsack(0, 0), 0)
        # items = []
        # items.append(Item(label='a', value=2, weight=2))
        # items.append(Item(label='b', value=4, weight=2))
        # items.append(Item(label='c', value=6, weight=4))
        # items.append(Item(label='d', value=9, weight=5))
        # total_weight = 8
        # expected_value = 13
        # results = knapsack.fill_knapsack(items, total_weight)
        # self.assertEqual(results[0].label, 'd')
        # self.assertEqual(results[1].label, 'b')
        # total_value = 0
        # for item in results:
        #     total_value += item.value
        # self.assertEqual(total_value, expected_value)
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
