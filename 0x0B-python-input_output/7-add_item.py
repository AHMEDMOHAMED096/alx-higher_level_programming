#!/usr/bin/python3
"""Adds all arguments to Python list, save them to file"""
import sys
import json
from os.path import isfile
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if isfile('add_item.json'):

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
