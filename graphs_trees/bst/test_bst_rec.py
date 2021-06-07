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
        # if not logger.disabled: self.nodes.append([self.data,self.left,self.right,self.parent])
        if not logger.disabled: self.nodes.append(self)
        logger.debug(f'Node.__init__ self:{self}, data:{self.data}, left:{self.left}, right:{self.right}, parent:{self.parent}')


    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                print(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')

    def set_left(self, node):
        logger.debug(f'Node.set_left called.')
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
            logger.debug(f'Bst.insert 1 current_node : {current_node}')
            # if current_node.data > node.data:
            #     while current_node.left != None:
            #         current_node = current_node.left
            #         logger.debug(f'Bst.insert 2 current_node : {current_node}')
            #     current_node.set_left(node)
            #     node.parent = current_node
            #     logger.debug(f'Bst.insert current_node.left is set to node {node}')
            # if current_node.data > node.data:
            #     is_occupied = current_node.left
            #     logger.debug(f'Bst.insert 2-1 is_occupied:{is_occupied}, current_node.left:{current_node.left}')
            # elif current_node.data < node.data: 
            #     is_occupied = current_node.right
            #     logger.debug(f'Bst.insert 2-2 is_occupied:{is_occupied}, current_node.right:{current_node.right}')
            # else:
            #     raise Exception(f'Something wrong')

            logger.debug(f'Bst.insert 3-00 while current_node:{current_node}')
            is_occupied = False
            i=0
            while is_occupied == False:
                i += 1
                if i>10:
                    logger.debug(f'Bst.insert overflow')
                    break
                logger.debug(f'Bst.insert 3-0 while ')
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
                    raise Exception(f'Something wrong')

            
            logger.debug(f'Bst.insert 4-0 after while current_node:{current_node} ')
            # current_node.data = node.data 


            # if current_node.data > node.data:
            #     logger.debug(f'Bst.insert 4-1 while current_node:{current_node} ')
            #     current_node.left = node.data
            # elif current_node.data < node.data: 
            #     logger.debug(f'Bst.insert 4-2 while current_node:{current_node} ')
            #     current_node.right = node.data
            # else:
            #     raise Exception(f'Something wrong')


    def ls_nodes(self):
        if Bst.the_root == None: 
            print(f'Bst.ls_nodes No nodes available.')
        else:
            Bst.the_root.ls_nodes()

class MyTestTree(unittest.TestCase):

    def test_tree_one(self):
        logger.debug(f'MyTestTree.test_tree_one called. ')
        bst = Bst()
        bst.insert(6)
        bst.ls_nodes()
        bst.insert(2)
        bst.ls_nodes()
        bst.insert(1)
        bst.ls_nodes()
        bst.insert(0)
        bst.ls_nodes()

        bst.insert(4)
        bst.ls_nodes()
        bst.insert(3)
        bst.ls_nodes()
        bst.insert(5)
        bst.ls_nodes()
        bst.insert(7)
        bst.ls_nodes()
        bst.insert(9)
        bst.ls_nodes()
        bst.insert(8)
        bst.ls_nodes()

class TestTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    # test = TestTree()
    # test.test_tree_one()
    # test.test_tree_two()

    mytest = MyTestTree()
    mytest.test_tree_one()

if __name__ == '__main__':
    main()
