""" 
デフォルトのテストはツリーの構成が2つのみ。この2つ以外にもパターンがあると考え以下のパターンに対応するものを作成。

			    2
		      1

			# rootにrightが無い
			# rootのleft childにrigthが無い
			=> rootのleft childが該当(1)


			bst = Solution(None)
			root = Node(2)
			node1 = Node(1)
			root.left = node1
			node1.parent = root
			print('1')
			self.assertEqual(bst.find_second_largest(),node1)

		      5
		     4
		    3
		   2
		  1
			bst = Solution(None)
			root = Node(5)
			node4 = Node(4)
			node3 = Node(3)
			node2 = Node(2)
			node1 = Node(1)
			root.left = node4
			node4.left = node3
			node3.left = node2
			node2.left = node1
			node1.parent = node2
			node2.parent = node3
			node3.parent = node4
			node4.parent = node5
			print('2')
			self.assertEqual(bst.find_second_largest(),node4)

			(上と同じ)
			rootにrightが無い
			rootのleft childにrigthが無い
			=> rootのleft childが該当(4)
	
  		     5
		    3
		   2 4
		   	bst = Solution(None)
			root = Node(5)
			node4 = Node(4)
			node3 = Node(3)
			node2 = Node(2)
			root.left = node3
			node3.left = node2
			node3.right = node4
			node2.parent = node3
			node3.parent = node5
			node4.parent = node3
			print('3')
			self.assertEqual(bst.find_second_largest(),node4)

			# rootにrightが無い
			# rootのleft childにrightがある
			# => rootのleft childのright childが該当(4)
			(直ぐ下のサブセット)

		    100
		  50
		    70
		   60 80
		   	bst = Solution(None)
			root = Node(100)
			node50 = Node(50)
			node70 Node(70)
			node60 Node(60)
			node80 Node(80)
			root.left = node50
			node50.right = node70
			node70.left = node60
			node70.right = node80
			node80.parent = node70
			node60.parent = node70
			node70.parent = node50
			node50.parent = root
			print('4')
			self.assertEqual(bst.find_second_largest(),node80)
			rootにrightが無い
			rootのleft childにrightがある(50に70がある)
			まだrigthがある
			=> 最後のrightの行き先が該当(80)

=======================================================================================

		      2
		     1 3
			bst = Solution(None)
			root = Node(2)
			node1 = Node(1)
			node3 = Node(3)
			root.left = node1
			root.right = node3
			node1.parent = root
			node3.parent = root
			print('5')
			self.assertEqual(bst.find_second_largest(),root)

			# rootにrightがある。
			# => どんづまりのrightの１つ手前が該当

		    5
		  4   8
		     7 9
			bst = Solution(None)
			root = Node(5)
			node4 = Node(4)
			node8 = Node(8)
			node7 = Node(7)
			node9 = Node(9)
			root.left = node4
			root.right = node8
			node4.left = node7
			node4.right = node9
			node4.parent = root
			node8.parent = root
			node7.parent = node8
			node9.parent = node8
			print('6')
			self.assertEqual(bst.find_second_largest(),node8)
			rootにrightがある。
			=> どんづまりのrightの１つ手前が該当

		    5
		  4   8
		     7 
			bst = Solution(None)
			root = Node(5)
			node4 = Node(4)
			node7 = Node(7)
			node8 = Node(8)
			root.left = node4
			root.right = node8
			node8.left = node7
			node4.parent = root
			node8.parent = root
			node7.parent = node9
			print('7')
			self.assertEqual(bst.find_second_largest(),node7)

			rootにrightがある
			8にrightが無くleftがある
			=> 7が該当		     


            50
		4     100
		    60
		      70
		        80
　　　 　　　　　79

			bst = Solution(None)
			root = Node(50)
			node4 = Node(4)
			node100 = Node(100)
			node60 Node(60)
			node70 Node(70)
			node80 Node(80)
			node79 Node(79)
			root.left = node4
			root.right = node100
			node100.left = node60
			node60.right = node70
			node70.right = node80
			node80.left = node79
			node79.parent = node80
			node80.parent = node70
			node70.parent = node60
			node60.parent = node100
			node4.parent = root
			node100.parent = root
			print('8')
			self.assertEqual(bst.find_second_largest(),node80)

			rootにrigthがある
			100にrightがなくleftがある
			60にrightがある
			=> 最後のrightが該当(80)


		     20
		       30
		         31
   			       32

			bst = Solution(None)
			root = Node(20)
			node30 Node(30)
			node31 Node(31)
			node32 Node(32)
			root.right = node30
			node30.right = node31
			node31.right = node32
			node32.parent = node31
			node31.parent = node30
			node30.parent = root
			print('9')
			self.assertEqual(bst.find_second_largest(),node31)

			rootにrightがある
			rightがあり続ける
			=> 最後のrightのparentが該当(31)

=======================================================================================

                 10
              5       15
           3   8    12  20
          2 4              30


               10
              5
             3 7
"""
import logging
import unittest
from typing import Type

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

    def __init__(self):
        logger.debug(f'Bst.__init___ called. ')
        self.__theRoot = None

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
        if self.__theRoot == None: 
            print(f'Bst.ls_nodes No nodes available.')
        else:
            self.__theRoot.ls_nodes()

    def return_node_by_data(self,data):
        return self.__theRoot.return_node_by_data(data)

    def in_order_traversal(self, node=None):
        if node==None: node=self.__theRoot  
        return    [i for i in self.inorder(node)]

    def inorder(self, node):
        if not isinstance(node,Node):
            return 
        yield from self.inorder(node.left)
        # print("====> ",node.data)
        yield node.data
        yield from self.inorder(node.right)



