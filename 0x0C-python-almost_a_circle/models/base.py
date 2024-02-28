#!/usr/bin/python3
''' Imported json module. '''
import json


class Base:
    ''' Base model class. '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' The constructor of Base class. '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        ''' This method writes the JSON string representation of list_objs
        to a file. '''
        json_data = []
        with open(f"{cls.__name__}.json", "w") as file:
            if not list_objs:
                file.write(json_data)
            else:
                json_data = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(json_data))

    @classmethod
    def create(cls, **dictionary):
        ''' This method  returns an instance with all
        attributes already set. '''
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        ''' This method returns a list of instances. '''
        with open(f"{cls.__name__}.json") as file:
            if not file:
                return []
            data = json.load(file)
            lst = [cls.create(**item) for item in data]
            return lst

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' This method returns the JSON string representation
        of list_dictionaries. '''
        if not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' This method returns the list of the JSON string
        representation json_string. '''
        if not json_string:
            return []
        return json.loads(json_string)

    def update(self, *args, **kwargs):
        ''' This method assigns an argument to each attribute
        based on args or kwargs '''
        for key, value in kwargs.items():
            setattr(self, key, value)
