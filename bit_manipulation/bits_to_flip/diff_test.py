str1 = '11101'
str2 = '01111'
for c1, c2 in zip(str1,str2):
    print(c1,c2)

lst = [(c1, c2) for c1, c2 in zip(str1,str2) if c1 != c2]
print(len(lst), lst)

# from difflib import ndiff 
# diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True), 
#              'ore\ntree\nemu\n'.splitlines(keepends=True))
# print(''.join(diff))
# # print(''.join(diff), end="")             

# diff = ndiff('11101'.splitlines(keepends=True), 
#              '01111'.splitlines(keepends=True))
# print(''.join(diff))
