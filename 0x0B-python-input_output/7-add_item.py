#!/usr/bin/python3
"""Adds all arguments to Python list, save them to file"""
import sys
import os
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items():
    filename = "add_item.json"
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_items()
