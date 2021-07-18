
import unittest
import logging
from collections import deque

from test_bst import Bst, Node
from results import Results

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


class BstLevelLists(Bst):

    def __init__(self, root) -> None:
        super().__init__()    
        root.nodes=[]
        self.theRoot = root
        self.root = self.theRoot    

    def create_level_lists(self):
        # TODO: Implement me
        pass
        return self.viewTree() 

    def viewTree(self):
        d1 = deque([self.theRoot])
        d2 = deque([])

        row_result = []
        result = []


        while len(d1):
            # whileループ中でd1の中身をd2に移す
            while len(d1):           
                d2.append(d1.pop())
            # print(f'---+ ')
            # d2の中身を全て処理する。left or rigthがある場合d1にappendする
            while len(d2):
                node = d2.pop()
                # print(f'{node.data} ', end='') 
                row_result.append(node.data)
                if node.left != None:   d1.append(node.left)
                if node.right != None:  d1.append(node.right) 
            result.append(row_result)
            row_result = []
        return result

class TestTreeLevelLists(unittest.TestCase):

    def test_tree_level_lists(self):
        bst = BstLevelLists(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(1)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        bst.insert(11)

        # bst.ls_nodes()

        levels = bst.create_level_lists()

        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        self.assertEqual(str(results_list[0]), '[5]')
        self.assertEqual(str(results_list[1]), '[3, 8]')
        self.assertEqual(str(results_list[2]), '[2, 4, 7, 9]')
        self.assertEqual(str(results_list[3]), '[1, 6, 10]')
        self.assertEqual(str(results_list[4]), '[11]')

        print('Success: test_tree_level_lists')


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == '__main__':
    main()
