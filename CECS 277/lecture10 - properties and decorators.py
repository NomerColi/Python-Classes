"""

Properties & Decorators

Properties - for when you want to make a method appear as an attribute

Access Control - public vs non-public
- Private: self.__x / instance._class__x
- Protected: self._x
- Public: self.x

Decorators - a cleaner version of property() placing @

"""

class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    # def _get_radius(self):
    #     return self._radius
    
    @property # decorator
    def radius(self):
        return self._radius
    
    # def _set_radius(self, radius):
    #     if type(radius) == int:
    #         if radius > 0:
    #             self._radius = radius
    #         else:
    #             raise ValueError("Radius must be postive")
    #     else:
    #         raise ValueError("Radius must be an integer")
    
    @radius.setter # decorator
    def radius(self, radius):
        if type(radius) == int:
            if radius > 0:
                self._radius = radius
            else:
                raise ValueError("Radius must be postive")
        else:
            raise ValueError("Radius must be an integer")
        
    def area(self):
        return self._radius * 2 * 3.14
    
    def __str__(self) -> str:
        return "Circle: radius: " + str(self._radius)
    
    #radius = property(_get_radius, _set_radius)

def main():
    c1 = Circle(2)
    print(c1)
    c1.radius = "ASD"
    c1.radius = -2
    print(c1.area())


main()