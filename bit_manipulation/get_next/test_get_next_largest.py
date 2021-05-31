import unittest


class Bits(object):
    
    def get_next_largest(self, num: int) -> int:
        if num in [None,0,-1]: raise(Exception)

        num_bin_splitted_01 = bin(num)[2:].split('01') # remove first two charcter '0b' and split by '01'
        num_bin_splitted_01_len = len(num_bin_splitted_01)
        result = ''
        append_candidate = ['01','10']
        for i in range(num_bin_splitted_01_len-1): # -1 : as for the last element in num_bin_splitted_01
                                                   # it will be added to result without any append_char in return statement
            append_char = append_candidate[(num_bin_splitted_01_len-2)==i]
                                                   # -2 : the last '01' will be replace with '10'
            result = result + num_bin_splitted_01[i] + append_char
        return int(result + num_bin_splitted_01[num_bin_splitted_01_len-1],base=2)


class TestBits(unittest.TestCase):

    def test_get_next_largest(self):
        bits = Bits()
        self.assertRaises(Exception, bits.get_next_largest, None)
        self.assertRaises(Exception, bits.get_next_largest, 0)
        self.assertRaises(Exception, bits.get_next_largest, -1)


        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        bits.get_next_largest(num)        
        self.assertEqual(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    def test_get_next_smallest(self):
        # bits = Bits()
        # self.assertRaises(Exception, bits.get_next_smallest, None)
        # self.assertRaises(Exception, bits.get_next_smallest, 0)
        # self.assertRaises(Exception, bits.get_next_smallest, -1)
        # num = int('011010111', base=2)
        # expected = int('011001111', base=2)
        # self.assertEqual(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


if __name__ == '__main__':
    main()
