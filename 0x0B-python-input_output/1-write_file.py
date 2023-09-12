#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """returns the number of characters written
    Args:
        filename (str): the name of the file
        text (str): the text to write to the file
    Return:
        the num of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
