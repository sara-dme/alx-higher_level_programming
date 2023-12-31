#!/usr/bin/python3

"""Define the inherits classes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class inherits from subclass"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
