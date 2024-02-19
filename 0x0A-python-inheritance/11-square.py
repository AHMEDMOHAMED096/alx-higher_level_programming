#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        """
        This method returns nicely readable string representation of an object.
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
