"""

Classes & Objects

Class
- a programmer defined data type
- represents an object
- code reuse
- construct objects

1. Encapsulation - a class provides a single location
2. Abstraction - a class allows you to define an interface to interact with
3. Cohesion - a class should be designed to represent a single object with a clear purpose
4. Extension and Reuse - one a class is created and tested, in can be reused in other programs or derived from to create new classes

Object - an instance of a class

Self - represents the instance of the class

Object References - point1. does not contain the actual data of the object
Shallow Copy
- point3 = point1
Deep Copy
point3 = copy.deepcopy(point1)


"""


class Point:
    """ Represents a point on the coordinatep lane.
    Attributes:
        x (int): x value of the point.
        y (int): y value of the point.
    """

    def __init__(self, x=0, y=0) -> None:
        """Sets the x and y values of the point"""
        self.x = y
        self.y = y

    def translate(self, dx, dy) -> None:
        """Shifts the point by dx and dy."""
        self.x += dx
        self.y += dy

    def __str__(self) -> str:
        """Returns the Point as a formmated string."""
        return "X = " + str(self.x) + " Y = " + str(self.y)

import copy


def movePoint(pt):
    pt.translate(1, 1)
    print(pt)


def newPoint():
    return Point()

def main():

    p1 = Point(1, 2)
    p1.translate(2, 3)
    print(p1)

    p2 = copy.deepcopy(p1)
    p2.translate(1, 1)
    print(p1)
    print(p2)


main()