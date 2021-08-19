"""
n x m matrix
"""
import sys


class Matrix(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

# def MM()


def printM(M):
    for i in M:
        print(i)
    print('\n')


matrices = [  # 158
    Matrix(5, 4),
    Matrix(4, 6),
    Matrix(6, 2),
    Matrix(2, 7)
]

matrices = [  # 124
    Matrix(2, 3),
    Matrix(3, 6),
    Matrix(6, 4),
    Matrix(4, 5)
]


p = [i.first for i in matrices]
p = p + [matrices[-1].second]
# print(f'p: {p} \n')

# n = len(p)  # number of matrices
M = [[sys.maxsize] * len(p) for i in range(len(matrices) + 1)]
# M = [[8] * len(p) for i in range(len(matrices) + 1)]
# printM(M)

""" 使わないエリアを0に """
for j in range(len(matrices) + 1):
    M[0][j] = 0

for i in range(1, len(matrices) + 1):
    for j in range(i):
        M[i][j] = 0
# printM(M)

""" 左上から右下の対角線を0に"""
for t in range(len(matrices) + 1):
    M[t][t] = 0
# printM(M)

len_mat = len(matrices)
limit_of_proc1 = len_mat
for t in range(1, len_mat):
    for d, i in enumerate(range(1, limit_of_proc1)):
        dd = d + 1
        for ddd, j in enumerate(range(dd, i + t)):
            # print(f'(t:{t}) i:{i} d:{d} dd:{dd} i+t:{i+t} k:{i+ddd}')
            # print(f'M[{dd}][{i+t}] = m[{i}][{i+ddd}] + m[{i+ddd+1}][{i+t}] + p[{d}]*p[{i+ddd}]*p[{i+t}]')
            print(
                f'1st:{M[i][i+ddd]} 2nd:{M[i+ddd+1][i+t]} 3rd:{p[d]*p[i+ddd]*p[i+t]} ')
            result = M[i][i + ddd] + M[i + ddd + 1][i + t] + \
                p[d] * p[i + ddd] * p[i + t]
            if M[dd][i + t] > result:
                M[dd][i + t] = result
    limit_of_proc1 -= 1

printM(M)

"""
p = [5,3,6,2,7]

1<=k<2     i k      k   j
m[1,2] = m[1,k] + m[k+1,2] + p0pkp2
m[1,2] = m[1,1] + m[2,2]  +  p0p1p2

2<=k<3
m[2,3] = m[2,k] + m[k+1,3] + p1pkp3
m[2,3] = m[2,2] + m[3,3] +   p1p2p3

3<=k<4
m[3,4] = m[3,k] + m[k+1,4] + p2pkp4
m[3,4] = m[3,3] + m[4,4] +   p2p3p4

------------------------------------
1<=k<3
m[1,3] = m[1,k] m[k+1,3] + p0pkp3
m[1,3] = m[1,1] m[2,3] +   p0p1p3
         m[1,2] m[3,3] +   p0p2p3
2<=k<4
m[2,4] = m[2,k] + m[k+1,4] + p1pkp4
m[2,4] = m[2,2] + m[3,4] +   p1p2p4
         m[2,3] + m[4,4] +   p1p3p4
------------------------------------
1<=k<4
m[1,4] = m[1,k] + m[k+1,4] + p0pkp4
m[1,4] = m[1,1] + m[2,4] +   p0p1p4
         m[1,2] + m[3,4] +   p0p2p4
         m[1,3] + m[4,4] +   p0p3p4

k   1<=k<2 2<=k<3 3<=k<4
    1<=k<3 2<=k<4
    1<=k<4
i 1,2,3   j 2,3,4
  1,2       3,4
  1         4


"""
