#!/usr/bin/python3
""" Module of a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: the matrix, a list of lists of int or floats
        div: the divisor, as an int or a float

    Return: a new matrix that contains the results of all the divisions
    """
    new_matrix = matrix[:]
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    error3 = "div must be a number"
    error4 = "division by zero"

    if not isinstance(matrix, list):
        raise TypeError(error1)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error1)
        if len(row) != len(matrix[0]):
            raise TypeError(error2)
        for e in row:
            if not isinstance(e, int) and not isinstance(e, float):
                raise TypeError(error1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(error3)
    if div == 0:
        raise ZeroDivisionError(error4)

    i = 0
    for row in matrix:
        j = 0
        new_row = row[:]
        for e in row:
            new_row[j] = round((e / div), 2)
            j += 1
        new_matrix[i] = new_row
        i += 1

    return new_matrix
