"""               0  1  2  3  4  5  6  7   8   9     """
""" Fib sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... """

def fibi(n):
    if n ==0 or n==1:
        return n
    

    minus_two = 0
    minus_one = 1
    for i in range(2,n+1):
        result = minus_two + minus_one
        minus_two = minus_one
        minus_one = result
    return result


print( '1 ', fibi(1) )
print( '2 ', fibi(2) )
print( '3 ', fibi(3) )
print( '4 ', fibi(4) )
print( '5 ', fibi(5) )
print( '6 ', fibi(6) )
print( '7 ', fibi(7) )
print( '8 ', fibi(8) )
print( '9 ', fibi(9) )
