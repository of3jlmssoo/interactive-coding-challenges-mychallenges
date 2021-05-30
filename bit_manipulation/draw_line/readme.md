width=32
x1=68
x2=80

len(screen)=20
initial screen [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
updated screen [0, 0, 0, 0, 0, 0, 0, 0, 15, 255, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                0  1  2  3  4  5  6  7  8    9    10  11 12 13 14 15 16 17 18 19
                elements 8,9,10

start_bit = 4   68 % 8 = 8 * 8 + 4
end_bit = 0     80 & 8 = 8 * 10 + 0

first_ull_byte  9    line(31) 68 / 8 = 8 line(33) 8+1
last_full_byte  9    80 // 8 = 10  10-1 = 9

for byteで
    screen[byte=9] = int('11111111', base=2)

start_byte  8   68//8 = 8  
end_byte  10    80//8 = 10