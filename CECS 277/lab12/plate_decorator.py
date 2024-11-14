""" Plate Decorator

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc
from plate import Plate


class PlateDecorator(Plate, abc.ABC):
    """Represents a Plate Decorator.
    Attributes:
        _plate (Plate)
    """
    def __init__(self, p) -> None:
        """Passes in plate
        Args:
            self (Plate)
            p: plate object
        Returns:
            none
        """
        self._plate = p

    def description(self) -> str:
        """Returns a string description of the plate and what is on it.
        Args:
            self (Plate)
        Returns:
            a string of the description
        """
        return self._plate.description()
    
    def area(self) -> int:
        """Returns the remaining square inches the plate can hold.
        Args:
            self (Plate)
        Returns:
            an integer of the area
        """
        return self._plate.area()
    
    def weight(self) -> int:
        """Returns the remaining number of ounces the plate can hold.
        Args:
            self (Plate)
        Returns:
            an integer of the weight
        """
        return self._plate.weight()
    
    def count(self) -> int:
        """Returns the number of food items the plate is currently holding.
        Args:
            self (Plate)
        Returns:
            an integer of the number of the food items
        """
        return self._plate.count()