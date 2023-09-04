#!/usr/bin/python3
"""class tha defines a regtangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of an rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of an rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))
