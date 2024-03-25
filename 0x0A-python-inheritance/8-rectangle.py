#!/usr/bin/python3
"""
A module that contains the Rectangle class inheriting from BaseGeometry
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
    - `width` and `height` must be private. No getter or setter
    - `width` and `height` must be positive integers, validated by
    `integer_validator`
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializer function that validates the values of width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
