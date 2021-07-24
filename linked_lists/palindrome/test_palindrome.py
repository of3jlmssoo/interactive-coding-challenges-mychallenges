"""
最近電車内で読んだpython関連のサイトでpalindromeが扱われていたので回分であることはすんなり理解。
ここでの課題はリンクリスト全体が回分になっているかどうか？であり、リンクリストの中に回分があるか？ではない。
そのためロジックは後者のケースに比べシンプルになる。

ループ回数はself.q//2回
一番前と一番後ろの比較から始めて内側に移動する
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

    def is_palindrome(self):
        # TODO: Implement me
        # pass
        """Empty list -> False"""
        """Single element list -> False"""
        if len(self.q) < 2:
            return False
        """Two or more element list, not a palindrome -> False"""
        """General case: Palindrome with even length -> True"""
        """General case: Palindrome with odd length -> True"""
        result = True
        for i in range(len(self.q) // 2):
            logger.debug(f'---{self.q[i].data} and {self.q[-1-i].data}')
            if self.q[i].data != self.q[-1 - i].data:
                result = False
        return result


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        # linked_list.ls_nodes()
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()
