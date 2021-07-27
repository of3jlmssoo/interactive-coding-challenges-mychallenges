"""
以下のように場合分けを考えたが大変そうなので、周囲を0で囲むことで例外処理をなくす案とする。

1行目左端   if 1, result+=2
            if right == 0, result+=1
            if down == 0, result+=1

1行目中間   if 1, result+=1
            if left == 0, result+=1
            if right ==0, result+=1
            if down == 0, result+=1

1行目右端   if 1, result+=2
            if left == 0, result+=1
            if down == 0, result+=1
            
最終行左端  if 1, result+=2
            if right == 0, result+=1
            if top == 0, result+=1

最終行中間  if 1, result+=1
            if left == 0, result+=1
            if right ==0, result+=1
            if top == 0, result+=1

最終行右端  if 1, result+=2
            if left == 0, result+=1
            if top == 0, result+=1

中間行左端  if 1, result+=1
            if right == 0, result+=1
            if top == 0, result+=1
            if down == 0, result+=1

中間行中間  
            if left == 0, result+=1
            if right ==0, result+=1
            if top == 0, result+=1
            if down == 0, result+=1

中間行右端  if 1, result+=1
            if left == 0, result+=1
            if top == 0, result+=1
            if down == 0, result+=1



[0,  0,  0,  0]
[0,  1,  2,  3]
[4,  5,  6,  7]
[8,  9, 10, 11]
[12, 13, 14, 15]
は以下のようになる。
[0,  0,  0,  0,  0, 0]
[0,  0,  1,  2,  3, 0]
[0,  4,  5,  6,  7, 0]
[0,  8,  9, 10, 11, 0]
[0, 12, 13, 14, 15, 0]
[0, 0,  0,  0,  0, 0]

col 周り(上から時計回り)
0   0,1,4,0
1   0,2,5,0
2   0,3,6,1
3   0,0,7,2
4   0,5,8,0
5   1,6,9,4
6   2,7,10,5
7   3,0,11,6
8   4,9,12,0
9   5,10,13,8
10  6,11,14,9
11  7,0,15,10
12  8,13,0,0
13  9,14,0,12
14  10,15,0,13
15  11,0,0,14

"""
import unittest


class Solution(object):

    def island_perimeter(self, grid):
        # TODO: Implement me
        # pass
        if grid is None:
            raise TypeError(f'Solution.island_perimeter: gird is None')

        """ 
        [0で囲む]
        0のみのリスト(長さは元のリストの各エレメントの長さ＋2)をnewgridに設定
        gridのデータの前後に0をつけてnewgridに追加
        0のみのリスト(長さは元のリストの長さ＋2)をnewgridの最後のデータとして追加
        """
        newgrid = [[0]*(len(grid[0])+2)]
        for g in grid:
            newgrid.append([0]+g+[0])
        newgrid.append([0]*(len(grid[0])+2))
        # for g in newgrid:
        #     print(g)
        # print('\n')
        # for g in newgrid[1:-1]:
        #     print(g[1:-1])
        # print('\n')

        """
        追加した0は対象外にして順次処理(gridのエレメントを行、列の順に一つずつ処理)
        エレメント(col)が1の場合、周囲の1の数を数えて4から引く(0の数となる)
        0の数をresultに追加する
        """
        result = 0
        for r, row in enumerate(newgrid[1:-1]):
            for c, col in enumerate(row[1:-1]):
                # print(f'{col}, {r}/{c+1}, {r+1}/{c+2}, {r+2}/{c+1}, {r+1}/{c}')
                if col == 1:
                    # print(f'{col}, {newgrid[r][c+1]}, {newgrid[r+1][c+2]}, {newgrid[r+2][c+1]}, {newgrid[r+1][c]}')
                    result = result + (4-[newgrid[r][c+1], newgrid[r+1][c+2], newgrid[r+2][c+1], newgrid[r+1][c]].count(1))

        # print(f'---result {result}')
        return result

class TestIslandPerimeter(unittest.TestCase):

    def test_island_perimeter(self):

        solution = Solution()
        self.assertRaises(TypeError, solution.island_perimeter, None)

        # data = [[0, 1, 2, 3],
        #         [4, 5, 6, 7],
        #         [8, 9, 10, 11],
        #         [12, 13, 14, 15]]
        # data = [[0, 1, 0, 0],
        #         [1, 1, 1, 0],
        #         [0, 1, 0, 0],
        #         [1, 1, 0, 0]]
        # solution.island_perimeter(data)

        data = [[1, 0]]
        expected = 4
        self.assertEqual(solution.island_perimeter(data), expected)
        data = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]
        expected = 16
        self.assertEqual(solution.island_perimeter(data), expected)
        print('Success: test_island_perimeter')


def main():
    test = TestIslandPerimeter()
    test.test_island_perimeter()


if __name__ == '__main__':
    main()
