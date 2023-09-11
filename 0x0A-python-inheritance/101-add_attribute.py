#!/usr/bin/python3
"""define afunction that add a new attribute to an object"""


def add_attribute(mc, var, name):
    """t adds a new attribute to an object if it’s possible:"""
    if hasattr(mc, var, name):
        raise TypeError("can't add new attribute")
    setattr(mc, var, name)
