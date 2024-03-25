#!/usr/bin/python3
"""
A module that defines a class named Rectangle.

- Private instance attributes: `width`:
    - property `def width(self):` to retrieve it.
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a `TypeError`
            exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError`
            exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it.
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError`
            exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError`
            exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`:
    `def __init__(self, width=0, height=0):`
"""


class Rectangle:
    """
    Defines a Rectangle with basic properties of a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width to a value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height to a value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
