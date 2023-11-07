#!/usr/bin/python3
"""Defines a text file writing function"""


def write_file(filename="", text=""):
    """Writes a string to UTF-8 file"""
    with open(filename, "w", encoding="utf-8") as my_file:
        count = my_file.write(text)
    return count
