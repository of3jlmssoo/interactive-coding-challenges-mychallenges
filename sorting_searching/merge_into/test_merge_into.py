"""
[前提]
Webと.pyとでmerge_intoの引数が異なるので.pyにあわせる形に修正
self.assertRaises(呼び出し元)の引数変更

"""
import copy
import unittest


class Array(object):

    def merge_into(self, source, dest, source_end_index):
        #   def merge_into(self, source, dest, source_end_index, dest_end_index):
        # TODO: Implement me
        # pass

        chkargs = [source is None, dest is None, source_end_index is None]
        if any(chkargs):
            raise TypeError(
                f'arg error Array.merge_into: {source=} {dest=} {source_end_index=}')

        chkargs = [source == -1, dest == -1, source_end_index == -1]
        if any(chkargs):
            raise ValueError(
                f'arg error Array.merge_into: {source=} {dest=} {source_end_index=}')

        self.result_list = [r for r in source if r is not None]

        for q in dest:
            if sum(tmp_list := [1 if q < d else 0 for d
                                in self.result_list]) == 0:
                self.result_list.append(q)
            else:
                # idx = tmp_list.index(1)
                self.result_list.insert(tmp_list.index(1), q)
            # print(f'{q=} {self.result_list=} \n')

        return self.result_list


class TestArray(unittest.TestCase):

    def test_merge_into(self):
        array = Array()
        # self.assertRaises(TypeError, array.merge_into, None, None, None, None)
        # self.assertRaises(ValueError, array.merge_into, [1], [2], -1, -1)
        self.assertRaises(TypeError, array.merge_into, None, None, None)
        self.assertRaises(ValueError, array.merge_into, [1], [2], -1)
        a = [1, 2, 3]
        # self.assertEqual(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        self.assertEqual(array.merge_into(a, [], len(a)), [1, 2, 3])
        a = [1, 2, 3]
        # self.assertEqual(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        self.assertEqual(array.merge_into(a, [], len(a)), [1, 2, 3])
        a = [1, 3, 5, 7, 9, None, None, None]
        b = [4, 5, 6]
        expected = [1, 3, 4, 5, 5, 6, 7, 9]
        # self.assertEqual(array.merge_into(a, b, 5, len(b)), expected)
        self.assertEqual(array.merge_into(a, b, 5), expected)
        print('Success: test_merge_into')


def main():
    test = TestArray()
    test.test_merge_into()


if __name__ == '__main__':
    main()
