""" Die for the Yahtzee Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random


class Die:
    """Represents a single Die.  Defaults to a 6-sided die.
    Attributes:
        _sides (int): number of sides on the die.
        _value (int): the value of the rolled die.
    """
    def __init__(self, sides=6):
        """Sets the number of sides of the die (default 6) and lets the die roll.
        Args:
            self (Die) - the Die instance being initialized
            sides (int): the number of sides.
        Returns:
            none
        """
        self._sides = sides
        self._value = self.roll()

    def roll(self) -> int:
        """Rolls the die to set the value of the die.  Returns that value (random value between 1-sides).
        Args:
            self (Die) - the Die instance being rolled
        Returns:
            an integer of the value.
        """
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self):
        """Returns the string representation of the die.
        Args:
            self (Die) - the Die instance to get a string representation for
        Returns:
            a string representing the Die to print.
        """
        return str(self._value)

    def __add__(self, other):
        """Returns the sum of the values of self and other.
        Args:
            self (Die) - the Die instance to get the value to add
            other (Die) - another Die instance to get the value to add
        Returns:
            an integer of the sum of the dies' values.
        """
        return self._value + other._value

    def __lt__(self, other):
        """Compares the two dice to see if self’s value is less than the other’s value.
        Args:
            self (Die) - the Die instance to check if it is less than the other instance
            other (Die) - another Die instance to check if self is less than this
        Returns:
            a boolean whether the self Die's value is less then the other's.
        """
        return self._value < other._value

    def __eq__(self, other):
        """Compares the two dice to see if self’s value is equal to the other’s value.
        Args:
            self (Die) - the Die instance to check if it has the same value with the other instance
            other (Die) - another Die instance to check if self has the same value with this
        Returns:
            a boolean whether the two instances have the same value.
        """
        return self._value == other._value
    
    def __sub__(self, other):
        """Returns the difference between the value of self and the value of other
        Args:
            self (Die) - the Die instance to get the value to subtract
            other (Die) - another Die instance to get the value to subtract
        Returns:
            an integer of subtracting other's value from self's value.
        """
        return self._value - other._value