"""
はじめ課題の趣旨が理解できなかった。
solutionやstackoverflowを読み、以下のように理解した。
https://stackoverflow.com/a/1878849

- ソートされているのであれば、valが中にあるかどうか判断するのは容易
- arrayをインデックスmidで分割する
- 右半分、左半分各々でソートされているかどうか判断する
- ソートされていれば、その際の開始 < val < その際の終りという容易な
  判定を行い、範囲の絞り込みを継続する
- なければ反対側
- もちろんどちらもソートされていないケースもある
という流れで進めるつもりでいたが、まず、
1. arrayを2つに分割するidxを生成
2. 分割した2つのarrayを対象に再帰呼び出し
3. return条件は、data[idx] == val: か start >= end: のいずれか
で骨組みを作成した(wrk.py)。
wrk.pyはarrayを最小単位まで正しく処理できるか確認するためにstart >= end:のみ設定しdata[idx] == val:は設定していない。
wrk2.pyでdata[idx] == val:を設定し、かつ、再帰呼び出しの結果をreturnするように設定を行った。
ここで動くようになったため、「その際の開始 < val < その際の終り」の条件判定は省略することにした。

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
logger.disabled = False


class Array(object):

    def search_sorted_array(self, array, val):
        # TODO: Implement me
        # pass
        chkargs = [array is None, val is None]
        if any(chkargs):
            raise TypeError(f'Array.search_sorted_array: arg error')

        return self._search_sorted_array(array, val, 0, len(array) - 1)

    def _search_sorted_array(self, data, val, start, end):

        idx = start + (end - start) // 2
        logger.debug(
            f'_search_sorted_array called: {data[0:1]=} {val=} {start=} {end=} {idx=} ')
        if data[idx] == val:
            logger.debug(f'1) return {idx=}')
            return idx

        if start >= end:
            if data[start] == val:
                logger.debug(f'2) return {start=}')
                return start
            if data[end] == val:
                logger.debug(f'3) return {end=}')
                return end
            logger.debug(f'4) return None ')
            return None

        if (result := self._search_sorted_array(
                data, val, start, idx - 1)) is not None:
            return result
        return self._search_sorted_array(data, val, idx + 1, end)


class TestArray(unittest.TestCase):

    def test_search_sorted_array(self):
        array = Array()
        # self.assertRaises(TypeError, array.search_sorted_array, None)
        self.assertRaises(TypeError, array.search_sorted_array, None, None)
        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)
        self.assertEqual(array.search_sorted_array([3, 1, 2], 0), None)
        data = [10, 12, 14, 1, 3, 5, 6, 7, 8, 9]
        self.assertEqual(array.search_sorted_array(data, val=1), 3)
        data = [1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(array.search_sorted_array(data, val=2), 2)
        print('Success: test_search_sorted_array')


def main():
    test = TestArray()
    test.test_search_sorted_array()


if __name__ == '__main__':
    main()
