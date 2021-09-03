"""
[参照]
https://en.wikipedia.org/wiki/Insertion_sort のアニメ

result_list : ソート済みのリスト
tmp_list :　その際のデータとresult_listを比較した結果を保管

dataのデータを順に処理
データとresult_listを比較し大きい場合1、小さい場合0
1が無い場合result_istにappend
1がある場合tmp_listの最初の1の位置をとって、result_listのその位置に追加


"""
import unittest
from collections import deque


class InsertionSort(object):

    def __init__(self) -> None:
        # self.d = deque()
        self.result_list = []

    def sort(self, data):
        # TODO: Implement me
        # pass
        if data is None:
            raise TypeError(f'InsertionSort.sort: arg error {data=}')

        if len(data) <= 1:
            return data

        # print(f'{data=}')
        # self.queue_append(data)

        # for q in self.d:
        for q in data:
            # tmp_list = [1 if q < d else 0 for d in self.result_list]
            # if sum(tmp_list) == 0:
            if sum(tmp_list := [1 if q < d else 0 for d
                                in self.result_list]) == 0:
                self.result_list.append(q)
            else:
                # idx = tmp_list.index(1)
                self.result_list.insert(tmp_list.index(1), q)
            # print(f'{q=} {self.result_list=} \n')

        return self.result_list

    def queue_append(self, data):
        for i in data:
            self.d.append(i)


class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        insertion_sort = InsertionSort()

        print('None input')
        self.assertRaises(TypeError, insertion_sort.sort, None)

        print('Empty input')
        self.assertEqual(insertion_sort.sort([]), [])

        print('One element')
        self.assertEqual(insertion_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(insertion_sort.sort(data), sorted(data))

        print('Success: test_insertion_sort')


def main():
    test = TestInsertionSort()
    test.test_insertion_sort()


if __name__ == '__main__':
    main()
