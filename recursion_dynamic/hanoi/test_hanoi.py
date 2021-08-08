"""
順番的にはStackの後だがhanoiで必要な分だけここで対応してしまう。
If we pop on an empty stack, do we return None?  Yes

[参照]
https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiex.html
Make one stepしながらツリーを指さしながら見る。

[テスト]
1) 動かそうにもスタックがないケース
2) 3枚のディスク(num_disks)を全て移し終えてそ

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


class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        # TODO: Implement me
        # pass

        if src is None or dest is None or buff is None:
            raise TypeError(f'Hanoi.move_disks. src or dest or buff is None')

        logger.debug(f'move_disks called at 1 {num_disks} {src} {dest} {buff}')
        if num_disks == 0:

            logger.debug(
                f'if num_disks==0 before append {num_disks} {src} {dest} {buff}')
            dest.append(src.pop())
            logger.debug(
                f'if num_disks==0 after append {num_disks} {src} {dest} {buff}')
        else:
            self.move_disks(num_disks - 1, src, buff, dest)

            logger.debug(
                f'else before append {num_disks} {src} {dest} {buff}')
            dest.append(src.pop())
            logger.debug(
                f'else after append {num_disks} {src} {dest} {buff}')

            self.move_disks(num_disks - 1, buff, dest, src)


class Stack(object):

    def __init__(self):
        self.__lst = []
        self.__id = ''

    def __str__(self) -> str:
        return str(self.__lst)

    def pop(self):
        if len(self.__lst) != 0:
            return self.__lst.pop(-1)
        else:
            return None

    def push(self, elem):
        self.__lst.append(elem)

    def append(self, elem):
        self.__lst.append(elem)


class TestHanoi(unittest.TestCase):

    def test_hanoi(self):
        hanoi = Hanoi()
        num_disks = 3
        src = Stack()
        buff = Stack()
        dest = Stack()

        print('Test: None towers')
        self.assertRaises(
            TypeError,
            hanoi.move_disks,
            num_disks,
            None,
            None,
            None)

        print('Test: 0 disks')
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), None)

        print('Test: 1 disk')
        src.push(5)
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), 5)

        print('Test: 2 or more disks')
        for disk_index in range(num_disks, -1, -1):
            src.push(disk_index)
        hanoi.move_disks(num_disks, src, dest, buff)
        for disk_index in range(0, num_disks):
            self.assertEqual(dest.pop(), disk_index)

        print('Success: test_hanoi')


def main():
    test = TestHanoi()
    test.test_hanoi()


if __name__ == '__main__':
    main()
