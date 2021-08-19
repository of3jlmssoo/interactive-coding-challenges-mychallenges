"""
[参照]
https://medium.com/@hichetanmore/matrix-chain-multiplication-using-dynamic-programming-22a137df955f
https://people.engr.tamu.edu/andreas-klappenecker/csce629-f17/csce411-set6c.pdf
https://home.cse.ust.hk/~dekai/271/notes/L12/L12.pdf

3つ目だけで良い。

"""
import unittest
import sys


class Matrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second


class MatrixMultiplicationCost(object):

    def find_min_cost(self, matrices):
        # TODO: Implement me
        # pass

        if matrices is None:
            raise TypeError(
                f'MatrixMultiplicationCost.find_min_cost: arg error {matrices}')
        if matrices == []:
            return 0

        p = [i.first for i in matrices]
        p = p + [matrices[-1].second]

        M = [[sys.maxsize] * len(p) for i in range(len(matrices) + 1)]

        """ 使わないエリアを0に """
        for j in range(len(matrices) + 1):
            M[0][j] = 0

        for i in range(1, len(matrices) + 1):
            for j in range(i):
                M[i][j] = 0

        """ 左上から右下の対角線を0に"""
        for t in range(len(matrices) + 1):
            M[t][t] = 0

        len_mat = len(matrices)
        limit_of_proc1 = len_mat
        for t in range(1, len_mat):
            for d, i in enumerate(range(1, limit_of_proc1)):
                dd = d + 1
                for ddd, j in enumerate(range(dd, i + t)):
                    # print(f'(t:{t}) i:{i} d:{d} dd:{dd} i+t:{i+t} k:{i+ddd}')
                    # print(f'M[{dd}][{i+t}] = m[{i}][{i+ddd}] + m[{i+ddd+1}][{i+t}] + p[{d}]*p[{i+ddd}]*p[{i+t}]')
                    # print(
                    # f'1st:{M[i][i+ddd]} 2nd:{M[i+ddd+1][i+t]}
                    # 3rd:{p[d]*p[i+ddd]*p[i+t]} ')
                    result = M[i][i + ddd] + M[i + ddd + 1][i + t] + \
                        p[d] * p[i + ddd] * p[i + t]
                    if M[dd][i + t] > result:
                        M[dd][i + t] = result
            limit_of_proc1 -= 1
        return M[1][-1]


class TestMatrixMultiplicationCost(unittest.TestCase):

    def test_find_min_cost(self):
        matrix_mult_cost = MatrixMultiplicationCost()
        self.assertRaises(TypeError, matrix_mult_cost.find_min_cost, None)
        self.assertEqual(matrix_mult_cost.find_min_cost([]), 0)
        matrices = [Matrix(2, 3),
                    Matrix(3, 6),
                    Matrix(6, 4),
                    Matrix(4, 5)]
        expected_cost = 124
        self.assertEqual(
            matrix_mult_cost.find_min_cost(matrices),
            expected_cost)

        """ 追加テスト """
        matrices = [  # 158
            Matrix(5, 4),
            Matrix(4, 6),
            Matrix(6, 2),
            Matrix(2, 7)
        ]
        expected_cost = 158
        self.assertEqual(
            matrix_mult_cost.find_min_cost(matrices),
            expected_cost)

        print('Success: test_find_min_cost')


def main():
    test = TestMatrixMultiplicationCost()
    test.test_find_min_cost()


if __name__ == '__main__':
    main()
