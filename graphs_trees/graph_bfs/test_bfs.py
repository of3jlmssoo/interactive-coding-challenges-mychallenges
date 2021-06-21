""" 
https://en.wikipedia.org/wiki/Breadth-first_search  
procedure BFS(G, root) is
    let Q be a queue
    label root as explored
    Q.enqueue(root)
    while Q is not empty do
        v := Q.dequeue()
        if v is the goal then
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as explored then
                label w as explored
                Q.enqueue(w)
"""
import unittest
import logging
from test_graph import State
from test_graph import Node
from test_graph import Graph
from test_graph import State
from collections import deque
from result import Results



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

class GraphBfs(Graph):

    def __init__(self) -> None:
        super().__init__()
        self.__dq = deque()

    def bfs(self, root, visit_func): # Breadth-first search
        # TODO: Implement me
        # pass

        self.__dq.append(root)
        while len(self.__dq) > 0:
            node = self.__dq.popleft()
            visit_func(node.key)
            for n in node.adj_nodes.values():
                if n.visit_state == State.unvisited:
                    self.__dq.append(n)
                    n.visit_state = State.visited

    def add_node(self,id):
        super().add_node(id)
        return self.nodes[id]


class TestBfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBfs, self).__init__()
        self.results = Results()

    def test_bfs(self):
        nodes = []
        graph = GraphBfs()
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
        # graph.return_nodes()


        graph.bfs(nodes[0], self.results.add_result)
        # print(f'000 {str(self.results)} 000')
        self.assertEqual(str(self.results), "[0, 1, 4, 5, 3, 2]")

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()
