#!/usr/bin/python3
""" Defines a function to check for if object is instance of a class """


def is_same_class(obj, a_class):
    """ A function that checks if the object is exactly an instance
    of the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class.

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if (type(obj) == a_class):
        return True
    return False
