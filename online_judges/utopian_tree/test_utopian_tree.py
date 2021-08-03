"""
春倍、夏+1m

0          1

1          2    = 1*2 
2          3

3          6    = 3*2 = (2+1)*2                                                 = (1*2+1)*2                          
4          7

5          14   = 7*2 = (6+1)*2 = ((3*2)+1)*2                                   = (((1*2+1)*2)+1)*2
6          15

7           30  = 15*2 = (14+1)*2 = (7*2+1)*2 = ((3*2+1)*2+1)*2                 = (((1*2+1)*2+1)*2+1)*2
8           31

9           62  = 31*2 = (15*2+1)*2 = ((7*2+1)*2+1)*2 = (((3*2+1)*2+1)*2+1)*2   = ((((1*2+1)*2+1)*2+1)*2+1)*2
10          63


偶数で考える。例えば10
(1*2+1)を10/2=5回繰り返す

奇数の場合1足した偶数で考え、結果から1引く

"""
import unittest


class Solution(object):

    def calc_utopian_tree_height(self, cycles):
        # TODO: Implement me
        # pass


        adj = 0
        if cycles % 2:
            adj = 1
        
        repeat_time = int((cycles + adj)/2)
        # print(f'cycles:{cycles}, repeat_time:{repeat_time}')

        x=1
        for i in range(repeat_time):
            x=self.calc_height(x)

        if adj:
            return x-1
        else:
            return x


    def calc_height(self,x):
        return (x*2+1)


class TestUtopianTree(unittest.TestCase):

    def test_utopian_tree(self):
        solution = Solution()
        # self.assertEqual(solution.calc_utopian_tree_height(0), 1)
        # self.assertEqual(solution.calc_utopian_tree_height(1), 2)
        # self.assertEqual(solution.calc_utopian_tree_height(4), 7)

        self.assertEqual(solution.calc_utopian_tree_height(15), 510)
        self.assertEqual(solution.calc_utopian_tree_height(14), 255)
        self.assertEqual(solution.calc_utopian_tree_height(13), 254)
        self.assertEqual(solution.calc_utopian_tree_height(12), 127)
        self.assertEqual(solution.calc_utopian_tree_height(11), 126)
        self.assertEqual(solution.calc_utopian_tree_height(10), 63)

        self.assertEqual(solution.calc_utopian_tree_height(9), 62)
        self.assertEqual(solution.calc_utopian_tree_height(8), 31 )
        self.assertEqual(solution.calc_utopian_tree_height(7), 30)
        self.assertEqual(solution.calc_utopian_tree_height(6), 15)
        self.assertEqual(solution.calc_utopian_tree_height(5), 14)
        self.assertEqual(solution.calc_utopian_tree_height(4), 7)
        self.assertEqual(solution.calc_utopian_tree_height(3), 6)
        self.assertEqual(solution.calc_utopian_tree_height(2), 3)
        self.assertEqual(solution.calc_utopian_tree_height(1), 2)
        self.assertEqual(solution.calc_utopian_tree_height(0), 1)


        print('Success: test_utopian_tree')


def main():
    test = TestUtopianTree()
    test.test_utopian_tree()


if __name__ == '__main__':
    main()
