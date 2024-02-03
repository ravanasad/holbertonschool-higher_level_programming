#!/usr/bin/python3
def matrix_divided(matrix, div):
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if isinstance(i, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if isinstance(j, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix

