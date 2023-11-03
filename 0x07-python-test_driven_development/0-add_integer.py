#!/usr/bin/python3
""" Defines addition function"""


def add_integer(a, b=98):
    """
    This function adds two numbers
    If the numbers are floats, they are first cast to integers.
    If the inputs are not integers or floats, a TypeError is raised.

    Parameters:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

    Returns:
    int: The sum of a and b as an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast 'a' and 'b' to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
