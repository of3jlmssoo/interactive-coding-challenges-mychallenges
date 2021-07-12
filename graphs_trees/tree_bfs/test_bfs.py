"""
1) 参考
    https://en.wikipedia.org/wiki/Breadth-first_search

2) 課題
- Bst系のNodeにはvisit_stateが無い。どう追加するか？

"""
import logging
import unittest
from collections import deque
from enum import Enum  # Python 2 users: Run pip install enum34

from results import Results
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
logger.disabled = True

class State(Enum):
    """copied from test_graph.py"""
    unvisited = 0
    visiting = 1
    visited = 2

class BstBfs(Bst):

    def __init__(self, root) -> None:
        """1)に対応。test_bst.pyにsetterを追加している"""
        super().__init__()    
        self.theRoot = root
        self.pdq = deque([]) # pdq:Python DeQueue

    def ls_nodes(self):
        if len(Node.nodes) == 0: 
            print(f'Node.ls_nodes No node available.')
        else:
            for n in Node.nodes:
                # logger.debug(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')
                print(f'Node.ls_nodes {n} data:{n.data}, left:{n.left}, right:{n.right}, parent:{n.parent}')



    def bfs(self, visit_func):
        # TODO: Implement me
        # pass
        # print(f'--- {self.theRoot}')

        for n in self.theRoot.nodes:        
            n.visit_status = State.unvisited

        # 1)参考URLのPseudocode    
        # 1  procedure BFS(G, root) is
        # 2      let Q be a queue
        # 3      label root as explored
        # 4      Q.enqueue(root)
        self.theRoot.visit_status = State.visited
        self.pdq.append(self.theRoot)
        # print(f'---{self.theRoot.data}')
        visit_func(self.theRoot.data)
        # 5      while Q is not empty do
        # 6          v := Q.dequeue()
        while len(self.pdq):
            v = self.pdq.popleft()
        ########### ignore the line 7 and 8
        # 7          if v is the goal then
        # 8              return v
        ########### ignore the line 7 and 8
        # 9          for all edges from v to w in G.adjacentEdges(v) do
        # 10              if w is not labeled as explored then
        # 11                  label w as explored
        # 12                  Q.enqueue(w)
            # HACK: 類似処理繰返し
            if v.left != None: 
                v.left.visit_status = State.visited
                self.pdq.append(v.left)
                # print(f'---{v.left.data}')
                visit_func(v.left.data)
            if v.right != None: 
                v.right.visit_status = State.visited
                self.pdq.append(v.right)
                # print(f'---{v.right.data}')
                visit_func(v.right.data)
class TestBfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBfs, self).__init__()
        self.results = Results()

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        # bst.ls_nodes()

        bst.bfs(self.results.add_result)
        self.assertEqual(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()
