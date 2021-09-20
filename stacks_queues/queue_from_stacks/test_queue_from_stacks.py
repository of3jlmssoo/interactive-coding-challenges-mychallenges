"""
[参照]
https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks

enqueue(0)
            0
            stackA
enqueue(1)
            1
            0
            stackA
enqueue(2)
            2
            1
            0
            stackA
dequeue()
                        2
                    1
                    0
            stackA  stackB
dequeue()
                        1
                    0
            stackA  stackB
dequeue()
                        0
            stackA  stackB
enqueue(5)
            5
            stackA
dequeue()
                    5
            stackA  stackB
"""
import unittest
from test_stack import Stack
from test_linked_list import Node


class QueueFromStacks(object):

    def __init__(self):
        # TODO: Implement me
        # pass
        self.stackA = Stack(None)
        self.stackB = Stack(None)

    def shift_stacks(self, source, destination):
        # TODO: Implement me
        # pass
        while source.peek() is not None:
            destination.push(source.pop())

    def enqueue(self, data):
        # TODO: Implement me
        # pass
        self.shift_stacks(self.stackB, self.stackA)
        self.stackA.push(data)

    def dequeue(self):
        # TODO: Implement me
        # pass
        # print(f'{self.stackB.pop()=}')
        self.shift_stacks(self.stackA, self.stackB)
        return self.stackB.pop()

    def list_queues(self):
        print(f'QueueFromStacks.list_queues: called. stackA')
        self.stackA.list_nodes()
        print('\nstackB')
        self.stackB.list_nodes()
        print('\n')


class TestQueueFromStacks(unittest.TestCase):

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        # queue.list_queues()

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        self.assertEqual(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == '__main__':
    main()
