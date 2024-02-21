#!/usr/bin/python3
""" Defines a function that represents the Pascal’s triangle. """


def pascal_triangle(n):
    """ A function that returns the Pascal’s triangle.
    Returns a list of lists of integers. """
    triangle = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        last_element = triangle[-1]
        new_list = [1]
        for j in range(len(last_element) - 1):
            new_list.append(last_element[j] + last_element[j + 1])
        new_list.append(1)
        triangle.append(new_list)
    return triangle
