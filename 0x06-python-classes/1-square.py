#!/usr/bin/python3
"""This is a class named Square that defines a square by its size"""


class Square:
    """
    Defines a square

    Attributes:
        size (int): The size of the square. It's a private attribute.
    """

    def __init__(self, size):
        """
        The constructor for the Square class.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
