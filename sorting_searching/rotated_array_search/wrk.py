"""
0 1 2 3 4 5 6 7 8 9

*func(data, val, 0, 9)
  idx = 0 + (9-0)//2 = 4        [0,1,2,3]     [5,6,7,8,9]
*  func(0,3) func(start,idx-1)
*  func(5,9) func(idx+1, end)

func(data,val,0,3)
  idx = 0 + (3-1)//2 = 1        [0] [2,3]
*  func(0,0)   check data[0] & return None
*  func(2,3)

func(data,val,5,9)                            [5,6] [8,9]
  idx = 5 + (9-5)//2 = 7
*  func(5,6)
*  func(8,9)

func(data,val,2,3)
  idx = 2 + (3-2)//2 = 2
*  func(2,1) check[2]=check[sart] and return  None
*  func(3,3) check[3]=check[end] and return None

func(data,val,5,6)
  idx = 5 + (6-5)//2 = 5
*  func(5,4) check[5]=check[start] and return None
*  func(6,6) check[6]=check[end] and return None

func(data,val,8,9)
  idx = 8 + (9-8)//2 = 8
*  func(8,7) check[8]=check[start] and return None
*  func(9,9) check[9]=check[end] and return None

[log]
_search_sorted_array called: data[0:1]=[0] val=1 start=0 end=9 idx=4
_search_sorted_array called: data[0:1]=[0] val=1 start=0 end=3 idx=1
1) retrun idx=1
_search_sorted_array called: data[0:1]=[0] val=1 start=0 end=0 idx=0
4) return None
_search_sorted_array called: data[0:1]=[0] val=1 start=2 end=3 idx=2
_search_sorted_array called: data[0:1]=[0] val=1 start=2 end=1 idx=1
1) retrun idx=1
3) return end=1
_search_sorted_array called: data[0:1]=[0] val=1 start=3 end=3 idx=3
4) return None
_search_sorted_array called: data[0:1]=[0] val=1 start=5 end=9 idx=7
_search_sorted_array called: data[0:1]=[0] val=1 start=5 end=6 idx=5
_search_sorted_array called: data[0:1]=[0] val=1 start=5 end=4 idx=4
4) return None
_search_sorted_array called: data[0:1]=[0] val=1 start=6 end=6 idx=6
4) return None
_search_sorted_array called: data[0:1]=[0] val=1 start=8 end=9 idx=8
_search_sorted_array called: data[0:1]=[0] val=1 start=8 end=7 idx=7
4) return None
_search_sorted_array called: data[0:1]=[0] val=1 start=9 end=9 idx=9
4) return None
None


"""


def _search_sorted_array(data, val, start, end):
    # result = None
    idx = start + (end - start) // 2
    print(
        f'_search_sorted_array called: {data[0:1]=} {val=} {start=} {end=} {idx=} ')
    if data[idx] == val:
        print(f'1) retrun {idx=}')
        # return idx

    if start >= end:
        if data[start] == val:
            print(f'2) return {start=}')
            return start
        if data[end] == val:
            print(f'3) return {end=}')
            return end
        print(f'4) return None ')
        return None

    _search_sorted_array(data, val, start, idx - 1)
    _search_sorted_array(data, val, idx + 1, end)


#        0   1   2  3  4  5  6  7  8  9
data = [10, 12, 14, 1, 3, 5, 6, 7, 8, 9]
val = 1

# data = [1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
# val = 2

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# data=[10, 12, 14, 1, 3, 5, 6, 7, 8, 9]
print(f'data=[ 0   1   2  3  4  5  6  7  8  9]')
print(f'{data=}')
print(_search_sorted_array(data, val, 0, len(data) - 1))
