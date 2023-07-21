#!/usr/bin/python3
"""
In this module a single function that creates Object from JSON file
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”.

    Args:
        filename (str) : String with name of file.

    """
    with open(filename, encoding="utf-8") as j_file:
        return json.load(j_file)
