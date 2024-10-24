"""

Interfaces & Mixins

Interfaces
subclass ---|> interface
specity additional behaviors or abilities for an implementing class
An abstract class that contains all abstract methods that all implementing classes will be then forced to override
When not all of your subclasses will require the added behavior, but some will have that code in common

- abstract class with all abstract method
- Polymorphic
- add additional behaviors
- usually have -able name


Mixins
classes that define and implement a single, well defined feature that can be used to add extra behaviors to different calsses in the same way
use inheritance "with-a"

- not abstract
- add additional behaviors
- multiple inheritance
- if all duplicated methods in subclasses
- name ----Mixin

"""

# animal.py
import abc

class Animal(abc.ABC):
    def __init__(self, n) -> None:
        self._name = n
    
    @property
    def name(self):
        return self._name
    
    @abc.abstractmethod
    def do_behavior(self, type):
        pass


# trainable.py
#import abc

class Trainable(abc.ABC):
    @abc.abstractmethod
    def sit(self):
        pass

    @abc.abstractmethod
    def fetch(self):
        pass

    @abc.abstractmethod
    def roll_over(self):
        pass

# dog.py
#import animal
#import trainable

class Dog(Animal, Trainable): # put the superclass first
    def sit(self):
        return self._name + " sits on the ground."

    def fetch(self):
        return self._name + " runs to fetch the ball"

    def roll_over(self):
        return self._name + " rolls around in the grass"
    
    def do_behavior(self, type):
        if type == 1:
            return self.sit()
        elif type == 2:
            return self.fetch()
        elif type == 3:
            return self.roll_over()

# cat.py
#import animal

class Cat(Animal):
    def Sleep(self):
        return self._name + " falls asleep in the sun."
    
    def do_behavior(self, type):
        return self.Sleep()
    

# main.py
#import dog
#import cat

def main():
    animals = [Cat(), Dog]
    animal_choice = int(input("1. Cat\n2. Dog\n"))
    trick_choice = int(input("1. Sit\n2. Fetch\n3. Roll Over\n"))
    animals[animal_choice - 1].do_behavior(trick_choice - 1)

main()
