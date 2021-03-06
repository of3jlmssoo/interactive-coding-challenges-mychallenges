""" test_compress.py alt case

正規表現で(\w\s)が1つ以上連続する単位でグルーピング
グルーピングされた各グループ(match.group())の長さが>2の場合
    then 文字＋繰返し数をresultに追加
    else そのままresultに追加
    
AA BB CC
AA BB CC

AAA B CC DDDD
A3  B CC D4
            
aa B CC E FFFF KK MMMMMM P t aaa mm anl aa rrrr s eeeeeeeee k t ooo
aa B CC E F4   KK M6     P t a3  mm anl aa r4   s e9        k t o3

3つ以上連続の場合置き換える
2つの場合はそのまま


"""
import unittest
import re

def compress_string(string: str) -> str:
    if string == None: return None
    if string == '': return ''

    pattern = re.compile(r'(\w|\s)\1*')

    iterator = pattern.finditer(string)
    result = ''
    for match in iterator:
        # print("1 ", match.group(), match.start(), match.end(), match.span()[0], match.span()[1])
        current_part_str = match.group()
        if (current_part_str_len := len(current_part_str)) > 2:
            result = result + current_part_str[0] + str(current_part_str_len)
            # print("result1 : ",result, match.group())
        else:
            result += match.group()
            # print("result2 : ",result)
    return result 


class TestCompressString(unittest.TestCase):

    def test_compress_string(self):
        print(f'test_compress_string')
        
        print( compress_string('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo') )

class TestCompress(unittest.TestCase):

    def test_compress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDD'), 'A3BCCD4')
        self.assertEqual(
            func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'),
            'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3',
        )
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)

    testcompressstring = TestCompressString()
    testcompressstring.test_compress_string()


if __name__ == '__main__':
    main()
