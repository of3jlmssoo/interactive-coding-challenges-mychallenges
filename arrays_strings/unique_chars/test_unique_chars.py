import unittest

class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self, func):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')

class Dummy(object):
    def dummy(self, string):
        if  string == None or 'foo' == None:
            return False
        elif string == '' or string == 'bar':
            return True
        else:
            return 0

class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self, func):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass

# from typing import TypeVar, Union

# T = TypeVar('T', True, False)

class UniqueCharsSet():
    
    # def __init__(self) -> None:    # except NameError:
    #     pass
    
    def has_unique_chars(self, string: str) -> bool:
        if string == None: return False
        return len(string) == len(set(string))


class UniqueChars():

    # def __init__(self) -> None:
    #     pass
    
    def has_unique_chars(self, string: str) -> bool:
        self.__word = []
        if string == None: return False
        for char in string:
            if char in self.__word:
                return False
            else:
                self.__word += char
        return True


class UniqueCharsInPlace():
    
    # def __init__(self) -> None:
    #     pass
        

    def has_unique_chars(self, string: str) -> bool:
        if string == None: return False
        for c in string:
            if string.count(c) > 1:
                return False
        return True


if __name__ == '__main__':
    main()
    # wordchecker = UniqueChars()
    # wordchecker = UniqueCharsSet()
    wordchecker = UniqueCharsInPlace()
    print( wordchecker.has_unique_chars(''), set(''))           # true
    print( wordchecker.has_unique_chars('bar'), set('bar') )    # true
    print( wordchecker.has_unique_chars('foo'), set('foo') )    # false
    print( wordchecker.has_unique_chars('barB'), set('barB') )  # true
    print( wordchecker.has_unique_chars(None))                  # false

