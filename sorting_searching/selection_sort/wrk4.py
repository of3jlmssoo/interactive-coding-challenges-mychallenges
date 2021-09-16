"""
0 1 2 3 4 5 6 7
8 4 3 7 6 5 2 1
  i=0 l=len-1-i=8-1-0=7
  min  max
  8    8
  4    8
  3    8
  2    8
  1@7  8@0
  swap i and l (special case)
0 1 2 3 4 5 6 7
1 4 3 7 6 5 2 8
  i=1 l=len-1-i=8-1-1=6
  min   max
  4     4
  3     4
  3     7
  2@6   7@3
  swap i=1 and 6
0 1 2 3 4 5 6 7
1 4 3 7 6 5 2 8
1 2 3 7 6 5 4 8
  swap l=6 and 3
0 1 2 3 4 5 6 7
0 1 2 4 6 5 7 8
  i=2 l=len-1-2=8-1-1=5
  min   max
  2     2
  2     4
  2@2   6@4
  swap i=2 and 2 (no need to execute)
  swap l=5 and 4
0 1 2 3 4 5 6 7
0 1 2 4 5 6 7 8










saku hiro <7a4wiy5vd638@gmail.com>
5:23 PM (1 hour ago)
to me

0 1 2 3 4 5 6 7
6 8 2 1 3 7 4 5
  i=0     i to len-1-i
  min max
  6      6
  6      8
  2      8
  1      8
  d[0]=1
  d[len-1-i]=8
0 1 2 3 4 5 6 7
6 8 2 1 3 7 4 5
1 5 2 6 3 7 4 8
swap  index i and index 1
swap index len-1-i and index 8
0 1 2 3 4 5 6 7
1 5 2 6 3 7 4 8
  i=1     i to len-1-i
  min max
  5      5
  2      5
  2      7
swap index i and index 2
swap index len-1-i and index 7
0 1 2 3 4 5 6 7
1 2 5 6 3 4 7 8
  i=2     i to len-1-i(=5)
  min max
  5      5
  5      6
  3      6
0 1 2 3 4 5 6 7
1 2 5 6 3 4 7 8
1 2 3 6 5 4 7 8
1 2 3 4 5 6 7 8
swap index i and index 3
swap index len-1-i and index 6

"""
data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
# data = [8, 4, 3, 7, 6, 5, 2, 1]

"""
for i in range(0,len(data)):
  min = i
  for j in range(i+1,len(data)):
    if data[j] < data[min]:
      min = j
  data[i], data[min] = data[min], data[i]
  print(data)
print(data)
"""
print(f'{data=}')
for i in range(0, len(data) // 2):
    min = i
    # max = len(data)-1-i
    max = i
    l = len(data) - 1 - i
    print(f'1) {min=} {max=} {i=} {l=}')
    for j in range(i + 1, len(data) - i):
        if data[j] < data[min]:
            min = j
        if data[j] > data[max]:
            max = j
    print(f'2) {min=} {max=} {i=} {l=} {j=}')

    if i == max and l == min:
        print(f'then {data[l]=} {data[i]=}')
        data[i], data[l] = data[l], data[i]
    else:
        print(f'else {data[min]=} {data[i]=}')
        print(f'else {data[min]=} {data[l]=}')
        data[i], data[min] = data[min], data[i]
        data[l], data[max] = data[max], data[l]
    print(data, '\n')
print(f'{data=}')
