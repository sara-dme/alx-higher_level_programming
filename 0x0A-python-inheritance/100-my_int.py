#!/usr/bin/python3
"""class MyInt inherits int"""


class MyInt(int):
    """operator inverted == and !="""

    def __eq__(self, value):
        """Replace == with !="""
        return self.real != value

    def __ne__(self, value):
        """replace != with == """
        return self.real == value
