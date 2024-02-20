#!/usr/bin/python3
""" Defines a function to write a string to a text file. """


def write_file(filename="", text=""):
    """ A function to write a string to a text file. """
    with open(filename, "w") as myfile:
        return myfile.write(text)
