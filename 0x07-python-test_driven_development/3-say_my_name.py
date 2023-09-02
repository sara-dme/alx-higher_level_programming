#!/usr/bin/python3

"""Defines a name"""

def say_my_name(first_name, last_name=""):
    """print a name.
    Args:
        first_name (str): 1er name to print.
        last_name (str): last name to print.
    Raises:
        TypeError: if are not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
