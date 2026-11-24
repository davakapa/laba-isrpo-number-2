import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(3), 28.2743338823)

    def test_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.8495559215)

    def test_perimeter_fractional_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), 3.1415926536)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(2, 5), 10)

    def test_area_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_equal_sides(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 5), 14)

    def test_perimeter_fractional_side(self):
        self.assertEqual(rectangle.perimeter(1.5, 4), 11)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_area_fractional_side(self):
        self.assertEqual(square.area(1.5), 2.25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(5, 3), 7.5)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_fractional_sides(self):
        self.assertEqual(triangle.perimeter(2.5, 3, 3.5), 9)
