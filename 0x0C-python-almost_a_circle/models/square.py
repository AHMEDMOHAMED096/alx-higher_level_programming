#!/usr/bin/python3
''' Defines a class named Square. '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square model class. '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        The constructor for the Square class.

        Parameters:
            size: The size of Square.
            x: set to 0 by default.
            y: set to 0 by default.
            id: The id of Square.
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        This is a getter method for the size attribute.

        Returns:
            int: The size of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method for the size attribute.

         Parameters:
            value (int): The new size of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    @property
    def size(self):
        """
        This is a getter method for the size attribute.

        Returns:
            int: The size of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method for the size attribute.

         Parameters:
            value (int): The new size of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    @property
    def x(self):
        """
        This is a getter method for the x attribute.

        Returns:
            int: x of Square
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is a setter method for the x attribute.

         Parameters:
            value (int): The new x of the Square.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        This is a getter method for the y attribute.

        Returns:
            int: y of Square
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is a setter method for the y attribute.

         Parameters:
            value (int): The new y of the Square.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This method returns the current Square area(int).
        """
        return self.__size * self.__size

    def display(self):
        '''
        This method prints in stdout the Square instance
        with the character #.
        '''
        print('\n' * self.y, end='')
        for j in range(self.size):
            print(' ' * self.x + '#' * self.size)

    def __str__(self):
        """
        This method returns nicely readable string representation of an object.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__size}")

    def update(self, *args, **kwargs):
        ''' This method assigns an argument to each attribute
        based on args or kwargs '''
        self.id = args[0] if len(args) > 0 else kwargs.get('id', self.id)
        self.size = args[1] if len(args) > 1 \
            else kwargs.get('size', self.size)

        self.size = args[2] if len(args) > 2 \
            else kwargs.get('size', self.size)

        self.x = args[3] if len(args) > 3 else kwargs.get('x', self.x)
        self.y = args[4] if len(args) > 4 else kwargs.get('y', self.y)
