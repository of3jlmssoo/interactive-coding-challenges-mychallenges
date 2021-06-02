""" Problem: Swap the odd and even bits of a positive integer with as few operations as possible.
できるだけ少ないオペレーションでa positive integerの偶数ビットと奇数ビットを入れ替える

"""

import logging
import unittest

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = True

class Bits(object):

    def pairwise_swap(self, num):
        # TODO: Implement me
        # pass
        if num == None: raise(TypeError)
        if num in [0,1,-1]: return num
        bin_num = bin(num)[2:]
        # bin_num= '111'
        # bin_num = '0123456789'
        if len(bin_num) % 2 != 0: raise ValueError('num length error')
        logger.debug(f'pairwise_swap() len and value of bin_num {len(bin_num)} {bin_num}')
        swapped_string=''
        for i in range(0,len(bin_num),2):
            swapped_string  = swapped_string + bin_num[i+1] + bin_num[i] 
        logger.debug(f'pairwise_swap() swapped_string {swapped_string}')
        return int(swapped_string,base=2)

        

class MyTestBits(unittest.TestCase):


    def test_pairwise_swap(self):

        bits = Bits()
        self.assertRaises(TypeError, bits.pairwise_swap, None)
        self.assertEqual(bits.pairwise_swap(0), 0)
        self.assertEqual(bits.pairwise_swap(1), 1)
        self.assertEqual(bits.pairwise_swap(-1), -1)

        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        # bits.pairwise_swap(num)
        self.assertEqual(bits.pairwise_swap(num), expected)
class TestBits(unittest.TestCase):

    def test_pairwise_swap(self):
        bits = Bits()
        self.assertEqual(bits.pairwise_swap(0), 0)
        self.assertEqual(bits.pairwise_swap(1), 1)
        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        self.assertEqual(bits.pairwise_swap(num), expected)
        self.assertRaises(TypeError, bits.pairwise_swap, None)
        
        print('Success: test_pairwise_swap')


def main():
    test = TestBits()
    test.test_pairwise_swap()

    mytest = MyTestBits()
    mytest.test_pairwise_swap()


if __name__ == '__main__':
    main()
