""" test_draw_line.py

Raises:
    TypeError: [description]
    ValueError: [description]
    ValueError: [description]
"""
import unittest




class BitsScreen(object):

    def draw_line(self, screen, width, x1, x2):
        if None in (screen, width, x1, x2):
            raise TypeError('Invalid argument: None')
        if not screen or not width:
            raise ValueError('Invalid arg: Empty screen or width')
        
        print("draw_line() len(screen) ", len(screen))

        MAX_BIT_VALUE = len(screen) * 8
        if x1 < 0 or x2 < 0 or x1 >= MAX_BIT_VALUE or x2 >= MAX_BIT_VALUE:
            raise ValueError('Invalid arg: x1 or x2 out of bounds')
        start_bit = x1 % 8
        end_bit = x2 % 8

        print("x1 ", x1, " x2 ", x2, "start_bit ", start_bit, " end_bit ", end_bit)

        first_full_byte = x1 // 8
        if start_bit != 0:
            first_full_byte += 1
        last_full_byte = x2 // 8
        if end_bit != (8 - 1):
            last_full_byte -= 1
        print("first_ull_byte ", first_full_byte, " last_full_byte ", last_full_byte)
        print("first_ull_byte ", first_full_byte, " last_full_byte+1 ", last_full_byte+1)


        for byte in range(first_full_byte, last_full_byte + 1):
            print("== byte ", byte)
            screen[byte] = int('11111111', base=2)

        start_byte = x1 // 8
        end_byte = x2 // 8

        print("start_byte ", start_byte, " end_byte ", end_byte)


        if start_byte == end_byte:
            left_mask = (1 << (8 - start_bit)) - 1
            right_mask = ~((1 << (8 - end_bit - 1)) - 1)
            mask = left_mask & right_mask
            screen[start_byte] |= mask
        else:
            start_mask = (1 << (8 - start_bit)) - 1
            end_mask = 1 << (8 - end_bit - 1)
            screen[start_byte] |= start_mask
            screen[end_byte] |= end_mask


class TestBitsScreen(unittest.TestCase):

    def test_draw_line(self):
        bits_screen = BitsScreen()
        screen = []
        for _ in range(20):
            screen.append(int('00000000', base=2))

        print("screen 1 ", screen)

        bits_screen.draw_line(screen, width=32, x1=68, x2=80)
        print("screen 2 ", screen)

        self.assertEqual(screen[8], int('00001111', base=2))
        self.assertEqual(screen[9], int('11111111', base=2))
        self.assertEqual(screen[10], int('10000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=2, x2=6)
        self.assertEqual(screen[0], int('00111110', base=2))
        bits_screen.draw_line(screen, width=32, x1=10, x2=13)
        self.assertEqual(screen[1], int('00111100', base=2))
        print('Success: test_draw_line')


def main():
    test = TestBitsScreen()
    test.test_draw_line()


if __name__ == '__main__':
    main()