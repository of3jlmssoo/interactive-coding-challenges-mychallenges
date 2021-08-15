"""
TODO: recursion化
"""
import enum
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
logger.disabled = True


class SeqProcessStatus(enum.Enum):
    NOTPROCESSED = enum.auto()
    PROCESSED = enum.auto()
    CONTINUING = enum.auto()
    BREAKED = enum.auto()


class Subsequence(object):

    def longest_inc_subseq(self, seq):
        # TODO: Implement me
        # pass

        argcheck = [seq is None]
        if any(argcheck):
            raise TypeError(
                f'Subsequence.longest_inc_subseq: arg error {seq}')

        argcheck = [seq == []]
        if any(argcheck):
            return []

        return self.find_longest_inc_subseq(seq)

    def find_longest_inc_subseq(self, seq):
        logger.debug(f'Subsequence.find_longest_inc_subseq: {seq}\n')
        seq_len = len(seq)
        max_len = 0
        result = []
        seq_proc_status = [SeqProcessStatus.NOTPROCESSED] * seq_len
        logger.debug(seq_proc_status)

        """
        seq = [3, 4, -1, 0, 6, 2, 3]
        逆順に順々に処理していく。
        1)  まず[-1]の3。次は3より小さいか？2。次は2より小さいか？6は小さくないので無視
            次は2より小さいか。0。次は0より小さいか...
        2)  最初に3,2,0,-1が見つかりこの長さは4。残りが5文字無いと最大長更新は無いので
            処理を行わない
        3)  TODO:done 処理効率化
                    [3, 4, -1, 0, 6, 2, 3]
                    後ろから2番目の2は3の流れに入っているので無視して良い
                    0は3からの流れと6からの流れの双方に関わるため無視しない

                    [3, 4, -1, 0, 100, 101, 102, 2, 3]
                    [-1,0,100,101,102] # 5

        4)  その他:追加テストデータ
                    [-1, 0, 100, 101, 102, 2, 3]
                    [-1,0,100,101,102] # 5

                    [-1, 0, 100, 101, 102, 2, 3,4 ,5]
                    [-1,0,2,3,4,5] #6
        """
        for i, m in enumerate(seq[::-1]):
            tmpresult = []
            current_n = m
            tmpresult.insert(0, m)

            cont_flag = SeqProcessStatus.CONTINUING

            if seq_len - i > max_len and \
                    seq_proc_status[i] == SeqProcessStatus.NOTPROCESSED:  # and以下の条件追加でChallengeのデータで5ループ節約
                for j, n in enumerate(seq[-2 - i::-1]):
                    if current_n > n:
                        tmpresult.insert(0, n)
                        current_n = n
                        if cont_flag == SeqProcessStatus.CONTINUING:
                            seq_proc_status[i + j + 1] = \
                                SeqProcessStatus.PROCESSED
                            logger.debug(
                                f'i:{i} j:{j} i+j:{i+j} n:{n} seq_proc_status:{seq_proc_status}')
                    else:
                        cont_flag = SeqProcessStatus.BREAKED
                    logger.debug(
                        f'n:{n} \t seq[-2 - i::-1][j-1]:{seq[-2 - i::-1][j-1]} \t  tmpresult[0]: {tmpresult[0]} \t i:{i} j:{j} tmpresult: {tmpresult}')
            if max_len < (l := len(tmpresult)):
                max_len = l
                result = tmpresult
        # print(result)
        return result


class TestLongestIncreasingSubseq(unittest.TestCase):

    def test_longest_increasing_subseq(self):
        subseq = Subsequence()
        self.assertRaises(TypeError, subseq.longest_inc_subseq, None)
        self.assertEqual(subseq.longest_inc_subseq([]), [])
        seq = [3, 4, -1, 0, 6, 2, 3]
        expected = [-1, 0, 2, 3]
        self.assertEqual(subseq.longest_inc_subseq(seq), expected)

        seq = [3, 4, -1, 0, 100, 101, 102, 2, 3]
        expected = [-1, 0, 100, 101, 102]  # 5
        self.assertEqual(subseq.longest_inc_subseq(seq), expected)

        seq = [-1, 0, 100, 101, 102, 2, 3]
        expected = [-1, 0, 100, 101, 102]  # 5
        self.assertEqual(subseq.longest_inc_subseq(seq), expected)

        seq = [-1, 0, 100, 101, 102, 2, 3, 4, 5]
        expected = [-1, 0, 2, 3, 4, 5]  # 6
        self.assertEqual(subseq.longest_inc_subseq(seq), expected)

        print('Success: test_longest_increasing_subseq')


def main():
    test = TestLongestIncreasingSubseq()
    test.test_longest_increasing_subseq()


if __name__ == '__main__':
    main()
