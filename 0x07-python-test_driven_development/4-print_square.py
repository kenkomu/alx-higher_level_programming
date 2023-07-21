#!/usr/bin/python3
"""This module consists of a single function that prints a square with #.

In this module a function called print_square is specified and its
functionality consists of printing a square with # of a size specified
in the parameters.

Example:
    An example in which the function is implemented is the following.

    print_square(2)
    ##
    ##


"""


def print_square(size):
    """ Prints a square with '#'.
    Args:
        size (int): length of the square.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
