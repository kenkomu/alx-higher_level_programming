#!/usr/bin/python3
""" This module creates a class with two methods, one to validate
and the other to find an area.
"""


class BaseGeometry:
    """ Class that represents the base geometry. """

    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
