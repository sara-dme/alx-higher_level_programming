#!/usr/bin/python3
""" defines a class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define the inherits classes"""


class Rectangle(BaseGeometry):
    """ class inherits from subclass"""

    def __init__(self, width, height):
        """initialize a new rectangle"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return (self.__height * self.__width)

    def __str__(self):
        """return the print() and str()"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
