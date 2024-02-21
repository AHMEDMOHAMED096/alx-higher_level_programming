#!/usr/bin/python3
""" Defines a function for reading a file. """


def read_file(filename=""):
    """ A function to read a text file. """

    with open(filename) as myfile:
        print(myfile.read())
