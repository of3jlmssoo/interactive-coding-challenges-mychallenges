"""
[結論]
- まずsuffix treeを検討するがギブアップ
- dynamic programmingの「前の計算結果を活かす」を意識しつつプログラムを作成することにする
- suffix treeをギブアップしたのは、suffix treeを理解し、それをpythonで活用するのに長い時間を要すると考えたため
- hanoi、knapsackで時間を要しているのでここは先に進むことを重要視する

[課題]
- recursionになっていない


--- 以下はsuffix treeに関してまとめたもの ---
[参照]
https://en.wikipedia.org/wiki/Suffix_tree#Description
https://en.wikipedia.org/wiki/Generalized_suffix_tree
https://www.researchgate.net/publication/51942252_ERA_Efficient_Serial_and_Parallel_Suffix_Tree_Construction_for_VeryLong_Strings/download
- ユニークターミネータが付与されている
- the leafのナンバーはストリングナンバーとスターティング・ポジション
- ???左から右へのtraversalはthe suffixesのソートされた順番に相当

上記researchgateのPDFを参照
https://en.wikipedia.org/wiki/Suffix_tree#/media/File:Suffix_tree_BANANA.svg
0123456
BANANA$

0 BANANA
1  ANANA =A+NA+NA
2   NANA = NA+NA
3    ANA = A+NA
4     NA = NA
5      A = A

https://en.wikipedia.org/wiki/Generalized_suffix_tree#/media/File:Suffix_tree_ABAB_BABA.svg
ストリングナンバーとスターティング・ポジション
ABABとBABA

Str:Posi
0:0 ABAB = A+B+A+B
0:1  BAB = B+A+B
0:2   AB = A+B
0:3    B = B

1:0 BABA = B+A+B+A
1:1  ABA = A+B+A
1:2   BA = B+A
1:3    A = A


"""
import collections
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


class StringCompare(object):

    def longest_common_subseq(self, str0, str1):
        # TODO: Implement me
        # pass

        argcheck = [str0 is None, str1 is None]
        if any(argcheck):
            raise TypeError(
                f'StringCompare.longest_common_subseq. arg error {str0} {str1}')

        argcheck = [str0 == '', str1 == '']
        if any(argcheck):
            return ''

        longstr, shortstr = self.set_str(str0, str1)
        logger.debug(f'longstr:{longstr}, shortstr:{shortstr}')

        matches = []
        match_len = 2
        """ 最低2文字連続を前提とする """

        """
        longstr     ABCDEFGHIJ
        shortstr    FOOBCDBCDE

        順々に処理していく。最初は2文字連続で同じ文字列があるかどうかを見る。
        その後一度3文字連続が見つかった場合、その後は3文字の連続する文字列が
        双方にあるかどうかをチェックする。以下同様。

        iのループ : shortstrを順に処理
        whileループ :
            例えばi=3の場合、shortstrの最初B(shortstr[3])からBC, BCD, BCDB, BCDBC, BCDBCD, BCDBCDEと順に処理する
                i:上の例の場合Bの位置を保持
                match_len : 何文字連続するかを保持。1文字一致は対象外とするため2から。match_lenの値以上に
                            連続するケースがあった場合match_lenを更新する
                該当文字列(BC, BCD,...)がmatchesになく、かつ、longstrに存在する場合
                    matchesにアペンド
                    match_lenを+1
                else    break(このelse breakで処理削減)

        """
        for i in range(len(shortstr)):
            while (coverage := i + match_len) <= len(shortstr):
                logger.debug(
                    f'i:{i} match_len:{match_len} {shortstr[i:coverage]}')

                if shortstr[i:coverage] not in matches and longstr.find(
                        shortstr[i:coverage]) >= 0:
                    matches.append(shortstr[i:coverage])
                    match_len += 1
                else:
                    break
        # matches=[]
        if matches:
            return matches[-1]
        else:
            raise UserWarning(f'nothing found')

    def set_str(self, str0, str1):
        """ 最初に長さに応じてlongstr、shortstrをセット(if/elif)
            長さが同じ場合使われている文字数に応じてセット(elif/elif)
            文字数も同じ場合longstr, shortstr = str0, str1(else)"""
        if len(str0) > len(str1):
            """ 長さチェック """
            longstr, shortstr = str0, str1
        elif len(str0) < len(str1):
            longstr, shortstr = str1, str0
        elif (str0len := len(collections.Counter(list(str0)))) > (str1len := len(collections.Counter(list(str1)))):
            """ 使われている文字数チェック """
            longstr, shortstr = str0, str1
        elif str0len < str1len:
            longstr, shortstr = str0, str1
        else:
            """ 長さ同じ、文字数同じケース """
            longstr, shortstr = str0, str1

        return longstr, shortstr


class TestLongestCommonSubseq(unittest.TestCase):

    def test_longest_common_subseq(self):
        str_comp = StringCompare()
        self.assertRaises(
            TypeError,
            str_comp.longest_common_subseq,
            None,
            None)
        self.assertEqual(str_comp.longest_common_subseq('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        self.assertEqual(str_comp.longest_common_subseq(str0, str1), expected)
        print('Success: test_longest_common_subseq')


def main():
    test = TestLongestCommonSubseq()
    test.test_longest_common_subseq()


if __name__ == '__main__':
    main()
