""" test_print_binary.py

bin(int)なのに対し0.625とかを対象とするので対応が必要。
https://note.nkmk.me/python-float-hex/とかhttps://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hexを参照するがギブアップ。
print_binary_solution.ipynbのAlgorithmを参考にするがアルゴリズムの情報だけでは不足。なのでCodeまで見てしまう。その上でアルゴリズムを補足

General case
0.625 -> 0.101
0.987654321 -> 'ERROR'

・resultを0にセット
・fractionを0.5にセット
・while num > 0のループ
  numとfractionを比較する
  if num >= fraction*   n0.625 vs f0.5  n0.125 vs f0.25     n0.125 vs f0.125
    add 1 to result     result=1                            result=101
    num -= fraction     num=0.125                           num=0
  else
    add 0 to result                     result=10
  if len(result)>32 return 'ERROR'
  fraction /= 2*        frac=0.25       f=0.125             f=0.0625
"""
import unittest
import logging
import struct
import sys

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

    def print_binary(self, num):
        if num == None: return 'ERROR'
        if num >= 1 or num <= 0: return 'ERROR'
        logger.debug(f'print_binary() called. num : {num}')
        f_max = sys.float_info.max
        # logger.debug(f'num in bin {self.double_to_hex(num)}')
        # logger.debug(f'num in bin {bin(int(self.double_to_hex(num), 16))}')


        # ・resultを0にセット
        # ・fractionを0.5にセット
        result = ''
        fraction = 0.5
        # ・while num > 0のループ
        # numとfractionを比較する
        # if num >= fraction*   n0.625 vs f0.5  n0.125 vs f0.25     n0.125 vs f0.125
        #     add 1 to result     result=1                            result=101
        #     num -= fraction     num=0.125                           num=0
        # else
        #     add 0 to result                     result=10
        # if len(result)>32 return 'ERROR'
        # fraction /= 2*        frac=0.25       f=0.125             f=0.0625
        while num:
            if num >= fraction:
                result = result + '1'
                num -= fraction
            else:
                result = result + '0'

            if len(result)>32: return 'ERROR'
            fraction /= 2

        result = '0.'+result
        logger.debug(f'print_binary() result {result}')
        return result

    def double_to_hex(self, f):
        return hex(struct.unpack('>Q', struct.pack('>d', f))[0])

class TestBits2(unittest.TestCase):

    def test_print_binary(self):

        bit = Bits()
        self.assertEqual(bit.print_binary(None), 'ERROR')
        self.assertEqual(bit.print_binary(0), 'ERROR')
        self.assertEqual(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        # logger.debug(f'test_print_binary() returned {bit.print_binary(num)}')
        self.assertEqual(bit.print_binary(num), expected)

class TestBits(unittest.TestCase):

    def test_print_binary(self):
        bit = Bits()
        self.assertEqual(bit.print_binary(None), 'ERROR')
        self.assertEqual(bit.print_binary(0), 'ERROR')
        self.assertEqual(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        self.assertEqual(bit.print_binary(num), expected)
        num = 0.987654321
        self.assertEqual(bit.print_binary(num), 'ERROR')
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_print_binary()

    mytest = TestBits2()
    mytest.test_print_binary()


if __name__ == '__main__':
    main()
