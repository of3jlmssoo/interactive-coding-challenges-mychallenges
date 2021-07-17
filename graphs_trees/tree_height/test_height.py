"""
[参考]
https://www.baeldung.com/cs/binary-tree-height


            5               1
        2       8           2
       1 3                  3


"""


import unittest
import logging
from collections import deque
from enum import Enum  # Python 2 users: Run pip install enum34

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
logger.disabled = False

class BstHeight(Bst):
    def __init__(self, root) -> None:
        super().__init__()    
        root.nodes=[]
        self.theRoot = root
        self.root = self.theRoot

    def height(self, node):
        # TODO: Implement me
        # pass
        if not isinstance(node, Node):
            return 0
        else:
            leftHeight = self.height(node.left)
            rightHeight = self.height(node.right)
            return max(leftHeight,rightHeight) + 1

class TestHeight(unittest.TestCase):

    def test_height(self):
        bst = BstHeight(Node(5))
        

        self.assertEqual(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.height(bst.root), 3)

        print('Success: test_height')


def main():
    test = TestHeight()
    test.test_height()


if __name__ == '__main__':
    main()
