import unittest


class Solution(object):

    def fizz_buzz(self, num):
        # TODO: Implement me
        # pass
        if num == None: raise TypeError(f'num is None')        
        if num == 0: raise ValueError(f'0 is specified(valueError)')

        result = []
        for i in range(1,num+1):
            result.append(str(i))
            if i%3 == 0: result[i-1] = 'Fizz'
            if i%5 == 0: result[i-1] = 'Buzz'
            if i%3 == 0 and i%5 == 0: result [i-1]= 'FizzBuzz'
        return result

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)

        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
