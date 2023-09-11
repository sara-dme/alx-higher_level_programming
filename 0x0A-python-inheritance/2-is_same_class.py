#!/usr/bin/python3

"""Define a checking function"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the specified class"""
    return (type(obj) == a_class)
