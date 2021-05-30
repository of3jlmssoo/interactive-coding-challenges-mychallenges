""" test_flip_bit.py

Can we assume the input is a 32 bit number? Yes
MAX_BITS = 32

00001111110111011110001111110000
    123456 123 1234   123456 
    6  +  1 + 3 = 10 

00000100111011101111100011111011
     1  123 123 12345   12345 11
            3 + 1 + 5 = 9

00010011101110111110001111101111
   1  123 123 12345   12345 1234
                      5   + 1 + 4 = 10

0を1つだけ1にして1の連続が最大化するケースの1の連続数を返す
連続する場所は記録しなくて良い

"""
import unittest
class Bits(object):

    MAX_BITS = 32

    def flip_bit(self, num):
        # TODO: Implement me
        # pass
        if num == None: raise(TypeError)
        if num == 0: return 1
        if num == -1: return Bits.MAX_BITS

        # print("flip_bit ", bin(num))
        # print("flip_bit ", bin(num)[2:].split('0')) # remove the first two characters
        # print(
        #     [len(ones) for ones in bin(num)[2:].split('0')]
        # )
        ones_len = [len(ones) for ones in bin(num)[2:].split('0')]
        # print("len(ones_len ", len(ones_len), " ones_len", ones_len)
        # max_value = 0
        
        # for l in range(len(ones_len)-1):
        #     if ones_len[l] != 0 and ones_len[l+1] != 0:
        #         if (ones_len[l] + ones_len[l+1]) > max_value:
        #             max_value = ones_len[l] + ones_len[l+1]
       
        # print("max_value ", max_value)

        ones_len_sum = [ones_len[i]+ones_len[i+1] for i in range(len(ones_len)-1) if ones_len[i] and ones_len[i+1] ]
        return max(ones_len_sum)+1

 
# [6, 3, 4, 0, 0, 6, 0, 0, 0, 0]
# max_value  9
 
        return max_value+1
                
                
class TestBits(unittest.TestCase):

    def test_flip_bit(self):
        bits = Bits()
        self.assertRaises(TypeError, bits.flip_bit, None)
        self.assertEqual(bits.flip_bit(0), 1)
        self.assertEqual(bits.flip_bit(-1), bits.MAX_BITS)

        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        # bits.flip_bit(num)
        self.assertEqual(bits.flip_bit(num), expected)

        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        self.assertEqual(bits.flip_bit(num), expected)

        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
       
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()
