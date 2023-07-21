#!/usr/bin/python3
"""This module consists of a single function that prints an introduction.

In this module a function called say_my_name is specified and its
functionality consists of saying an specified name and lastname passed
by parameters.

Example:
    An example in which the function is implemented is the following.

    say_my_name("Walter", "White")
    Walter White


"""


def say_my_name(first_name, last_name=""):
    """ Prints a the name in a sentence.
    Args:
        first_name (str): first name to print.
        last_name (str): last name to print.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
