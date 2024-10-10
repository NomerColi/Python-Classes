"""

Testing and Debugging

Testing - the process of checking osftware to make sure that your code is working correctly

Unit Tests - small, fast, automated tests that are performed on small chunks of code

assertEqual
assertNotEqual
assertTrue
assertFalse
assertIs
assertIsNot
assertIsNone
assertIsNotNone
assertIn
assertNotIn
assertIsInstance
assertAlmostEqual
assertNotAlmostEqual
assertGreater
assertGreaterEqual
assertLess
assertLessEqual
assertListEqual
assertDictEqual

Testing Strategy - You should go through and prioritize the most critical parts
AAA
Arrange - create all objects and variables needed to do the test
Act - call the method that need to be tested
Assert - verify the result with an assert statement

independent


Debugging - the proecess of stepping through your code one statement at a time

"""


import unittest


def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 3), 5, "Sum")
    def test_sub(self):
        self.assertEqual(subtract(2, 3), -1, "Subtract")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius * self.radius

    def calc_circumference(self):
        return 2 * 3.14 * self.radius


class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(2)
        self.assertEqual(c.calc_area(), 12.56)

    def test_circumference(self):
        c = Circle(3)
        self.assertEqual(c.calc_circumference(), 18.84)


def main():
    unittest.main(exit=False)


main()