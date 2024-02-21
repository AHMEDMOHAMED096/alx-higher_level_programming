#!/usr/bin/python3
""" Defines a function that returns a list of lists of integers
representing the Pascal’s triangle. """


def pascal_triangle(n):
    """ A function that returns a list of lists of integers
    representing the Pascal’s triangle. """

    triangle = []
    for i in range(n):
        if n <= 0:
            print(triangle)
        if not triangle:
            triangle.append([1])
    last_element = triangle[-1]
    new_list = [1]

    for j in range(len(last_element) - 1):
        new_list.append(last_element[j] + last_element[j + 1])

    new_list.append(1)
    triangle.append(new_list)


return triangle
