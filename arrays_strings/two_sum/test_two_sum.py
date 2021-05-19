import unittest


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.two_sum, None, None)
        self.assertRaises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


class MyTest(unittest.TestCase):

    def test_two_sum(self):
        print(f'start of MyTest')
        solution = Solution()
        self.assertRaises(TypeError, solution.two_sum, None, None)
        self.assertRaises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(solution.two_sum(nums, target), expected)
        target = 8; expected = [1, 4]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = 6; expected = [0, 4]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = 5; expected = [1, 2]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = 4; expected = [0, 1]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = 3; expected = [0, 2]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = -6; expected = [0, 3]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = -4; expected = [1, 3]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = -5; expected = [2, 3]; self.assertEqual(solution.two_sum(nums, target), expected)
        target = -2; expected = [3, 4]; self.assertEqual(solution.two_sum(nums, target), expected)
        print(f'end of MyTest')

class Solution():

    def two_sum(self, nums: list, target: int) -> list:
        """two_sum find two indicesなので、足してtargetになる2つの値の組合せを探し、その値のインデックスを返す。
        3つ以上の組合せは考慮しなくて良い。
        また、Is there exactly one solution? Yesなので1つ組合せが見つかったら終えて良い

        Args:
            nums   (list): 探索対象のリスト
            target (int) : 合計してこの値になる

        Returns:
            str: 一文字の異なるキャラクター

        TestCases:
            None input -> TypeError
            [] -> ValueError
            [1, 3, 2, -7, 5], 7 -> [2, 4]
        """
        if nums == None or target == None:
            raise TypeError('TypeError : None specified in nums or target')
        if nums == []:
            raise ValueError('ValueErrr : None specified in nums or target')
        for i, num  in enumerate(nums):
            if (num2 := target - num) in nums:
                return [i,nums.index(num2)]       




if __name__ == '__main__':
    main()
    test = MyTest()
    test.test_two_sum()
