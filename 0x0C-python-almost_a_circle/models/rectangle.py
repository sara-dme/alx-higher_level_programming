#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize value for rectangle object"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter for widht"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """Getter of x var"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter of x"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter of y"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """prints in stdout Rectangle with character #"""
        for i in range(self.y):
            print()
        for i in range(0, self.height):
            print(" " * self.x, end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ string method"""
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for var in order:
                try:
                    setattr(self, var, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for var in order:
                try:
                    setattr(self, var, kwargs[var])
                except KeyError:
                    pass

    def to_dictionary(self):
        """ returns the dictionary
        representation of a Rectangle"""
        order = ['x', 'y', 'id', 'height', 'width']
        attrs = {}
        for val in order:
            attrs[val] = getattr(self, val)
        return attrs
