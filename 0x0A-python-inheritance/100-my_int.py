#!/usr/bin/python3
"""
A module that contains the MyInt class inheriting from int
- MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """
    A class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        Returns the opposite of the equality comparison
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Returns the opposite of the inequality comparison
        """
        return super().__eq__(other)
    