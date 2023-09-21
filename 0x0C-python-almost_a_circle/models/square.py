#!/usr/bin/python3
"""Module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif (val < 0):
            raise ValueError("width must be > 0")
        self.width = val

    def update(self, *args, **kwargs):
        """Method that  assigns attributes:"""
        order = ['id', 'size', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for val in order:
                try:
                    setattr(self, val, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for val in order:
                try:
                    setattr(self, val, kwargs[val])
                except KeyError:
                    pass

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        order = ['id', 'x', 'size', 'y']
        attrs = {}
        for val in order:
            attrs[val] = getattr(self, val)
        return attrs
