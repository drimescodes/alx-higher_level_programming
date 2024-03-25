#!/usr/bin/python3
"""
A function to check the instance of an object
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
