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


class Grid(object):

    def find_path(self, matrix):
        # TODO: Implement me
        # pass
        if matrix is None or matrix == [[]]:
            return None

        result = self._find_path(matrix, 0, 0)
        # print(result)
        return result

    def _find_path(self, matrix, row, col):
        # pass
        result = []
        max_row = len(matrix)
        max_col = len(matrix[0])

        logger.debug(
            f'(1) row: {row}, col: {col}, max_row: {max_row}, max_col: {max_col}')

        """ 呼び出しパート """
        """ 右方向へ """
        if (col + 1) < max_col and matrix[row][col + 1] == 1:
            result = self._find_path(matrix, row, col + 1)
        """ 下方向へ """
        if (row + 1) < max_row and matrix[row + 1][col] == 1:
            result = self._find_path(matrix, row + 1, col)

        """ returnパート """
        if row == max_row - 1 and col == max_col - 1:
            """ 右下(目的地)にたどり着いた場合は右下(目的地)のrow,colをリターンする """
            logger.debug(f'return part starts {row} and {col}')
            return [(row, col)]
        """ [行き詰まり条件] """
        """ 1) 右端で下が0 right_end_below_zero """
        """ 2) 一番下で右が0 bottom_rigth_zero """
        """ 3) 右も下も0 right_zero_below_zero """
        """ 行き詰まった場合、return [] """
        # if (
        #     ((col + 1 == max_col) and (matrix[row + 1][col] == 0)) or
        #     ((row + 1 == max_row) and (matrix[row][col + 1] == 0)) or
        #     ((row + 1 != max_row) and (col + 1 != max_col) and
        #      (matrix[row + 1][col] == 0) and (matrix[row][col + 1] == 0))
        # ):
        if (self.right_end_below_zero(row, max_row, col, max_col, matrix) or
            self.bottom_rigth_zero(row, max_row, col, max_col, matrix) or
                self.right_zero_below_zero(row, max_row, col, max_col, matrix)):
            logger.debug(f'no more routes {row} and {col}')
            return []

        logger.debug(f'just before last return {row} and {col}')
        if result:
            return [(row, col)] + result

    def right_end_below_zero(self, row, max_row, col, max_col, matrix):
        return ((col + 1 == max_col) and (matrix[row + 1][col] == 0))

    def bottom_rigth_zero(self, row, max_row, col, max_col, matrix):
        return ((row + 1 == max_row) and (matrix[row][col + 1] == 0))

    def right_zero_below_zero(self, row, max_row, col, max_col, matrix):
        return ((row + 1 != max_row) and (col + 1 != max_col) and
                (matrix[row + 1][col] == 0) and (matrix[row][col + 1] == 0))


class TestGridPath(unittest.TestCase):

    def test_grid_path(self):
        grid = Grid()
        self.assertEqual(grid.find_path(None), None)
        self.assertEqual(grid.find_path([[]]), None)
        max_rows = 8
        max_cols = 4
        matrix = [[1] * max_cols for _ in range(max_rows)]
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[3][0] = 0
        matrix[4][2] = 0
        matrix[5][3] = 0
        matrix[6][1] = 0
        matrix[6][3] = 0
        matrix[7][1] = 0
        result = grid.find_path(matrix)
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2),
                    (7, 2), (7, 3)]
        self.assertEqual(result, expected)
        matrix[7][2] = 0
        result = grid.find_path(matrix)
        self.assertEqual(result, None)
        print('Success: test_grid_path')


def main():
    test = TestGridPath()
    test.test_grid_path()


if __name__ == '__main__':
    main()
