def find_diff_xor(str1, str2):
    result = 0
    for char in str1:
        result ^= ord(char)
        print(f"=== str1 === char:{char}, ord(char):{ord(char)}, result:{result}, bin(ord(char):{bin(ord(char))},  bin(result):{bin(result)}")

    print(f"=== between str1 and str2 === result:{result}, bin(result):{bin(result)}")
    
    for char in str2:
        result ^= ord(char)
        print(f"=== str2 === char:{char}, ord(char):{ord(char)}, result:{result}, bin(ord(char):{bin(ord(char))},  bin(result):{bin(result)}")

    print(f"=== before return === result:{result}, chr(result):{chr(result)}")
    return chr(result)


print(find_diff_xor('ab', 'aab'))
print( "=============================" )
print(find_diff_xor('aab', 'ab'))
print( "=============================" )
print(find_diff_xor('abcd', 'abcde'))
print( "=============================" )
print(find_diff_xor('aaabbcdd', 'abdbacade'))
