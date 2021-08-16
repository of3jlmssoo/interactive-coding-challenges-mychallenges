"""
recursionにはなっている。。。しかし、計算量削減の余地あり

[メモ]
'abcabcdefgghiijhiij'
abcabc  6       next d
def     3       next g
gghii   5       next j
jhiij   5

ただしhiijhiijの8がMAX
思いつく対応方法は以下の2つ

(1) さかのぼり
gghii   5       next j
のところでnext jではなくnext hとする
最後のg+1の位置からのコールとなる

(2) 総当り
string = 'abcabcdefgghiijhiij'
for i in range(len(string)):
    string[i:]
で総当りする。

(2)総当りから(1)さかのぼりへ
(2)総当りではstringを順番に処理してくが、recursive callの際スライス指定してしまっている(string[1:])。
(1)さかのぼりに変更するには処理済みのデータが必要になる。
案として思いついたのは以下の2案。
a) スライス指定をやめてインデックス指定にする
b) stringを追加引数で渡し、スライス処理は残しておく。追加指定されたstringでさかのぼる
a)案で変更を行う。

- 総当り方式のままスライス指定をインデックス指定に変更する
- 総当り方式の処理量を簡易に計測する
- 総当り方式をやめる

test_longest_substr.py "called string" x 515 (全テストケース合計)
test_longest_substr2.py "called string" x 115 (全テストケース合計)

"""
import logging
import unittest

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = True


class Solution(object):

    def longest_substr(self, string, k):
        # TODO: Implement me
        # pass

        argcheck = [string is None, not isinstance(k, int)]
        if any(argcheck):
            raise TypeError(f'Solution.longest_substr: arg error. {string}')

        if string == '':
            return 0

        # result = 0
        # for i in range(len(string)):
        #     k_chars = [None] * k
        #     result = max(result,
        #                  self._longest_substr(string[i:], k, k_chars, 0, 0))
        # return result

        result = 0
        k_chars = [None] * k
        result = max(result, self._longest_substr(string, k, k_chars, 0, 0))
        return result

    def _longest_substr(self, string, k, k_chars, substr_len, idx):

        # print(
        # f'called string:{string}, k:{k}, k_chars:{k_chars},
        # substr_len:{substr_len}, idx:{idx}')

        if string[idx] in k_chars or k_chars.count(None) > 0:
            """ 既出文字か文字種数制限内の場合 """
            if string[idx] not in k_chars:
                """ 文字種制限内で新文字の場合 """
                k_chars[k_chars.index(None)] = string[idx]
            substr_len += 1

            # if len(string) > 1:
            if len(string) > idx + 1:
                """ まだ先がある場合 """
                # substr_len += 1
                return self._longest_substr(
                    string, k, k_chars, substr_len, idx + 1)
            else:
                return substr_len
        # elif len(string) > 1:
        elif idx + 1 < len(string):
            """ 新文字で残り2文字以上のケース """
            """ self.find_next_positionとnew_idxでさかのぼり"""
            new_idx = self.find_next_position(string, k_chars, idx)
            k_chars = [None] * k
            return max(substr_len,
                       self._longest_substr(string, k, k_chars, 0, new_idx))
        else:
            """ 新文字で残り1文字のケース """
            return substr_len

        """
        0123456789012345678
        abcabcdefgghiijhiij
                   A  A
                   |  idx=14
                   this index, 11, should be returned
                   k_chars:['g', 'h', 'i']
        """

    def find_next_position(self, string, k_chars, idx):
        # pass
        logger.debug(
            f'find_next_position 1: string: {string}, k_chars:{k_chars}, idx:{idx}')
        logger.debug(
            f'find_next_position 2: string[0:idx]: {string[0:idx]}, k_chars[0]:{k_chars[0]}')
        # lst = [i for i, x in enumerate(string[0:idx]) if x == k_chars[0]]
        # print(f'lst: {lst}')
        # return lst[-1] + 1
        # lst = [i for i, x in enumerate(string[0:idx]) if x == k_chars[0]]
        # print(f'lst: {lst}')
        return [i for i, x in enumerate(
            string[0:idx]) if x == k_chars[0]][-1] + 1


class TestSolution(unittest.TestCase):

    def test_longest_substr(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.longest_substr, None)
        self.assertRaises(TypeError, solution.longest_substr, None, None)
        self.assertRaises(TypeError, solution.longest_substr, 'abc', 'abc')
        self.assertEqual(solution.longest_substr('', k=3), 0)
        self.assertEqual(solution.longest_substr('abcabcdefgghiij', k=3), 6)

        """ 以下追加テストケース """
        self.assertEqual(
            solution.longest_substr(
                'abcabcdefgghiijhiij', k=3), 8)
        self.assertEqual(solution.longest_substr('abcabcdefgghighij', k=3), 7)
        print('Success: test_longest_substr')


def main():
    test = TestSolution()
    test.test_longest_substr()


if __name__ == '__main__':
    main()
