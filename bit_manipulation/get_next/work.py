#   * Input:         0000 0000 1101 0111
#   * Next largest:  0000 0000 1101 1011
#   * Next smallest: 0000 0000 1100 1111

bin1 = '0000000011010111'
bin2 = '0000000011011011'
bin3 = '0000000011001111'

print(
    int(bin1, base=2),
    int(bin2, base=2),
    int(bin3, base=2),
)
# bin1 = '0000000011010111'
# bin2 = '0000000011011011'
bina =   '0000000011011110'
print(int(bina, base=2))
#
# 一番右の01を見つけて、0と１を入れ替える。
# 1の数は同じでという条件のもとでthe next largest numberを探すというお題なので01は見つかるはず
#
# bin1 = '0000000011010111'
# bin3 = '0000000011001111'
# 10を見つけて入れ替える     
print("=============================")
print( bin1.split('01'))
# bin1 = '0000000 01 1 01 01  11'
#       ['0000000', '1', '', '11']
splitted_01 = bin1.split('01')
print(splitted_01)
splitted_01_len = len(splitted_01)
print(splitted_01_len)
restored = ''
for i in range(splitted_01_len-1):

    append_candidate = ['01','99']
    append_char=append_candidate[(splitted_01_len-2)==i]

    restored = restored + splitted_01[i] + append_char
    # restored = restored + splitted_01[i] + '01' # + splitted_01[i+1]
    print("==> ", i, "===> ",restored)
    print("--> ", i, "---> ",bin1)
restored = restored + splitted_01[splitted_01_len-1]
print(restored)
print(bin1)
    
