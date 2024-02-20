#!/usr/bin/python3
""" Defines a function to append a string to a text file. """


def append_write(filename="", text=""):
    """ A function to append a string to a text file. """
    with open(filename, "a") as myfile:
        return myfile.write(text)
