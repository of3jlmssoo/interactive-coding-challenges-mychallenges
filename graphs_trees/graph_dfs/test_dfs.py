""" test_dfs.py
https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode
このPseudocodeは、for all directed edges from v to w that are in G.adjacentEdges(v) doのfrom v to wのvが理解できず。
https://ja.wikipedia.org/wiki/%E6%B7%B1%E3%81%95%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2 の記載がシンプル

"""
import unittest
import logging
from test_graph import State
from test_graph import Node
from test_graph import Graph
from test_graph import State
from results    import Results
from collections import deque

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



class GraphDfs(Graph):

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def add_node(self,id):
        super().add_node(id)
        return self.nodes[id]

    def dfs(self, root, visit_func):
        # TODO: Implement me
        # pass
        logger.debug(f'GraphDfs.dfs root:{root}, root.visit_state:{root.visit_state}')
        root.visit_state = State.visited
        visit_func(root)
        logger.debug(f'root.self.adj_nodes.values(): {root.adj_nodes.values()}') 
        for r in root.adj_nodes.values():
            if r.visit_state == State.unvisited:
                self.dfs(r, visit_func)



class TestDfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDfs, self).__init__()
        self.results = Results()

    def test_dfs(self):
        nodes = []
        graph = GraphDfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))

        logger.debug(f'nodes:{nodes}')
        
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.dfs(nodes[0], self.results.add_result)
        # print( str(self.results) )
        self.assertEqual(str(self.results), "[0, 1, 3, 2, 4, 5]")
        # self.assertEqual(str(self.results), "[0, 1, 3, 2, 5, 4]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()
