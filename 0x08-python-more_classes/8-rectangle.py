#!/usr/bin/python3
"""class tha defines a regtangle"""


class Rectangle:
    """represent a rectangle.

    attribute:
        number_of_instances (int): the number of rectangle instance
        print_symbol (any): the symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle
        Args:
            rect_1 (Rectagle): the 1st rectangle
            rect_2 (Rectangle): the 2nd rectangle
        Raise:
            TypeError: if rect_1 or rect_2 not rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """return the printable of an rectangle using  character"""
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle = ""
        for col in range(self.height):
            for row in range(self.width):
                rectangle = rectangle + self.print_symbol
            if col < self.height - 1:
                rectangle = rectangle + "\n"
        return (rectangle)

    def __repr__(self):
        """return the string of a rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle = rectangle + ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """print message in deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
