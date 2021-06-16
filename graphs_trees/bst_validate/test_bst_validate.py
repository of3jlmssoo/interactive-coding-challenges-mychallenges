import unittest
import logging

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
        logger.debug(f'Node.__init__ nodes:{Node.nodes}')


    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                logger.debug(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')
                # print(f'Node.ls_nodes: ',n.data, n, n.left, n.right, n.parent) 

    def return_node_by_data(self, data):
        # for n in Node.nodes:
        #     print("== ", n.data, n)
        return [n for n in Node.nodes if n.data==data][0]

    def clear_nodes(self):
        Node.nodes = []

class Bst(object):

    # the_root = None

    def __init__(self, root):
        logger.debug(f'Bst.__init___ called. ')
        self.__theRoot = root

    def clear_nodes(self):
        for n in self.__theRoot.nodes:
            del n
        self.__theRoot.clear_nodes()

    def insert(self, data):
    # ・Bst.insert
        # ・dataでNodeを作成
        # ・insert_into_tree(ルートノード、直前に作成したノード)

        logger.debug(f'Bst.insert called. data : {data}')
        node = Node(data)
        # if self.__theRoot == None:
        #     self.__theRoot = node
        # else:
        #     self.__insertIntoTree(self.__theRoot, node)
        self.__insertIntoTree(self.__theRoot, node)
        return node
    # ・insert_into_tree(ツリー上の既存ノード, 今回のノード)
    # ・引数の両ノードのdataを比較して、ツリー上の既存ノードのleftかrightを選ぶ
    # ・left or rightがNoneであればこのツリー上の既存ノードを今回のノードの親ノードに設定する
    # ・left or rightに別のノードが設定されている場合insert_into_tree(別のノード, 今回のノード)で再帰呼出し
    def __insertIntoTree(self, current_node, node):
        if current_node.data > node.data:
            if current_node.left == None:
                current_node.left = node
                node.parent = current_node
            elif isinstance(current_node.left, Node):
                current_node = current_node.left
                self.__insertIntoTree(current_node, node)
            else:
                print(f'Bst.__insertIntoTree 1 : something wrong current_node:{current_node}, node:{node}')
        if current_node.data < node.data:
            if current_node.right == None:
                current_node.right = node
                node.parent = current_node
            elif isinstance(current_node.right, Node):
                current_node = current_node.right
                self.__insertIntoTree(current_node, node)
            else:
                print(f'Bst.__insertIntoTree 2 : something wrong current_node:{current_node}, node:{node}')


    def ls_nodes(self):
        if self.__theRoot == None: 
            print(f'Bst.ls_nodes No nodes available.')
        else:
            self.__theRoot.ls_nodes()

    def return_node_by_data(self,data):
        return self.__theRoot.return_node_by_data(data)

    def in_order_traversal(self):
        return    [i for i in self.inorder(self.__theRoot) ]

    def inorder(self, node):
        if not isinstance(node,Node):
            return 
        yield from self.inorder(node.left)
        # print("====> ",node.data)
        yield node.data
        yield from self.inorder(node.right)


class BstValidate(Bst):

    def validate(self):
        # TODO: Implement me
        # pass
        if self.__theRoot == None: raise TypeError(f'TypeError the tree is empty.')
        
class TestBstValidate(unittest.TestCase):

    def test_bst_validate_empty(self):
        bst = BstValidate(None)
        bst.validate()

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        self.assertEqual(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        self.assertEqual(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.assertRaises(TypeError, test.test_bst_validate_empty)
    # test.test_bst_validate()


if __name__ == '__main__':
    main()
