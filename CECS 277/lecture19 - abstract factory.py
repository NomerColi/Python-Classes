"""

Abstract Factory
- creational
- produce products
- different families of product
- multiple interfaces
- matrix of products
- no process product

"""

### first example
import abc

# productA.py
class ProductA(abc.ABC):
    @abc.abstractmethod
    def func_a(self):
        pass

# productB.py
class ProductB(abc.ABC):
    @abc.abstractmethod
    def func_b(self):
        pass

# productA1.py
class ProductA1(ProductA):
    def func_a(self):
        return "Product A1"

# productA2.py
class ProductA2(ProductA):
    def func_a(self):
        return "Product A2"

# productB1.py
class ProductB1(ProductB):
    def func_b(self):
        return "Product B1"

# productB2.py
class ProductB2(ProductB):
    def func_b(self):
        return "Product B2"
    
# abstractFactory.py
class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def create_prod_a(self):
        pass

    @abc.abstractmethod
    def create_prod_b(self):
        pass

# factory1.py
class Factory1(AbstractFactory):
    def create_prod_a(self):
        return ProductA1()
    
    def create_prod_b(self):
        return ProductB1()


# factory2.py
class Factory2(AbstractFactory):
    def create_prod_a(self):
        return ProductA2()
    
    def create_prod_b(self):
        return ProductB2()


def main():
    fact1 = Factory1()
    pA1 = fact1.create_prod_b()
    print(pA1.func_a())

main()


### second example

# regular.py
class Regular(abc.ABC):
    @abc.abstractmethod
    def eat_fries(self):
        pass

# spicy.py
class Spicy(abc.ABC):
    @abc.abstractmethod
    def eat_fries(self):
        pass

    @abc.abstractmethod
    def dip_in_ranch(self):
        pass