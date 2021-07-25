""" ギブアップ

Algorithm
Refer to the Solution Notebook. If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.
のアドバイスに従う。参照したのは以下のサイトなど。

[参照]
https://www.geeksforgeeks.org/subtract-two-numbers-without-using-arithmetic-operators/
https://en.wikipedia.org/wiki/Subtractor
https://daeudaeu.com/arithmetic_operations/
https://github.com/donnemartin/interactive-coding-challenges/blob/master/math_probability/sub_two/sub_two_solution.ipynb

[メモ]
引き算を行う
繰り下げを考慮する

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


class Solution(object):

    def sub_two(self, a, b):
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b
        borrow = (~a & b) << 1
        if borrow != 0:
            return self.sub_two(result, borrow)
        return result


class MySolution(object):

    def sub_two(self, a, b):
        print(f'a:{a}, bin(a):{bin(a)}')
        print(f'b:{b},   bin(b):{bin(b)}')
        if a is None or b is None:
            raise TypeError('a or b cannot be None')
        result = a ^ b  # 排他的論理和（XOR）
        print(f'r:{result}, bin(r):{bin(result)} XOR　排他的論理和')
        print(f'\n')

        borrow = (~a & b) << 1  # aにビット反転。~aは-(a+1)となる値を返す。
        print(f'a:{a}, bin(a):{bin(a)}')
        print(f'~a:{~a}, bin(~a):{bin(~a)}　ビット反転。~aは-(a+1)となる値を返す')
        print(f'b:{b},      bin(b):{bin(b)}')
        print(f'~a&b                :{~a&b} 論理積')
        print(f'(~a&b)<<1:           {(~a&b)<<1}')

        if borrow != 0:
            return self.sub_two(result, borrow)
        return result


class MyTestSubTwo(unittest.TestCase):

    def my_test_sub_two(self):
        solution = MySolution()
        # self.assertEqual(solution.sub_two(7, 5), 2)
        # self.assertEqual(solution.sub_two(-5, -7), 2)
        self.assertEqual(solution.sub_two(-5, 7), -12)
        # self.assertEqual(solution.sub_two(5, -7), 12)

        print('Success: my_test_sub_two')


class TestSubTwo(unittest.TestCase):

    def test_sub_two(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.sub_two, None)
        self.assertEqual(solution.sub_two(7, 5), 2)
        self.assertEqual(solution.sub_two(-5, -7), 2)
        self.assertEqual(solution.sub_two(-5, 7), -12)
        self.assertEqual(solution.sub_two(5, -7), 12)
        print('Success: test_sub_two')


def main():
    test = TestSubTwo()
    test.test_sub_two()

    test = MyTestSubTwo()
    test.my_test_sub_two()


if __name__ == '__main__':
    main()
