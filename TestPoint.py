import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""        

    def test_eq(self):
        """ADD YOUR OWN DOCSTRING"""

    def test_equidistant(self):
        """ADD YOUR OWN DOCSTRING"""

    def test_within(self):
        """ADD YOUR OWN DOCSTRING"""

unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects