import unittest


class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        # TODO: Implement me
        # pass

        argchks = [num_stacks <= 0, stack_size <= 0]
        if any(argchks):
            raise ValueError(f'Stacks.__init__: arg error')

        self._num_stacks = num_stacks
        self._stack_size = stack_size

        self._lst = [None] * self._num_stacks * self._stack_size

    def abs_index(self, stack_index):
        # TODO: Implement me
        pass

    def set_start_end(self, idx):
        start = idx * self._stack_size
        return start, start + self._stack_size - 1

    def push(self, stack_index, data):
        # TODO: Implement me
        # pass
        start, end = self.set_start_end(stack_index)
        if self._lst[end] is not None:
            # print(f'Stacks.push: stack full')
            raise Exception(f'Stacks.push: stack full')
            # return

        for x in reversed(range(start, end + 1)):
            self._lst[x] = self._lst[x - 1]

        self._lst[start] = data

    def pop(self, stack_index):
        # TODO: Implement me
        # pass
        start, end = self.set_start_end(stack_index)
        if self._lst[start] is None:
            raise Exception('Stacks.pop: emty stack')
            # return

        result = self._lst[start]

        for x in range(start, end):
            self._lst[x] = self._lst[x + 1]
        self._lst[end] = None
        # print(f'pop() will return {result}')
        return result


class TestStacks(unittest.TestCase):

    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        self.assertEqual(stacks.pop(0), 2)
        self.assertEqual(stacks.pop(0), 1)
        self.assertEqual(stacks.pop(1), 3)
        self.assertEqual(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 100
    test = TestStacks()
    test.assertRaises(Exception, test.test_pop_on_empty, num_stacks,
                      stack_size)
    test.assertRaises(Exception, test.test_push_on_full, num_stacks,
                      stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()
