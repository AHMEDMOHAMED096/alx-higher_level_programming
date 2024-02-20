#!/usr/bin/python3

""" imported json module. """
import json
""" Defines a function that writes an Object to a text file,
using a JSON representation. """


def save_to_json_file(my_obj, filename):
    """ A function that writes an Object to a text file,
    using a JSON representation. """

    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
