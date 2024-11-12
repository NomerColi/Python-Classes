"""

Decorator
structural
allows you to dynamically attach additional behaviors and responsibilities on to your objects
chaining the features together




"""

import abc
class Pizza(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


#import pizza
class PizzaSmall(Pizza):
    def get_price(self):
        return 5

    def get_description(self):
        return "Small Pizza "


#import pizza
class PizzaLarge(Pizza):
    def get_price(self):
        return 7

    def get_description(self):
        return "Large Pizza "


#import abc
#import pizza
class Decorator(Pizza, abc.ABC):
    def __init__(self, p):
        self._pizza = p

    def get_price(self):
        return self._pizza.get_price()

    def get_description(self):
        return self._pizza.get_description()


#import decorator
class Pepperoni(Decorator):
    def get_price(self):
        return super().get_price() + 1

    def get_description(self):
        return super().get_description() + "+ Pepperoni "


#import decorator
class Mushrooms(Decorator):
    def get_price(self):
        return super().get_price() + .5

    def get_description(self):
        return super().get_description() + "+ Mushrooms "


#import pizza_small
#import pizza_large
#import pepperoni
#import mushrooms
def main():
    p = PizzaSmall()
    p = Mushrooms(p)
    p = Pepperoni(p)
    print(p.get_description()) # Small Pizza +Mushrooms +Pepperoni
    print(p.get_price())       # 8.5

main()