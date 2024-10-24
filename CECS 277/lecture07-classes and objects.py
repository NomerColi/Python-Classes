"""

Classes & Objects

Design
1. Summarize program
2. Find nouns - become objects
3. has / done
4. attributes methods
5. Write code

Class Design - start with basic set of steps and then expand as needed
1. Write a full description of what you want your program to do
2. Look through your description, usually items that are nouns or objects will become the classes
3. Make a list of the classes you decide to create
4. Expand on your class as needed

Operator Overloading
add the ability for our objects to be used with operators

Relational Operators
- lt
- le
- gt
- ge
- eq
- ne

Mathematical Operators
- add
- sub
- mul
- truediv
- floordiv
- mod
- pow

Bitwise Operators
- and
- or
- xor
- lshift
- rshift

Other Operators
- getitem
- len
- int
- float
- str
- repr


"""

class Rectangle:
    """Represents a rectangle on the coordinate plane.
    Attributes:
        x (int): location x of the rectangle
        y (int): location of y of the rectangle
        width (int): width of the rect
        height (int): height of the rect
    """
    
    def __init__(self, x=0, y=0, w=1, h=1):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def translate(self, dx, dy):
        """Shifts the rectangle's location by dx, dy."""
        self.x += dx
        self.y += dy

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ") W= " + str(self.width) + " H= " + str(self.height)
    
    def __add__(self, other):
        return Rectangle(self.x, self.y, self.width + other.width, self.height + other.height)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height
    

def main():
    rect = Rectangle(1, 2, 4, 5)
    print(rect)

main()