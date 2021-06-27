import unittest
import logging
from test_graph import State
from test_graph import Node
from test_graph import Graph
from test_graph import State
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

class Dependency(object):

    def __init__(self, node_key_before, node_key_after):
        self.node_key_before = node_key_before
        self.node_key_after = node_key_after

class node_key(object):
    def __init__(self, val) -> None:
        self.__key=val

    @property
    def key(self):
        return self.__key

class BuildOrder(object):

    def __init__(self, dependencies):
        # TODO: Implement me
        # pass
        self.__processed_nodes = [] # each element will be accessed by .key
        self.__processed_nodes_work = [] # [d, f, g, c, b, a, e]
        self.__dependencies = dependencies
        
        self.__dependenciesList=[]
        self.__rootNodes=[]         # ルートノードを保管
        self.__groupStr=[]          # [[f,c,b,a,e],[d,g]]
        self.__groupNode=[]         # [ [[d, g]], [[f, c], [f, b], [f, a], [c, a], [b, a], [a, e], [b, e]] ]

        for n in self.__dependencies:
            self.__dependenciesList.append([n.node_key_before, n.node_key_after])
        logger.debug(f'self.__dependencies: {self.__dependencies}\n')
        logger.debug(f'self.__dependencies_list: {self.__dependenciesList}\n')

    def find_build_order(self):
        """find_build_order 
        ルートノードは最初にでてくる
        dependencyは順番にでてくる
        ノード値の重複は無い
        """
        # TODO: Implement me
        # pass
        
        for n in self.__dependencies:
            self.make_work_lists(n)
        # print(f'--> self.__groupStr: {self.__groupStr}')
        # print(f'==> self.__groupNode: {self.__groupNode}')

        if self.check_cycle(): 
            print(f'BuildOrder.find_build_order cycle found')
            return None

        return self.process_nodes()

    def process_nodes(self): 
        """process_nodes
        前提：独立ツリーの数は2つ

        self.__processed_nodes_workは以下のようになる。
        ['d', 'f', 'g', 'c', 'b', 'a', 'e']

        .keyアクセスが必要なので、class node_key()を定義した上でself.__processed_nodesへ変換して保管

        self.__groupNode: [[['d', 'g']], [['f', 'c'], ['f', 'b'], ['f', 'a'], ['c', 'a'], ['b', 'a'], ['a', 'e'], ['b', 'e'], ['e', 'f']]]
        d系列とf系列の2つの系列がある。d系列の長さは1でf系列の長さは8。lにminの1がセットされる(l=1)
        重なっている部分(d系列[0]とf系列[0])はキャラクターの順番に注意が必要。
        長いf系列のf系列[l:]は出てきた順番にセットする
        """
        l = min([len(l) for l in self.__groupNode])
        for i in range(l):
            # 重なっている部分を処理
            # 下の最初のforループ：各系列のデータのnode_key_beforeをセットする
            # 下の2つ目のforループ：各系列のデータのnode_key_afterをセットする
            #
            # HACK: hack x 2
            #
            for n in self.__groupNode: 
                if n[i][0] not in self.__processed_nodes_work: self.__processed_nodes_work.append(n[i][0])
            for n in self.__groupNode: 
                if n[i][1] not in self.__processed_nodes_work: self.__processed_nodes_work.append(n[i][1])
        for j, longerNode in enumerate(self.__groupNode):
            # 長い方の系列(f系列)に関し後続の未処理部分を処理
            if len(longerNode) > l:
                for rest in self.__groupNode[j][l:]:
                    if rest[0] not in self.__processed_nodes_work: self.__processed_nodes_work.append(rest[0])
                    if rest[1] not in self.__processed_nodes_work: self.__processed_nodes_work.append(rest[1])
        # print(f'BuildOrder.process_nodes() l:{l} self.__processed_nodes:{self.__processed_nodes_work}')
        for n in self.__processed_nodes_work:
            # 単純なキャラクターのリストを.keyアクセスできるように変換
            self.__processed_nodes.append(node_key(n))

        return self.__processed_nodes

    def check_cycle(self):
        """check_cycle
        テストデータの場合、fとdはnode_key_beforeに登場するがnode_key_afterには登場しない
        fやdのようにnode_key_afterに登場しないキャラクターを数える
        この数と系列数を比較する。同じであればcycle無し
        """
        first_col_list = []
        second_col_list = []
        result = 0
        for g in self.__groupNode:
            first_col_list = set([c[0] for c in g])
            second_col_list = set([c[1] for c in g])
            for fc in first_col_list:
                if fc not in second_col_list: 
                    result += 1
        
        return not(len(self.__groupNode) == result)

    def make_work_lists(self,node):
        """make_work_lists 
        前提:ツリーは独立している

        サンプルデータの場合、ワーク用リストself.__groupStrとself.__groupNodeは以下のようになる。
        self.__groupStr: [['d', 'g'], ['f', 'c', 'b', 'a', 'e']]
            self.__groupStr[0] 'd'系のメンバーを集めている
            self.__groupStr[1] 'f'系のメンバーを集めている
        self.__groupNode: [[['d', 'g']], [['f', 'c'], ['f', 'b'], ['f', 'a'], ['c', 'a'], ['b', 'a'], ['a', 'e'], ['b', 'e'], ['e', 'f']]]
            self.__groupNode[0] 'd'系のデータを集めている
            self.__groupNode[1] 'f'系のデータを集めている
        """
        logger.debug(f'BuildOrder.check_new_or_exist node.node_key_before:{node.node_key_before} node.node_key_after:{node.node_key_after} self.__groupStr:{self.__groupStr}')
        if len(self.__groupStr) == 0:
            # 1つ目のエントリーを処理
            self.__groupStr=[[node.node_key_before]]
            self.__groupStr[0].append(node.node_key_after)
            self.__groupNode=[[[node.node_key_before, node.node_key_after]]]
            logger.debug(f'BuildOrder.make_work_lists() {self.__groupNode}')
        else:
            for i in range(len(self.__groupStr)):
                # nodeのbeforeかafterがすでにself.__groupStrにある場合、ここ
                if node.node_key_before in self.__groupStr[i] or node.node_key_after in self.__groupStr[i]:
                    if node.node_key_before not in self.__groupStr[i]: self.__groupStr[i].append(node.node_key_before)
                    if node.node_key_after not in self.__groupStr[i]: self.__groupStr[i].append(node.node_key_after)
                    self.__groupNode[i].append([node.node_key_before, node.node_key_after])
                    # self.__groupNode.insert(i,[node.node_key_before, node.node_key_after])
                    return
            # 新しいエントリーの場合ここで追加
            l = len(self.__groupStr)
            self.__groupStr.insert(l,[node.node_key_before])
            self.__groupStr[l].append(node.node_key_after)
            self.__groupNode.insert(l,[[node.node_key_before, node.node_key_after]])
            
    
        return 

        # logger.debug(f'self.__rootNodes: {self.__rootNodes}\n')