class Solution(Bst):
# class Solution():
    def __init__(self, root):
        self.__theRoot = root

    def find_second_largest(self):
        # TODO: Implement me
        # pass

        if self.__theRoot == None: raise TypeError(f'Solution.first_second_largest TypeError')

        # rootにrightが無い
        # rootのleft childにrigthが無い
        if self.__theRoot.right == None and self.__theRoot.left.right == None:
            return self.__theRoot.left
        #
        #      5
		#     3
		#    2 4
        #    
        # # rootにrightが無い
        # rootのleft childにrightがある
        # => rootのleft childのright childが該当(4)
        if self.__theRoot.right == None and (result := self.__theRoot.left.right) != None:
            while result.right != None:
                result = result.right
            return result
        #
        # rootにrightがある。
        # => どんづまりのrightの１つ手前が該当
        if (result := self.__theRoot.right) != None:
            while result.right != None:
                result = result.right
            if result.right == None and result.left == None:
                return result.parent
            elif result.left.right == None:
                return result.left
            else:
                result = result.left
                while result.right:
                    result = result.right
                return result



class MyTestBstSecondLargest(unittest.TestCase):

    def test_bst_second_largest(self):
        # bst = Solution(None)
        root = Node(2)
        bst = Solution(root)
        node1 = Node(1)
        root.left = node1
        node1.parent = root
        root.ls_nodes()
        print('my test 1', end='')
        self.assertEqual(bst.find_second_largest(),node1)
        print(' completed')
        root.clear_nodes()
        del root, node1

        root = Node(5)
        bst = Solution(root)
        node4 = Node(4)
        node3 = Node(3)
        node2 = Node(2)
        node1 = Node(1)
        root.left = node4
        node4.left = node3
        node3.left = node2
        node2.left = node1
        node1.parent = node2
        node2.parent = node3
        node3.parent = node4
        node4.parent = root
        print('my test 2', end='')
        self.assertEqual(bst.find_second_largest(),node4)
        print(' completed')
        root.clear_nodes()
        del root, node4, node3, node2, node1

        root = Node(5)
        bst = Solution(root)
        node4 = Node(4)
        node3 = Node(3)
        node2 = Node(2)
        root.left = node3
        node3.left = node2
        node3.right = node4
        node2.parent = node3
        node3.parent = root
        node4.parent = node3
        print('my test 3', end='')
        self.assertEqual(bst.find_second_largest(),node4)
        print(' completed')
        root.clear_nodes()
        del root, node4, node3, node2

        root = Node(100)
        bst = Solution(root)
        node50 = Node(50)
        node70 = Node(70)
        node60 = Node(60)
        node80 = Node(80)
        root.left = node50
        node50.right = node70
        node70.left = node60
        node70.right = node80
        node80.parent = node70
        node60.parent = node70
        node70.parent = node50
        node50.parent = root
        print('my test 4', end='')
        self.assertEqual(bst.find_second_largest(),node80)
        print(' completed')
        root.clear_nodes()
        del root, node50, node70, node60, node80

        root = Node(2)
        bst = Solution(root)
        node1 = Node(1)
        node3 = Node(3)
        root.left = node1
        root.right = node3
        node1.parent = root
        node3.parent = root
        # root.ls_nodes()
        print('my test 5', end='')
        self.assertEqual(bst.find_second_largest(),root)
        print(' completed')
        root.clear_nodes()
        del root, node1, node3

        root = Node(5)
        bst = Solution(root)
        node4 = Node(4)
        node8 = Node(8)
        node7 = Node(7)
        node9 = Node(9)
        root.left = node4
        root.right = node8
        node8.left = node7
        node8.right = node9

        node4.parent = root
        node8.parent = root
        node7.parent = node8
        node9.parent = node8
        print('my test 6', end='')
        self.assertEqual(bst.find_second_largest(),node8)
        print(' completed')
        root.clear_nodes()
        del root, node4, node8, node7, node9

        root = Node(5)
        bst = Solution(root)
        node4 = Node(4)
        node7 = Node(7)
        node8 = Node(8)
        root.left = node4
        root.right = node8
        node8.left = node7
        node4.parent = root
        node8.parent = root
        node7.parent = node8
        # root.ls_nodes()
        print('my test 7', end='')
        self.assertEqual(bst.find_second_largest(),node7)
        print(' completed')
        root.clear_nodes()
        del root, node4, node7, node8


        root = Node(50)
        bst = Solution(root)
        node4 = Node(4)
        node100 = Node(100)
        node60 = Node(60)
        node70 = Node(70)
        node80 = Node(80)
        node79 = Node(79)
        root.left = node4
        root.right = node100
        node100.left = node60
        node60.right = node70
        node70.right = node80
        node80.left = node79
        node79.parent = node80
        node80.parent = node70
        node70.parent = node60
        node60.parent = node100
        node4.parent = root
        node100.parent = root
        # root.ls_nodes()
        print('my test 8', end='')
        self.assertEqual(bst.find_second_largest(),node80)
        print(' completed')
        root.clear_nodes()
        del root, node4, node100, node60, node70, node80, node79

        root = Node(20)
        bst = Solution(root)
        node30 = Node(30)
        node31 = Node(31)
        node32 = Node(32)
        root.right = node30
        node30.right = node31
        node31.right = node32
        node32.parent = node31
        node31.parent = node30
        node30.parent = root
        # root.ls_nodes()
        print('my test 9', end='')
        self.assertEqual(bst.find_second_largest(),node31)
        print(' completed')
        root.clear_nodes()
        del root, node30, node31, node32


