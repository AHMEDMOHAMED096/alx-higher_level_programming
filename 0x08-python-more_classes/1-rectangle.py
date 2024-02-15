#!/usr/bin/python3
"""
This is an class named rectangle that defines
a rectangle by its width and height
"""


class Rectangle:
    """ Defines a rectangle
     Attributes:
        width (int): The width of rectangle. It's a private attribute.
        height (int): The height of rectangle. It's a private attribute.
    """

    def __init__(self, width=0, height=0):
        """
        The constructor for the rectangle class.

        Parameters:
            width (int, optional): The width of rectangle. Defaults to 0.
            height (int, optional): The height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This is a getter method for the width attribute.

        Returns:
            int: The width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is a setter method for the width attribute.

         Parameters:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This is a getter method for the height attribute.

        Returns:
            int: The height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is a setter method for the height attribute.

         Parameters:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
