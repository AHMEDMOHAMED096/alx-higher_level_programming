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

    number_of_instances = 0
    print_symbol = None

    def __init__(self, width=0, height=0):
        """
        The constructor for the rectangle class.

        Parameters:
            width (int, optional): The width of rectangle. Defaults to 0.
            height (int, optional): The height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        This method returns nicely readable string representation of an object.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return '\n'.join([Rectangle.print_symbol * self.__width] * self.__height)

    def __repr__(self):
        """
        This method returns a printable representation of an object.
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        This is a destructor method
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
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

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This method returns the current rectangle area(int).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method returns the current rectangle perimeter(int).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
