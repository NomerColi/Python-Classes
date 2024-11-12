"""

Adapter
structural
- structural
- incompatible interfaces
- polymorphism
- methods
- Parameters
- return types
- wrong units

Types
1. Object Adapter - which is composed of the incompatible Adaptee class
2. Class Adapter - which inherits from the incompatible Adaptee class

"""

class UsableInterface():
    pass

class Adaptee:
    def unusable_method(self):
        return "Unusual"
    
#import usable_fu
class Adapter:
    def __init__(self) -> None:
        self._adapt = Adapter()

    def usable_method(self):
        return self.unusable_method() + " into Usable method"

#main
#import adapter
def main():
    usable = Adapter()
    print(usable.unusual_method())


#Example 2

# triangle.pyq
#import shape
#impprt righttriangle

class Triangle(Shape):
    def __init__(self, b, h):
        self._triangle = RightTriangle(b, h)

    def area(self):
        return self._trangle_calc_area()
    def parimeter(self):
        #return self._calc_hypotenus
        pass