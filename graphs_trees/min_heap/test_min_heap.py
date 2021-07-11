"""
(1)テスト内容の違い
test_min_heap.pyとmin_heap_challenge.ipynbのテスト内容が異なる

[test_min_heap.py] [min_heap_challenge.ipynb]
peek_min()1回のみ   peek_min()多数
(insert(20)の後)
self.assertEqual(heap.array[0], 20)
                    self.assertEqual(heap.peek_min(), 20)
(他のinsert()でも同様)

TODO: rest_min_heap.pyにpeek_min()とself.assertEqual(heap.peek_min(), 20)を追加する

(2)参考情報
https://en.wikipedia.org/wiki/Heap_(data_structure)
In a min heap, the key of P is less than or equal to the key of C.[2] The node at the "top" of the heap (with no parents) is called the root node.
P:Parent,　C:Child

given a node at index i, its children are at indices 2i + 1 and 2i + 2, and its parent is at index floor((i-1)/2). 

https://en.wikipedia.org/wiki/Min-max_heap

https://www.cs.cmu.edu/~tcortina/15-121sp10/Unit06B.pdf
Inserting into a min-heap
 Place the new element in the next available
position in the array.
 Compare the new element with its parent. If the
new element is smaller, than swap it with its
parent.
 Continue this process until either
- the new element’s parent is smaller than or
equal to the new element, or
- the new element reaches the root (index 0 of
the array) 

(3)テストデータ
入力順 : 20, 5, 15, 22, 40, 3

array : [3,20,5,22,40,15]

(4)メソッド
class MinHeap()では以下の5メソッド
__init__
extract_min minのノードを除く
peek_min    minのノードを返す     
insert      ノードを追加する
_bubble_up  (今はおいておく)
 
"""
import math
import unittest
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

class MinHeap(object):

    def __init__(self):
        # TODO: Implement me
        # pass
        self.array = []
        logger.debug(f'MinHeap.__init__ called. self.array : {self.array}')


    def extract_min(self):
        # TODO: Implement me
        # pass    
        if len(self.array) == 0: return None

    def peek_min(self):
        # TODO: Implement me
        # pass
        if len(self.array) == 0: return None

    def insert(self, data):
        # TODO: Implement me
        # pass
        self.array.append(data)
        # print(f'1) parent index is {math.floor((len(self.array)-1)/2)}')
        # print(f'2) parent {self.array[math.floor(self.array.index(data)/2)]} child {self.array[self.array.index(data)]}')
        i = 0
        parent_index = math.floor((self.array.index(data)-1)/2)
        child_index  = self.array.index(data)
        while self.array.index(data) != 0 and self.array[parent_index] > self.array[child_index]:
            # print(f'parent_index:{parent_index}, child_index:{child_index}, self.array[parent_index]:{self.array[parent_index]}, self.array[child_index]:{self.array[child_index]}')
            self.array[parent_index], self.array[child_index] = self.array[child_index], self.array[parent_index]
            parent_index = math.floor((self.array.index(data)-1)/2)
            child_index  = self.array.index(data)
            i += 1
            if i>100: 
                print(f'i>100')
                break

    def _bubble_up(self, index):
        # TODO: Implement me
        pass

class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        heap = MinHeap()

        self.assertEqual(heap.peek_min(), None)
        self.assertEqual(heap.extract_min(), None)
        heap.insert(20)
        self.assertEqual(heap.array[0], 20)
        heap.insert(5)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        heap.insert(15)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        heap.insert(22)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        self.assertEqual(heap.array[3], 22)
        heap.insert(40)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        self.assertEqual(heap.array[3], 22)
        self.assertEqual(heap.array[4], 40)
        heap.insert(3)
        self.assertEqual(heap.array[0], 3)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 5)
        self.assertEqual(heap.array[3], 22)
        self.assertEqual(heap.array[4], 40)
        self.assertEqual(heap.array[5], 15)
        # mins = []
        # while heap:
        #     mins.append(heap.extract_min())
        # self.assertEqual(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()
