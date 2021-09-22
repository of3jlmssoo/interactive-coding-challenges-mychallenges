"""
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

self.assertEqual(queue.dequeue(), 2)
self.assertEqual(queue.dequeue(), 3)
self.assertEqual(queue.dequeue(), 4)

順番
2
2 3
2 3 4
3 4
4

If there is one item in the list, do you expect the first and last pointers to both point to it?
Yes
=> the first pointerとthe last pointerがあることになっている
"""
import unittest


class Node(object):

    def __init__(self, data):
        # TODO: Implement me
        # pass
        self._data = data
        self._link = None

    @property
    def data(self):
        return self._data

    # @data.setter
    # def data(self, value):
    #     self._data = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value


class Queue(object):

    def __init__(self):
        # TODO: Implement me
        # pass
        self._start_pointer = None
        self._last_pointer = None

    def enqueue(self, data):
        # TODO: Implement me
        # pass
        data_node = Node(data)
        if self._start_pointer is None and self._last_pointer is None:
            self._start_pointer = data_node
            self._last_pointer = data_node
            return

        self._last_pointer.link = data_node
        self._last_pointer = data_node

    def dequeue(self):
        # TODO: Implement me
        # pass
        if self._start_pointer is None and self._last_pointer is None:
            return None

        result = self._start_pointer.data
        dequeued_node = self._start_pointer
        if self._start_pointer == self._last_pointer:
            # result = self._start_pointer.data
            # dequeued_node = self._start_pointer
            self._start_pointer = None
            self._last_pointer = None
            del dequeued_node
            return result

        # result = self._start_pointer.data
        # dequeued_node = self._start_pointer
        self._start_pointer = self._start_pointer.link
        del dequeued_node
        return result


class TestQueue(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        self.assertEqual(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
