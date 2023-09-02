#!/bin/usr/python3
"""Define a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    Args:
        matrix (list): list of elements can be ints or floats
        div: number to use for the division
    Raises:
        TypeError: if matrix (list of lists) not integers/floats
        TypeError: if rows aren't in same size
        TypeError: if div is not an int or float.
        ZeroDivisionError: if division by 0
    Return:
        A new matrix with result of division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [n for row in matrix for n in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
    if div == 0:
            raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda n: round(n / div, 2), row)) for row in matrix])
