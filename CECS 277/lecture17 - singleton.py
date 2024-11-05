"""

Singleton

Design Patterns
general solutions to common problems in software design

Types
- Creational: provide a systematic way of creating objects
- Structural: define and build relationships between classes to form them into a larger structure that is flexible and extensible
- Behavioral: make for better interactions and communication between objects


Singleton - a creational design pattern
- make sure that there is only a single instance
- provides a global access point to it

"""

# singleton.py
class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, x):
        if not Singleton._initialized:
            self._x = x
            Singleton._initialized = True

    def inc_x(self):
        self._x += 1

    def __str__(self) -> str:
        return super().__str__() + " x: " + str(self._x)
    
# main.py
# import singleton
def main():
    s1 = Singleton(1)
    s2 = Singleton(5)
    print(s1)
    print(s2)

    s1.inc_x()
    print(s1)
    print(s2)

    s3 = Singleton(10)
    print(s1)
    print(s2)
    print(s3)
    
main()