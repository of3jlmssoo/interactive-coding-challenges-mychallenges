"""
[前提]
前提をおく。
- 重複は無い

[考慮点]
- そもそもNode情報を辿ってループの開始ノードを見つければ良いのか？
　あるいは、self.qもセットした上でループの開始ノードを見つけるのか？ <= これを目指す

- find_loop_start()が返すのはNoneかノード(ループの開始となるノード)
- Is this a singly linked list? Yesなのでループは1つと考えて良さそう

- LinkedList/MyLinkedList.__init__の拡張
  LinkedList/MyLinkedListとNodeの呼び方の観点で、テストの前半はこれまでと同様。
  後半は新しい形態。LinkedList/MyLinkedListを呼ばずにNodeのコールだけでリンク情報が
  形成される(これまではNode(data)だったのがここではNode(data,link)で呼び出し)。
  その上で linked_list = MyLinkedList(node0)して
  self.assertEqual(linked_list.find_loop_start(), node3)している
  この呼び出し形態及びこれまでのLinkedList/MyLinkedListだと、self.qが形成されない
  よって、__init__を拡張する。

  LinkedList/MyLinkedListのself.qをfor inしてもノードを取り出すだけなので
  node.nextがループしていも問題は無いが、self.qを作る際が問題。
  ループを回り続けることになる。

  link!=None and node.next not existingの場合、insert_to_frontを呼ぶとinsert_to_front内で
  Node()がコールされるのでinsert_to_frontは使わずself.qにappendする形式をとる

- 素直にnode.nextにしておくべきだった。。。
    - vs codeのChange All occurrencesでlinkをnextに
    - self.nextを追加してself.next用setter/getterを作成しsetterでself.link = self.next
    - import Nodeをやめてcopy Nodeしてnext versionを作る。。。


1) Node() of test_linked_list.py改修
    Nodeでself.next = self.link
    self.next用のsetter/getter

2)  MyLinkedList.__init__
    node.linkがinstance(node.link,Node)の場合ループ
        node.dataが既にある場合self.__loop_startにセットの上break
        node.dataが初の場合記録
        nodeがself.qに無い場合アペンド
        node = node.link
3)  find_loop_start()が返すのはNoneかノード

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

    def __init__(self, head=None):

        self.__loop_start = None

        super().__init__(head=head)

        """
        2)  MyLinkedList.__init__
            node.linkがinstance(node.link,Node)の場合ループ
                node.dataが既にある場合self.__loop_startにセットの上break
                node.dataが初の場合記録
                nodeがself.qに無い場合アペンド
                node = node.link
        """
        """
        3)  find_loop_start()が返すのはNoneかノード
        """
        if head:
            logger.debug(f'MyLinkedList.__init__ 1: {self.head} {self.q}')
            already_exist = []
            n = self.head.next
            while isinstance(n, Node):  # and n.data not in already_exist:
                logger.debug(
                    f'MyLinkedList.__init__ 2: {already_exist} {n.data}')
                # self.__loop_start = n.data
                if n.data in already_exist:
                    self.__loop_start = n
                    break
                already_exist.append(n.data)
                if n not in self.q:
                    self.q.append(n)
                n = n.next
            logger.debug(
                f'MyLinkedList.__init__ 3:{self.q} {self.__loop_start}')

    def find_loop_start(self):
        """
        3)  find_loop_start()が返すのはNoneかノード
        """
        # TODO: Implement me
        # pass
        if self.__loop_start is None or isinstance(self.__loop_start, Node):
            return self.__loop_start
        else:
            print(f'MyLinkedList.find_loop_start: something wrong...')


class TestFindLoopStart(unittest.TestCase):

    def my_test(self):
        print('my test starts 1.')
        node3 = Node(3)
        linked_list = MyLinkedList(node3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(1)
        # linked_list.ls_nodes()
        node3.next = linked_list.q[0]
        # linked_list.ls_nodes()
        print('my test starts 2.')
        node3 = Node(3)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        linked_list = MyLinkedList(node1)
        print('my test starts 3.')
        node3 = Node(3)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node3.next = node1
        linked_list = MyLinkedList(node1)

    def test_find_loop_start(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: One element')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Two elements')
        linked_list.append(2)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Three or more elements')
        linked_list.append(3)
        self.assertEqual(linked_list.find_loop_start(), None)

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyLinkedList(node0)
        self.assertEqual(linked_list.find_loop_start(), node3)

        print('Success: test_find_loop_start')


def main():
    test = TestFindLoopStart()
    test.test_find_loop_start()
    test.my_test()


if __name__ == '__main__':
    main()
