#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry class."""


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry class attributes."""

    def __init__(self, width, height):
        """Intializes a new Rectangle instance.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
