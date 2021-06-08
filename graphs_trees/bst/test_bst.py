""" test_bst.py
[既存コードの修正]
class TestTreeの__init__とin_order_traversalのところは修正を行った。

[参考情報]
(1) https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%9C%A8   
(2) https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2
(3) https://en.wikipedia.org/wiki/Tree_traversal

(1)を参考にclassの構造を決める


[0-9でのできあがりイメージ例]
データ入力順番 6 2 1 4 0 3 5 7 9 8

      6   
   2     7
 1   4      9
0   3 5    8

in-orderの場合のアウトプット順 0 1 2 3 4 5 6 7 8 9


[insertの処理の流れ]
node : ツリーにインサートされるノード
current_node : 
    ・最初はルートノードが設定される。最終的にはnodeの親ノードが設定される
    ・ループ
        ・dataの大小によりcurrent_nodeのleftかrightが選ばれる
        ・left or rightがNoneであればこのcurrent_nodoが親ノードになる
        ・left of rightがNoneでなければleft or rigthに設定されたノードをcurrent_nodeにセットする


[insert処理の流れメモ]
6 > 4
    2 > 1: 2.left = 1
    2 < 4: 2.right = 4 

6 > 0
    2 > 0
        1 > 0: 1.left = 0
6 > 3
    2 < 3
        4 > 3: 4.left = 3

6 > 5
    2 < 5
        4 < 5: 4.right = 5

まずルートと比較
    2と比較
        １と比較
        ４と比較

[(3)の情報 inorder]
inorder(node)
    if (node == null)
        return
    inorder(node.left)
    visit(node)
    inorder(node.right)




"""
import logging
import unittest

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

    nodes = []

    def __init__(self, data):
        # TODO: Implement me
        # pass
        logger.debug(f'Node.__init__ called. data:{data}')
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.nodes.append(self)
        logger.debug(f'Node.__init__ self:{self}, data:{self.data}, left:{self.left}, right:{self.right}, parent:{self.parent}')


    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                logger.debug(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')

    def set_left(self, node):
        self.left = node
        logger.debug(f'Node.set_left called. self.left {self.left}')

class Bst(object):

    the_root = None

    def __init__(self):
        logger.debug(f'Bst.__init___ called. ')
        pass

    def insert(self, data):
        # TODO: Implement me
        # pass
        logger.debug(f'Bst.insert called. data : {data}')
        node = Node(data)
        if Bst.the_root == None:
            Bst.the_root = node
        else:
            current_node = Bst.the_root
            is_occupied = False
            i=0
            while is_occupied == False:
                # i += 1
                # if i>10:
                #     logger.debug(f'Bst.insert overflow')
                #     break
                if current_node.data > node.data:
                    logger.debug(f'Bst.insert 3-1 while current_node:{current_node} current_node.left:{current_node.left}')
                    if current_node.left == None:
                        logger.debug(f'Bst.insert 3-1-1 while current_node:{current_node} current_node.left:{current_node.left}')
                        is_occupied = True
                        current_node.left = node
                        node.parent = current_node
                    current_node = current_node.left
                elif current_node.data < node.data: 
                    logger.debug(f'Bst.insert 3-2 while ')
                    if current_node.right == None:
                        is_occupied = True
                        current_node.right = node
                        node.parent = current_node
                    current_node = current_node.right
                else:
                    raise Exception(f'Something wrong. current_node.data:{current_node.data}, node.data:{node.data}')

    def ls_nodes(self):
        if Bst.the_root == None: 
            print(f'Bst.ls_nodes No nodes available.')
        else:
            Bst.the_root.ls_nodes()

    def in_order_traversal(self):
        # print(
        #     [i for i in self.inorder(Bst.the_root) ]
        # )
        return    [i for i in self.inorder(Bst.the_root) ]

    def inorder(self, node):
        if not isinstance(node,Node):
            return 
        yield from self.inorder(node.left)
        # print("====> ",node.data)
        yield node.data
        yield from self.inorder(node.right)

class MyTestTree(unittest.TestCase):

    def test_tree_one(self):
        logger.debug(f'MyTestTree.test_tree_one called. ')
        bst = Bst()
        bst.insert(6)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(2)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(1)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(0)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(4)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(3)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(5)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(7)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(9)
        # logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        bst.insert(8)
        logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        print( bst.in_order_traversal() )

class TestTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()
        # self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        
        logger.debug(f'ls_nodes() {bst.ls_nodes()}')

        # in_order_traversal(bst.root, self.results.add_result)
        # self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')
        # self.results.clear_results()
        self.assertEqual(bst.in_order_traversal(), [1, 2, 3, 5, 8])
        
        print('Success: test_tree_one')

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        # in_order_traversal(bst.root, self.results.add_result)
        # self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')
        
        logger.debug(f'ls_nodes() {bst.ls_nodes()}')
        self.assertEqual(bst.in_order_traversal(), [1, 2, 3, 4, 5])

        print('Success: test_tree')


def main():
    # test = TestTree()
    # test.test_tree_one()
    # test.test_tree_two()

    mytest = MyTestTree()
    mytest.test_tree_one()

if __name__ == '__main__':
    main()
