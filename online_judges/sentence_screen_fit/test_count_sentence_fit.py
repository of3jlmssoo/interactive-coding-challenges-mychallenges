"""
Example 1 
rows = 2, cols = 8, sentence = ["hello", "world"] -> 1
   12345678
r1 hello-
r2 world

Example 2 
rows = 3, cols = 6, sentence = ["a", "bcd", "e"] -> 2
   123456
r1 a-bcd-
r2 e-a-
r3 bcd-e
   123456

Example 3
    row = 4
    col = 5
    sentence = ["I", "had", "apple", "pie"]
１行目　I-had
    Explanation:
        I-had
        apple
        pie-I
        had--
=> hadとappleの間に-は無い

colの範囲に収まるか と 行の制限
=> 行数でループする
"""
import unittest
import copy
import logging


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

    def __init__(self) -> None:
        self.__remainings = []
        self.__result = 0

    def count_sentence_fit(self, sentence, rows, cols):
        # TODO: Implement me
        # pass
        if sentence is None:
            raise TypeError(f'Solution.count_sentence_fit: sentence is None')

        if rows < 0 or cols < 0:
            raise ValueError(f'Solution.count_sentence_fit: rows < 0 or cols < 0')

        """ 初期化 """
        used_cols = 0
        self.__remainings=[]
        self.__result = 0
        for r in range(rows):
            """ 行の数だけループする """
            used_cols = 0
            while (remaining_cols := (cols-used_cols))>0:
                """ ここではワードがcolsに収まるかどうかだけを見る。収まらない場合return_word()で
                    返して次の行の数だけループで改めてget_next_word()する """
                """ how many times a sentence can fit on a screen(self.__result)の管理は """
                """ get_next_word(), check_sentenceに任せる"""
                logger.debug(f'while loop col:{cols}, used_cols:{used_cols}, remaining_cols:{remaining_cols}')

                next_word = self.get_next_word(sentence)

                if (word_len:=len(next_word)) == remaining_cols or (word_len:=len(next_word))+1 == remaining_cols:
                    """ ぴったり収まるケース """
                    logger.debug(f'ぴったり収まるケース r:{r}, next_word:{next_word}, word_len:{word_len}, remaining_cols:{remaining_cols}')
                    break
                elif word_len < remaining_cols:
                    """ 余裕があるケース """
                    logger.debug(f'余裕があるケース r:{r}, next_word:{next_word},  word_len:{word_len}, remaining_cols:{remaining_cols}, used_cols:{used_cols}')
                    used_cols = used_cols + word_len+1
                    remaining_cols = cols - used_cols
                else:
                    """ あふれるケース """
                    logger.debug(f'あふれるケース')
                    self.return_word(next_word)
                    break

        self.check_sentence(self.__remainings)
        return self.__result

    def return_word(self,word):
        """ あふれるケース """
        """ 戻す """
        self.__remainings = [word] + self.__remainings

    def get_next_word(self,sentence)->str:
        """ sentenceをself.__remainingsにコピーの上先頭の要素をnext_wordとして返す """
        """ sentenceをself.__remainingsにコピーする際、
            self.__result(how many times a sentence can fit on a screen)をカウントアップする """
        if not self.__remainings:
            self.__remainings = copy.deepcopy(sentence)
            self.__result = self.__result + 1
        result = self.__remainings.pop(0)
        return result

    def check_sentence(self, remaings):
        """ sentenceをself.__remainingsにコピーしたが使い切っていない場合
            self.__resultをマイナス1する """
        if self.__remainings:
            self.__result = self.__result - 1
    
class TestSolution(unittest.TestCase):

    def test_count_sentence_fit(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.count_sentence_fit,
                          None, None, None)
        self.assertRaises(ValueError, solution.count_sentence_fit,
                          'abc', rows=-1, cols=-1)
        sentence = ["hello", "world"]
        expected = 1
        self.assertEqual(solution.count_sentence_fit(sentence, rows=2, cols=8),
                         expected)
        sentence = ["a", "bcd", "e"]
        expected = 2
        self.assertEqual(solution.count_sentence_fit(sentence, rows=3, cols=6),
                         expected)
        sentence = ["I", "had", "apple", "pie"]
        expected = 1
        self.assertEqual(solution.count_sentence_fit(sentence, rows=4, cols=5),
                         expected)
        print('Success: test_count_sentence_fit')


def main():
    test = TestSolution()
    test.test_count_sentence_fit()


if __name__ == '__main__':
    main()
