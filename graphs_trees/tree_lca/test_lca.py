"""
[方針]
self.assertEqual(binary_tree.lca(root, node1, node8), node3)
node1からrootまでパスを記録する
node8からrootまでパスを記録する
短い方のパスについてindex=1から処理を行う
    長い方のパスにあるかどうか
    あったらそれを返す

[考慮点1]
問題の一部として提供されているclass Node(object):にself.parentが無い。
これは追加すれば良いとする。
しかし、class TestLowestCommonAncestor(unittest.TestCase)に
手を入れないとするとself.parent情報をセットする機会が無い。
	root = node10
	node0 = Node(0)
	binary_tree = BinaryTree()
	self.assertEqual(binary_tree.lca(root, node0, node5), None)
	self.assertEqual(binary_tree.lca(root, node5, node0), None)
１行目でrootをセットしているが、これが使われるのは、4行目以降。
よってbinary_tree.lca()の中でself.parentをセットすることにする。

[考慮点2]
ツリーが1つではない。
rootからツリー情報を作成する際、keyをリストに保管しておく。
node1とnode2についてin the listをチェックしてなければNoneを返す。
"""
import unittest
import logging
from collections import deque



logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = False

class Node(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

        self.parent = None

    def __repr__(self):
        return str(self.key)

class BinaryTree(object):

    def __init__(self):
        self.nodes = []

    def setParent(self,node):
        self.nodes.append(node)
        if node.left != None: 
            node.left.parent = node
            self.setParent(node.left)
        if node.right != None: 
            node.right.parent = node
            self.setParent(node.right)

    def viewTree(self,root):
        """
                    10
                5       9
              12  3   18  20
                 1 8     40
        d1の推移
            10              while in whileでd2に移す処理。left or rigthがある場合d1にappendする
            5 9             同上
            12 3 18 20      同上
            1 8 40          同上
        """
        d1 = deque([root])
        d2 = deque([])
        while len(d1):
            # whileループ中でd1の中身をd2に移す
            while len(d1):           
                d2.append(d1.pop())
            # print(f'---+ ')
            # d2の中身を全て処理する。left or rigthがある場合d1にappendする
            while len(d2):
                node = d2.pop()
                # print(f'{node} ', end='') 
                if node.left != None:   d1.append(node.left)
                if node.right != None:  d1.append(node.right) 



    def lca(self, root, node1, node2):
        # TODO: Implement me
        # pass

        # self.parentをセットする。keyをself.nodesにappendする
        self.setParent(root)
        self.viewTree(root)
        
        # node1とnode2が共にself.nodesにinでなければNoneを返す
        if node1 not in self.nodes and node2 not in self.nodes:
            return None

        # node1からrootへ辿る(パス)。node2からrootへ辿る(パス)
        self.__lst1 = []
        self.__lst2 = []
        self.makePathToRoot(self.__lst1, node1)
        self.makePathToRoot(self.__lst2, node2)

        # print(f'--------------------- {self.__lst1}')
        # print(f'--------------------- {self.__lst2}')

        if len(self.__lst1) > len(self.__lst2): 
            result = self.findLCA(self.__lst2,self.__lst1)
        else:
            result = self.findLCA(self.__lst1,self.__lst2)
        # print(f'--------result:{result}')
        return result

    def findLCA(self, lst1, lst2): # Find the lowest common ancestor
        for n in lst1: 
            if n in lst2:
                return n

    def makePathToRoot(self,lst,node):
        while(node.parent != None):
            lst.append(node)
            node = node.parent
        lst.append(node) # append for root node
        
        

        # 短い方のindex=1から順に長い方のパスに存在するかチェックする。あればそれを返す
class TestLowestCommonAncestor(unittest.TestCase):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        self.assertEqual(binary_tree.lca(root, node0, node5), None)
        self.assertEqual(binary_tree.lca(root, node5, node0), None)

        # binary_tree.lca(root, node1, node8)
        
        self.assertEqual(binary_tree.lca(root, node1, node8), node3)
        self.assertEqual(binary_tree.lca(root, node12, node8), node5)
        self.assertEqual(binary_tree.lca(root, node12, node40), node10)
        self.assertEqual(binary_tree.lca(root, node9, node20), node9)
        self.assertEqual(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()
