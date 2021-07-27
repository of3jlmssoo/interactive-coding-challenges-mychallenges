"""
Is the input sorted by time?    No
Can you have enter and exit elements for the same timestamp?
    Yes you can, order of enter and exit is not guaranteed

            Data(1, 2, EventType.ENTER), 2
            Data(3, 2, EventType.EXIT),
            Data(3, 1, EventType.ENTER), 1
            Data(7, 3, EventType.ENTER), 4
            Data(8, 2, EventType.EXIT),  2
            Data(9, 2, EventType.EXIT),  0

            Period(7, 8)) 7 to 8

折角なので、積極的理由は無いがpandasを使う。

- timestampを集約して
- num_peopleが最大の行を識別し
- 最大の行＋次の行をリスト化する
"""
import logging
import unittest
from enum import Enum
from typing import Type

import pandas as pd

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


class Data(object):

    def __init__(self, timestamp, num_people, event_type):
        self.timestamp = timestamp
        self.num_people = num_people
        self.event_type = event_type

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Period(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return str(self.start) + ', ' + str(self.end)


class EventType(Enum):

    ENTER = 0
    EXIT = 1


class Solution(object):

    def find_busiest_period(self, data):
        # TODO: Implement me
        # pass
        if data is None:
            raise TypeError(f'Solution.find_busiest_period: data == None')

        if data == []:
            return None

        df_in = self.make_dfin(data)                # インプットデータのpandas dataframe化
        grouped_df_in = df_in.groupby('timestamp')  # timestampが重複しているのでgroupby
        summary_df = (grouped_df_in.sum().cumsum()) # 重複をsumして更に累積化
        idx = summary_df.index.get_loc(summary_df['signed_num_people'].idxmax()) # num_peopleが最大の行インデックスをidxに保存
        data_for_Period =  list(summary_df.index[idx:idx+2]) # timestampがdataframeのindexとなっているので最大のインデックスと次のインデックスをリスト化する 
        return Period(data_for_Period[0], data_for_Period[1])

    def make_dfout(self):
        return pd.DataFrame(columns=['timestamp', 'num_people'])

    def make_dfin(self, data):
        df = pd.DataFrame(columns=['timestamp', 'num_people', 'event_type'])

        for d in data:
            # print(d, d.timestamp, d.num_people, d.event_type)
            df = df.append({'timestamp': d.timestamp,
                           'num_people': d.num_people,
                           'signed_num_people': self.mk_signed_nump(d.num_people, d.event_type),
                            'event_type': d.event_type},
                           ignore_index=True)
        df = df.sort_values('timestamp')
        return df

    def mk_signed_nump(self,num,event_type):
        if event_type == EventType.EXIT:
            num = num * -1
        return num

class TestSolution(unittest.TestCase):

    def test_find_busiest_period(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_busiest_period, None)
        self.assertEqual(solution.find_busiest_period([]), None)
        data = [
            Data(3, 2, EventType.EXIT),
            Data(1, 2, EventType.ENTER),
            Data(3, 1, EventType.ENTER),
            Data(7, 3, EventType.ENTER),
            Data(9, 2, EventType.EXIT),
            Data(8, 2, EventType.EXIT),
        ]

        # solution.find_busiest_period(data)

        self.assertEqual(solution.find_busiest_period(data), Period(7, 8))
        print('Success: test_find_busiest_period')


def main():
    test = TestSolution()
    test.test_find_busiest_period()


if __name__ == '__main__':
    main()
