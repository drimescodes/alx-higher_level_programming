#!/usr/bin/python3
"""
This module defines a function (`add_integer`) that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    Args:
        a (int): first integer.
        b (int): second integer.
    Returns:
        The addition of the two integers.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
