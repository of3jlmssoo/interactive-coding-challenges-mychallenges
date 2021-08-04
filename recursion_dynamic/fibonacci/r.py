"""               0  1  2  3  4  5  6  7   8   9     """
""" Fib sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... """
"""
    fibr(6)

    fib(0) = 0 (固定)
    fib(1) = 1 (固定)
    fib(2) = fib(0) + fib(1) = 1
    fib(3) = fib(1) + fib(2) = 2
    fib(4) = fib(2) + fib(3) = 3
"""
def fibr(n):
    result = 0


    if n>= 2:
        result = _fibr(n-2) + _fibr(n-1)

    return result
    """
    6でコール   _fibr(4) + _fibr(5)

    """
def _fibr(i):
    print(f'_fibr({i})')
    result = 0
    if i ==0 or i==1:
        print(f'{i} will be returned')
        return i
    return  _fibr(i-2) + _fibr(i-1)    

print( fibr(9) )
