""" priority_queue.pyは削除する
その上でclass PriorityQueueNode(object):とclass PriorityQueue(object):をpriority_queue_challenge.ipynbからコピーする

前提：Can we assume there aren't any duplicate keys?  Yes

extract_min()について
    while priority_queue.array:
        mins.append(priority_queue.extract_min().key)

    priority_queue.arrayがなくならないとループを抜けない
    extract_min()が一度呼ばれると、
        その時点で一番小さいkeyを探す
        ループを抜けるため必ずpop()する

"""
import unittest
import sys

class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        # TODO: Implement me
        # pass
        self.array.append(node)

    def extract_min(self):
        # TODO: Implement me
        # pass
        if len(self.array) == 0: return None
        min_val = sys.maxsize
        min_pos = -1
        for i, n in enumerate(self.array):
            if min_val > (current_val := n.key):
                min_val = current_val
                min_pos = i
        return self.array.pop(min_pos)


    def decrease_key(self, obj, new_key):
        # TODO: Implement me
        # pass
        for n in self.array:
            if n.obj == obj:
                n.key = new_key

    def sort_queue(self):
        return    sorted([self.array[i].key  for i in range(len(self.array))])
        
class TestPriorityQueue(unittest.TestCase):

    def test_priority_queue(self):
        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.extract_min(), None)
        priority_queue.insert(PriorityQueueNode('a', 20))
        priority_queue.insert(PriorityQueueNode('b', 5))
        priority_queue.insert(PriorityQueueNode('c', 15))
        priority_queue.insert(PriorityQueueNode('d', 22))
        priority_queue.insert(PriorityQueueNode('e', 40))
        priority_queue.insert(PriorityQueueNode('f', 3))
        priority_queue.decrease_key('f', 2)
        priority_queue.decrease_key('a', 19)
        print("=== ", priority_queue.array)
        self.assertEqual(priority_queue.sort_queue(),  [2, 5, 15, 19, 22, 40])
        # mins = [] 
        # while priority_queue.array:
        #     mins.append(priority_queue.extract_min().key)
        # self.assertEqual(mins, [2, 5, 15, 19, 22, 40])
        print('Success: test_min_heap')


def main():
    test = TestPriorityQueue()
    test.test_priority_queue()


if __name__ == '__main__':
    main()

        # result = 0
        # for char in str1:
        #     result ^= ord(char)
        #     # print(f"=== str1 === char:{char}, ord(char):{ord(char)}, result:{result}, bin(ord(char):{bin(ord(char))},  bin(result):{bin(result)}")

        # # print(f"=== between str1 and str2 === result:{result}, bin(result):{bin(result)}")
        
        # for char in str2:
        #     result ^= ord(char)
        #     # print(f"=== str2 === char:{char}, ord(char):{ord(char)}, result:{result}, bin(ord(char):{bin(ord(char))},  bin(result):{bin(result)}")

        # # print(f"=== before return === result:{result}, chr(result):{chr(result)}")
        # return chr(result)