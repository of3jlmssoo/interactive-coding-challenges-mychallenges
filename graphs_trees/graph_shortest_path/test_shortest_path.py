import logging
import unittest
from collections import deque

from test_graph import Graph, Node, State

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

class ShortestPath(object):

    def __init__(self, graph):
        # TODO: Impclement me
        # pass
        self.path_weight = {}   # {'a': 0, 'b': 4, 'c': 3, 'e': 2, 'd': 4, 'g': None, 'h': 6, 'i': 9, 'f': None} 
        self.__whoUpdated = {}  # 
        self.__graph = graph    # 対象グラフを保管
        for n in graph.nodes:
            self.path_weight[n]=float('inf')
        logger.debug(f'ShortestPath.__init__ {self.path_weight}')

        for n in graph.nodes:        
            if ( graph.nodes[n].visit_state != State.unvisited ): 
                raise TypeError(f'ShortestPath.__init__ State.unvisited error')
            self.__whoUpdated[n] = None

    def find_shortest_path(self, start_node_key, end_node_key):
        """
        5つのパート
        1) 開始ノードのself.path_weightを0にセット
        2) 開始ノードの隣接ノードのself.path_weightを更新
        3) 開始のノードの隣接ノードに移動して更に先の隣接ノードのself.path_weightを更新
        4) 残りのノードの処理
        5) start_node_keyからend_node_keyの間のノードをリストアップ
        """
        # TODO: Implement me
        # pass

        """1) 開始ノードのself.path_weightを0にセット"""
        """start_node_keyのノードを0にセット"""
        # if self.path_weight[start_node_key] == None:
        if self.path_weight[start_node_key] == float('inf'):
           self.path_weight[start_node_key] = 0 
        logger.debug(f'ShortestPath.find_shortest_path self.path_weight:{self.path_weight}')
        logger.debug(f'ShortestPath.find_shortest_path adj_nodes:{self.__graph.nodes[start_node_key].adj_nodes}')

        """2) 開始ノードの隣接ノードのself.path_weightを更新"""
        """start_node_keyの隣接ノードのself._path_weight更新。start_node_keyのweight+start_node_keyから該当ノードへのweight"""
        for adj_n in self.__graph.nodes[start_node_key].adj_nodes.values():
            # print(adj_n)
            # print(self.__graph.nodes[start_node_key].adj_weights[str(adj_n)])
            self.path_weight[str(adj_n)] = self.path_weight[start_node_key] + self.__graph.nodes[start_node_key].adj_weights[str(adj_n)]
            self.__whoUpdated[str(adj_n)] = start_node_key
        logger.debug(f'ShortestPath.find_shortest_path self.path_weight:{self.path_weight}')
        logger.debug(f'ShortestPath.find_shortest_path self.__whoUpdated:{self.__whoUpdated}')
        """start_node_keyのノードをvisistedにセット。"""
        """self.__whoUpdatedは最初のノードなので更新しない。更新するとしたら自分の値か"""
        self.__graph.nodes[start_node_key].visit_state = State.visited
        logger.debug(f'ShortestPath.find_shortest_path node:{start_node_key} visit_state:{self.__graph.nodes[start_node_key].visit_state}' )
        logger.debug(f'ShortestPath.find_shortest_path self.path_weight:{self.path_weight}')


        """3) 開始のノードの隣接ノードに移動して更に先の隣接ノードのself.path_weightを更新"""
        """start_node_keyの隣接ノードをweigthの軽い順にソート"""
        next_nodes = sorted([n for n in self.path_weight.items() if n[1] != float('inf') and n[0] != start_node_key], key=lambda x:x[1])
        # next_nodes = sorted([n for n in self.path_weight.items() if n[1] != None and n[0] != start_node_key], key=lambda x:x[1], reverse=True)
        """start_node_keyの隣接ノードの各々についてweightを更新"""
        for n in next_nodes:
            # print(n)
            for adj_n in self.__graph.nodes[n[0]].adj_nodes.values():
                # print("    ", n[1], self.__graph.nodes[n[0]].adj_weights[str(adj_n)], "    ", self.path_weight[str(adj_n)] )
                """self._path_weight更新。start_node_keyのweight+start_node_keyから該当ノードへのweight"""
                # if self.path_weight[str(adj_n)] == None or (n[1]+self.__graph.nodes[n[0]].adj_weights[str(adj_n)]) < self.path_weight[str(adj_n)]:
                if self.path_weight[str(adj_n)] == float('inf') or (n[1]+self.__graph.nodes[n[0]].adj_weights[str(adj_n)]) < self.path_weight[str(adj_n)]:
                    self.path_weight[str(adj_n)] = n[1] + self.__graph.nodes[n[0]].adj_weights[str(adj_n)]
                    """TODO 誰が最低値を更新したか記録する"""
                    self.__whoUpdated[str(adj_n)] = n[0]
            """TODO 該当ノードをvisistedにする"""
            self.__graph.nodes[n[0]].visit_state = State.visited
            logger.debug(f'ShortestPath.find_shortest_path node:{n[0]} visit_state:{self.__graph.nodes[start_node_key].visit_state}' )
            # self.__graph.return_nodes()

        logger.debug(f'ShortestPath.find_shortest_path self.path_weight:{self.path_weight}')
        logger.debug(f'ShortestPath.find_shortest_path self.__whoUpdated:{self.__whoUpdated}')

        """4) 残りのノードの処理"""
        """ HACK: duplicated code with the above."""
        while( n:= self.next_node()):
            for adj_n in self.__graph.nodes[n[0]].adj_nodes.values():
                # print("    ", n[1], self.__graph.nodes[n[0]].adj_weights[str(adj_n)], "    ", self.path_weight[str(adj_n)] )
                """self._path_weight更新。start_node_keyのweight+start_node_keyから該当ノードへのweight"""
                # if self.path_weight[str(adj_n)] == None or (n[1]+self.__graph.nodes[n[0]].adj_weights[str(adj_n)]) < self.path_weight[str(adj_n)]:
                if self.path_weight[str(adj_n)] == float('inf') or (n[1]+self.__graph.nodes[n[0]].adj_weights[str(adj_n)]) < self.path_weight[str(adj_n)]:
                    self.path_weight[str(adj_n)] = n[1] + self.__graph.nodes[n[0]].adj_weights[str(adj_n)]
                    """TODO 誰が最低値を更新したか記録する"""
                    self.__whoUpdated[str(adj_n)] = n[0]
            """TODO 該当ノードをvisistedにする"""
            self.__graph.nodes[n[0]].visit_state = State.visited
            logger.debug(f'ShortestPath.find_shortest_path self.path_weight:{self.path_weight}')
            logger.debug(f'ShortestPath.find_shortest_path self.__whoUpdated:{self.__whoUpdated}')
            logger.debug(f'ShortestPath.find_shortest_path node:{n[0]} visit_state:{self.__graph.nodes[start_node_key].visit_state}' )

        """5) start_node_keyからend_node_keyの間のノードをリストアップ"""
        return self.make_route(start_node_key, end_node_key)

    def make_route(self, start_node_key, end_node_key):
        """
        self.__whoUpdated:{'a': None, 'b': 'c', 'c': 'a', 'e': 'a', 'd': 'c', 'g': 'd', 'h': 'd', 'i': 'g', 'f': 'h'}
        self.assertEqual(result, ['a', 'c', 'd', 'g', 'i'])
        """
        route = [end_node_key]
        current_node = end_node_key
        l = len(self.__whoUpdated)

        while current_node!=start_node_key and l>=0:
            route.append(self.__whoUpdated[current_node])
            current_node = self.__whoUpdated[current_node]
        route.reverse()
        return route

    def next_node(self):
        unvisited_nodes_weight = {}
        # unvisted_nodes = [n for n in self.__graph.nodes if self.__graph.nodes[n].visit_state == State.unvisited]
        for m in [n for n in self.__graph.nodes if self.__graph.nodes[n].visit_state == State.unvisited]:
            unvisited_nodes_weight[m]=self.path_weight[m]
        logger.debug(f'ShortestPath.next_node unvisited_nodes_weight:{unvisited_nodes_weight}')

        if len(unvisited_nodes_weight) == 0:
            return 0
        else:
            # unvisited_nodes_weight = sorted(unvisited_nodes_weight.items(), key=lambda x:x[1])
            logger.debug(f'ShortestPath.next_node will be returned {sorted(unvisited_nodes_weight.items(), key=lambda x:x[1])[0]}') # 最初のエントリー('d', 4)を返す
            return sorted(unvisited_nodes_weight.items(), key=lambda x:x[1])[0] # 最初のエントリー('d', 4)を返す


        


