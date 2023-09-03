#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define Test unittest for max_integer()"""

    def test_list(self):
        """test a ordered list of integers"""
        lst = [1, 2, 3, 5]
        self.assertEqual(max_integer(lst), 5)

    def test_list_1(self):
        """ test unordred list of integers"""
        lst = [1, 3, 4, 2]
        self.assertEqual(max_integer(lst), 4)

    def test_lst_2(self):
        """test max in beginning"""
        lst = [10, 2, 5, 5, 6]
        self.assertEqual(max_integer(lst), 10)

    def test_lst_3(self):
        """test a list with a single element"""
        lst = [5]
        self.assertEqual(max_integer(lst), 5)

    def test_lst_4(self):
        """test an empty list"""
        lst = []
        self.assertEqual(max_integer(lst), None)

    def test_lst_5(self):
        """test a string"""
        lst = "Hello"
        self.assertEqual(max_integer(lst), 'o')

    def test_lst_6(self):
        """test list of float"""
        lst = [1.1, 1.2, 1.3, 1.4, -9]
        self.assertEqual(max_integer(lst), 1.4)

    def test_lst_7(self):
        """test list of string"""
        lst = ["ali", "badr", "reda", "sara"]
        self.assertEqual(max_integer(lst), "sara")

    def test_lst_8(self):
        """test an empty string"""
        self.assertEqual(max_integer(""), None)

    if __name__ == '__main__':
        unittest.main()
