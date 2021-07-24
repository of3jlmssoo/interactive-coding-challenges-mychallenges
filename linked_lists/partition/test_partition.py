"""
リストを3つ用意する。1つはless_nodesでもう1つはgreater_nodes、最後はsame_nodes
元のリストから1つずつエレメントを取り出す
    Xより小さければless_nodes
    Xと同じならsame_nodes
    Xより大きければgreater_nodes
less_nodes+same_nodes+greater_nodesを返す

"""
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
logger.disabled = True


class MyLinkedList(LinkedList):

    def partition(self, data):
        # TODO: Implement me
        pass

        """Empty list -> []"""
        """One element list -> [element]"""
        if len(self.q) < 2:
            print(f'MyLinkedList.partition: {self.q}')
            return self.q

        """Left linked list is empty"""
        """Right linked list is empty"""
        """General case"""
        """Partition = 10"""
        """Input: 4, 3, 7, 8, 10, 1, 10, 12"""
        """Output: 4, 3, 7, 8, 1, 10, 10, 12"""

        """リストを3つ用意する。1つはless_nodesでもう1つはgreater_nodes、最後はsame_nodes"""
        less_nodes = []
        same_nodes = []
        greater_nodes = []
        """元のリストから1つずつエレメントを取り出す"""
        """    Xより小さければless_nodes"""
        """    Xと同じならsame_nodes"""
        """    Xより大きければgreater_nodes"""

        for n in self.q:
            if n.data < data:
                less_nodes.append(n)
            if n.data == data:
                same_nodes.append(n)
            if n.data > data:
                greater_nodes.append(n)
        """less_nodes+same_nodes+greater_nodesを返す"""
        self.q = less_nodes + same_nodes + greater_nodes
        return self


class TestPartition(unittest.TestCase):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        self.assertEqual(partitioned_list.get_all_data(),
                         [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()
