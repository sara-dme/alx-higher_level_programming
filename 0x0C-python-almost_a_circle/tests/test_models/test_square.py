#!/usr/bin/python3
"""Unittest for square.py file
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class Test_Square(unittest.TestCase):
    """define a class to evaluate test cases"""

    def test_init(self):
        """check for instance"""
        s = Square(1)
        self.assertIsInstance(s, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(id(Square) != id(Base))
        self.assertTrue(type(Square) == type(Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(id(Square) != id(Rectangle))
        self.assertTrue(type(Rectangle) == type(Square))
        s2 = Square(2)
        self.assertTrue(type(s) == type(s2))
        self.assertFalse(id(s) == id(s2))

    def test_attr(self):
        """check attribute"""
        s1 = Square(10)
        self.assertEqual(s1.id, 4)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(20)
        self.assertEqual(s2.id, 5)
        self.assertEqual(s2.size, 20)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0) 
        
        s3 = Square(10, 20)
        self.assertEqual(s3.id, 6)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 20)
        self.assertEqual(s3.y, 0)    
        
        s4 = Square(10, 2, 4, 50)
        self.assertEqual(s4.id, 50)
        self.assertEqual(s4.size, 10)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 4)
        
        s5 = Square(10, 2, 6)
        self.assertEqual(s5.id, 7)
        self.assertEqual(s5.size, 10)
        self.assertEqual(s5.x, 2)
        self.assertEqual(s5.y, 6) 
 
        s6 = Square(10, 2, 4, 55)
        s6.id = 55
        self.assertEqual(s6.id, 55)
        s6.size = 100
        self.assertEqual(s6.size, 100)
        s6.x = 20
        self.assertEqual(s6.x, 20)
        s6.y = 50
        self.assertEqual(s6.y, 50)

    def test_error(self):
        """check errors"""
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(AttributeError):
            r1 = Square(10, 80)
            r1.to_json()
        with self.assertRaises(ValueError):
            rr = Square(10, -20)
        with self.assertRaises(TypeError):
            r1 = Square(10, "4")
        with self.assertRaises(TypeError):
            r2 = Square(10, 4, "5")
        with self.assertRaises(TypeError):
            r3 = Square(10, 4, 20, 12, 25, 10)
        with self.assertRaises(ValueError):
            r4 = Square(-10, 4)
        with self.assertRaises(ValueError):
            r5 = Square(0, 10)
        with self.assertRaises(ValueError):
            r6 = Square(10, -1)
        with self.assertRaises(ValueError):
            r7 = Square(20, 10, -9, 5)

        with self.assertRaises(ValueError):
            r1.x = -9
        with self.assertRaises(ValueError):
            r1.size = -9
        with self.assertRaises(ValueError):
            r1.y = -9
        with self.assertRaises(TypeError):
            r1.x = "1"
        with self.assertRaises(TypeError):
            r1.y = "1"
        with self.assertRaises(TypeError):
            r1.size= "1"
 
        with self.assertRaises(TypeError):
            r1.update(10, 20, "55", 12)   

        with self.assertRaises(TypeError):
            r1.update(id=10, x=20, y="55", size=12)

        with self.assertRaises(ValueError):
            r1.update(10, 20, -9, 12)

        with self.assertRaises(ValueError):
            r1.update(id=10, x=20, y=-9, size=45)

        with self.assertRaises(AttributeError):
            r = None
            r.to_dictionary
    
    def test_area(self):
        """check area method"""
        r = Square(3, 2)
        area = r.area()
        self.assertEqual(area, 9)

        r1 = Square(2, 4, 2, 10)
        area = r1.area()
        self.assertEqual(area, 4)

        r2 = Square(3, 3, 5)
        area = r2.area()
        self.assertEqual(area, 9)

        r3 = Square(5)
        area = Square.area(r3)
        self.assertEqual(area, 25)

    def test_str(self):
        """check str method"""
        r = Square(2, 2, 3, 10)
        self.assertEqual(str(r), "[Square] (10) 2/3 - 2")

        r1 = Square(5, 5, 1)
        self.assertEqual(str(r1), "[Square] (14) 5/1 - 5")

        r2 = Square(2, 2)
        self.assertEqual(r2.__str__(), "[Square] (15) 2/0 - 2")

    def test_update(self):
        """check update method"""
        r = Square(5)
        self.assertEqual(r.__str__(), "[Square] (16) 0/0 - 5")

        r.update(10)
        self.assertEqual(r.__str__(), "[Square] (10) 0/0 - 5")
        r.update(1, 2)
        self.assertEqual(r.__str__(), "[Square] (1) 0/0 - 2")
        r.update(x=12)
        self.assertEqual(r.__str__(), "[Square] (1) 12/0 - 2")
        r.update(x=1, y=3, size=11)
        self.assertEqual(r.__str__(), "[Square] (1) 1/3 - 11")
        r.update(10, 10, 10, 10, x=1, size=2, y=3, id=44)
        self.assertEqual(r.__str__(), "[Square] (10) 10/10 - 10")

    def test_dictionary(self):
        """check to_dictionary method"""

        r1 = Square(10, 2, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 2, 'y': 1, 'id': 8, 'size': 10})

        r2 = Square(1, 1)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, {'x': 1, 'y': 0, 'id': 9, 'size': 1})

        r3 = Square(10, 0, 2)
        r3_dictionary = r3.to_dictionary()
        self.assertEqual(r3_dictionary, {'x': 0, 'y': 2, 'id': 10, 'size': 10})

        r4 = Square(10, 2, 5, 6)
        r4_dictionary = r4.to_dictionary()
        self.assertEqual(r4_dictionary, {'x': 2, 'y': 5, 'id': 6, 'size': 10})
