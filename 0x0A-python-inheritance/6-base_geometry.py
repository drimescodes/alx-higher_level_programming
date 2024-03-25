#!/usr/bin/python3
"""
A module that contains a class BaseGeometry
- Public instance method: `def area(self):` that raises an `Exception`
with the message `area() is not implemented`
"""


class BaseGeometry:
    """
    A class BaseGeometry
    """

    def area(self):
        """
        Calculates the area of a geometric shape
        """
        raise Exception("area() is not implemented")
