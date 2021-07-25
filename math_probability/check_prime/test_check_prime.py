"""
[参考]
https://www.educative.io/courses/introduction-to-computers-and-programming/g2l3zmBPqxG
"""
import unittest


class Math(object):

    def check_prime(self, num):
        # TODO: Implement me
        # pass

        if num is None or not isinstance(num, int):
            raise TypeError(f'Math.check_prime: {num}')

        if num < 2:
            return False

        # if num > 1:
        #     for i in range(2, num // 2):
        #         if (num % i) == 0:
        #             print(num, "is not a prime number")
        #             break
        #         else:
        #             print(num, "is a prime number")
        # else:
        #     print(num, "is not a prime number")

        i = 2
        result = True
        while i <= num / 2:
            rem = num % i
            if rem != 0:
                i = i + 1
            else:
                result = False
                break
        return result


class TestMath(unittest.TestCase):

    def test_check_prime(self):
        math = Math()
        self.assertRaises(TypeError, math.check_prime, None)
        self.assertRaises(TypeError, math.check_prime, 98.6)
        self.assertEqual(math.check_prime(0), False)
        self.assertEqual(math.check_prime(1), False)
        self.assertEqual(math.check_prime(97), True)
        self.assertEqual(math.check_prime(4), True)
        print('Success: test_check_prime')


def main():
    test = TestMath()
    test.test_check_prime()


if __name__ == '__main__':
    main()
