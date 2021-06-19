""" test_bst_validate.py

result 
ルートノードの場合
    (node.left < node.data) and (node.right > node.data)であるはず
ルートノード以外の場合


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
                logger.debug(f'Node.ls_nodes(1) {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')
                print(f'Node.ls_nodes(2): ',n.data, n, n.left, n.right, n.parent) 

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
        self.root = root

    def clear_nodes(self):
        for n in self.root.nodes:
            del n
        self.root.clear_nodes()

    def insert(self, data):
    # ・Bst.insert
        # ・dataでNodeを作成
        # ・insert_into_tree(ルートノード、直前に作成したノード)

        logger.debug(f'Bst.insert called. data : {data}')
        node = Node(data)
        # if self.root == None:
        #     self.root = node
        # else:
        #     self.__insertIntoTree(self.root, node)
        self.__insertIntoTree(self.root, node)
        return node
    # ・insert_into_tree(ツリー上の既存ノード, 今回のノード)
    # ・引数の両ノードのdataを比較して、ツリー上の既存ノードのleftかrightを選ぶ
    # ・left or rightがNoneであればこのツリー上の既存ノードを今回のノードの親ノードに設定する
    # ・left or rightに別のノードが設定されている場合insert_into_tree(別のノード, 今回のノード)で再帰呼出し
    def __insertIntoTree(self, current_node, node):
        if current_node.data >= node.data:
            if current_node.left == None:
                current_node.left = node
                node.parent = current_node
            elif isinstance(current_node.left, Node):
                current_node = current_node.left
                self.__insertIntoTree(current_node, node)
            else:
                print(f'Bst.__insertIntoTree 1 : something wrong current_node:{current_node}, node:{node}')
        elif current_node.data < node.data:
            if current_node.right == None:
                current_node.right = node
                node.parent = current_node
            elif isinstance(current_node.right, Node):
                current_node = current_node.right
                self.__insertIntoTree(current_node, node)
            else:
                print(f'Bst.__insertIntoTree 2 : something wrong current_node:{current_node}, node:{node}')


    def ls_nodes(self):
        if self.root == None: 
            print(f'Bst.ls_nodes No nodes available.')
        else:
            self.root.ls_nodes()

    def return_node_by_data(self,data):
        return self.root.return_node_by_data(data)

    # def in_order_traversal(self):
    #     return    [i for i in self.inorder(self.root) ]
    def in_order_traversal(self, node=None):
        if node==None: node=self.root
        return    [i for i in self.inorder(node)]

    def inorder(self, node):
        if not isinstance(node,Node):
            return 
        yield from self.inorder(node.left)
        # print("====> ",node.data)
        yield node.data
        yield from self.inorder(node.right)


class BstValidate(Bst):

    # Bst()のinorder()はnode.dataを返す。BstValidate(Bst)のinorder()はnodeを返す
    def inorder(self, node):
        if not isinstance(node,Node):
            return 
        yield from self.inorder(node.left)
        # print("====> ",node.data)
        yield node
        yield from self.inorder(node.right)

    def validate(self):
        # TODO: Implement me
        # pass
        if self.root == None: raise TypeError(f'TypeError the tree is empty.')
        result = 0; # 0 is valid

        # 前半ではルートの左側のノードはroot.data > node.dataであることを確認
        # ルートの右側のノードはroot.data < node.dataであることを確認
        # 

        # print(self.in_order_traversal(self.root.left))
        for n in self.in_order_traversal(self.root.left):
            logger.debug(f'BstValidate.validate check left side n.data:{n.data}, self.root.data:{self.root.data}')
            if n.data > self.root.data: result += 1
        # print( self.in_order_traversal(self.root.right))
        for n in self.in_order_traversal(self.root.right):
            logger.debug(f'BstValidate.validate check right side n.data:{n.data}, self.root.data:{self.root.data}')
            if n.data < self.root.data: result += 1
        logger.debug(f'BstValidate.validate result:{result}')

        if result: return False

        # rootを第一層、root.left & root.rightを第二層とする
        # 第二層を含む第二層以下について全ノードをチェック
        # チェック自体はcheck_ups()で行う 
        for n in self.in_order_traversal(self.root.left):
            logger.debug(f'BstValidate.validate check left side nodes. n:{n}, n.data:{n.data}')
            result = result + self.check_ups(n, n.data)
        for n in self.in_order_traversal(self.root.right):
            logger.debug(f'BstValidate.validate check left side right. n:{n}, n.data:{n.data}')
            result = result + self.check_ups(n, n.data)

        if result: return False
        else: return True

    def check_ups(self, node, data):
        # 回帰呼び出しだが、dataは最初にコールされた際のdata値が使われ続ける
        # nodeについては回帰の度にnode.parentがnodeパラメータとして使われる
        # 
        # 指定されたnodeとnode.parentの関係を把握する
        # node.parent.left == nodeの場合node.parent.data < dataであるべき
        # node.parent.rigth == nodeの場合node.parent.data > dataであるべき
        # node.parent.parent != Noneの場合再帰する

        # self.root.ls_nodes()
        logger.debug(f'BstValidate.check_ups node:{node}, data:{data}')
        result = 0
        if node.parent.left != None and node.parent.left == node:
            if node.parent.data < data:
                result = result + 1
                return result
        if node.parent.right != None and node.parent.right == node:
            if node.parent.data > data:
                result = result + 1
            return result

        if node.parent.parent != None:
            result = result + self.check_ups(node.parent, data)

        return result


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
        # bst.ls_nodes()
        print("bst.validate():",bst.validate())

        self.assertEqual(bst.validate(), True)
        print('Success: test_bst_validate(first part)')

        #      5
        #    5   8
        #     20
        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        bst.ls_nodes()
        self.assertEqual(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.assertRaises(TypeError, test.test_bst_validate_empty)
    test.test_bst_validate()


if __name__ == '__main__':
    main()
