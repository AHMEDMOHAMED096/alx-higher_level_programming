#!/usr/bin/python3
""" The MyList class """


class MyList(list):
    """ A subclass of list """

    def __init__(self):
        """ Is responsible for initializing the attributes of the object """
        super().__init__()

    def print_sorted(self):
        """ Prints the sorted list """
        print(sorted(self))
