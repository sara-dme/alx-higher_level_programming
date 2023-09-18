#!/usr/bin/python3
"""Unitest for rectangle.py file"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """Define a class to evaluate test cases for rectangle"""

    def test_init(self):
        """check for instance"""
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 3)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_attr(self):
        """check attr"""
        r = Rectangle(10, 60)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 60)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        rr = Rectangle(12, 45)
        self.assertEqual(rr.id, 2)
        self.assertEqual(rr.width, 12)
        self.assertEqual(rr.height, 45)
        self.assertEqual(rr.x, 0)
        self.assertEqual(rr.y, 0)

        r1 = Rectangle(10, 2, 4, 6)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)

        r2 = Rectangle(10, 60, 2, 4, 50)
        self.assertEqual(r2.id, 50)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 60)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 4)

    def test_error(self):
        """check errors"""
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(ValueError):
            rr = Rectangle(10, -20)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "4")
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 4, "5")
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 4, 20, 12, 25, 10)
        with self.assertRaises(TypeError):
            r4 = Rectangle(-10, 4)
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r6 = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r7 = Rectangle(20, 10, -9, 5)
        with self.assertRaises(ValueError):
            r8 = Rectangle(20, 10, 6, -9)

        with self.assertRaises(ValueError):
            r1.x = -9
        with self.assertRaises(ValueError):
            r1.height = -9
        with self.assertRaises(ValueError):
            r1.y = -9
        with self.assertRaises(ValueError):
            r1.width = -9
        with self.assertRaises(TypeError):
            r1.x = "1"
        with self.assertRaises(TypeError):
            r1.y = "1"
        with self.assertRaises(TypeError):
            r1.width = "1"
        with self.assertRaises(TypeError):
            r1.height = "1"
 
        with self.assertRaises(TypeError):
            r1.update(10, 20, "55", 12)   

        with self.assertRaises(TypeError):
            r1.update(id=10, x=20, y="55", width=12, height=20)

        with self.assertRaises(ValueError):
            r1.update(10, 20, -9, 12)

        with self.assertRaises(ValueError):
            r1.update(id=10, x=20, y=-9, width=12, height=23)

        with self.assertRaises(AttributeError):
            r = None
            r.to_dictionary

    def test_area(self):
        """check area method"""
        r = Rectangle(3, 2)
        area = r.area()
        self.assertEqual(area, 6)

        r1 = Rectangle(30, 20, 4, 2, 10)
        area = r1.area()
        self.assertEqual(area, 600)

        r2 = Rectangle(3, 3, 5)
        area = r2.area()
        self.assertEqual(area, 9)

        r3 = Rectangle(3, 5)
        area = Rectangle.area(r3)
        self.assertEqual(area, 15)

    def test_str(self):
        """check str method"""
        r = Rectangle(1, 2, 2, 3, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 2/3 - 1/2")

        r1 = Rectangle(1, 1, 2)
        self.assertEqual(str(r1), "[Rectangle] (15) 2/0 - 1/1")

        r2 = Rectangle(1, 2, 2, 3, 10)
        self.assertEqual(r2.__str__(), "[Rectangle] (10) 2/3 - 1/2")

    def test_update(self):
        """check update method"""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r.update(1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/3 - 4/2")

    def test_dictionary(self):
        """check to_dictionary method"""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 11, 'height': 2, 'width': 10})


        r2 = Rectangle(10, 2)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, {'x': 0, 'y': 0, 'id': 2, 'height': 2, 'width': 10})


        r3 = Rectangle(10, 2)
        r3_dictionary = r3.to_dictionary()
        self.assertEqual(r3_dictionary, {'x': 0, 'y': 0, 'id': 3, 'height': 2, 'width': 10})

        r4 = Rectangle(10, 2, 1, 9, 10)
        r4_dictionary = r4.to_dictionary()
        self.assertEqual(r4_dictionary, {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10})
