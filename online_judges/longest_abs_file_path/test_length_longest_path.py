"""
'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' -> 32

dir \n\t subdir1 \n\t\t file1.ext
                 \n\t\t subsubdir1
    \n\tsubdir2  \n\t\t subsubdir2 \n\t\t\t file2.ext
3       7               10                  9    = 29
   1            1                   1            = 3

'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' -> 32

dir

\n\t
dir subdir1                         [{\n\t:subdir1}]
\n\t\t
dir subdir1 file1.ext               [{\n\t:dir subdir1, \n\t\t:file1.ext}]
\n\t\t
dir subdir1 file1.ext
dir subdir1 subsubdir1              [{\n\t:dir subdir1, \n\t\t:file1.ext}, {\n\t:dir subdir1}]
                                    [{\n\t:dir subdir1, \n\t\t:file1.ext}, {\n\t:dir subdir1, \n\t\t:subsubdir1}]
\n\t
dir subdir1 file1.ext
dir subdir1 subsubdir1
dir subdir2                         [{\n\t:dir subdir1, \n\t\t:file1.ext}, {\n\t:dir subdir1, \n\t\t:subsubdir1},]
\n\t\t
dir subdir1 file1.ext
dir subdir1 subsubdir1
dir subdir2 subsubdir2
\n\t\t\t
dir subdir1 file1.ext
dir subdir1 subsubdir1
dir subdir2 subsubdir2 file2.ext


(\\n)(\\t)+

\\n(\\t)+[\\w.]+ match

"""
from typing import Type
import unittest
import logging
import re

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

    def length_longest_path(self, file_system):
        # TODO: Implement me
        # pass
        if file_system is None:
            raise TypeError(
                f'Solution.length_longest_path: file_system == None')

        if file_system == '':
            return 0

        dic = {}

        m = re.match(r'^\w+', file_system)
        print(m.group())

        dic[0] = m.group()

        regex = r'\n\t+[\w.]+'
        m = re.findall(regex, file_system)
        print(m)

        for n in m:
            print(n.count('\t'))

class TestSolution(unittest.TestCase):

    def test_length_longest_path(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.length_longest_path, None)
        self.assertEqual(solution.length_longest_path(''), 0)
        file_system = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        expected = 32

        solution.length_longest_path(file_system)

        # self.assertEqual(solution.length_longest_path(file_system), expected)
        print('Success: test_length_longest_path')


def main():
    test = TestSolution()
    test.test_length_longest_path()


if __name__ == '__main__':
    main()
