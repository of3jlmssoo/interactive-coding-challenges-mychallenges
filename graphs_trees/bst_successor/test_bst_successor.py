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


class BstSuccessor(object):

    def follow_right(self, node):
        logger.debug(f'BstSuccessor.follow_right node:{node}')
        while node.right!=None:
            node = node.right
        return node.data

    def follow_left(self, node):
        logger.debug(f'BstSuccessor.follow_left node:{node}')
        while node.left!=None:
            node = node.left
        return node.data

    def get_next(self, node):
        # TODO: Implement me
        # pass
        logger.debug(f'BstSuccessor.get_next called. node:{node}')
        if node == None: raise TypeError(f'BstSuccessor.get_next. Type Error. None specified')

        if node.right != None and node.right.left == None: return node.right.data
        if node.right != None and node.right.left != None: return self.follow_left(node.right.left)

        data=node.data
        i=0
        logger.debug(f'BstSuccessor.get_next before while data:{data}, node.data:{node.data}, node:{node} , node.parent.data:{node.parent.data}')
        while node.parent != None and node.parent.data < data:
            logger.debug(f'BstSuccessor.get_next in while data:{data}, node.parent:{node.parent}, node.parent.data:{node.parent.data}')
            node = node.parent
            i+=1
            if i>100: break
        logger.debug(f'BstSuccessor.get_next after while node:{node}, node.parent:{node.parent}')
        if node.parent != None: 
            return node.parent.data
        else: 
            return None

        # return node.parent.data
class MyTestBstSuccessor(unittest.TestCase):

    def test_bst_successor(self):
        logger.debug(f'MyTestBstSuccessor.test_bst_successor called')
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)
        bst.ls_nodes()

        bst_successor = BstSuccessor()
        self.assertEqual(bst_successor.get_next(nodes[4]), 5)
        self.assertEqual(bst_successor.get_next(nodes[5]), 6)
        self.assertEqual(bst_successor.get_next(nodes[8]), 9)
        self.assertEqual(bst_successor.get_next(nodes[15]), None)

        self.assertEqual(bst_successor.get_next(nodes[1]), 2)
        self.assertEqual(bst_successor.get_next(nodes[2]), 3)
        self.assertEqual(bst_successor.get_next(nodes[3]), 4)
        self.assertEqual(bst_successor.get_next(nodes[6]), 7)
        self.assertEqual(bst_successor.get_next(nodes[7]), 8)
        self.assertEqual(bst_successor.get_next(nodes[9]), 10)
        self.assertEqual(bst_successor.get_next(nodes[10]), 12)
        self.assertEqual(bst_successor.get_next(nodes[12]), 15)

        print('Success: my_test_bst_successor')



class TestBstSuccessor(unittest.TestCase):

    def test_bst_successor_empty(self):
        print('Success: test_bst_successor_empty called')
        bst_successor = BstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = BstSuccessor()
        self.assertEqual(bst_successor.get_next(nodes[4]), 5)
        self.assertEqual(bst_successor.get_next(nodes[5]), 6)
        self.assertEqual(bst_successor.get_next(nodes[8]), 9)
        self.assertEqual(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.assertRaises(TypeError, test.test_bst_successor_empty)

    mytest = MyTestBstSuccessor()
    mytest.test_bst_successor()


if __name__ == '__main__':
    main()
