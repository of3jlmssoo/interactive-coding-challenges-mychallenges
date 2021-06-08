""" test_bst_rec.py

参考情報によると再帰呼出を使うことがデファクトになっているようである。
test_bst.pyでは再帰呼出を使わなかったため、test_bst_rec.pyで再帰呼出方式に対応する。

[参考情報]
(1) https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%9C%A8   
(2) https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2
(3) https://en.wikipedia.org/wiki/Tree_traversal

(1)を参考にclassの構造を決める

[流れ]
・テストコードからはdataだけを指定してBst.insertをコールする
・Bst.insert
    ・dataでNodeを作成
    ・insert_into_tree(ルートノード、直前に作成したノード)
・insert_into_tree(ツリー上の既存ノード, 今回のノード)
    ・引数の両ノードのdataを比較して、ツリー上の既存ノードのleftかrightを選ぶ
    ・left or rightがNoneであればこのツリー上の既存ノードを今回のノードの親ノードに設定する
    ・left or rightに別のノードが設定されている場合insert_into_tree(別のノード, 今回のノード)で再帰呼出し


[頭の体操]
def Bst.__insert(current_node, node):
    if current_node.data > node.data
        if current.node.left == None:
            current_node.left = node
            node.parenet = current = node
        elif isinstance(current_node.node.left, Node):
            current_node = current_node.left
            Bst.__insert(current_node, node)
        else:
            print("something wrong)
    if current_node.data < node.data):
        if current_node.node.right == None:
            current_node.right = node
            node.parenet = current = node
        elif isinstance(current_node.node.right, Node):
            current_node = current_node.right
            Bst.__insert(current_node, node)
        else:
            print("something wrong)
↑
def Bst.__insert(current_node, node):
    (current_node.data > node.data) & current.node.left == None 
        current_node.left = node
        node.parenet = current = node
    (current_node.data > node.data) & current_node.node.left <> None
        current_node = current_node.left
        Bst.__insert(current_node, node)
    (current_node.data < node.data) & current_node.node.right == None
        current_node.right = node
        node.parenet = current = node
    (current_node.data < node.data) & current_node.node.right <> None
        current_node = current_node.right
        Bst.__insert(current_node, node)


            
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
logger.disabled = True

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
        logger.debug(f'Node.__init__ nodes:{Node.nodes}')


    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                logger.debug(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')


class Bst(object):

    # the_root = None

    def __init__(self):
        logger.debug(f'Bst.__init___ called. ')
        self.__theRoot = None

    def insert(self, data):
    # ・Bst.insert
        # ・dataでNodeを作成
        # ・insert_into_tree(ルートノード、直前に作成したノード)

        logger.debug(f'Bst.insert called. data : {data}')
        node = Node(data)
        if self.__theRoot == None:
            self.__theRoot = node
        else:
            self.__insertIntoTree(self.__theRoot, node)

    # ・insert_into_tree(ツリー上の既存ノード, 今回のノード)
    # ・引数の両ノードのdataを比較して、ツリー上の既存ノードのleftかrightを選ぶ
    # ・left or rightがNoneであればこのツリー上の既存ノードを今回のノードの親ノードに設定する
    # ・left or rightに別のノードが設定されている場合insert_into_tree(別のノード, 今回のノード)で再帰呼出し
    def __insertIntoTree(self, current_node, node):
        if current_node.data > node.data:
            if current_node.left == None:
                current_node.left = node
                node.parenet = current = node
            elif isinstance(current_node.left, Node):
                current_node = current_node.left
                self.__insertIntoTree(current_node, node)
            else:
                print(f'Bst.__insertIntoTree 1 : something wrong current_node:{current_node}, node:{node}')
        if current_node.data < node.data:
            if current_node.right == None:
                current_node.right = node
                node.parenet = current_node
            elif isinstance(current_node.right, Node):
                current_node = current_node.right
                self.__insertIntoTree(current_node, node)
            else:
                print(f'Bst.__insertIntoTree 2 : something wrong current_node:{current_node}, node:{node}')


    def ls_nodes(self):
        # if Bst.the_root == None: 
        #     print(f'Bst.ls_nodes No nodes available.')
        # else:
        #     Bst.the_root.ls_nodes()
        if self.__theRoot == None: 
            print(f'Bst.ls_nodes No nodes available.')
        else:
            self.__theRoot.ls_nodes()

    def in_order_traversal(self):
        # print(
        #     [i for i in self.inorder(Bst.the_root) ]
        # )
        # return    [i for i in self.inorder(Bst.the_root) ]
        return    [i for i in self.inorder(self.__theRoot) ]

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
        self.assertEqual( bst.in_order_traversal(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] )
        print('Success: MyTestTree.test_tree_one')

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

        print('Success: test_tree_two')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()

    mytest = MyTestTree()
    mytest.test_tree_one()

if __name__ == '__main__':
    main()
