""" Problem: Swap the odd and even bits of a positive integer with as few operations as possible.
できるだけ少ないオペレーションでa positive integerの偶数ビットと奇数ビットを入れ替える


1つ前のinsert_m_into_n.pyを文字列処理で対応した後、insert_m_into_n_solution.ipynbのAlgorithmパートを見る。
やはり文字列処理ではなくビットオペレーションで処理していることを確認。
test_pairwsize_swap.pyもまず文字列処理で対応した後ビットオペレーションで対応する。

偶数ビットのみ抜き出す
抜き出した結果を左にシフト
奇数ビットのみ抜き出す
抜き出した結果を右ににシフト
シフトした2つをorで合成

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

class Bits2(object):

    def pairwise_swap(self, num):
        if num == None: raise(TypeError)
        if num in [0,1,-1]: return num
        bin_num = bin(num)[2:]
        if len(bin_num) % 2 != 0: raise ValueError('num length error')
        logger.debug(f'Bits2.pairwise_swap() len and value of bin_num {len(bin_num)} {bin_num}')
        # 偶数ビットのみ抜き出す
        # 抜き出した結果を左にシフト
        # 109876543210
        # 100111110110
        #  A A A A A A          
        #  0 1 1 1 1 0
        # 000101010100
        #  0b101010100 pasted
        # 0b1010101000 pasted
        logger.debug(f'Bits2.pairwise_swap() 1st step and operation { bin(num & 0b010101010101) }')
        even_bits = bin((num & 0b010101010101) << 1)
        logger.debug(f'Bits2.pairwise_swap() even_bits {even_bits}')

        # 奇数ビットのみ抜き出す
        # 抜き出した結果を右ににシフト
        #   109876543210
        #   100111110110
        #   A A A A A A          
        #   1 0 1 1 0 1
        #   100010100010
        # 0b100010100010 
        #  0b10001010001
        logger.debug(f'Bits2.pairwise_swap() 2nd step and operation { bin(num & 0b101010101010) }')
        odd_bits = bin((num & 0b101010101010) >> 1)
        logger.debug(f'Bits2.pairwise_swap() odd_bits {odd_bits}')
        # シフトした2つをorで合成
        # 0000011011111001 expected
        #    0b11011111001 pasted
        logger.debug(f'Bits2.pairwise_swap() even and odd_bits {bin(int(even_bits,base=2) | int(odd_bits,base=2))}')
        return int(bin(int(even_bits,base=2) | int(odd_bits,base=2)),base=2)

        

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
        
        bits2 = Bits2()
        self.assertRaises(TypeError, bits2.pairwise_swap, None)
        self.assertEqual(bits2.pairwise_swap(0), 0)
        self.assertEqual(bits2.pairwise_swap(1), 1)
        self.assertEqual(bits2.pairwise_swap(-1), -1)

        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        # bits2.pairwise_swap(num)
        self.assertEqual(bits2.pairwise_swap(num), expected)

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

        bits = Bits2()
        self.assertEqual(bits.pairwise_swap(0), 0)
        self.assertEqual(bits.pairwise_swap(1), 1)
        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        self.assertEqual(bits.pairwise_swap(num), expected)
        self.assertRaises(TypeError, bits.pairwise_swap, None)
        
        print('Success: Bits() test_pairwise_swap')


def main():
    test = TestBits()
    test.test_pairwise_swap()

    mytest = MyTestBits()
    mytest.test_pairwise_swap()


if __name__ == '__main__':
    main()
