"""
意味が分からなかったが、"Add two numbers whose digits are stored in a linked list in reverse order"で
googleし、1つ目のエントリーが[参考]に記載したサイト。このExplanationを読んで理解できた。
[参考]
https://leetcode.com/problems/add-two-numbers/ のExplanation

# Input 1: 6->5->None
# Input 2: 9->8->7
# Result: 5->4->8

      56
    +789
    ----
     845 -> 5,4,8

# Input 1: 6->5->4
# Input 2: 9->8->7
# Result: 5->4->2->1

     456
    +789
    ----
    1245 -> 5,4,2,1

first_list、second_list各々に対し
index=0はx1
index=1はx10
index=2はx100
で足していく

足す

reverseしてreturnする

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
logger.disabled = False


class MyLinkedList(LinkedList):

    def add_reverse(self, first_list, second_list):
        # TODO: Implement me
        # pass
        if not first_list or not second_list:
            return None

        """first_list、second_list各々に対し"""
        """index=0はx1"""
        """index=1はx10"""
        """index=2はx100"""
        """で足していく"""
        """足す"""
        result_int = self.make_int(first_list) + self.make_int(second_list)
        # print(f'---{result_int}')

        """reverseしてreturnする"""
        for n in (list(str(result_int))):
            self.insert_to_front(int(n))

        return self

    def make_int(self, lst):
        result = 0
        i = 1
        for n in lst.q:
            # print(f'--- {n.data}')
            result += n.data * i
            i = i * 10
        return result


class TestAddReverse(unittest.TestCase):

    def test_add_reverse(self):
        print('Test: Empty list(s)')
        self.assertEqual(MyLinkedList().add_reverse(None, None), None)
        self.assertEqual(MyLinkedList().add_reverse(Node(5), None), None)
        self.assertEqual(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')


def main():
    test = TestAddReverse()
    test.test_add_reverse()


if __name__ == '__main__':
    main()
