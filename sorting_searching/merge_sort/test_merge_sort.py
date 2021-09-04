"""
[参照]
https://en.wikipedia.org/wiki/Merge_sortのアニメと図

1. リストのエレメントを2つずつ1つのリストにまとめるループ構造を作成
2. まとめたエレメント毎にソート。wikiとは異なるが、まとめたエレメント(これもリスト)から最小値を取り出す処理を繰り返す
"""
import unittest


class MergeSort(object):

    def sort(self, data):
        # TODO: Implement me
        # pass

        if data is None:
            raise TypeError(f'MergeSort.sort: arg error {data=}')

        argchks = [data == [], len(data) == 1]
        if any(argchks):
            return data

        data = [[d] for d in data]
        result_list = []
        while len(result_list) != 1:
            # print(f'1) data={str(data):60} {result_list=}')
            result_list = [i + j for i, j in zip(data[0::2], data[1::2])]
            for i, d in enumerate(result_list):
                tmp_list = []
                while d:
                    tmp_list.append(min(d))
                    d.remove(min(d))
                result_list[i] = tmp_list

            if len(data) % 2:
                result_list = result_list + [data[-1]]

            data = result_list

        return result_list[0]


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        merge_sort = MergeSort()

        print('None input')
        self.assertRaises(TypeError, merge_sort.sort, None)

        print('Empty input')
        self.assertEqual(merge_sort.sort([]), [])

        print('One element')
        self.assertEqual(merge_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(merge_sort.sort(data), sorted(data))

        print('Success: test_merge_sort')

        """ additional tests """
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1, 0]  # 10 elements
        self.assertEqual(merge_sort.sort(data), sorted(data))

        data = [6, 5, 3, 1, 8, 7, 2, 4]
        self.assertEqual(merge_sort.sort(data), sorted(data))

        data = [38, 27, 43, 3, 9, 82, 10]
        self.assertEqual(merge_sort.sort(data), sorted(data))

        print('Success: test_merge_sort2')


def main():
    test = TestMergeSort()
    test.test_merge_sort()


if __name__ == '__main__':
    main()
