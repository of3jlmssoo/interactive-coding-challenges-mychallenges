""" test_bit.py

- index : 右からのビットの位置
- msb : most significant bit
- lsb : least significant bit
  
get_bit     indexの位置のbitを返す
set_bit     indexの位置にbitをセットする
clear_bit   indexの位置のbitをクリアする
clear_bits_msb_to_index msbからindex(indexの位置を含む)をクリアする
clear_bits_index_to_lsb lsbからindex(indexの位置を含む)をクリアする
update_bit  indexの位置のbitにvalueをセットする

9876543210
0b10001110
0123456789
7-index

10001110
16318421
2426
8
128+8+4+2=142

bin_to_ten()
pythonのbin()が不要な0を追加してくれない。0x+8桁のフォーマット前提で途中まで進めたためbin()のreturnの長さ<10の場合、bin_to_ten()で0をパッディングする

"""
import unittest

class Bit(object):

    def __init__(self, number):
        # # TODO: Implement me
        # pass
        self.__numInt = number

    def get_bit(self, index):
        # TODO: Implement me
        # pass
        result=[False,True]
        return result[int(bin(self.__numInt)[9-index])]

    def set_bit(self, index):
        # TODO: Implement me
        # pass

        # self.__numBin = bin(self.__numInt)
        # # print(f'set_bit 1 {self.__numBin}')
        # if len(self.__numBin) < 10:
        #     # print("=== too short ", self.__numBin[0:2], '0'*(10-len(self.__numBin)), self.__numBin[2:])
        #     self.__numBin = self.__numBin[0:2]+'0'*(10-len(self.__numBin))+self.__numBin[2:]
        # # print(f'set_bit 2 {self.__numBin}')
            
        # # self.__one = '1'; print(f'set_bit 3 {self.__numBin[0:9-index]} {self.__one} {self.__numBin[9-index+1:]} ')
        
        self.__numBin = self.bin_to_ten(bin(self.__numInt))
        return int(self.__numBin[0:9-index]+'1'+self.__numBin[9-index+1:], base=2)

    def clear_bit(self, index):
        # TODO: Implement me
        # pass
        # self.__numBin = bin(self.__numInt)
        self.__numBin = self.bin_to_ten(bin(self.__numInt))
        return int(self.__numBin[0:9-index]+'0'+self.__numBin[9-index+1:], base=2)

    def clear_bits_msb_to_index(self, index):
        # TODO: Implement me
        # pass
        # self.__numBin = bin(self.__numInt)
        self.__numBin = self.bin_to_ten(bin(self.__numInt))
        # print('0b'+'0'*(8-index)+self.__numBin[10-index:])
        return int('0b'+'0'*(8-index)+self.__numBin[10-index:], base=2)

    def clear_bits_index_to_lsb(self, index):
        # TODO: Implement me
        # pass
        self.__numBin = self.bin_to_ten(bin(self.__numInt))
        print( self.__numBin[:9-index]+'0'*(index+1) )
        return int(self.__numBin[:9-index]+'0'*(index+1), base=2) 

    def update_bit(self, index, value):
        # TODO: Implement me
        # pass
        self.__numBin = self.bin_to_ten(bin(self.__numInt))
        return int(self.__numBin[0:9-index]+str(value)+self.__numBin[9-index+1:], base=2)

    def bin_to_ten(self, bin_output: str):
        # if len(bin_output) < 10:
        #     result = bin_output[0:2]+'0'*(10-len(bin_output))+bin_output[2:]
        # else:
        #     result = bin_output
        # return result

        STR_LEN = 10 # change two 10s to STR_LEN

        result = [bin_output, bin_output[0:2]+'0'*(10-len(bin_output))+bin_output[2:]]
        return result[len(bin_output) < 10]



class myTestBit(unittest.TestCase):

    def test_bit(self):
        number = int('11111111', base=2)
        bit = Bit(number)
        del bit

        number = int('00000000', base=2)
        bit = Bit(number)

        print(f'test set_bit')
        print(f'{bin(bit.set_bit(index=1))}')
        print(f'{bin(bit.set_bit(index=2))}')
        print(f'{bin(bit.set_bit(index=3))}')
        print(f'{bin(bit.set_bit(index=4))}')
        print(f'{bin(bit.set_bit(index=5))}')
        print(f'{bin(bit.set_bit(index=6))}')
        print(f'{bin(bit.set_bit(index=7))}')
        print(f'{bin(bit.set_bit(index=0))}')
        del bit

        number = int('11111111', base=2)
        bit = Bit(number)

        print(f'test clear_bits_msb_to_index')
        print(f'{bin(bit.clear_bits_msb_to_index(index=1))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=2))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=3))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=4))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=5))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=6))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=7))}')
        print(f'{bin(bit.clear_bits_msb_to_index(index=0))}')

        print(f'test bin_to_ten')
        print(bit.bin_to_ten('0b1'))
        print(bit.bin_to_ten('0b11'))
        print(bit.bin_to_ten('0b111'))
        print(bit.bin_to_ten('0b1111'))
        print(bit.bin_to_ten('0b11111'))
        print(bit.bin_to_ten('0b111111'))
        print(bit.bin_to_ten('0b1111111'))
        print(bit.bin_to_ten('0b11111111'))

        print(f'test clear_bits_index_to_lsb')
        del bit
        number = int('11111111', base=2)
        bit = Bit(number)
        bit.clear_bits_index_to_lsb(index=1)
        bit.clear_bits_index_to_lsb(index=2)
        bit.clear_bits_index_to_lsb(index=3)
        bit.clear_bits_index_to_lsb(index=4)
        bit.clear_bits_index_to_lsb(index=5)
        bit.clear_bits_index_to_lsb(index=6)
        bit.clear_bits_index_to_lsb(index=7)
        bit.clear_bits_index_to_lsb(index=0)

class TestBit(unittest.TestCase):

    def test_bit(self):
        number = int('10001110', base=2)

        bit = Bit(number)
        self.assertEqual(bit.get_bit(index=3), True)
        
        expected = int('10011110', base=2)
        bit.set_bit(index=4)
        self.assertEqual(bit.set_bit(index=4), expected) 
        
        bit = Bit(number)
        expected = int('10000110', base=2)
        self.assertEqual(bit.clear_bit(index=3), expected) 

        bit = Bit(number)
        expected = int('00000110', base=2)
        self.assertEqual(bit.clear_bits_msb_to_index(index=3), expected) 
        
        bit = Bit(number)
        expected = int('10000000', base=2)
        self.assertEqual(bit.clear_bits_index_to_lsb(index=3), expected)

        bit = Bit(number)
        self.assertEqual(bit.update_bit(index=3, value=1), number) 
        
        bit = Bit(number)
        expected = int('10000110', base=2)
        self.assertEqual(bit.update_bit(index=3, value=0), expected) 
        
        bit = Bit(number)
        expected = int('10001111', base=2)
        self.assertEqual(bit.update_bit(index=0, value=1), expected)
        print('Success: test_bit')


def main():
    test = TestBit()
    test.test_bit()

    mytest = myTestBit()
    mytest.test_bit()


if __name__ == '__main__':
    main()