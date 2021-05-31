""" test_insert_m_into_n.py

insert m into n

[Test Case]
i      = 2
j      = 6
n      = 0000 0100 0000 0000
m      = 0000 0000 0001 0011
result = 0000 0100 0100 1100

mの1の一番左から一番右の1まで1 0011。len=5
j=6 to i=2 6/5/4/3/2 len=5

nの6 to 2をクリアする
n      = 0000 0100 0xxx xx00
mの1の一番左から一番右の1までを取り出す1 0011
クリアしたところに押し込む
n      = 0000 0100 0xxx xx00
                    100 11
         0000 0100 0100 1100           
result = 0000 0100 0100 1100

[Test]
            0123456789012345
n =         0000010000111101
m =         0000000000010011
expected =  0000010001001101
i=2
j=6

m 1 to 1 : 10011

    0123456789012345
n = 0000010000111101
             |   |
          15-6  15-2
n = 000001000xxxxx01
result
  = 0000010001001101
expected 
  = 0000010001001101

"""
import unittest
import re

class MyTestBit(unittest.TestCase):

    def test_my_test_bit(self):
        print(f'test_my_test_bit')
        myBits = Bits()
        n = int('0000010000111101', base=2)
        m = int('0000000000010011', base=2)
        print(myBits.insert_m_into_n(m, n, i=2, j=6 ))

class Bits(object):

    def insert_m_into_n(self, m, n, i, j):
        # TODO: Implement me
        # pass
        print("insert_m_into_n() called")
 
        pattern = re.compile(r'1[01]*1')
        iterator = pattern.finditer(bin(m))
        for match in iterator:
            string = match.group()
            # print("len(string) and string ",len(string), string)
            if (j-i+1) != len(string): raise ValueError("length error")
        # print("n_bin[2:] ", bin(n)[2:] )
        n_bin = self.bin_to_ten(bin(n))[2:] 
        # print("n_bin len and its value ", len(n_bin), n_bin)
        # print("three length ", len(n_bin), len(n_bin[0:15-j]),  len(string), len(n_bin[15-i+1:] ))
        result = n_bin[0:15-j]+string+n_bin[15-i+1:] 
        # print("---> ", result)
        return int(result,base=2)
            
    def bin_to_ten(self, bin_output: str):

        STR_LEN = 16 + 2 # 16 bit number and '0b

        result = [bin_output, bin_output[0:2]+'0'*(STR_LEN-len(bin_output))+bin_output[2:]]
        return result[len(bin_output) < STR_LEN]

class TestBit(unittest.TestCase):

    def test_insert_m_into_n(self):
        n = int('0000010000111101', base=2)
        m = int('0000000000010011', base=2)
        expected = int('0000010001001101', base=2)
        bits = Bits()
        self.assertEqual(bits.insert_m_into_n(m, n, i=2, j=6), expected)
        print('Success: test_insert_m_into_n')


def main():
    test = TestBit()
    test.test_insert_m_into_n()

    mytest = MyTestBit()
    mytest.test_my_test_bit()

if __name__ == '__main__':
    main()
