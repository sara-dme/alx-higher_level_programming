#!/usr/bin/python3


class BaseGeometry():

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the integer:
        Args:
            name (string): name
            value (int) : value to validate
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")
