"""
[参照]
https://afteracademy.com/blog/sort-a-stack-using-another-stack
を見たが、以下のソリューションステップと例を結びつけて考えるのが難しい。インプットのスタックは[1, 2, 5, 3, 4]で、
最初に取り出されるエレメントが1(左)で次は4(右)。その次は3(右)。

ソリューションステップ
1) Create a temporary stack say aux_stack.
2) Repeat until the input_stack is not empty
3) Pop an element from input_stack call it temp_value.
4) While aux_stack is not empty and top of the aux_stack < temp_value, pop data from aux_stack and push it to the input_stack
5) Push temp_value to the aux_stack
6) return the aux_stack.

例
Element taken out: 1
Input Stack: [2, 5, 3, 4]
Aux Stack: [1]

Element taken out: 4
Input Stack: [2, 5, 3]
Aux Stack: [1, 4]

Element taken out: 3
Input Stack: [2, 5, 4]
Aux Stack: [1]

Element taken out: 3
Input Stack: [2, 5, 4]
Aux Stack: [1, 3]

Element taken out: 4
Input Stack: [2, 5]
Aux Stack: [1, 3, 4]

Element taken out: 5
Input Stack: [2]
Aux Stack: [1, 3, 4, 5]

Element taken out: 2
Input Stack: [5]
Aux Stack: [1, 3, 4]

Element taken out: 2
Input Stack: [5, 4]
Aux Stack: [1, 3]

Element taken out: 2
Input Stack: [5, 4, 3]
Aux Stack: [1]

Element taken out: 2
Input Stack: [5, 4, 3]
Aux Stack: [1, 2]

Element taken out: 3
Input Stack: [5, 4]
Aux Stack: [1, 2, 3]

Element taken out: 4
Input Stack: [5]
Aux Stack: [1, 2, 3, 4]

Element taken out: 5
Input Stack: []
Aux Stack: [1, 2, 3, 4, 5]

Output - [1, 2, 3, 4, 5]

[前提]
When sorted, should the largest element be at the top or bottom?        Top

[再考]
# pop from input_stack and save the value to temp
# (compare temp and peek of aux_stack)
# if temp > peek of aux_stack:
#     push temp to aux_stack
# else:
      while aux.peek() is not None and temp < peek of aux_stack and
#       pop from aux_stack and push it to input_stack
#     push temp to aux_stack

INPUT						AUX						T
1	2	5	3	4
	1	2	5	3								4
	1	2	5	3						4
		1	2	5						4		3
	1	2	5	4								3
	1	2	5	4						3
		1	2	5						3		4
		1	2	5					3	4
			1	2					3	4		5
			1	2				3	4	5
				1				3	4	5		2
			1	5					3	4		2
		1	5	4						3		2
	1	5	4	3								2
	1	5	4	3						2
		1	5	4						2		3
		1	5	4					2	3
			1	5					2	3		4
			1	5				2	3	4
				1				2	3	4		5
				1			2	3	4	5
							2	3	4	5		1
				5				2	3	4		1
			5	4					2	3		1
		5	4	3						2		1
	5	4	3	2								1
	5	4	3	2						1
		5	4	3						1		2
		5	4	3					1	2
			5	4					1	2		3
			5	4				1	2	3
				5				1	2	3		4
				5			1	2	3	4
							1	2	3	4		5
						1	2	3	4	5


"""
import unittest
from random import randint

from test_linked_list import Node
from test_stack import Stack

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


class MyStack(Stack):

    def __init__(self, top=None):
        super().__init__(None)
        self.aux_stack = Stack(None)

    def sort(self):
        # TODO: Implement me
        # pass

        self.list_two_stacks()
        while self.peek() is not None:
            tmp_val = self.pop()
            if not logger.disabled:
                print(f'while {tmp_val} ', end='')
            if self.aux_stack.peek() is None or tmp_val > self.aux_stack.peek():
                self.aux_stack.push(tmp_val)
                if not logger.disabled:
                    print(f'then --- ', end='')
                    self.list_two_stacks()
            else:
                while self.aux_stack.peek() is not None and tmp_val < self.aux_stack.peek():
                    self.push(self.aux_stack.pop())
                self.aux_stack.push(tmp_val)
                if not logger.disabled:
                    print(f'else --- ', end='')
                    self.list_two_stacks()
        return self.aux_stack

    def list_two_stacks(self):
        if not logger.disabled:
            if self.peek() is not None:

                current_node = self._start_node
                print(f'{current_node.data}', end='')
                while current_node.link is not None:
                    current_node = current_node.link
                    print(f'{current_node.data}', end='')

            print(f' --- ', end='')
            if self.aux_stack.peek() is not None:
                current_node = self.aux_stack._start_node
                print(f'{current_node.data}', end='')
                while current_node.link is not None:
                    current_node = current_node.link
                    print(f'{current_node.data}', end='')
            print('\n')


class TestSortStack(unittest.TestCase):

    def get_sorted_stack(self, stack, numbers):
        for x in numbers:
            stack.push(x)
        sorted_stack = stack.sort()
        return sorted_stack

    def test_sort_stack(self, stack):
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack(stack, [])
        self.assertEqual(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack(stack, [1])
        self.assertEqual(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) for x in range(num_items)]

        numbers = [2, 7, 8, 3, 9, 9, 7, 10, 8, 7]
        # numbers = [1, 2, 5, 3, 4]
        # print(f'{numbers=}')

        sorted_stack = self.get_sorted_stack(stack, numbers)
        sorted_numbers = []
        for _ in range(num_items):
            sorted_numbers.append(sorted_stack.pop())
        self.assertEqual(sorted_numbers, sorted(numbers, reverse=True))

        print('Success: test_sort_stack')


def main():
    test = TestSortStack()
    test.test_sort_stack(MyStack())
    # test.test_sort_stack(MyStackSimplified())


if __name__ == '__main__':
    main()
