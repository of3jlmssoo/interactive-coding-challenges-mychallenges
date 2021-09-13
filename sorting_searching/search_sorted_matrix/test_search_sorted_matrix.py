"""
これで良いのか？？？
"""
import unittest


class SortedMatrix(object):

    def find_val(self, matrix, val):
        # TODO: Implement me
        # pass

        chkargs = [matrix is None, val is None]
        if any(chkargs):
            raise TypeError(f'SortedMatrix.find_val: arg error')


        row = None
        col = None
        # for i, mtrx in enumerate(matrix):
        #     if val in mtrx:
        #         col = mtrx.index(val)
        #         row = i
        # if row != None and col != None:
        #     return (row, col)
        # else:
        #     return None
        mtrx = [(h, i.index(val)) for h, i in enumerate(matrix) if val in i]
        return mtrx[0] if mtrx else None
class TestSortedMatrix(unittest.TestCase):

    def test_find_val(self):
        matrix = [[20, 40, 63, 80],
                  [30, 50, 80, 90],
                  [40, 60, 110, 110],
                  [50, 65, 105, 150]]
        sorted_matrix = SortedMatrix()
        self.assertRaises(TypeError, sorted_matrix.find_val, None, None)
        self.assertEqual(sorted_matrix.find_val(matrix, 1000), None)
        self.assertEqual(sorted_matrix.find_val(matrix, 60), (2, 1))
        print('Success: test_find_val')


def main():
    test = TestSortedMatrix()
    test.test_find_val()


if __name__ == '__main__':
    main()
