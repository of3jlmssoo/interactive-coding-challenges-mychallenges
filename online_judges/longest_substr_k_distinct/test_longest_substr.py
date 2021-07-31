"""
self.assertEqual(solution.longest_substr('abcabcdefgghiij', k=3), 6)
abcabc defgghiij abcのk=3 charactersで6桁

self.assertEqual(solution.longest_substr('abcabcdefgghighij', k=3), 7)
abcabcdef　gghighi j 	ghiで最大7桁
"""
import unittest
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
logger.disabled = False


class Solution(object):

    def longest_substr(self, string, k):
        # TODO: Implement me
        # pass

        if string is None:
            raise TypeError(f'Solution.longest_substr: string==None')
        if string == '':
            return 0

        result = 0
        # kdis_cs = []

        """ result = the length of the longest substring
            stringを先頭から一文字ずつ処理する
            外のforループリストkdis_csにこの一文字を保管する
                内の引き続く文字を保管する
                    文字種数がkを超えた場合break
                    文字種数がkを超えない場合引き続く文字を保管する
                resultとlen(kdis_cs)を比較して最大長が更新の場合resultを更新
            return result
        """

        for i, c in enumerate(string):

            kdis_cs = []
            kdis_cs.append(c)

            for ii, cc in enumerate(string[i + 1:]):

                if len(set(kdis_cs + [cc])) > k:
                    break
                kdis_cs.append(cc)
            logger.debug(
                f'Solution.longest_substr 1: result:{result}, kdis_cs:{kdis_cs}')

            if result < (l := len(kdis_cs)):
                result = l

        logger.debug(
            f'Solution.longest_substr 2: result:{result}, kdis_cs:{kdis_cs}')
        return result


class TestSolution(unittest.TestCase):

    def test_longest_substr(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.longest_substr, None)
        self.assertEqual(solution.longest_substr('', k=3), 0)
        self.assertEqual(solution.longest_substr('abcabcdefgghiij', k=3), 6)
        self.assertEqual(solution.longest_substr('abcabcdefgghighij', k=3), 7)
        print('Success: test_longest_substr')


def main():
    test = TestSolution()
    test.test_longest_substr()


if __name__ == '__main__':
    main()
