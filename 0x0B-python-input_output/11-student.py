#!/usr/bin/python3
"""class Student that defines a student"""


class Student():
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize a new student
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.__dict__.update(json)
