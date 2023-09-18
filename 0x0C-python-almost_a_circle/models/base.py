#!/usr/bin/python3
"""Base Module"""
import json
import csv


class Base:
    """the base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method that returns the JSON string"""
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dict.append(dictionary)
            json_str = Base.to_json_string(list_dict)
        with open(filename, 'w') as fl:
            if list_objs is None:
                fl.write("[]")
            else:
                fl.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of the JSON string representation"""
        if json_string is None or bool(json_string) is False:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        list_instance = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                list_dict = cls.from_json_string(json_string)
                for val in list_dict:
                    inst = cls.create(**val)
                    list_instance.append(inst)
        except FileNotFoundError:
            return list_instance
        return list_instance


