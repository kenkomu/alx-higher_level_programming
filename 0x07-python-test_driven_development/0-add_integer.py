#!/usr/bin/python3
"""This module consists of a single function that adds.

In this module a function called add_integers is specified and its
functionality consists of adding two values passed by parameter.

Example:
    An example in which the function needs to be implemented is the following.

    add_integers(3, 4)
    7

    add_integers(3, -3)
    0

"""


def add_integer(a, b=98):
    """ Returns the addition of two parameters.
    Args:
        a (int): integer that represents the first number to add.
        b (int): integer that represents the second number to add.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    try:
        sum = int(a) + int(b)
        return sum
    except OverflowError:
        raise OverflowError("cannot convert float infinity to integer")
