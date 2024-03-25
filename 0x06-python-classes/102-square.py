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
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square
  area
- You are not allowed to import any module
"""


class Square:
    """The Square class"""

    def __init__(self, size=0):
        """Initialising the Square class"""
        self.size = size

    def area(self):
        """Returns the current square area"""
        return self.__size**2

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

    def __lt__(self, other):
        """Less than comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparison"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal to comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison"""
        return self.area() >= other.area()
