
"""
fib_dynamicについては、https://trykv.medium.com/how-to-solve-minimum-coin-change-f96a758ccade 
で紹介されたQuoraの引用に基づき以下のように考える。
・前の計算結果を(どこかに)保持しておく
・次の計算はこの計算結果を利用する

(1) クラスのインスタンスで計算結果をとっておく or
(2) def fib_recursive(self, n)で計算結果をとっておきdef _fibd()がそれを利用する
(3) def _fibd()の中で計算結果をとっておく
のいずれかがある。
(1)は他にiterativeとかrecursiveがあるなかでdynamicだけが使うインスタンス変数を作ることになる
(3)はiterativeと似る
よって(2)とする

"""
import unittest

class Math(object):
    """               0  1  2  3  4  5  6  7   8   9     """
    """ Fib sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... """


    def fib_iterative(self, n):
        # TODO: Implement me
        # pass
        if n ==0 or n==1:
            return n
        minus_two = 0
        minus_one = 1
        for i in range(2,n+1):
            result = minus_two + minus_one
            minus_two = minus_one
            minus_one = result
        return result

    def fib_recursive(self, n):
        # TODO: Implement me
        # pass
        result = 0

        if n>= 2:
            result = self._fibr(n-2) + self._fibr(n-1)
        elif n==0 or n==1:
            result = self._fibr(n)

        return result
    
    def _fibr(self, i):
        if i == 0 or i == 1:
            # print(f'{i} will be returned')
            return i
        return self._fibr(i - 2) + self._fibr(i - 1)    

    def fib_dynamic(self, n):
        # TODO: Implement me
        # pass
        fib_nums = []
        for i in range(n + 1):
            fib_nums.append(self._fibd(i, fib_nums))
            # print(f'fib_nums:{fib_nums}')

        # print(f'-----------------------{fib_nums}')
        return fib_nums[-1]

    def _fibd(self, i, lst):
        # print(f'_fibd called {i}, lst:{lst}')
        if i == 0 and len(lst) == 0:
            # print('then')
            return 0
        elif i == 1 and len(lst) == 1:
            # print('elif')
            return 1
        elif i >= 2:
            # print('else')
            return lst[-2] + lst[-1]
        

class TestFib(unittest.TestCase):

    def test_fib(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        self.assertEqual(result, expected)
        print('Success: test_fib')


def main():
    test = TestFib()
    math = Math()
    test.test_fib(math.fib_recursive)
    test.test_fib(math.fib_dynamic)
    test.test_fib(math.fib_iterative)


if __name__ == '__main__':
    main()

    
