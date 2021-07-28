import logging
import re
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
logger.disabled  = True


class Solution(object):

    def format_license_key(self, license_key, k):
        # TODO: Implement me
        # pass

        dash = '-'
        regex = r'.{'+str(k)+'}'

        if license_key == None or k == None:
            raise TypeError(f'Solution.format_license_key: license_key == None or k == None')

        work_key = license_key
        work_key = re.sub(dash, '', work_key)
        if len(work_key) <= k:
            return ''

        """ 分割して、resultのエレメントとして保管してjoin & upperする"""
        result = []
        # 2-4A0r7-4k
        # 24A0r74k
        # 24-A0r-74k

        """ ダッシュを除いた文字列の長さをkで割りあまりを求める """
        """ 結果の先頭はこのあまりの長さ分になるが、0の場合に結果が
            ダッシュ始まりになってしまう。そのためあまり0の場合は
            resultにアペンドしない。 """
        start_len = len(work_key) % k
        if start_len:
            result.append(work_key[0:start_len])

        m = re.findall(regex, work_key[start_len:])
        for i, match in enumerate(m):
            logger.debug(f'Solution.format_license_key: {i}, {match}')
            result.append(match)

        logger.debug(f'Solution.format_license_key: {license_key}')
        logger.debug(f'Solution.format_license_key: {work_key}')
        logger.debug(f'Solution.format_license_key: {result}')

        return dash.join(result).upper()

class TestSolution(unittest.TestCase):

    def test_format_license_key(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.format_license_key, None, None)
        license_key = '---'
        k = 3
        expected = ''
        self.assertEqual(solution.format_license_key(license_key, k), expected)

        license_key = '2-4A0r7-4k'
        k = 3
        expected = '24-A0R-74K'
        self.assertEqual(solution.format_license_key(license_key, k), expected)

        license_key = '2-4A0r7-4k'
        k = 4
        expected = '24A0-R74K'
        self.assertEqual(solution.format_license_key(license_key, k), expected)
        print('Success: test_format_license_key')

def main():
    test = TestSolution()
    test.test_format_license_key()


if __name__ == '__main__':
    main()
