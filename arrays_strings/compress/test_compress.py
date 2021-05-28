""" test_compress.py

groupbyでstringを分割。AABの場合、['A', 'A'], ['B']
分割された要素のlen > 1の場合、const_charsに[分割された要素の長さ、分割された要素]のリストをappend
    const_chars=[[2, ['A', 'A']],,,]
const_charsを分割された要素の長さでソート。降順
ソートされたリストの1つ目の”分割された要素のlen” > 2の場合then
    replace( 一文字取出*len, 一文字取出+str(len))

self.assertEqual(func('AABBCC'), 'AABBCC')
self.assertEqual(func(  'AAA B CC DDDD E'), 
                        'A3  B C2 D4   E')
self.assertEqual(func(' B AAA CC DDDD'), '
                        B A3  C2 D4')
self.assertEqual(func('AAA B AA CC DDDD'), '
                       A3  B A2 C2 D4')
問題は2連続の際に置換えが発生するケースと発生しないケースがある。

python normal expression continuos characters
https://stackoverflow.com/questions/6306098/regexp-match-repeated-characters
[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
とあるが、実際には、AAABAACCDDDD の場合、
    A ['A', 'A', 'A']
    B ['B']
    C ['C', 'C']
    D ['D', 'D', 'D', 'D']
    E ['E']
が返される。

"""
import unittest
from itertools import groupby

class CompressString(object):

    def compress(self, string):
        # TODO: Implement me
        # pass
        if string == None: return None
        if string == '': return ''
        
        
        grouped_by_string = [list(g) for k, g in groupby(string)]
        cont_chars=[]
        [cont_chars.append([len(list(i)), i]) for i in grouped_by_string if len(list(i))>1]

        target_lst = (sorted(cont_chars, key=lambda x: x[0], reverse=True))
        if target_lst[0][0] > 2:
            for i,l in enumerate(target_lst):
                # print(i,l, str(l[1][0]*l[0]), str(l[1][0]+str(l[0])))
                string = string.replace(str(l[1][0]*l[0]), str(l[1][0]+str(l[0])))
                # print(string)
        return string

class TestCompressString(unittest.TestCase):

    def test_compress_string(self):
        print(f'test_compress_string')
        compstr = CompressString()
        
        print( compstr.compress('AAABAACCDDDD'))
        # self.assertEqual(compstr.compress('AAABAACCDDDD'), )
        
class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(func('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)

    testcompressstring = TestCompressString()
    testcompressstring.test_compress_string()

if __name__ == '__main__':
    main()
