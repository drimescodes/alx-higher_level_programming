#!/usr/bin/python3
"""
A module that defines the Rectangle class that inherits from BaseGeometry
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
    - `width` and `height` must be private. No getter or setter
    - `width` and `height` must be positive integers, validated by
    `integer_validator`
- the `area()` method implemented
- `print()` should print, and `str()` should return, the following
rectangle description: `[Rectangle] <width>/<height>`
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

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
