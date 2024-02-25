#!/usr/bin/python3
''' Defines a Base class. '''


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        ''' The instance constructor.
        Parameters:
            id: initialized with None
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
