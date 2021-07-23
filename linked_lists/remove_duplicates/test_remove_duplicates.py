import unittest
import logging
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

    def remove_dupes(self):
        # TODO: Implement me
        pass

        # Empty linked list -> []
        if not self.q:
            return self.q
        # One element linked list -> [element]
        # General case with no duplicates
        # General case with duplicates


class TestRemoveDupes(unittest.TestCase):

    def test_remove_dupes(self, linked_list):
        print('Test: Empty list')
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        # linked_list.insert_to_front(1)
        # linked_list.insert_to_front(1)
        # linked_list.insert_to_front(3)
        # linked_list.insert_to_front(2)
        # linked_list.insert_to_front(3)
        # linked_list.insert_to_front(1)
        # linked_list.insert_to_front(1)
        # linked_list.remove_dupes()
        # self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        # print('Test: General case, no duplicates')
        # linked_list.remove_dupes()
        # self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print('Success: test_remove_dupes\n')


def main():
    test = TestRemoveDupes()
    linked_list = MyLinkedList(None)
    test.test_remove_dupes(linked_list)


if __name__ == '__main__':
    main()
