import logging
import unittest
from collections import deque

from test_graph import Graph, Node, State
from test_shortest_path_weights import ShortestPath

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

class GraphShortestPath(Graph):

    def __init__(self):
        super().__init__()
        self.__shortest_path = None 

    def add_node(self,id):
        id=str(id)
        super().add_node(id)
        return self.nodes[id]
    
    def add_edge(self, source, dest, weight=0):
        source=str(source)
        dest=str(dest)
        super().add_edge(source, dest, weight)

    def shortest_path(self, source_key, dest_key):
        # TODO: Implement me
        pass

        # print(self.nodes)

        """
        HACK:ShortestPath(self)のコールがここでこの形態で良いか検討する。
        以下の理由からここに、この形態に至る。
        - ShortestPath()を利用したい 
        - GraphShortestPath()の__init__でコールするとエラーになる
        - shortest_path()は同じグラフを前提に繰返しコールされる
        """
        if self.__shortest_path == None:
            self.__shortest_path = ShortestPath(self)
        
        result = self.__shortest_path.find_shortest_path(str(source_key), str(dest_key))
        

        """ルートが無い場合self.__shortest_path.find_shortest_path()がNoneを返すことに対応"""
        """
        HACK:resultに要素がある場合int()で数値に変換できることを前提にしている。
        アルファベットの場合ValueErrorが起きるのでこれをキャッチするように修正する
        """
        if result != None:
            for i in range(len(result)):
                result[i] = int(result[i])

        return result

class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        nodes = []
        graph = GraphShortestPath()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        # graph.return_nodes()
        # print("-----", graph.shortest_path(nodes[0].key, nodes[2].key) )

        self.assertEqual(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        self.assertEqual(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        self.assertEqual(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()
