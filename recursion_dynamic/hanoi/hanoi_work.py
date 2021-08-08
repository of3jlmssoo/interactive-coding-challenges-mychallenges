"""
FUNCTION MoveTower(disk, source, dest, spare):
IF disk == 0, THEN:
  move disk from source to dest
ELSE:
  MoveTower(disk - 1, source, spare, dest)   // Step 1 above
  move disk from source to dest              // Step 2 above
  MoveTower(disk - 1, spare, dest, source)   // Step 3 above
END IF



"""


"""
[4, 3, 2, 1, 0]
called from  0  n: 4 A B C                  [4, 3, 2, 1, 0] [] []
called from  1      n: 3 A C B              [4, 3, 2, 1, 0] [] []
called from  1          n: 2 A B C          [4, 3, 2, 1, 0] [] []
called from  1              n: 1 A C B      [4, 3, 2, 1, 0] [] []
called from  1                  n: 0 A B C  [4, 3, 2, 1, 0] [] []
                                    1-1) A  [4, 3, 2, 1, 0] B [] C []   ############## called from  1  n: 0
                                    1-2) A  [4, 3, 2, 1] B [0] C []     ############## called from  1  n: 0
                                    2-1) A  [4, 3, 2, 1] B [0] C []     ############## called from  1  n: 1
                                    2-2) A  [4, 3, 2] B [0] C [1]       ############## called from  1  n: 1
called from  2                  n: 0 B C A  [0] [1] [4, 3, 2]
                                    1-1) A  [4, 3, 2] B [0] C [1]       ############## called from  2  n: 0
                                    1-2) A  [4, 3, 2] B [] C [1, 0]     ############## called from  2  n: 0
                                    2-1) A  [4, 3, 2] B [] C [1, 0]     ############## called from  1  n: 2
                                    2-2) A  [4, 3] B [2] C [1, 0]       ############## called from  1  n: 2
called from  2              n: 1 C B A      [1, 0] [2] [4, 3]
called from  1                  n: 0 C A B  [1, 0] [4, 3] [2]
                                    1-1) A  [4, 3] B [2] C [1, 0]       ############## called from  1  n: 0
                                    1-2) A  [4, 3, 0] B [2] C [1]       ############## called from  1  n: 0
                                    2-1) A  [4, 3, 0] B [2] C [1]       ############## called from  2  n: 1
                                    2-2) A  [4, 3, 0] B [2, 1] C []     ############## called from  2  n: 1
called from  2                  n: 0 A B C  [4, 3, 0] [2, 1] []
                                    1-1) A  [4, 3, 0] B [2, 1] C []     ############## called from  2  n: 0
                                    1-2) A  [4, 3] B [2, 1, 0] C []     ############## called from  2  n: 0
                                    2-1) A  [4, 3] B [2, 1, 0] C []     ############## called from  1  n: 3
                                    2-2) A  [4] B [2, 1, 0] C [3]       ############## called from  1  n: 3
called from  2          n: 2 B C A          [2, 1, 0] [3] [4]
called from  1              n: 1 B A C      [2, 1, 0] [4] [3]
called from  1                  n: 0 B C A  [2, 1, 0] [3] [4]
                                    1-1) A  [4] B [2, 1, 0] C [3]       ############## called from  1  n: 0
                                    1-2) A  [4] B [2, 1] C [3, 0]       ############## called from  1  n: 0
                                    2-1) A  [4] B [2, 1] C [3, 0]       ############## called from  1  n: 1
                                    2-2) A  [4, 1] B [2] C [3, 0]       ############## called from  1  n: 1
called from  2                  n: 0 C A B  [3, 0] [4, 1] [2]
                                    1-1) A  [4, 1] B [2] C [3, 0]       ############## called from  2  n: 0
                                    1-2) A  [4, 1, 0] B [2] C [3]       ############## called from  2  n: 0
                                    2-1) A  [4, 1, 0] B [2] C [3]       ############## called from  2  n: 2
                                    2-2) A  [4, 1, 0] B [] C [3, 2]     ############## called from  2  n: 2
called from  2              n: 1 A C B      [4, 1, 0] [3, 2] []
called from  1                  n: 0 A B C  [4, 1, 0] [] [3, 2]
                                    1-1) A  [4, 1, 0] B [] C [3, 2]     ############## called from  1  n: 0
                                    1-2) A  [4, 1] B [0] C [3, 2]       ############## called from  1  n: 0
                                    2-1) A  [4, 1] B [0] C [3, 2]       ############## called from  2  n: 1
                                    2-2) A  [4] B [0] C [3, 2, 1]       ############## called from  2  n: 1
called from  2                  n: 0 B C A  [0] [3, 2, 1] [4]
                                    1-1) A  [4] B [0] C [3, 2, 1]       ############## called from  2  n: 0
                                    1-2) A  [4] B [] C [3, 2, 1, 0]     ############## called from  2  n: 0
                                    2-1) A  [4] B [] C [3, 2, 1, 0]     ############## called from  0  n: 4
                                    2-2) A  [] B [4] C [3, 2, 1, 0]     ############## called from  0  n: 4
called from  2      n: 3 C B A              [3, 2, 1, 0] [4] []
called from  1          n: 2 C A B          [3, 2, 1, 0] [] [4]
called from  1              n: 1 C B A      [3, 2, 1, 0] [4] []
called from  1                  n: 0 C A B  [3, 2, 1, 0] [] [4]
                                    1-1) A  [] B [4] C [3, 2, 1, 0]     ############## called from  1  n: 0
                                    1-2) A  [0] B [4] C [3, 2, 1]       ############## called from  1  n: 0
                                    2-1) A  [0] B [4] C [3, 2, 1]       ############## called from  1  n: 1
                                    2-2) A  [0] B [4, 1] C [3, 2]       ############## called from  1  n: 1
called from  2                  n: 0 A B C  [0] [4, 1] [3, 2]
                                    1-1) A  [0] B [4, 1] C [3, 2]       ############## called from  2  n: 0
                                    1-2) A  [] B [4, 1, 0] C [3, 2]     ############## called from  2  n: 0
                                    2-1) A  [] B [4, 1, 0] C [3, 2]     ############## called from  1  n: 2
                                    2-2) A  [2] B [4, 1, 0] C [3]       ############## called from  1  n: 2
called from  2              n: 1 B A C      [4, 1, 0] [2] [3]
called from  1                  n: 0 B C A  [4, 1, 0] [3] [2]
                                    1-1) A  [2] B [4, 1, 0] C [3]       ############## called from  1  n: 0
                                    1-2) A  [2] B [4, 1] C [3, 0]       ############## called from  1  n: 0
                                    2-1) A  [2] B [4, 1] C [3, 0]       ############## called from  2  n: 1
                                    2-2) A  [2, 1] B [4] C [3, 0]       ############## called from  2  n: 1
called from  2                  n: 0 C A B  [3, 0] [2, 1] [4]
                                    1-1) A  [2, 1] B [4] C [3, 0]       ############## called from  2  n: 0
                                    1-2) A  [2, 1, 0] B [4] C [3]       ############## called from  2  n: 0
                                    2-1) A  [2, 1, 0] B [4] C [3]       ############## called from  2  n: 3
                                    2-2) A  [2, 1, 0] B [4, 3] C []     ############## called from  2  n: 3
called from  2          n: 2 A B C          [2, 1, 0] [4, 3] []
called from  1              n: 1 A C B      [2, 1, 0] [] [4, 3]
called from  1                  n: 0 A B C  [2, 1, 0] [4, 3] []
                                    1-1) A  [2, 1, 0] B [4, 3] C []     ############## called from  1  n: 0
                                    1-2) A  [2, 1] B [4, 3, 0] C []     ############## called from  1  n: 0
                                    2-1) A  [2, 1] B [4, 3, 0] C []     ############## called from  1  n: 1
                                    2-2) A  [2] B [4, 3, 0] C [1]       ############## called from  1  n: 1
called from  2                  n: 0 B C A  [4, 3, 0] [1] [2]
                                    1-1) A  [2] B [4, 3, 0] C [1]       ############## called from  2  n: 0
                                    1-2) A  [2] B [4, 3] C [1, 0]       ############## called from  2  n: 0
                                    2-1) A  [2] B [4, 3] C [1, 0]       ############## called from  2  n: 2
                                    2-2) A  [] B [4, 3, 2] C [1, 0]     ############## called from  2  n: 2
called from  2              n: 1 C B A  [1, 0] [4, 3, 2] []
called from  1                  n: 0 C A B  [1, 0] [] [4, 3, 2]
                                    1-1) A  [] B [4, 3, 2] C [1, 0]     ############## called from  1  n: 0
                                        1-2) A  [0] B [4, 3, 2] C [1]       ############## called from  1  n: 0
                                    2-1) A  [0] B [4, 3, 2] C [1]       ############## called from  2  n: 1
                                    2-2) A  [0] B [4, 3, 2, 1] C []     ############## called from  2  n: 1
called from  2                  n: 0 A B C  [0] [4, 3, 2, 1] []
                                    1-1) A  [0] B [4, 3, 2, 1] C []     ############## called from  2  n: 0
                                    1-2) A  [] B [4, 3, 2, 1, 0] C []   ############## called from  2  n: 0

"""
"""
5, 4, 3, 2, 1, 0]
called from  0  n: 5 A B C [5, 4, 3, 2, 1, 0] [] []
called from  1  n: 4 A C B [5, 4, 3, 2, 1, 0] [] []

called from  1  n: 3 A B C [5, 4, 3, 2, 1, 0] [] []
called from  1  n: 2 A C B [5, 4, 3, 2, 1, 0] [] []

called from  1  n: 1 A B C [5, 4, 3, 2, 1, 0] [] []
called from  1  n: 0 A C B [5, 4, 3, 2, 1, 0] [] []

called from  2  n: 0 C B A [0] [1] [5, 4, 3, 2]
called from  2  n: 1 B C A [1, 0] [2] [5, 4, 3]

called from  1  n: 0 B A C [1, 0] [5, 4, 3] [2]
called from  2  n: 0 A C B [5, 4, 3, 0] [2, 1] []

called from  2  n: 2 C B A [2, 1, 0] [3] [5, 4]
called from  1  n: 1 C A B [2, 1, 0] [5, 4] [3]

called from  1  n: 0 C B A [2, 1, 0] [3] [5, 4]
called from  2  n: 0 B A C [3, 0] [5, 4, 1] [2]

called from  2  n: 1 A B C [5, 4, 1, 0] [3, 2] []
called from  1  n: 0 A C B [5, 4, 1, 0] [] [3, 2]

called from  2  n: 0 C B A [0] [3, 2, 1] [5, 4]
called from  2  n: 3 B C A [3, 2, 1, 0] [4] [5]
called from  1  n: 2 B A C [3, 2, 1, 0] [5] [4]
called from  1  n: 1 B C A [3, 2, 1, 0] [4] [5]
called from  1  n: 0 B A C [3, 2, 1, 0] [5] [4]
called from  2  n: 0 A C B [5, 0] [4, 1] [3, 2]
called from  2  n: 1 C A B [4, 1, 0] [5, 2] [3]
called from  1  n: 0 C B A [4, 1, 0] [3] [5, 2]
called from  2  n: 0 B A C [3, 0] [5, 2, 1] [4]
called from  2  n: 2 A C B [5, 2, 1, 0] [4, 3] []
called from  1  n: 1 A B C [5, 2, 1, 0] [] [4, 3]
called from  1  n: 0 A C B [5, 2, 1, 0] [4, 3] []
called from  2  n: 0 C B A [4, 3, 0] [1] [5, 2]
called from  2  n: 1 B C A [1, 0] [4, 3, 2] [5]
called from  1  n: 0 B A C [1, 0] [5] [4, 3, 2]
called from  2  n: 0 A C B [5, 0] [4, 3, 2, 1] []
called from  2  n: 4 C B A [4, 3, 2, 1, 0] [5] []
called from  1  n: 3 C A B [4, 3, 2, 1, 0] [] [5]
called from  1  n: 2 C B A [4, 3, 2, 1, 0] [5] []
called from  1  n: 1 C A B [4, 3, 2, 1, 0] [] [5]
called from  1  n: 0 C B A [4, 3, 2, 1, 0] [5] []
called from  2  n: 0 B A C [5, 0] [1] [4, 3, 2]
called from  2  n: 1 A B C [1, 0] [5, 2] [4, 3]
called from  1  n: 0 A C B [1, 0] [4, 3] [5, 2]
called from  2  n: 0 C B A [4, 3, 0] [5, 2, 1] []
called from  2  n: 2 B A C [5, 2, 1, 0] [3] [4]
called from  1  n: 1 B C A [5, 2, 1, 0] [4] [3]
called from  1  n: 0 B A C [5, 2, 1, 0] [3] [4]
called from  2  n: 0 A C B [3, 0] [4, 1] [5, 2]
called from  2  n: 1 C A B [4, 1, 0] [3, 2] [5]
called from  1  n: 0 C B A [4, 1, 0] [5] [3, 2]
called from  2  n: 0 B A C [5, 0] [3, 2, 1] [4]
called from  2  n: 3 A B C [3, 2, 1, 0] [5, 4] []
called from  1  n: 2 A C B [3, 2, 1, 0] [] [5, 4]
called from  1  n: 1 A B C [3, 2, 1, 0] [5, 4] []
called from  1  n: 0 A C B [3, 2, 1, 0] [] [5, 4]
called from  2  n: 0 C B A [0] [5, 4, 1] [3, 2]
called from  2  n: 1 B C A [5, 4, 1, 0] [2] [3]
called from  1  n: 0 B A C [5, 4, 1, 0] [3] [2]
called from  2  n: 0 A C B [3, 0] [2, 1] [5, 4]
called from  2  n: 2 C B A [2, 1, 0] [5, 4, 3] []
called from  1  n: 1 C A B [2, 1, 0] [] [5, 4, 3]
called from  1  n: 0 C B A [2, 1, 0] [5, 4, 3] []
called from  2  n: 0 B A C [5, 4, 3, 0] [1] [2]
called from  2  n: 1 A B C [1, 0] [5, 4, 3, 2] []
called from  1  n: 0 A C B [1, 0] [] [5, 4, 3, 2]
called from  2  n: 0 C B A [0] [5, 4, 3, 2, 1] []
A: []
B: [5, 4, 3, 2, 1, 0]
C: []



"""

