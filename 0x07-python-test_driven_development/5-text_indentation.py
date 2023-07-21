#!/usr/bin/python3
"""This module consists of a single function that prints a texts with
new lines when a special character is encountered.

In this module a function called text_indentation() is specified and its
functionality consists of printing a text and adding two new lines each time
a ? . or : is found.

Example:
    An example in which the function is implemented is the following.

    text_indentation("Hello. World")
    Hello

    World

"""


def text_indentation(text):
    """ prints a text with 2 new lines after the characters: ., ? and :
    Args:
        text (str): text to divide.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("{}\n\n".format(text[i]), end="")
            i += 1
            while text[i] == " ":
                i += 1
                continue
            continue
        print(text[i], end="")
        i += 1