class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        graph = Graph()
        graph.add_edge('a', 'b', weight=5)
        graph.add_edge('a', 'c', weight=3)
        graph.add_edge('a', 'e', weight=2)
        graph.add_edge('b', 'd', weight=2)
        graph.add_edge('c', 'b', weight=1)
        graph.add_edge('c', 'd', weight=1)
        graph.add_edge('d', 'a', weight=1)
        graph.add_edge('d', 'g', weight=2)
        graph.add_edge('d', 'h', weight=1)
        graph.add_edge('e', 'a', weight=1)
        graph.add_edge('e', 'h', weight=4)
        graph.add_edge('e', 'i', weight=7)
        graph.add_edge('f', 'b', weight=3)
        graph.add_edge('f', 'g', weight=1)
        graph.add_edge('g', 'c', weight=3)
        graph.add_edge('g', 'i', weight=2)
        graph.add_edge('h', 'c', weight=2)
        graph.add_edge('h', 'f', weight=2)
        graph.add_edge('h', 'g', weight=2)
        
        # graph.return_nodes()
        
        shortest_path = ShortestPath(graph)

        # shortest_path.find_shortest_path('a', 'i')

        result = shortest_path.find_shortest_path('a', 'i')
        self.assertEqual(result, ['a', 'c', 'd', 'g', 'i'])
        self.assertEqual(shortest_path.path_weight['i'], 8)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()
