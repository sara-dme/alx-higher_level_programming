#!/usr/bin/python3
"""Defines an addition function of two integer."""

def add_integer(a, b=98):
    """Return a + b.
    Args:
        a: argument 1
        b: argument 2
    Return:
        sum of the 2 arguments
    Raises:
        TypeError: if a or b not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
