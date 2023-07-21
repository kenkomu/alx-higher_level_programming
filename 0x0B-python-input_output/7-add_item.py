#!/usr/bin/python3
"""
In this module a single function that adds
arguments Python list, and saves it to a file
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    object = load_from_json_file('add_item.json')
except:
    object = []

if len(sys.argv) > 1:
    object.extend(sys.argv[1:])

save_to_json_file(object, 'add_item.json')
