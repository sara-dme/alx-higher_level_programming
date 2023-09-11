#!/usr/bin/python3
"""define a rectabgle subclass , child square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class """

    def __init__(self, size):
        """initialize a new square
        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
