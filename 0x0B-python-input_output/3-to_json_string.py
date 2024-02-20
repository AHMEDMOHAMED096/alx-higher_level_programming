#!/usr/bin/python3

""" imported json module. """
import json
""" Defines a function that returns the JSON representation of an object. """


def to_json_string(my_obj):
    """ A function that returns the JSON representation of an object. """
    return json.dumps(my_obj)
