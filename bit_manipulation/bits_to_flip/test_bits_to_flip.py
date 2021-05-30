""" test_bits_to_flip.py


"""
import unittest

class Bits(object):
    def bits_to_flip(self, a: int, b: int) -> int:
        if a == None or b == None: raise(KeyError)

        return len( [(c1, c2) for c1, c2 in zip(self.bin_to_ten(bin(a)), self.bin_to_ten(bin(b))) if c1 != c2]  )

    def bin_to_ten(self, bin_output: str):
        result = [bin_output, bin_output[0:2]+'0'*(10-len(bin_output))+bin_output[2:]]
        return result[len(bin_output) < 10]

class myTestBits(unittest.TestCase):

    def test_bits(self):
        bits = Bits()
        a = int('11101', base=2)
        b = int('01111', base=2)
        print("return from bits_to_flip ", bits.bits_to_flip(a, b))

        with self.assertRaises(KeyError):
            bits.bits_to_flip(a, None)
        with self.assertRaises(KeyError):
            bits.bits_to_flip(None, b)
        with self.assertRaises(KeyError):
            bits.bits_to_flip(None, None)


class TestBits(unittest.TestCase):

    def test_bits_to_flip(self):
        bits = Bits()
        a = int('11101', base=2)
        b = int('01111', base=2)
        expected = 2
        self.assertEqual(bits.bits_to_flip(a, b), expected)
        print('Success: test_bits_to_flip')


def main():
    test = TestBits()
    test.test_bits_to_flip()

    mytest = myTestBits()
    mytest.test_bits()



class TestBits(unittest.TestCase):

    def test_bits_to_flip(self):
        bits = Bits()
        a = int('11101', base=2)
        b = int('01111', base=2)
        expected = 2
        self.assertEqual(bits.bits_to_flip(a, b), expected)
        print('Success: test_bits_to_flip')


def main():
    test = TestBits()
    test.test_bits_to_flip()

    mytest = myTestBits()
    mytest.test_bits()



if __name__ == '__main__':
    main()
