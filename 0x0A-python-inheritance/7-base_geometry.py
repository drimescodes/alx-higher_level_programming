#!/usr/bin/python3
"""
A module that contains a class BaseGeometry
- Public instance method: `def area(self):` that raises an `Exception`
with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):`
that validates `value`
    - If `value` is not an integer: raise a `TypeError` exception,
    with the message `<name> must be an integer`
    - If `value` is less or equal to `0`: raise a `ValueError`
    exception with the message `<name> must be greater than 0`
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

    def integer_validator(self, name, value):
        """
        Validates the value
        Args:
            name (str): The name of the value
            value (int): The value to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
