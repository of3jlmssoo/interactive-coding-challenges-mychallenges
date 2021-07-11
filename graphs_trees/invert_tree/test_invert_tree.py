"""
                5
            2       7
          1   3    6  9

単純にオリジナルのツリーのleftとrightを入れ替えれば良いのか。
-> 単純に入れ替える。

[課題]
1)  class InverseBst(Bst)はbst = InverseBst(root)でrootを引数にしている。
    一方、class Bst(object):はdef __init__(self):で引数無し
2)  Bstのinsert()はリターン無し。InverseBstのinsertはnode2 = bst.insert(2)でreturnを期待

"""
import logging
import unittest
from test_bst import Node, Bst

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


def swap_left_right(self):
    """入替えメソッド。invert_tree()でNodeに追加する"""
    self.left, self.right = self.right, self.left

class InverseBst(Bst):

    def __init__(self, root) -> None:
        """1)に対応。test_bst.pyにsetterを追加している"""
        super().__init__()    
        self.theRoot = root

    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                logger.debug(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')


    def invert_tree(self):
        # TODO: Implement me
        # pass
        Node.swap_left_right = swap_left_right
        for n in self.theRoot.nodes:
            # print(n, n.left, n.right,'\n')
            n.swap_left_right()
            # print(n, n.left, n.right,'\n')
        return self.theRoot            

    def insert(self, data):
        """Bst()のメソッドに処理(return)を追加"""
        super().insert(data)
        return self.node



class TestInvertTree(unittest.TestCase):

    def test_invert_tree(self):
        root = Node(5)
        bst = InverseBst(root)
        node2 = bst.insert(2)
        node3 = bst.insert(3)
        node1 = bst.insert(1)
        node7 = bst.insert(7)
        node6 = bst.insert(6)
        node9 = bst.insert(9)

        # root.ls_nodes()

        result = bst.invert_tree()
        
        self.assertEqual(result, root)
        self.assertEqual(result.left, node7)
        self.assertEqual(result.right, node2)
        self.assertEqual(result.left.left, node9)
        self.assertEqual(result.left.right, node6)
        self.assertEqual(result.right.left, node3)
        self.assertEqual(result.right.right, node1)

        print('Success: test_invert_tree')

        print(f'issubclass? {issubclass(InverseBst,Bst)}')
        print(f'InverseBst.mro() : {InverseBst.mro()}')

def main():
    test = TestInvertTree()
    test.test_invert_tree()


if __name__ == '__main__':
    main()