A = [5, 4, 3, 2, 1, 0]
# A = [4, 3, 2, 1]
# A = [3, 2, 1]
A = [1, 2, 3]
A = [0, 1, 2]
A = [0, 1, 2, 3, 4, 5]
B = []
C = []
A = [5, 4, 3, 2, 1, 0]


def move_tower(n, source, target, spare, idx):

    print(
        'called from ', idx, ' n:', n, which_tower(
            id(source)), which_tower(
            id(target)), which_tower(
                id(spare)), source, target, spare)

    if n == 0:
        print(
            '           1-1)', which_tower(
                id(A)), A, which_tower(
                id(B)), B, which_tower(
                id(C)), C, '##############', 'called from ', idx, ' n:', n)

        target.append(source.pop())
        print(
            '           1-2)', which_tower(
                id(A)), A, which_tower(
                id(B)), B, which_tower(
                id(C)), C, '##############', 'called from ', idx, ' n:', n)
    else:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move_tower(n - 1, source, spare, target, 1)
        print(
            '           2-1)', which_tower(
                id(A)), A, which_tower(
                id(B)), B, which_tower(
                id(C)), C, '##############', 'called from ', idx, ' n:', n)

        # Move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        # print(A, B, C, '##############', sep='\n')
        print(
            '           2-2)', which_tower(
                id(A)), A, which_tower(
                id(B)), B, which_tower(
                id(C)), C, '##############', 'called from ', idx, ' n:', n)

        # Move the n - 1 disks that we left on auxiliary onto target
        move_tower(n - 1, spare, target, source, 2)


ida = id(A)
idb = id(B)
idc = id(C)


def which_tower(idx):
    if idx == ida:
        return "A"
    elif idx == idb:
        return 'B'
    elif idx == idc:
        return 'C'


print(A)
move_tower(A[0], A, B, C, 0)
print('A:', A)
print('B:', B)
print('C:', C)
