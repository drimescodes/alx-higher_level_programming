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
- Public class attribute `number_of_instances`:
    - Initialized to `0`
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
- Public class attribute `print_symbol`:
    - Initialized to `#`
    - Used as symbol for string representation
    - Can be any type
- Instantiation with optional `width` and `height`:
    `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle
    perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
    - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to
    recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` when an instance of Rectangle is deleted
"""


class Rectangle:
    """
    Defines a Rectangle with basic properties of a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """
        Initializes a Rectangle with optional width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        """
        Retrieves the width.
        """
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """
        Sets the width to a value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """
        Retrieves the height.
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Sets the height to a value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width] * self.__height
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the rectangle to be able to
        recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self) -> None:
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
