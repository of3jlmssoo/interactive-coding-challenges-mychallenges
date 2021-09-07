"""
[基本的な考え方]
適当にpivotの位置を決める
pivotの左側に> pivotがある場合pivotの右側に移す
pivotの右側に< pivotがある場合pivotの左側に移す
(この時点でpivotの左側はpivotより小さいものばかりになっているが順番がソートされていない。
pivotの右側はpivotより大きいものばかりになっているが順番がソートされていない)
以下左半分で同様の処理を行い、右半分でも同様の処理を行う。
アレイの要素が2未満になったらリターンする

"""
import unittest
import numpy as np


class QuickSort(object):

    def sort(self, data):
        # TODO: Implement me
        # pass

        if data is None:
            raise TypeError(f'QuickSort.sort: arg error {data=}')

        if len(data) < 2:
            return data

        idx = len(data) // 2
        left_left, left_right = self.divide_small_large(data[idx], data[0:idx])
        right_left, right_right = self.divide_small_large(
            data[idx], data[idx + 1:])
        # print(f'{data=} {idx=} {data[0:idx]=} {data[idx+1:]}')
        left = left_left + right_left
        right = left_right + right_right

        return self.sort(left) + [data[idx]] + self.sort(right)

    def divide_small_large(self, base_val, arr):

        return [i for i in arr if i <= base_val], \
            [i for i in arr if i > base_val]


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        quick_sort = QuickSort()

        print('None input')
        self.assertRaises(TypeError, quick_sort.sort, None)

        print('Empty input')
        self.assertEqual(quick_sort.sort([]), [])

        print('One element')
        self.assertEqual(quick_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(quick_sort.sort(data), sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort()


if __name__ == '__main__':
    main()
