lst=[
    [1,'a',[11,'aa',[111,'aaa',[]]]],
    [2,'b',[]],
    [3,'c',[]],
]
print(f'lst             {lst}')
print(f'lst[0][2]       {lst[0][2]}')
print(f'lst[0][2][2]    {lst[0][2][2]}')
print(f'lst[0][2][2][0] {lst[0][2][2][0]}')
print(f'lst[0][2][2][1] {lst[0][2][2][1]}')
print(f'lst[0][2][2][2] {lst[0][2][2][2]}')

lst_format = [None,None,[]]
lst = [lst_format for l in range(10)]
print(
    len(lst)
)

for i in range(10):
    print(i, i%3)

