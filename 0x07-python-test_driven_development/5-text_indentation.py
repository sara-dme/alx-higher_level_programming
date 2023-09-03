#!/usr/bin/python3

""" Defines a text indention function"""

def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): theh text to print
    Raises:
        TypeError: if text isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    ln = len(text)

    while i < ln and text[i] == " ":
        i = i + 1

    while i < ln:
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ":.?":
            if text[i] in ":.?":
                print("\n")
            i = i + 1
            while i < ln and text[i] == " ":
                i = i + 1
            continue
        i += 1
