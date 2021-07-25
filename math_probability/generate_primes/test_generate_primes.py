import unittest
from test_check_prime import Math


class PrimeGenerator(object):

    def generate_primes(self, max_num):
        # TODO: Implement me
        # pass

        result = []

        if max_num is None or not isinstance(max_num, int):
            raise TypeError(f'Math.check_prime: {max_num}')

        m = Math()
        for i in range(max_num):
            # print(i, m.check_prime(i))
            result = result + [m.check_prime(i)]

        return result


class TestMath(unittest.TestCase):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        self.assertRaises(TypeError, prime_generator.generate_primes, None)
        self.assertRaises(TypeError, prime_generator.generate_primes, 98.6)

        prime_generator.generate_primes(20)

        self.assertEqual(prime_generator.generate_primes(20),
                         [False,
                          False,
                          True,
                          True,
                          False,
                          True,
                          False,
                          True,
                          False,
                          False,
                          False,
                          True,
                          False,
                          True,
                          False,
                          False,
                          False,
                          True,
                          False,
                          True])
        print('Success: generate_primes')


def main():
    test = TestMath()
    test.test_generate_primes()


if __name__ == '__main__':
    main()
