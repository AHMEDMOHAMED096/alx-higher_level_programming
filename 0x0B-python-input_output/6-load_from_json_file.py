#!/usr/bin/python3

""" imported json module. """
import json
""" Defines a function that creates an Object from a “JSON file”. """


def load_from_json_file(filename):
    """ A function that creates an Object from a “JSON file”. """

    with open(filename) as myfile:
        return json.load(myfile)
