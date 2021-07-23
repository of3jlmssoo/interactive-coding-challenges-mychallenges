"""
[課題]
今ひとつ理解できず。
Test Casesは以下の記述。
Delete on empty list -> None
Delete None -> None
Delete on one node -> [None]
Delete on multiple nodes

実際のテストは以下の4つ。Test Casesと上手く関連付けできず。
1)テスト1
MyLinkedList(None)
delete_node(None)
(しかし)get_all_data()で[]を返す。
ということは、MyLinkedList(None)でself.q=[None]とする。
test_linked_listのLinkedListではself.qにNoneは含めないようになっている
この点の修正が必要

2) テスト2
Noneではない唯一のエントリーを削除した場合self.q=[None]とする
self.headの修正も必要

3) テスト3
最初でのもなく最後でもないエントリーを削除した場合Noneは登場せず
削除したエントリーの前後をつなげる

4) テスト4
最後のエントリーを削除した場合最後のエントリーをNoneにする。
直前のエントリーのnode.linkをNoneに設定する

"""
import unittest
import logging
from test_linked_list import Node, LinkedList

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

    def __init__(self, head):
        super().__init__(head=head)
        """Noneをnodeとして追加する。self.qが空の時のみNoneをノードとしてセットする"""
        if not self.q and head is None:
            self.q = [None]

    def insert_to_front(self, data):
        logger.debug(f'MyLinkedList.insert_to_front. called {data} {self.q}')
        """ self.q = [None]の場合self.qをクリアした上でinsert_to_front()をコールする
            オリジナルのinsert_to_front()はreturn self.nodeしないため、オリジナルの
            nodeをself.nodeにした上でreturn self.nodeする
        """
        if len(self.q) == 1 and self.q[0] is None:
            self.q = []
        super().insert_to_front(data)
        return self.node

    def delete_node(self, node):
        logger.debug(f'MyLinkedList.delete_node 1. called {self.q}')
        """ 1)テスト1
            MyLinkedList(None)
            delete_node(None)
            (しかし)get_all_data()で[]を返す。
            ということは、MyLinkedList(None)でself.q=[None]とする。
            test_linked_listのLinkedListではself.qにNoneは含めないようになっている
            この点の修正が必要
            2) テスト2
            Noneではない唯一のエントリーを削除した場合self.q=[None]とする
            self.headの修正も必要
        """
        if len(self.q) == 1:
            if node is None:
                self.q = []
            else:
                self.q[0] = None
            return
        """ 3) テスト3
            最初でのもなく最後でもないエントリーを削除した場合Noneは登場せず
            削除したエントリーの前後をつなげる
            0 1 2 3 4
            [1,2,3,4,5]
                A
        """
        logger.debug(
            f'MyLinkedList.delete_node 3-1. called {node} -- and -- {self.q}')
        logger.debug(
            f'MyLinkedList.delete_node 3-2. called {self.q.index(node)}  {len(self.q) - 1}')
        idx = self.q.index(node)
        if 1 < idx < (len(self.q) - 1):
            """ 最初と最後以外のノードを処理 """
            self.q = list(filter(lambda x: x != node, self.q))  # 該当エレメントを削除
            self.q[idx - 1].link = self.q[idx]                  # リンクを処理
            if not logger.disabled:
                for n in self.q:
                    print(
                        f'MyLinkedList.delete_node 3-3.{n.data} and {n.link}')
            """ 4) テスト4
                最後のエントリーを削除した場合最後のエントリーをNoneにする。
                直前のエントリーのnode.linkをNoneに設定する
            """
        elif idx == len(self.q) - 1:
            """ 最後のノードを処理 """
            self.q[-1] = None
            self.q[-2].link = self.q[-1]

        if not logger.disabled:
            for n in self.q:
                if n is not None:
                    print(
                        f'MyLinkedList.delete_node 3-4.{n.data} and {n.link}')
                else:
                    print(
                        f'MyLinkedList.delete_node 3-5.{n}')
        logger.debug(f'MyLinkedList.delete_node. end {self.q}')

    def ls_nodes(self):
        print(f'MyLinkedList.ls_nodes. {self.q}')

    # def get_all_data(self):
    #     # pass
    #     # TODO: Implement me
    #     return [n.data if n is not None else None for n in self.q]


class TestDeleteNode(unittest.TestCase):

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        self.assertEqual(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        self.assertEqual(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')


def main():
    test = TestDeleteNode()
    test.test_delete_node()


if __name__ == '__main__':
    main()
