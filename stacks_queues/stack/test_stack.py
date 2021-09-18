import unittest
import copy
from test_linked_list import Node
import logging


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

# class Node(object):

#     def __init__(self, data):
#         # TODO: Implement me
#         pass


class Stack(object):

    def __init__(self, top=None):
        # TODO: Implement me
        # pass

        self._start_node = top if top else None

    def push(self, data):
        # TODO: Implement me
        # pass

        next_node = None
        if self._start_node:
            next_node = copy.deepcopy(self._start_node)
        self._start_node = Node(data)
        if next_node:
            self._start_node.link = next_node

    def pop(self):
        # TODO: Implement me
        # pass
        if not self._start_node:
            return None

        logger.debug(f'pop() 1 {self._start_node=} {self._start_node.data=}')
        result = self._start_node.data
        # if self._start_node.link is not None:
        #     self._start_node = self._start_node.link
        # else:
        #     self._start_node = None
        self._start_node = self._start_node.link if self._start_node.link is not None else None

        logger.debug(f'pop() 2 {self._start_node=} {result=}')
        return result

    def peek(self):
        # TODO: Implement me
        # pass
        # if not self._start_node:
        #     return None
        # return self._start_node.data
        return self._start_node.data if self._start_node else None

    def is_empty(self):
        # TODO: Implement me
        # pass
        return False if self._start_node else True

    def list_nodes(self):
        if not self._start_node:
            return

        current_node = self._start_node
        print(f'{current_node.data=}')
        while current_node.link is not None:
            current_node = current_node.link
            print(f'{current_node.data=}')

    # def list_nodes2(self):
    #     # if self._start_node:
    #     #     current_node = self._start_node
    #     # else:
    #     #     return
    #     if not self._start_node:
    #         return
    #     current_node = self._start_node
    #     while current_node.link is not None:
    #         print(f'{current_node.data=}')
    #         current_node = current_node.link
    #     print(f'{current_node.data=}')


class TestStack(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        # self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        # stack.list_nodes()
        self.assertEqual(stack.pop(), 3)
        # stack.list_nodes()
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        # stack.list_nodes()
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.is_empty(), True)

        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
