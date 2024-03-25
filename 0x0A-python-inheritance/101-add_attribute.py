#!/usr/bin/python3
"""
A function that adds a new attribute to an object if it's possible
- If it's not possible, raise a `TypeError` exception with the message
`can't add new attribute` if the object can't have new attribute
- You are not allowed to use `try/catch`
- You are not allowed to import any module
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