class TestBuildOrder(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBuildOrder, self).__init__()
        self.dependencies = [
            Dependency('d', 'g'),
            # Dependency('g', 'z'), # additional data for test
            Dependency('f', 'c'),
            Dependency('f', 'b'),
            Dependency('f', 'a'),
            Dependency('c', 'a'),
            Dependency('b', 'a'),
            Dependency('a', 'e'),
            Dependency('b', 'e'),
            # Dependency('d', 'g'),
            # Dependency('e', 'f')
        ]

    def test_build_order(self):
        build_order = BuildOrder(self.dependencies)
        
        build_order.find_build_order()
        processed_nodes = build_order.find_build_order()

        expected_result0 = ('d', 'f')
        expected_result1 = ('c', 'b', 'g')
        self.assertTrue(processed_nodes[0].key in expected_result0)
        self.assertTrue(processed_nodes[1].key in expected_result0)
        self.assertTrue(processed_nodes[2].key in expected_result1)
        self.assertTrue(processed_nodes[3].key in expected_result1)
        self.assertTrue(processed_nodes[4].key in expected_result1)
        self.assertTrue(processed_nodes[5].key == 'a')
        self.assertTrue(processed_nodes[6].key == 'e')

        print('Success: test_build_order')

    def test_build_order_circular(self):
        self.dependencies.append(Dependency('e', 'f'))
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        self.assertTrue(processed_nodes is None)

        print('Success: test_build_order_circular')


def main():
    test = TestBuildOrder()
    test.test_build_order()
    test.test_build_order_circular()


if __name__ == '__main__':
    main()
