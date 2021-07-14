""" 
[参考]
http://faculty.washington.edu/jstraub/dsa/slides/09Binary%20Trees/540PreorderTraversal.html
http://faculty.washington.edu/jstraub/dsa/slides/09Binary%20Trees/560PostOrderTraversal.html
http://faculty.washington.edu/jstraub/dsa/slides/09Binary%20Trees/510InorderTraversal.html
このコードを見るとなぜpre,in,postなのか良くわかる。

[後悔]
Class Nodeに、楽をするためにクラス変数nodesを作ってしまった。
そのため今回のような2つのツリーでの連続テストに対応する必要があった。
    bst = BstDfs(Node(5))
    一連のテスト
    bst = BstDfs(Node(1))
    一連のテスト
仕方がないのでClass Nodeにメソッドdef clear_nodes()を追加。    
    bst = BstDfs(Node(5))
    一連のテスト
    clear_nodes()
    bst = BstDfs(Node(1))
    一連のテスト
とすることで対応。

[BstDfsのroot]
*traversal()を呼び出す際の引数としてクラスの変数としてrootが期待されている。
一方、ペアレントクラスBstで対応する変数はself.__theRoot。
よって、チャイルドクラスBstDfsで、
    self.root = self.theRoot
とすることで対処療法をとる。

"""
import unittest
import logging
from collections import deque
from enum import Enum  # Python 2 users: Run pip install enum34

from results import Results
from test_bst import Bst, Node

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = True

class State(Enum):
    """copied from test_graph.py"""
    unvisited = 0
    visiting = 1
    visited = 2

class BstDfs(Bst):
    
    def __init__(self, root) -> None:
        super().__init__()    
        root.nodes=[]
        self.theRoot = root
        self.root = self.theRoot
        self.pdq = deque([]) # pdq:Python DeQueue
    
    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                # logger.debug(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')
                print(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')


    def in_order_traversal(self, node, visit_func):
        # TODO: Implement me
        # pass

        if node.left != None: self.in_order_traversal(node.left, visit_func)
        # print(f'- {node} {node.data} {node.left} {node.right}')
        visit_func(node.data)
        if node.right != None: self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        # TODO: Implement me
        # pass
        # print(f'-- {node} {node.data} {node.left} {node.right}')
        visit_func(node.data)
        if node.left != None: self.pre_order_traversal(node.left, visit_func)
        if node.right != None: self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self,node, visit_func):
        # TODO: Implement me
        # pass
        if node.left != None: self.post_order_traversal(node.left, visit_func)
        if node.right != None: self.post_order_traversal(node.right, visit_func)
        # print(f'-- {node} {node.data} {node.left} {node.right}')
        visit_func(node.data)


class TestDfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDfs, self).__init__()
        self.results = Results()

    def test_dfs(self):
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        # bst.ls_nodes()

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        bst.theRoot.clear_nodes()

        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        # bst.ls_nodes()

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()
