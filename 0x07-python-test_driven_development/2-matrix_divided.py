#!/usr/bin/python3
"""This module consists of a single function that divides a matrix's values.

In this module a function called matrix_divided is specified and its
functionality consists of dividing each value of the matrix by a value
specified in parameters.

Example:
    An example in which the function is implemented is the following.

    matrix_divided([[2, 4], [6, 12]], 2)
    [[1, 2], [3, 6]]


"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix.
    Args:
        matrix (list): matrix that is going to divide each value.
        div (int/float): number that is going to divide the matrix.
    """
    try:
        if type(matrix) != list or type(matrix[0]) != list:
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)
    except TypeError:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    new = []
    if n_columns == 0:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        inside = []
        if len(i) != n_columns:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(msg1)
            inside.append(round(j / div, 2))
        new.append(inside)
    return new
