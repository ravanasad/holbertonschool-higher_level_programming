#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    if isinstance(matrix, list) is False:
        raise TypeError(err1)
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if isinstance(i, list) is False:
            raise TypeError(err1)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if isinstance(j, (int, float)) is False:
                raise TypeError(err1)
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
