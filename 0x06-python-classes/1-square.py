#!/usr/bin/python3
"""
Writing a Square class that defines a square by: (based on `0-square.py`)
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verifiction)
- You are not allowed to import any module
"""


class Square:
    """A Square Class :)"""

    def __init__(self, size):
        """Instantiate the square size"""
        self.__size = size
