#!/usr/bin/python3
"Unittest for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """define a class to evaluate test cases for base"""

    def test_init(self):
        """check for instance"""
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertFalse(type(b) == type(Base))
        self.assertFalse(id(b) == id(Base))
        b1 = Base()
        self.assertTrue(type(b) == type(b1))
        self.assertFalse(id(b) == id(b1))

    def test_attr(self):
        """check attribute"""
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_raise_errors(self):
        """check for errors"""
        with self.assertRaises(NameError):
            b1 = Bases()
        with self.assertRaises(AttributeError):
            b1 = Base()
            b1.to_dictionary()
        with self.assertRaises(AttributeError):
            b =  Base()
            print(b.y)
