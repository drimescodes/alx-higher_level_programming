#!/usr/bin/python3
"""
Square class
- Inherited from Rectangle
- Private instance attribute: size
- Getter and setter for size
- __init__ method
    - Initialize size using super() with width and height
- __str__ method
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Update attributes of Square"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
