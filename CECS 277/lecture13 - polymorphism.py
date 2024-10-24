"""

Polymorphism
the ability for objects to react differently based on their type
- multiple forms
- inheritance - multiple types
- react differently based on type
- overrided methods

Duck Typing
if the object has the methods that are needed, then it can be used without checking its type.

Method Overriding
when a method in a subclass has the same name as a method in the superclass
guaranteed to have the overriden function

Object Class
a class from which all classes automatically inherit

"""

class Duck:
    """Represents a duck."""
    def quack(self):
        """Quacks the duck."""
        return "Quack"

class Dog(Duck):
    """Represents a dog."""
    def quack(self):
        """Quacks the dog."""
        return "Woof!"

class Cat(Duck):
    """Represents a cat."""
    def meow(self):
        """Meows the cat."""
        return "Meow"

def main():
    ducks = [Duck(), Duck(), Dog(), Duck(), Cat()]
    for d in ducks:
        print(d.quack())  # Quack Quack Woof! Quack Exception

main()