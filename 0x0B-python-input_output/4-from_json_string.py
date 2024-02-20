#!/usr/bin/python3

""" imported json module. """
import json
""" Defines a function that returns an object represented by a JSON string. """


def from_json_string(my_str):
    """ A function that returns an object represented by a JSON string.. """
    return json.loads(my_str)
