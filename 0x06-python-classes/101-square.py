#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 3-square.py)

- Private instance attribute: `size`:
- - property def `size(self):` to retrieve it
- - property setter `def size(self, value):` to set it:
- - - `size` must be an integer, otherwise raise a `TypeError` exception
      with the message `size must be an integer`
- - - if `size` is less than `0`, raise a `ValueErro`r exception with the
      message `size must be >= 0`
- Private instance attribute: `position`:
- - property def `position(self):` to retrieve it
- - property setter `def position(self, value):` to set it:
- - - `position` must be a tuple of 2 positive integers, otherwise raise a
      `TypeError` exception with the message `position must be a tuple of 2
      positive integers`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square
  area
- Public instance method: `def my_print(self):` that prints in stdout the
- - if `size` is equal to 0, print an empty line
- - `position` should be use by using space - Don't fill lines by spaces
- Printing a `Square` instance should have the same behaviour as `my_print()`
- You are not allowed to import any module
"""


class Square:
    """The Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialising the Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position value"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size**2

    def my_print(self):
        if not self.__size:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of the Square class"""
        if not self.__size:
            return ""
        res = ""
        for _ in range(self.__position[1]):
            res += "\n"
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                res += " "
            for _ in range(self.__size):
                res += "#"
            res += "\n"
        return res[:-1]
