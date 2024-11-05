"""

Factor Method
- a creational
- minimizes dependencies by removing the process of creating objects
- replaces it with a factory interface for creating those objects
- produce products
- one type of product
- one interface
- list of products
- process product

"""

import abc
class Cookie(abc.ABC):
    @abc.abstractmethod
    def eat_cookie(self):
        pass


#import cookie
class DropCChip(Cookie):
    def eat_cookie(self):
        return "Eating a Chocolate Chip cookie."


#import cookie
class DropPB(Cookie):
    def eat_cookie(self):
        return "Eating a Peanut Butter cookie."


#import abc
class CookieFactory(abc.ABC):
    def process_cookie(self, type):
        cookie = self.make_cookie(type)
        return cookie.eat_cookie()

    @abc.abstractmethod
    def make_cookie(self, type):
        pass


#import cookie_factory
#import drop_cchip
#import drop_pb
class DropFactory(CookieFactory):
    def make_cookie(self, type):
        if type == "CC":
            return DropCChip()
        if type == "PB":
            return DropPB()


#import drop_factory
def main():
    fact = DropFactory()
    print(fact.process_cookie("CC"))
    print(fact.process_cookie("PB"))

main()