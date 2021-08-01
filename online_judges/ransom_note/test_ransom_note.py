import unittest
import copy


class Solution(object):

    def match_note_to_magazine(self, ransom_note, magazine):
        # TODO: Implement me
        # pass

        if ransom_note is None:
            raise TypeError(
                f'Solution.match_note_to_magazine: ransom_note is None')

        if ransom_note == '' and magazine == '':
            return True

        mag_letters = copy.deepcopy(list(magazine))
        for c in ransom_note:
            try:
                mag_letters.remove(c)
            except ValueError:
                return False
        return True


class TestRansomNote(unittest.TestCase):

    def test_ransom_note(self):
        solution = Solution()
        self.assertRaises(
            TypeError,
            solution.match_note_to_magazine,
            None,
            None)
        self.assertEqual(solution.match_note_to_magazine('', ''), True)
        self.assertEqual(solution.match_note_to_magazine('a', 'b'), False)
        self.assertEqual(solution.match_note_to_magazine('aa', 'ab'), False)
        self.assertEqual(solution.match_note_to_magazine('aa', 'aab'), True)
        print('Success: test_ransom_note')


def main():
    test = TestRansomNote()
    test.test_ransom_note()


if __name__ == '__main__':
    main()