class TestBstSecondLargest(unittest.TestCase):

    def test_bst_second_largest(self):
        sol = Solution(None)
        self.assertRaises(TypeError, sol.find_second_largest)



        # root = Node(10)
        # bst = Solution(root)
        # node5 = bst.insert(5)
        # node15 = bst.insert(15)
        # node3 = bst.insert(3)
        # node8 = bst.insert(8)
        # node12 = bst.insert(12)
        # node20 = bst.insert(20)
        # node2 = bst.insert(2)
        # node4 = bst.insert(4)
        # node30 = bst.insert(30)
        # self.assertEqual(bst.find_second_largest(), node20)


        # root = Node(10)
        # bst = Solution(root)
        # node5 = bst.insert(5)
        # node3 = bst.insert(3)
        # node7 = bst.insert(7)

        bst = Bst()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(8)
        bst.insert(12)
        bst.insert(20)
        bst.insert(2)
        bst.insert(4)
        bst.insert(30)
        # bst.ls_nodes()
        sol = Solution(bst.return_node_by_data(10))
        self.assertEqual(sol.find_second_largest(), bst.return_node_by_data(20))
        bst.clear_nodes()
        del bst
        del sol
        print('Success: test_bst_second_largest 1')

        bst = Bst()
        bst.insert(10)
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.ls_nodes()
        sol = Solution(bst.return_node_by_data(10))
        self.assertEqual(sol.find_second_largest(), bst.return_node_by_data(7))
        bst.clear_nodes()
        del bst, sol
        print('Success: test_bst_second_largest 2')


def main():
    test = TestBstSecondLargest()
    test.test_bst_second_largest()

    mytest = MyTestBstSecondLargest()
    mytest.test_bst_second_largest()

if __name__ == '__main__':
    main()
