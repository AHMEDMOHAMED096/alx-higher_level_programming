#!/usr/bin/python3

""" imported sys module
    imported 5-save_to_json_file module
    imported 6-load_from_json_file """
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
""" Write a script that adds all arguments to a Python list
and then save them to a file. """


try:
    items = load_from_json_file('add_item.json')
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, 'add_item.json')
