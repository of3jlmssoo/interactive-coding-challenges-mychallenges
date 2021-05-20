import unittest
""" rotation_challenge.ipynbに記載のURLのAlgorithmを参考にする。
元の文字列をずらしているのでs1 in s2+s2でrotationしたかどうかが判明する。

rotation_challenge.ipynbではclass Rotation(object)が定義されており、かつ、
Problem: Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring.の記述があるので
コピーの上利用する。
"""
class Rotation(object):

    def is_substring(self, s1, s2):
        # TODO: Implement me
        # pass
        return (s1 in s2+s2)

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        # Call is_substring only once
        # pass
        if s1 == None or s2 == None:    return False
        if len(s1) != len(s2):          return False
        if len(s1) == 0 and len(s2) == 0:   return True
        if len(s1) == 0 and len(s2) > 0:    return False
        if len(s1) > 0 and len(s2) == 0:    return False
        return (self.is_substring(s1,s2))

class TestRotation(unittest.TestCase):

    def test_rotation(self):
        rotation = Rotation()
        self.assertEqual(rotation.is_rotation('o', 'oo'), False)
        self.assertEqual(rotation.is_rotation(None, 'foo'), False)
        self.assertEqual(rotation.is_rotation('foo', None), False) # added
        self.assertEqual(rotation.is_rotation('', 'foo'), False)
        self.assertEqual(rotation.is_rotation('foo', ''), False) # added
        self.assertEqual(rotation.is_rotation('', ''), True)
        self.assertEqual(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')

    
def main():
    pass
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()