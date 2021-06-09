""" test_bst_min.py

math.floorで真ん中のエントリーを選択
左半分処理
    左半分のエントリー数が4以上
        真中を選んで左半分処理を再び
    左半分のエントリー数が3つ 
        真中を親ノード、小さいを方をleft、大きい方をrightに設定
        小さい方の親ノードを設定
        大きい方の親ノードを設定
    左半分のエントリー数が2つ 
        大きい方を親ノード、小さい方をleftに設定
        小さい方の親ノードを設定

右半分処理

                          x
                    x          x
                  x    x     x    x
                 x x  x x   x x  x x

                 ４つ以上なら分割
                 １つならそのままleftかrightへセット
                 ２つなら大きい方が上、小さほうがleft
                 ３つなら真ん中が上、小さいほうがleft、大きいほうがright
                 ４つ以上なら分割
"""
import logging
import math
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



class MinBst(object):

    def __init__(self):
        logger.debug(f'MinBst.__init___ called. ')
        self.__theRoot = None
        self.__height = 0

    def create_min_bst(self, array):
        # TODO: Implement me
        # pass
        logger.debug(f'MinBst.create_min_bst called. ')
        return self.__create_min_bst(array, None)

    def __create_min_bst(self, array, parent_node):
        logger.debug(f'MinBst.__create_min_bst called. ')

        l = math.floor(len(array)//2)
        
        print( array[0:l], array[l], array[l+1:])
        node = Node(array[l])
        if self.__theRoot == None:
            logger.debug(f'MinBst.__create_min_bst self__theRoot == None. ')
            self.__theRoot = node
            parent_node = node

        if len(array[0:l]): 
            logger.debug(f'MinBst.__create_min_bst left. ')
            parent_node.left = node 
            node.parent = parent_node
            self.__create_min_bst(array[0:l], node)
        if len(array[l+1:]): 
            logger.debug(f'MinBst.__create_min_bst right. ')
            parent_node.right = node 
            node.parent = parent_node
            self.__create_min_bst(array[l+1:], node)

        return self.__theRoot

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



class MyTestBstMin(unittest.TestCase):

    def test_bst_min(self):
        min_bst = MinBst()
        # array = [0, 1, 2, 3, 4, 5, 6]
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        root = min_bst.create_min_bst(array)

        # self.assertEqual(height(root), 3)
        

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(unittest.TestCase):

    def test_bst_min(self):
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 4)

        print('Success: test_bst_min')


def main():
    # test = TestBstMin()
    # test.test_bst_min()
    
    mytest = MyTestBstMin()
    mytest.test_bst_min()


if __name__ == '__main__':
    main()
