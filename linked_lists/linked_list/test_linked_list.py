"""
[参考]
https://people.engr.ncsu.edu/efg/210/s99/Notes/LinkedList.1.html

node
    info
    link(to the next node)
head pointer
link of the last ndoe is null

"""
import unittest
import logging


logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
# DEBUG INFO WARNIG ERROR CRTICAL
logger.setLevel(logging.DEBUG)
ch.setLevel(logging.DEBUG)
logger.disabled = True


class Node(object):

    def __init__(self, data, next_node=None):
        # pass
        # TODO: Implement me
        print(f'Node.__init__:{data=} inited')
        self.__data = data
        self.__link = next_node

        self.__next = self.__link

    def __str__(self):
        pass
        # TODO: Implement me
        return str(self.data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, n):
        self.__data = n

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, n):
        self.__link = n

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n
        self.__link = self.__next


class LinkedList(object):

    def ls_nodes(self):
        for n in self.q:
            print(f'{n} {n.data} {n.link}')

    def __init__(self, head=None):
        pass
        # TODO: Implement me
        self.head = head
        # self.q = deque([])
        self.q = []
        if head is not None:
            self.q = self.q + [head]
        logger.debug(f'LinkedList.__init__: called')

    def __len__(self):
        # pass
        # TODO: Implement me
        return len(self.q)

    def insert_to_front(self, data):
        pass
        # TODO: Implement me
        logger.debug(f'LinkedList.__init__: called')
        if data is None:
            return

        self.node = Node(data, None)
        self.head = self.node
        if self.q:
            self.node.link = self.q[0]
        else:
            self.node.link = None
        self.q = [self.node] + self.q
        logger.debug(
            f'LinkedList.insert_to_front: {self.head} {self.q} {self.node.link}')

        """
        head pointer = node10
        node10.info = 10
        node10.link = None
        """

    def append(self, data):
        pass
        # TODO: Implement me
        if data is None:
            return

        node = Node(data, None)
        if self.head is None:
            self.head = node

        if self.q:
            self.q[-1].link = node
        else:
            node.link = None

        self.q = self.q + [node]
        logger.debug(
            f'LinkedList.insert_to_front: {self.head} {self.q} {node.link}')

    def find(self, data):
        pass
        # TODO: Implement me
        for n in self.q:
            if n.data == data:
                return n.data
        return None

    def delete(self, data):
        # pass
        # TODO: Implement me
        """
        1. empty listでの、存在しないデータを削除しようとする。何もしない
            ValueErrorが起きる
        2. delete noneしようとする。何もしない
        3. 3要素で真ん中を削除。linkをセットする
        4. 存在しないものを削除しようとする

        5. 先頭を削除
        6. 一番最後を削除
        """

        """ 1. empty listでの、存在しないデータを削除しようとする。何もしない
                ValueErrorが起きる
            2. delete noneしようとする。何もしない
            4. 存在しないものを削除しようとする
        """
        try:
            # idx = self.q.index(data)
            idx = [str(n.data) for n in self.q].index(data)
        except ValueError:
            print(f'LinkedList.delete: ValueError occured. {data} {self.q}')
            # for n in self.q:
            #     print(f'---{n.data}')
            #     print(f'{type(data)} {type(n.data)}')
            return
        self.q.pop(idx)
        # print(f'--------{idx} {len(self.q) + 1}')
        if idx == 0:
            """ 5. 先頭を削除 """
            self.head = self.q[0]
            self.q[0].link = self.q[idx + 1]
        elif idx == len(self.q):
            """ 6. 一番最後を削除"""
            self.q[idx - 1].link = None
        else:
            """ 3. 3要素で真ん中を削除。linkをセットする"""
            self.q[idx - 1].link = self.q[idx]

    def print_list(self):
        pass
        # TODO: Implement me

    def get_all_data(self):
        # pass
        # TODO: Implement me
        # return [n.data for n in self.q]
        return [n.data if n is not None else None for n in self.q]


class TestLinkedList(unittest.TestCase):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

        # linked_list.ls_nodes()

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

        # linked_list.ls_nodes()

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        self.assertEqual(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        self.assertEqual(node, None)

        print('Success: test_find\n')

        # linked_list.ls_nodes()

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')

        # linked_list.ls_nodes()

        linked_list.delete('a')

        # linked_list.ls_nodes()

        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        self.assertEqual(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(len(linked_list), 3)

        print('Success: test_len\n')

    def test_delete2(self):

        print('2 Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        # linked_list.ls_nodes()
        linked_list.delete('10')
        # print('\n')
        # linked_list.ls_nodes()
        # print('\n')

        linked_list = LinkedList(None)
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        # linked_list.ls_nodes()
        linked_list.delete('bc')
        # print('\n')
        # linked_list.ls_nodes()

        print('2 Success: test_delete\n')


def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()

    test.test_delete2()


if __name__ == '__main__':
    main()
