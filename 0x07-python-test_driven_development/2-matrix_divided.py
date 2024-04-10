#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divides all elements of matrix
    Args:
    matrix (list): A list of list of integer or float
    div (int/float). the number to divide the element by.
    Returns:
    list: A new matrix with the elements divided by div, rounded to 2dp.
    Raises:
    TypeError: if matrix is not list of lists of integer/floats or if div is not a number
    ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, int):
        raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            return [[round (element / div, 2) for element in row] for row  in matrix]
