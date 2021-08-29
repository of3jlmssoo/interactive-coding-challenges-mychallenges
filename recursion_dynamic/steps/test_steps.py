"""
recursion_dynamicの中の順番を間違えた気がする。これをまず行うべきだった
"""
import unittest


class Steps(object):

    def count_ways(self, num_steps):
        # TODO: Implement me
        # pass

        chkargs = [num_steps is None, num_steps == -1]
        if any(chkargs):
            raise TypeError(f'Step.count_ways: {num_steps=}')

        _steps = [1, 2, 3]
        _total = 0
        return self._count_ways(_steps, num_steps, _total)

    def _count_ways(self, _steps, num_steps, _total):

        if _total > num_steps:
            return 0
        if _total == num_steps:
            return 1

        result = 0
        for s in _steps:
            result += self._count_ways(_steps, num_steps, _total + s)

        return result


class TestSteps(unittest.TestCase):

    def test_steps(self):
        steps = Steps()
        self.assertRaises(TypeError, steps.count_ways, None)
        self.assertRaises(TypeError, steps.count_ways, -1)
        self.assertEqual(steps.count_ways(0), 1)
        self.assertEqual(steps.count_ways(1), 1)
        self.assertEqual(steps.count_ways(2), 2)
        self.assertEqual(steps.count_ways(3), 4)
        self.assertEqual(steps.count_ways(4), 7)
        self.assertEqual(steps.count_ways(10), 274)
        print('Success: test_steps')


def main():
    test = TestSteps()
    test.test_steps()


if __name__ == '__main__':
    main()
