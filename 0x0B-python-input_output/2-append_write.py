#!/usr/bin/python3
"""Defines a text file appending function"""


def append_write(filename="", text=""):
    """Appends a string at the end of UTF-8 file

    Parameters:
    filename: The name of file to append to
    text: The string to append to file

    Return: The number of characters added"""

    with open(filename, "a", encoding="utf-8") as my_file:
        count = my_file.write(text)
    return count
