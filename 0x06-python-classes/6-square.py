#!/usr/bin/python3
"""This is a class named Square that defines a square
by its size and position"""


class Square:
    """
    Defines a square

    Attributes:
        size (int): The size of the square. It's a private attribute.
        position (tuple): The position of the square. It's a private attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Parameters:
            size (int, optional): The size of the square.
            Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position
            is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        This is a getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is a setter method for the position attribute.

        Parameters:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        This method returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints in stdout the square with the character #.

        If size is equal to 0, it prints an empty line.
        Position should be used by using space.
        Don’t fill lines by spaces when position[1] > 0
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size)
