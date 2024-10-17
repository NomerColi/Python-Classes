"""

Multiple Inheritance
a class inherits from two or more classes

class A(B, C)

Diamond Problem
two classes inherit from a common superclass and override methods from superclass
and then another class inherits from the first two classes using multiple inheritance

Method Resolution Order (MRO)
the order that a method is searched for in the hierarchy of classes when it gets called


"""

class Animal:
    """Representation of a cat."""
    def speak(self):
        """Makes a generic animal speak."""
        return "..."

class Cat(Animal):
    """Representation of a cat."""
    def speak(self):
        """Meows the cat."""
        return "Meow!"

class Dog(Animal):
    """Representation of a dog."""
    def speak(self):
        """Barks the dog."""
        return "Woof!"


class CatDog(Cat, Dog):
    """Representation of a cat dog."""
    def speak(self):
        """Makes the cat dog speak."""
        return super().speak() + "Meoof"

def main():
    cd1 = CatDog()
    print(cd1.speak()) # Meoof!

    print(CatDog.__mro__) # MRO

main()