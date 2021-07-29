"""
[テストデータ]
'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' -> 32

dir \n\t subdir1 \n\t\t file1.ext
                 \n\t\t subsubdir1
    \n\tsubdir2  \n\t\t subsubdir2 \n\t\t\t file2.ext
3       7               10                  9    = 29
   1            1                   1            = 3

dir subdir1  file1.ext
dir subdir1  subsubdir1
dir tsubdir2 subsubdir2 file2.ext


[データ]

(a)対象名称の       (b)リスト処理に (c)処理インディケータ(gap)
\tの数              おける\tの数    (c) = (a) - (b)
0       dir         0                0
1       subdir1     0               +1
2       file1.ext   1               +1
2       subsubdir1  2                0
1       subdir2     2               -1
2       subsubdir2  1               +1
3       file2.ext   2               +1
                    next (b) = (b) + (c)

1カラム目の数値は\tの数
2カラム目はフォルダーかファイルの名前


[データ保管(リスト)]
output_list = [
    [dir, subdir1,  file1.ext],
    [dir, subdir1, subsubdir1],
    [dir, tsubdir2, subsubdir2, file2.ext]
]

[処理]
olst = [[]]     アウトプット用リスト準備
olst_idx = 0    アウトプット用リストのインデックス初期化
t_num = 0       tの数のカウンター初期化

先頭のデータを処理するために'\n'をアペンドする
リストを順に処理
    \tの数チェック(inputlist[x][0]-t_num)
        +1  olst_idx変更無しケース
            名称をolst[olst_idx]に追加

        =   olst_idx+=1ケース
            olst[olst_idx]をolstにappend(deep copy)
            olst_idx+=1
            最後のエレメントを置換え

            ただし、\tの数が0の場合は例外処理(一番最初のデータ。例ではdir)
            この場合olstは空の状態なので単純にappend

        -1  olst_idx+=1ケース
            olst[olst_idx]をolstにappend(deep copy)。ただし、全コピーではなく先頭から'\t'の数分だけコピーする
            olst_idx+=1
            olst[olst_idx]にアペンド
        t_num更新


"""
from typing import Type
import unittest
import logging
import re
import copy
from functools import reduce
from operator import add


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

    def length_longest_path(self, file_system):
        # TODO: Implement me
        # pass
        if file_system is None:
            raise TypeError(
                f'Solution.length_longest_path: file_system == None')

        if file_system == '':
            return 0

        """
        olst = [[]]     アウトプット用リスト準備
        olst_idx = 0    アウトプット用リストのインデックス初期化
        t_num = 0       tの数のカウンター初期化
        """
        olst = [[]]
        olst_idx = 0
        t_num = 0
        """ 先頭のデータを処理するために'\n'をアペンドする """
        file_system = '\n' + file_system

        """ リストを順に処理 """
        regex = r'\n\t*[\w.]+'
        m = re.findall(regex, file_system)

        for n in m:
            if not logger.disabled:
                print('n.count(t):', n.count('\t'), ' , t_num:',
                      t_num, ', gap:', (n.count('\t') - t_num), ',\
                word:', re.sub('\n\t*', '', n), end='')

            """ \tの数チェック(inputlist[x][0]-t_num) """
            if (gap := (n.count('\t') - t_num)) == 1:
                """+1   olst_idx変更無しケース
                        名称をolst[olst_idx]に追加 """
                olst[olst_idx].append(re.sub('\n\t*', '', n))
            elif gap == 0:
                if n.count('\t') == 0:
                    """ ただし、\tの数が0の場合は例外処理(一番最初のデータ。例ではdir)
                        この場合olstは空の状態なので単純にappend"""
                    olst[olst_idx].append(re.sub('\n\t*', '', n))
                else:
                    """=    olst_idx+=1ケース
                            olst[olst_idx]をolstにappend(deep copy)
                            olst_idx+=1
                            最後のエレメントを置換え"""
                    olst.append(copy.deepcopy(olst[olst_idx]))
                    olst_idx = olst_idx + 1
                    olst[1][-1] = re.sub('\n\t*', '', n)
            elif gap == -1:
                """-1   olst_idx+=1ケース
                        olst[olst_idx]をolstにappend(deep copy)。ただし、全コピーではなく先頭から'\t'の数分だけコピーする
                        olst_idx+=1
                        olst[olst_idx]にアペンド"""
                olst.append(copy.deepcopy(olst[olst_idx][0:n.count('\t')]))
                olst_idx = olst_idx + 1
                olst[olst_idx].append(re.sub('\n\t*', '', n))
            else:
                # print(' --- else', end='')
                raise ValueError(
                    f'Solution.length_longest_path: something wrong.')
            if not logger.disabled:
                print(' olst : ', olst)
            # print('\n')
            """ t_num更新 """
            t_num = t_num + gap

        return self.calc_length2(olst)    
        # return self.calc_length(olst)

    def calc_length2(self,lst):

        """ lst_lenは引数lst(リスト内リスト)の内側のリストの要素数-1。スラッシュの数となる"""
        """ chr_lenは引数lst(リスト内リスト)の内側のリストの各要素の文字数を合計したもの"""
        """ 2つのリストを足して最大値を求めてreturnする"""
        lst_len = [len(j)-1 for j in [list(map(len,i)) for i in lst]]       # [2, 2, 3]
        chr_len = [reduce(add,j) for j in [list(map(len,i)) for i in lst]]  # [19.20,29]

        return max(list(map(add, lst_len, chr_len)))

    def calc_length(self,lst):
        result=0 # max length
        for m in lst:
            __len = 0
            for n in m:
                __len = __len + len(n)
            __len = __len + (len(m)-1)    
            if __len > result:
                result = __len
        return result

class TestSolution(unittest.TestCase):

    def test_length_longest_path(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.length_longest_path, None)
        self.assertEqual(solution.length_longest_path(''), 0)
        file_system = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        expected = 32

        # solution.length_longest_path(file_system)

        self.assertEqual(solution.length_longest_path(file_system), expected)
        print('Success: test_length_longest_path')


def main():
    test = TestSolution()
    test.test_length_longest_path()


if __name__ == '__main__':
    main()
