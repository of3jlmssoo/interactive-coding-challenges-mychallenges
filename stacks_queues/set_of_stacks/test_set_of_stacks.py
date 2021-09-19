import unittest
from test_stack import Stack
from test_linked_list import Node


class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        # TODO: Implement me
        # pass
        self._num_element = []
        self._stack_lst = []
        self._capacity = capacity

        self.make_new_stack()

    def make_new_stack(self):
        self._num_element.append(0)
        self._stack_lst.append(Stack(None))

    def push(self, data):
        # TODO: Implement me
        # pass
        if self.is_full():
            self.make_new_stack()

        self._num_element[-1] += 1
        self._stack_lst[-1].push(data)

    def pop(self):
        # TODO: Implement me
        # pass
        if not self._stack_lst:
            return None

        result = self._stack_lst[-1].pop()
        self._num_element[-1] -= 1

        if self._num_element[-1] == 0:
            self._num_element.pop(-1)
            self._stack_lst.pop(-1)

        return result

    def is_full(self):
        # TODO: Implement me
        # pass
        return True if self._num_element[-1] == self._capacity else False


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        # TODO: Implement me
        # pass
        self.stack_with_capacity = StackWithCapacity(
            None, indiv_stack_capacity)

    def push(self, data):
        # TODO: Implement me
        # pass
        self.stack_with_capacity.push(data)

    def pop(self):
        # TODO: Implement me
        # pass
        return self.stack_with_capacity.pop()


class TestSetOfStacks(unittest.TestCase):

    def test_set_of_stacks(self):
        print('Test: Push on an empty stack')
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print('Test: Push on a non-empty stack')
        stacks.push(5)

        print('Test: Push on a capacity stack to create a new one')
        stacks.push('a')

        print('Test: Pop on a stack to destroy it')
        self.assertEqual(stacks.pop(), 'a')

        print('Test: Pop general case')
        self.assertEqual(stacks.pop(), 5)
        self.assertEqual(stacks.pop(), 3)

        print('Test: Pop on no elements')
        self.assertEqual(stacks.pop(), None)

        print('Success: test_set_of_stacks')


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == '__main__':
    main()
