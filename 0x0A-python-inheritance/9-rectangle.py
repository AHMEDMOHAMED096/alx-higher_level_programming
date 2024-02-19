#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry class attributes."""

    def __init__(self, width, height):
        """The constructor for the rectangle class.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        This method returns nicely readable string representation of an object.
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
