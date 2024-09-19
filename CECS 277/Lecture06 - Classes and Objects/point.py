"""

Classes & Objects

- a programmer defined data type
- represents an object
- code reuse
- construct objects

1. Encapsulation - a class provides a single location
2. Abstraction - a class allows you to define an interface to interact with
3. Cohesion - a class should be designed to represent a single object with a clear purpose
4. Extension and Reuse - one a class is created and tested, in can be reused in other programs or derived from to create new classes

Object - an instance of a class


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

def main():
    pass


main()
