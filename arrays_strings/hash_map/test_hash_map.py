"""
1. 以下のコメント意識
    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test

2.  hash_table = HashTable(10)
    hash_table.set(0, 'foo')
    hash_table.set(10, 'foo3') -> 正常終了が期待されている
    よって、10区画を用意しても単純に0なら[0]とはいかない
3. For collision resolution, can we use chaining?  Yes 
    https://en.wikipedia.org/wiki/Hash_table#Separate_chainingを参考にすると、
    0  = keys => hash-function => buckets(今回の場合10個) => 0 and foo with only one mark
    10 = keys => hash-function => buckets(今回の場合10個) => 10 and foo3 with only one mar
    もし11が10のケースとhash-functionの値が同じ値になるとする
    11 = keys => hash-function => buckets(今回の場合10個) => 10 and foo3 with continued mark 11 and 11sfooooo
                                                                        chaining
4. Do we have to validate inputs?  No                                                                
    しかし、keyが重複しているとchainingでvalueを取得できなくなるのでkeyの重複は不可とする

lst = [
    [[0,'a'],[0,'aa'],[0,'aaa']],
    [[1,'b'],[1,'bb']],
    [None,None],
    [[2,'c']]
]                                                                        
"""

import copy
import dataclasses
import unittest


@dataclasses.dataclass
class Item(object):

    # def __init__(self, key, value):
        # TODO: Implement me
        # pass
    key: int
    value: str
    NextObj : object = None

class TestItem(unittest.TestCase):

    def test_item(self):
        print(f'test_item')
        item = Item(1,'a')
        self.assertEqual(item.key, 1)
        self.assertEqual(item.value, 'a')

    # def test_hashtable_init(self):
        print(f'test_hash_table_init')
        ht = HashTable(3)
        self.assertEqual(isinstance(ht,HashTable), True)
        self.assertEqual(ht.get_length_of_hash(), 3)

        print(f'test__hash_function')
        self.assertEqual(ht._hash_function(0), 0)
        self.assertEqual(ht._hash_function(1), 1)
        self.assertEqual(ht._hash_function(2), 2)
        self.assertEqual(ht._hash_function(3), 0)

        print(f'test_get_with_no_element')
        # ht.get(0)
        try:
            ht.get(0)
        except KeyError:
            print('test_get_with_no_element_KeyError')
            # raise KeyError('get KeyError')

        print(f'test_set')
        print(f'test_set 1 ht.lst {ht.lst}')
        self.assertEqual(ht.lst, [[[None, None, None]], [[None, None, None]], [[None, None, None]]])
        ht.set(0, 'foo')
        self.assertEqual(ht.lst, [[[0, 'foo', None]], [[None, None, None]], [[None, None, None]]])
        ht.set(3, 'Buu')
        self.assertEqual(ht.lst, [[[0, 'foo', None], [3, 'Buu', None]], [[None,None,None]],[[None,None,None]]])
        ht.set(6, 'ZZZ')
        self.assertEqual(ht.lst, [[[0, 'foo', None], [3,'Buu', None], [6,'ZZZ', None]], [[None,None,None]],[[None,None,None]]])

        ht.set(1, 'ONEONE')
        self.assertEqual(ht.lst, [[[0, 'foo', None], [3,'Buu', None], [6,'ZZZ', None]], [[1,'ONEONE',None]],[[None,None,None]]])
        ht.set(2, 'TWO')
        self.assertEqual(ht.lst, [[[0, 'foo', None], [3,'Buu', None], [6,'ZZZ', None]], [[1,'ONEONE',None]],[[2,'TWO',None]]])
        try:
            ht.set(2, 'TWOTWO') # key duplicated
        except KeyError:
            print('test_set key duplicated')

        # print(f'test_get')
        # print(f'test_get ht.get(2) {ht.get(2)}')

        # try:
        #     print(f'test_set 2 ht.lst {ht.lst}')
        #     ht.set(0, 'ABC')
        #     print(f'test_set 3 ht.lst {ht.lst}')
        # except KeyError:
        #     print('test_set_overflow')

class HashTable(object):
# class HashTable:

    # lstFormat = [None,None,None] # [key, value, chained?]
    # already_used =[]

    def __init__(self, size):
        # TODO: Implement me
        # pass
        # lst_format = [None,None,None] # [key, value, chained?]


        self.lstFormat = [None,None,None]
        self.__lst = [[self.lstFormat] for i in range(size)]
        # self.__lst = [[HashTable.lstFormat] for i in range(size)]
        
        # HashTable.already_used =[]
        # print(f'init {HashTable.already_used}')
        self.__alreadyUsed = []

    @property
    def lst(self):
        return self.__lst

    def get_length_of_hash(self) -> int:
        return len(self.__lst)

    def _hash_function(self, key):
        # TODO: Implement me
        # pass
        return key % self.get_length_of_hash()

    def set(self, key, value):
        # TODO: Implement me
        # pass

        # if key in HashTable.already_used:
        if key in self.__alreadyUsed:
            # raise KeyError(f'set() key {key} is already used {HashTable.already_used}')
            raise KeyError(f'set() key {key} is already used {self.__alreadyUsed}')
        else:
            # HashTable.already_used.append(key)
            self.__alreadyUsed.append(key)

        # if self.__lst[self._hash_function(key)] == [HashTable.lstFormat]:
        if self.__lst[self._hash_function(key)] == [self.lstFormat]:
            # in case of blank
            self.__lst[self._hash_function(key)] = [[key, value, None]]
            # print(f'set then {self.__lst}')
        else:
            # print(f'set else 1 {self.__lst}')
            # print(f'set else 2 {self.__lst[self._hash_function(key)][0]} + {[key,value,None]}')
            self.__lst[self._hash_function(key)] = self.__lst[self._hash_function(key)] + [[key,value,None]]
            # print(f'set else 3 {self.__lst}')

    def get(self, key):
        # TODO: Implement me
        # pass
        # self.__lst[self._hash_function(key)]
        # specified key does not exist
        if type(self.__lst[self._hash_function(key)][0]) != int:
            raise KeyError('get KeyError')


    def remove(self, key):
        # TODO: Implement me
        pass

class TestHashMap(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print("Test: creating a hash table")
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        # self.assertEqual(hash_table.get(0), 'foo')
        # hash_table.set(1, 'bar')
        # self.assertEqual(hash_table.get(1), 'bar')

        # print("Test: set on a non empty hash table index")
        # hash_table.set(10, 'foo2')
        # self.assertEqual(hash_table.get(0), 'foo')
        # self.assertEqual(hash_table.get(10), 'foo2')

        # print("Test: set on a key that already exists")
        # hash_table.set(10, 'foo3')
        # self.assertEqual(hash_table.get(0), 'foo')
        # self.assertEqual(hash_table.get(10), 'foo3')

        # print("Test: remove on a key that already exists")
        # hash_table.remove(10)
        # self.assertEqual(hash_table.get(0), 'foo')
        # self.assertRaises(KeyError, hash_table.get, 10)

        # print("Test: remove on a key that doesn't exist")
        # self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()

    testitem = TestItem()
    testitem.test_item()

if __name__ == '__main__':
    main()
