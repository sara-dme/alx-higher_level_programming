#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        newMatrix = newMatrix + [list(map(lambda x: x ** 2, row))]
    return newMatrix
