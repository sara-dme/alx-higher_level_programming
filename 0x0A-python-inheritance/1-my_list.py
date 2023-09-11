#!/usr/bin/python3
"""Define a class that inherits from list"""


class MyList(list):
    """this is a super class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
