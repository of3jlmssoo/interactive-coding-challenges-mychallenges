"""
https://en.wikipedia.org/wiki/Graph_theory
A graph in this context is made up of vertices (also called nodes or points) which are connected by edges (also called links or lines).

"""
import unittest
from enum import Enum  # Python 2 users: Run pip install enum34
import logging

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

    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0 # number of incoming lines
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        # TODO: Implement me
        # pass
        self.adj_nodes[neighbor.key] = neighbor
        self.adj_weights[neighbor.key] = weight 
        logger.debug(f'Node.add_neighbor self.key:{self.key}, neighbor:{neighbor}, weight:{weight}, neighnor.key:{neighbor.key}, self.adj_nodes[neighbor.key]:{self.adj_nodes[neighbor.key]}')
        logger.debug(f'     self.incoming_edges:{self.incoming_edges}, self.adj_nodes:{self.adj_nodes}, self.adj_weights:{self.adj_weights}')

    def remove_neighbor(self, neighbor):
        # TODO: Implement me
        # pass
        self.adj_nodes.pop(neighbor.key)
        neighbor.incoming_edges -= 1

    def list_node(self):
        return self.key, self.visit_state, self.incoming_edges, self.adj_nodes, self.adj_weights


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, id):
        # TODO: Implement me
        # pass
        if id not in self.nodes:
            self.nodes[id] = Node(id)

    #graph.add_edge(0, 1, weight=5)
    def add_edge(self, source, dest, weight=0):
        # TODO: Implement me
        # pass
        if source not in self.nodes:
            self.nodes[source]=Node(source)
        if dest not in self.nodes:
            self.nodes[dest]=Node(dest)

        self.nodes[source].add_neighbor(self.nodes[dest], weight)
        self.nodes[dest].incoming_edges += 1

    def add_undirected_edge(self, source, dest, weight=0):
        # TODO: Implement me
        # pass
        self.add_edge(source, dest, weight)
        self.add_edge(dest, source, weight)

    def __repr__(self):
        return str(self.nodes)

    def return_nodes(self): #, node):
        for n in self.nodes.values():
            print(n.list_node())

class TestGraph(unittest.TestCase):

    def create_graph(self):
        graph = Graph()
        for key in range(0, 6):
            graph.add_node(key)
        return graph

    def test_graph(self):
        graph = self.create_graph()
        logger.debug(f'TestGraph.test_graph graph:{graph}')
        print('Success: test_graph() called')

        graph.add_edge(0, 1, weight=5)
        if logger.disabled == False: graph.return_nodes()
        graph.add_edge(0, 5, weight=2)
        if logger.disabled == False: graph.return_nodes()
        graph.add_edge(1, 2, weight=3)
        graph.add_edge(2, 3, weight=4)
        graph.add_edge(3, 4, weight=5)
        graph.add_edge(3, 5, weight=6)
        graph.add_edge(4, 0, weight=7)
        graph.add_edge(5, 4, weight=8)
        graph.add_edge(5, 2, weight=9)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[3].key], 4)
        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[4].key], 5)
        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[5].key], 6)
        self.assertEqual(graph.nodes[4].adj_weights[graph.nodes[0].key], 7)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[4].key], 8)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[2].key], 9)

        self.assertEqual(graph.nodes[0].incoming_edges, 1)
        self.assertEqual(graph.nodes[1].incoming_edges, 1)
        self.assertEqual(graph.nodes[2].incoming_edges, 2)
        self.assertEqual(graph.nodes[3].incoming_edges, 1)
        self.assertEqual(graph.nodes[4].incoming_edges, 2)
        self.assertEqual(graph.nodes[5].incoming_edges, 2)

        graph.nodes[0].remove_neighbor(graph.nodes[1])
        self.assertEqual(graph.nodes[1].incoming_edges, 0)
        graph.nodes[3].remove_neighbor(graph.nodes[4])
        self.assertEqual(graph.nodes[4].incoming_edges, 1)

        self.assertEqual(graph.nodes[0] < graph.nodes[1], True)

        print('Success: test_graph')

    def test_graph_undirected(self):
        # pass
        graph = self.create_graph()
        graph.add_undirected_edge(0, 1, weight=5)
        graph.add_undirected_edge(0, 5, weight=2)
        graph.add_undirected_edge(1, 2, weight=3)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[0].key], 5)
        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[0].key], 2)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[1].key], 3)

        print('Success: test_graph_undirected')


def main():
    test = TestGraph()
    test.test_graph()
    test.test_graph_undirected()


if __name__ == '__main__':
    main()
