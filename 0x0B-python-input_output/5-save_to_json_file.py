#!/usr/bin/python3
"""
In this module a single function that writes Object to text file, using JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a
    JSON representation

    Args:
        my_obj (JSON): String to deserialize.
        filename (str) : String with name of file.

    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
