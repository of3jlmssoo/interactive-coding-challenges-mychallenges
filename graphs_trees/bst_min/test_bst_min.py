""" test_bst_min.py

math.floorで真ん中のエントリーを選択
左半分処理
    左半分のエントリー数が4以上
        真中を選んで左半分処理を再び
    左半分のエントリー数が3つ 
        真中を親ノード、小さいを方をleft、大きい方をrightに設定
        小さい方の親ノードを設定
        大きい方の親ノードを設定
    左半分のエントリー数が2つ 
        大きい方を親ノード、小さい方をleftに設定
        小さい方の親ノードを設定

右半分処理
"""

import unittest


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(unittest.TestCase):

    def test_bst_min(self):
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 4)

        print('Success: test_bst_min')


def main():
    test = TestBstMin()
    test.test_bst_min()


if __name__ == '__main__':
    main()
