#!/usr/bin/python3
"""Defines a text file appending function"""


def append_write(filename="", text=""):
    """Appends a string at the end of UTF-8 file"""
    with open(filename, "a", encoding="utf-8") as my_file:
        count = my_file.append(text)
    return count
