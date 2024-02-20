#!/usr/bin/python3
""" Defines a Student class. """


class Student:
    """ Represent a Student class. """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A method that retrieves a dictionary representation
        of a Student instance. """
        return self.__dict__
