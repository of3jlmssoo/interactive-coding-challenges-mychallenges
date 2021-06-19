import logging
import unittest
from test_bst_validate import Bst
from test_bst_validate import Node
from test_bst_validate import BstValidate

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

class BstBalance(BstValidate):

    def check_balance(self):
        # TODO: Implement me
        # pass
        if self.root == None: raise TypeError(f'BstBalance.check_balance TypeError(None)')
        if self.root.left == None and self.root.right == None:
            return True

        left_len  = self.check_downs(self.root.left) 
        right_len = self.check_downs(self.root.right)

        logger.debug(f'left_len   {left_len}')
        logger.debug(f'left_right {right_len}')

        # root.left配下のノードの末端ノード(left==None and right==None)までの距離が
        # リストに降順でセットされるので[0]と[1]を比較する。rigthも同様
        # 最後にleftとrightの差をチェックする
        if len(left_len) > 1  and (left_len[0]-left_len[1]) > 1:
            return False
        if len(right_len) > 1 and (right_len[0]-right_len[1]) > 1:
            return False
        if abs(left_len[0]-right_len[0])>1:
            return False
        return True

    def check_downs(self, node):
        # nodeで指定されたノード配下で、かつleft==None and right==Noneのノードをlast_nodesにセット
        # last_nodesの各ノードのルートまでの距離をlast_nodes_lengthsにセットしてソートの上returnする
        last_nodes = [n for n in self.in_order_traversal(node) if n.left==None and n.right == None]
        last_nodes_lengths =[]
        for n in last_nodes:
            i=0
            p = n
            while  p.parent != None:
                i = i + 1
                p = p.parent
            last_nodes_lengths.append(i)
        return sorted(last_nodes_lengths, reverse=True)

         

class TestCheckBalance(unittest.TestCase):

    def test_check_balance_empty(self):
        print('Success: test_check_balance_empty')
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        self.assertEqual(bst.check_balance(), True)
        #     5
        #   3   8
        #  1 4 
        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        # bst.ls_nodes()

        # bst.check_balance()
        self.assertEqual(bst.check_balance(), True)
        print('Success: test_check_balance first part')

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        self.assertEqual(bst.check_balance(), False)
        print('Success: test_check_balance second part')

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.check_balance(), True)

        print('Success: test_check_balance third part')


def main():
    test = TestCheckBalance()
    test.assertRaises(TypeError, test.test_check_balance_empty)
    test.test_check_balance()


if __name__ == '__main__':
    main()
