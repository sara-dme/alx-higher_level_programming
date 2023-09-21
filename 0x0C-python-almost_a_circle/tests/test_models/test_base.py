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
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)

    def test_id_value(self):
        """checks when id has an integer value"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1.id = 4
        self.assertEqual(b1.id, 4)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)
        b2 = Base(0)
        self.assertEqual(b2.id, 0)
        b1.__init__(30)
        self.assertEqual(b1.id, 30)

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

    def test_json_string(self):
        """check for json string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = (r1.to_dictionary())
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 1], ["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))
