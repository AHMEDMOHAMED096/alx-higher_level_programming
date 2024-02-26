#!/usr/bin/python3
''' Defines a class named Rectangle. '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle model class. '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        The constructor for the Rectangle class.

        Parameters:
            width: The width of Rectangle.
            height: The height of Rectangle.
            x: set to 0 by default.
            y: set to 0 by default.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            value (int): The new width of the Rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equals 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        This is a getter method for the height attribute.

        Returns:
            int: The height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is a setter method for the height attribute.

         Parameters:
            value (int): The new height of the Rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equals 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        This is a getter method for the x attribute.

        Returns:
            int: x of Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is a setter method for the x attribute.

         Parameters:
            value (int): The new x of the Rectangle.

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
            int: y of Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is a setter method for the y attribute.

         Parameters:
            value (int): The new y of the Rectangle.

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
        This method returns the current Rectangle area(int).
        """
        return self.__width * self.__height

    def display(self):
        '''
        This method prints in stdout the Rectangle instance
        with the character #.
        '''
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """
        This method returns nicely readable string representation of an object.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}")
    
    def update(self, *args):
        ''' This method assigns an argument to each attribute. '''
        self.id = args[0] if len(args) > 0 else kwargs.get('id', self.id)
        self.width = args[1] if len(args) > 1 else kwargs.get('width', self.width)
        self.height = args[2] if len(args) > 2 else kwargs.get('height', self.height)
        self.x = args[3] if len(args) > 3 else kwargs.get('x', self.x)
        self.y = args[4] if len(args) > 4 else kwargs.get('y', self.y)
