"""

Classes & Objects - Class Relationships

Class Relationships Types
- Dependency: class A 'uses' an instance of class B // A - - - - > B (dash arrow)
    parameter
- Aggregation: class A 'has' one or more references to class B // A <>---- B (solid arrow and hollow diamond)
    attribute, the instance of class B is not constructed in class A
- Composition: class A 'owns' an instance of class B // A <|>---- B (solid arrow and solid diamond)
    attribute, constructed in the class
- Inheritance: class B 'is a' instance of class A // A <|---- B (solid arrow)
    Class B is derived from class A

"""

import random

# die.py
class Die:
    def __init__(self, sides=6) -> None:
        self._sides = sides
        self._value = 0

    def roll(self):
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self):
        return str(self._value)
    
    def __add__(self, other):
        return self._value + other._value
    
    def __lt__(self, other):
        return self._value < other._value
    
    def __eq__(self, other):
        return self._value == other._value
    

# monopoly.py
class Monopoly:
    def __init__(self) -> None:
        self._dice = [Die(), Die()]
    
    def roll(self):
        for d in self._dice:
            d.roll()

    def __str__(self):
        s = ""
        self._dice.sort()
        for i, d in enumerate(self._dice):
            s += "D" + str(i + 1) + ": " + str(d) + " "
        s += "Sum=" + str(self._dice[0] + self._dice[1])
        if self._dice[0] == self._dice[1]:
            s += "You threw the same one"
        return s
    

# main.py
def main():
    m = Monopoly()
    m.roll()
    print(m)

main()