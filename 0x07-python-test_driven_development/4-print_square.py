#!/usr/bin/python3

"""Defines a  function that prints a square with the character #"""

def print_square(size):
    """Print a square using # character.
    Args:
        size (int): is the size length of the square.
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
