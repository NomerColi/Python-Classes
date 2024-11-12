""" Plate for Thanksgiving Dinner

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc

class Plate(abc.ABC):
    @abc.abstractmethod
    def description(self) -> str:
        """Returns a string description of the plate and what is on it.
        Args:
            self (Plate)
        Returns:
            a string of the description
        """
        pass
    @abc.abstractmethod
    def area(self) -> int:
        """Returns the remaining square inches the plate can hold.
        Args:
            self (Plate)
        Returns:
            an integer of the area
        """
        pass
    @abc.abstractmethod
    def weight(self) -> int:
        """Returns the remaining number of ounces the plate can hold.
        Args:
            self (Plate)
        Returns:
            an integer of the weight
        """
        pass
    @abc.abstractmethod
    def count(self) -> int:
        """Returns the number of food items the plate is currently holding.
        Args:
            self (Plate)
        Returns:
            an integer of the number of the food items
        """
        pass