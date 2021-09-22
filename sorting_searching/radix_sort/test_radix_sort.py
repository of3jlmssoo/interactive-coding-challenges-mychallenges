import unittest


class RadixSort(object):

    def sort(self, array, base=10):
        # TODO: Implement me
        # pass
        if array is None:
            raise TypeError(f'Radixsort.sort: arg error {array=}')

        if not array:
            return array

        # エレメントの最大文字数取得
        max_l = max([len(str(s)) for s in array])

        # 0をアペンドして桁数あわせ
        array_s = [str(s).zfill(max_l) for s in array]

        # 10のエレメントをもったリストresultとresult_tmpを初期化
        result = [[] * 1 for i in range(10)]
        result[0] = array_s
        result_tmp = [[] * 1 for i in range(10)]

        """
        処理の流れ
        1. 1の位でグルーピングする。最大10グループに分かれる
        2. 10の位でグルーピングする。最大10グループに分かれる
        3. 100の位でグルーピングする。最大10グループに分かれる

        リストresult
        処理の流れで最大10のグループに分けられる。これら各々を保持するために10のリストを要素とする


        最大桁数回ループする
            resultの最大10の要素各々(outer_i)を処理
                outer_iの各々(inner_i。ソート対象)について処理
                    例題の場合i=2,1,0。i=2の場合1桁目の値を
                    インデックス　int(str(inner_i)[i])　として
                    result_tmpに保存
            resultをresult_tmpで上書き
            result_tmpを初期化
        """
        for i in reversed(range(max_l)):
            for outer_i in result:
                for inner_i in outer_i:
                    result_tmp[int(str(inner_i)[i])].append(inner_i)
            result = result_tmp
            result_tmp = [[] * 1 for i in range(10)]

        # 10の要素からなるリストresultのエレメントを1つのリストにまとめてリターン
        return [int(i) for j in result for i in j]


class TestRadixSort(unittest.TestCase):

    def test_sort(self):
        radix_sort = RadixSort()
        self.assertRaises(TypeError, radix_sort.sort, None)
        self.assertEqual(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        self.assertEqual(radix_sort.sort(array), expected)
        print('Success: test_sort')


def main():
    test = TestRadixSort()
    test.test_sort()


if __name__ == '__main__':
    main()
