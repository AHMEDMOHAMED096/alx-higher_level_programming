#!/usr/bin/python3
""" Defines a function that returns the JSON representation of an object. """


def to_json_string(my_obj):
    """ A function that returns the JSON representation of an object. """
    return str(json.dumps(my_obj))
