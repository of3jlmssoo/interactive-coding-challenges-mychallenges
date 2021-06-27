""" test_path_exists.py

ln -s  ../utils/results.py
ln -s  ../graph/test_graph.py

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

class ResultsNode(Results):

    def __init__(self) -> None:
        super().__init__()

    def add_result(self, result):
        self.results.append(result)

class GraphPathExists(Graph):

    def __init__(self) -> None:
        super().__init__()
        self.results = ResultsNode()

    def add_node(self,id):
        super().add_node(id)
        return self.nodes[id]

    def path_exists(self, start, end):
        self.results.clear_results()
        return self.path_exists_body(start, end)

    def path_exists_body(self, start, end):
        # TODO: Implement me
        # pass
        logger.debug(f'GraphPathExists.path_exists() start:{start}, start.visit_state:{start.visit_state}')
        start.visit_state = State.visited
        # visit_func(start)
        self.results.add_result(start)
        # logger.debug(f'start.self.adj_nodes.values(): {start.adj_nodes.values()}') 
        for r in start.adj_nodes.values():
            if r.visit_state == State.unvisited:
                self.path_exists_body(r, self.results.add_result)
        
        logger.debug(f'GraphPathExists.path_exists() end:{end} type(end):{type(end)} in start.adj_nodes:{start.adj_nodes}. self.results:{self.results} type(self.results):{type(self.results)}')
        if end in self.results.results:
            return True
        else:
            return False

class TestPathExists(unittest.TestCase):

    def test_path_exists(self):
        nodes = []
        graph = GraphPathExists()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)

        # logger.debug(f'TestPathExists.test_path_exists() nodes:{nodes}')
        self.assertEqual(graph.path_exists(nodes[0], nodes[2]), True)
        self.assertEqual(graph.path_exists(nodes[0], nodes[0]), True)
        self.assertEqual(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()
