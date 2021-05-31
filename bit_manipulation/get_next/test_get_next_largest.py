import unittest


class Bits(object):

    def check_num(self, num:int ) -> bool:
        if num in [None,0,-1]: raise(Exception)
        else: return True

    def get_next_largest(self, num: int) -> int:

        self.check_num(num) 

        append_candidate = ['01','10']
        # num_bin_splitted_01 = bin(num)[2:].split(append_candidate[0]) # remove first two charcter '0b' and split by '01'
        # num_bin_splitted_01_len = len(num_bin_splitted_01)
        # result = ''
        # for i in range(num_bin_splitted_01_len-1): # -1 : as for the last element in num_bin_splitted_01
        #                                            # it will be added to result without any append_char in return statement
        #     append_char = append_candidate[(num_bin_splitted_01_len-2)==i]
        #                                            # -2 : the last '01' will be replace with '10'
        #     result = result + num_bin_splitted_01[i] + append_char
        # return int(result + num_bin_splitted_01[num_bin_splitted_01_len-1],base=2)
        return self.change_num(append_candidate, num) 

    def get_next_smallest(self, num: int) -> int:
        # if num in [None,0,-1]: raise(Exception)
        self.check_num(num) 

        append_candidate = ['10','01']
        # num_bin_splitted_01 = bin(num)[2:].split(append_candidate[0]) # remove first two charcter '0b' and split by '01'
        # num_bin_splitted_01_len = len(num_bin_splitted_01)
        # result = ''
        # for i in range(num_bin_splitted_01_len-1): # -1 : as for the last element in num_bin_splitted_01
        #                                            # it will be added to result without any append_char in return statement
        #     append_char = append_candidate[(num_bin_splitted_01_len-2)==i]
        #                                            # -2 : the last '01' will be replace with '10'
        #     result = result + num_bin_splitted_01[i] + append_char
        
        return self.change_num(append_candidate, num) 
            # print("same!")

        # return int(result + num_bin_splitted_01[num_bin_splitted_01_len-1],base=2)

    def change_num(self, candidates: list, num:int) -> int:
        result = ''
        num_bin_splitted_01 = bin(num)[2:].split(candidates[0]) # remove first two charcter '0b' and split by '01' or '10' (cadidate[0])
        num_bin_splitted_01_len = len(num_bin_splitted_01)
        for i in range(num_bin_splitted_01_len-1): # -1 : as for the last element in num_bin_splitted_01
                                                   # it will be added to result without any append_char in return statement
            append_char = candidates[(num_bin_splitted_01_len-2)==i]
                                                   # -2 : the last candidates[0] will be replace with candidates[1]
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
        bits = Bits()
        self.assertRaises(Exception, bits.get_next_smallest, None)
        self.assertRaises(Exception, bits.get_next_smallest, 0)
        self.assertRaises(Exception, bits.get_next_smallest, -1)
        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        self.assertEqual(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


if __name__ == '__main__':
    main()
