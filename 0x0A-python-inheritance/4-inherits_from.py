#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
