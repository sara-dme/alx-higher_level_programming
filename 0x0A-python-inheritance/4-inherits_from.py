#!/usr/bin/python3

"""Define achecking function"""


def inherits_from(obj, a_class):
    """check if an instance of a class that inherited from the specified class
    Args:
        obj (any): the object to check
        a_class (object): class
    Return:
        True if it is the case, False otherwise
     """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
