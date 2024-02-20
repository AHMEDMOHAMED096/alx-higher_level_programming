#!/usr/bin/python3
""" Defines a function that returns a list of lists of integers
representing the Pascal’s triangle. """


def pascal_triangle(n):
    """ A function that returns a list of lists of integers
    representing the Pascal’s triangle. """

    mylist = []

    if n <= 0:
        return mylist
    return mylist.append([n])
