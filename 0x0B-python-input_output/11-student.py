#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 11-student.py)
"""


class Student:
    """
    A class Student that defines a student by: (based on 11-student.py)
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
