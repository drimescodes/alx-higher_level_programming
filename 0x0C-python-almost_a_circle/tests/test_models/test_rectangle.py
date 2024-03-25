#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        """Set up for all methods"""
        Rectangle._Base__nb_objects = 0

    def test_id(self):
        """Test id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 21)

    def test_width(self):
        """Test width attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.width, 10)

    def test_height(self):
        """Test height attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.height, 2)

    def test_x(self):
        """Test x attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.x, 0)
        r4 = Rectangle(10, 2, 3, 0, 0)
        self.assertEqual(r4.x, 3)

    def test_y(self):
        """Test y attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.y, 0)
        r4 = Rectangle(10, 2, 3, 0, 0)
        self.assertEqual(r4.y, 0)

    def test_width_TypeError(self):
        """Test width TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("-inf"), 10)

    def test_height_TypeError(self):
        """Test height TypeError"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (1, 2))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float("nan"))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float("inf"))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float("-inf"))

    def test_x_TypeError(self):
        """Test x TypeError"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (1, 2))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float("nan"))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float("inf"))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float("-inf"))

    def test_y_TypeError(self):
        """Test y TypeError"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, float("nan"))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, float("inf"))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, float("-inf"))

    def test_width_ValueError(self):
        """Test width ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 3)

    def test_height_ValueError(self):
        """Test height ValueError"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0, 3)

    def test_x_ValueError(self):
        """Test x ValueError"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 4)

    def test_y_ValueError(self):
        """Test y ValueError"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4, 5)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display method"""
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(2, 2)
        self.assertEqual(r2.display(), None)
        r3 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r3.display(), None)

    def test_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (22) 1/0 - 5/5")
        r3 = Rectangle(5, 5)
        self.assertEqual(r3.__str__(), "[Rectangle] (23) 0/0 - 5/5")

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(
            r1.to_dictionary(),
            {"x": 1, "y": 9, "id": 24, "height": 2, "width": 10},
        )
        r2 = Rectangle(1, 1)
        self.assertEqual(
            r2.to_dictionary(),
            {"x": 0, "y": 0, "id": 25, "height": 1, "width": 1},
        )
        r3 = Rectangle(1, 1, 1)
        self.assertEqual(
            r3.to_dictionary(),
            {"x": 1, "y": 0, "id": 26, "height": 1, "width": 1},
        )
        r4 = Rectangle(1, 1, 1, 1)
        self.assertEqual(
            r4.to_dictionary(),
            {"x": 1, "y": 1, "id": 27, "height": 1, "width": 1},
        )
        r5 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(
            r5.to_dictionary(),
            {"x": 1, "y": 1, "id": 1, "height": 1, "width": 1},
        )


if __name__ == "__main__":
    unittest.main()
