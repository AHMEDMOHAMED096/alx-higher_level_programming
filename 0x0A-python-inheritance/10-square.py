#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle class."""


class Square(Rectangle):
    """A square Class."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This method returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
