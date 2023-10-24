#!/usr/bin/python3
"""This is a class named Square that defines a square by its size"""


class Square:
    """
    Defines a square

    Attributes:
        size (int): The size of the square. It's a private attribute.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Parameters:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method for the size attribute.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
