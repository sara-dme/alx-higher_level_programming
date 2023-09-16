#!/usr/bin/python3
"""Base Module"""


class Base:
    """the base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
