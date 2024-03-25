#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def setUp(self):
        """Set up for all methods"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """Test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_save_to_file(self):
        """Test save_to_file method"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([Square(1, 2)])
        with open("Square.json", "r") as file:
            self.assertEqual(
                file.read(), '[{"id": 1, "size": 1, "x": 2, "y": 0}]'
            )

    def test_from_json_string(self):
        """Test from_json_string method"""
        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Square.from_json_string("[]"), [])
        self.assertEqual(Square.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_create(self):
        """Test create method"""
        s1 = Square(1, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(s2.__str__(), "[Square] (4) 2/3 - 1")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """Test load_from_file method"""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(
            list_squares_input[0].__str__(), "[Square] (4) 2/3 - 1"
        )
        self.assertEqual(
            list_squares_input[1].__str__(), "[Square] (8) 6/7 - 5"
        )
        self.assertEqual(
            list_squares_output[0].__str__(), "[Square] (4) 2/3 - 1"
        )
        self.assertEqual(
            list_squares_output[1].__str__(), "[Square] (8) 6/7 - 5"
        )

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "")
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "")
        Square.save_to_file_csv([Square(1, 2)])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "1,1,2,0\n")


if __name__ == "__main__":
    unittest.main()
