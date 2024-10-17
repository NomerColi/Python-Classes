"""

Abstract Class

Abstraction
the process of extracting out common features and attributes of similar objects and placing them into an abstract class

Abstract Base Classes (ABCs)
1. when you want to create a superclass that all of your subclasses inherit from, but you do not want to be able to create any objects
2. when you want to force each of your subclasses to conform to a particular interface
- no objects created from the class
- force subclasses to override all funcs



"""

import abc
class Animal(abc.ABC):
    def __init__(self, n, a) -> None:
        self.name = n
        self.age = a
    
    def __str__(self):
        return "Name _ " + self.name + " Age = " + str(self.age) + "says = " + self.make_noise()
    
    @abc.abstractmethod
    def make_noise(self):
        pass

class Dog(Animal):
    def make_noise(self):
        return "The dog barks"
    

def main():
    d1 = Dog("SA", 2)
    print(d1)

class Mug:
    def add_coffee(self, coffee):
        self.coffee = coffee

    def stir_coffee(self):
        return self.coffee.stir_coffee()
        
main()