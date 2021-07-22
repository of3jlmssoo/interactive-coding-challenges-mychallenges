import unittest
import unittest
import logging
# from test_delete_mid import MyLinkedList
from test_linked_list import LinkedList, Node

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


class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        # TODO: Implement me
        # pass

        # Empty list -> None
        # k is >= the length of the linked list -> None
        if not self.q or k >= len(self.q):
            return None
        # One element, k = 0 -> element
        # General case with many elements, k < length of linked list
        return self.q[k].data


class Test(unittest.TestCase):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        self.assertEqual(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()
