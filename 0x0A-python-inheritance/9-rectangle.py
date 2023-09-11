#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define the inherits classes"""


class Rectangle(BaseGeometry):
    """ class inherits from subclass"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        return (self.height * self.width)

    def __str__(self):
        return ("[Rectangle] " + str(self.width) + "/" + str(self.height))
