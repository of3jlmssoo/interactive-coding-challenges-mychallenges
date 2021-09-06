"""
[課題]
Problem: Given an array of 32 integers, find an int not in the input. Use a minimal amount of memory.
"Use a minimal amount of memory."に重点を置く。
- そもそもメモリー使用量を気にしたことがなく、かつ、メモリー使用状況の把握の方法も知らないため

[参考]
https://stackoverflow.com/questions/7153659/generate-an-integer-that-is-not-among-four-billion-given-ones
のhttps://stackoverflow.com/a/7156847

https://pypi.org/project/bitarray/
"このライブラリーはbooleansのアレイを効率良くrepresentsするオブジェクトタイプを提供する”

https://pypi.org/project/memory-profiler/

# python -m memory_profiler example.py

(
test_new_int.pyにはwebの方に記載されているfrom bitstring import BitArray  # run pip install bitstringが無い
これに気付かなかったので、bitstringではなくstackoverflowにあったbitarrayを利用

このファイルでは使っていないが、対応の途中ではtracemallocとmemory_profilerを試してみた
)
"""
import unittest
# from bitstring import BitArray  # run pip install bitstring
from bitarray import bitarray
# import numpy as np


class Bits(object):

    def new_int(self, array, max_size):
        # TODO: Implement me
        # pass

        argchks = [array is None, array == []]
        if any(argchks):
            raise TypeError(f'Bits.new_int: arg error {array=}')

        my_bit_array = bitarray(max_size)
        # print(f'{my_bit_array.__sizeof__()=}')
        my_bit_array.setall(0)

        for a in array:
            my_bit_array[a] = 1

        # return my_bit_array.index(0)
        try:
            return my_bit_array.index(0)
        except ValueError:
            return None


class TestBits(unittest.TestCase):

    def test_new_int(self):
        bits = Bits()
        max_size = 32
        self.assertRaises(TypeError, bits.new_int, None, max_size)
        self.assertRaises(TypeError, bits.new_int, [], max_size)
        data = [item for item in range(30)]
        data.append(31)
        self.assertEqual(bits.new_int(data, max_size), 30)
        data = [item for item in range(32)]
        self.assertEqual(bits.new_int(data, max_size), None)
        print('Success: test_find_int_excluded_from_input')


def main():
    test = TestBits()
    test.test_new_int()


if __name__ == '__main__':
    main()
