import math
radius = 5.0

def func():
    pass
func()

class Sample:
    pass
sample = Sample()

class Dog:
    species = "Mammal" # static?
    def __init__(self, breed="unidentified", name="unnamed", spots=False):
        self.breed = breed
        self.name = name
        self.spots = spots

dog1 = Dog()
print(dog1.breed)
print(dog1.name)

dog2 = Dog("Lab", "Bob", "Something")