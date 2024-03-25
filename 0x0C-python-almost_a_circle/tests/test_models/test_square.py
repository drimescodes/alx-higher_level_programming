#!/usr/bin/python3
"""Unittest for models/square.py"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        """Set up for all methods"""
        Square._Base__nb_objects = 0

    def test_id(self):
        """Test id attribute"""
        s1 = Square(10)
        self.assertEqual(s1.id, 73)

    def test_size(self):
        """Test size attribute"""
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        s2 = Square(2)
        self.assertEqual(s2.size, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.size, 10)
        s4 = Square(10, 0, 0, 0)
        self.assertEqual(s4.size, 10)

    def test_x(self):
        """Test x attribute"""
        s1 = Square(10)
        self.assertEqual(s1.x, 0)
        s2 = Square(2, 3)
        self.assertEqual(s2.x, 3)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.x, 0)
        s4 = Square(10, 3, 0, 0)
        self.assertEqual(s4.x, 3)

    def test_y(self):
        """Test y attribute"""
        s1 = Square(10)
        self.assertEqual(s1.y, 0)
        s2 = Square(2, 3, 4)
        self.assertEqual(s2.y, 4)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.y, 0)
        s4 = Square(10, 3, 4, 0)
        self.assertEqual(s4.y, 4)

    def test_area(self):
        """Test area method"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s2 = Square(2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.area(), 64)
        s4 = Square(10, 3, 4, 0)
        self.assertEqual(s4.area(), 100)

    def test_display(self):
        """Test display method"""
        s1 = Square(4)
        self.assertEqual(s1.display(), None)
        s2 = Square(2)
        self.assertEqual(s2.display(), None)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.display(), None)
        s4 = Square(10, 3, 4, 0)
        self.assertEqual(s4.display(), None)

    def test_str(self):
        """Test __str__ method"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 1, 0, 0)
        self.assertEqual(s2.__str__(), "[Square] (0) 1/0 - 5")

    def test_update(self):
        """Test update method"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        s1.update(x=1, size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 1/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {
            "id": 76,
            "size": 10,
            "x": 2,
            "y": 1
        })
        s2 = Square(1, 1)
        self.assertEqual(s2.to_dictionary(), {
            "id": 77,
            "size": 1,
            "x": 1,
            "y": 0
        })
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.to_dictionary(), {
            "id": 12,
            "size": 10,
            "x": 0,
            "y": 0
        })
        s4 = Square(10, 3, 4, 0)
        self.assertEqual(s4.to_dictionary(), {
            "id": 0,
            "size": 10,
            "x": 3,
            "y": 4
        })
