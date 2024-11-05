""" Dragon for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc
from entity import Entity
import random

class Dragon(Entity):
    """Represents a Dragon.
    Attributes:
        _special_attacks (int): the remaining number of special attacks the Dragon can perform
    """
    def __init__(self, name, max_hp, num_sp) -> None:
        """Initiates the Dragon instance.
        Args:
            self (Dragon) - the Dragon instance being initiated
            name (str): the name
            max_hp (int): the maximum health point
            num_sp (int): the number of special attacks the Dragon can perform in a game
        Returns:
            none
        """
        super().__init__(name, max_hp)
        self._special_attacks = num_sp

    @property
    def special_attacks(self):
        return self._special_attacks

    def decrement_special_attacks(self) -> None:
        """Decrements the remaining number of special attacks the Dragon can perform.
        Args:
            self (Dragon) - the Dragon instance decrementing special attacks
        Returns:
            none
        """
        self._special_attacks -= 1
        if self._special_attacks < 0:
            self._special_attacks = 0
    
    def basic_attack(self, opponent) -> str:
        """- Tail attack - The hero takes a random amount of damage in the range 3 - 7.
        Args:
            self (Dragon) - the Dragon instance attacking
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string with the description of the attack and the damage dealt to the hero.
        """
        pass
    
    @abc.abstractmethod
    def special_attack(self, opponent) -> str:
        """Performs special attack to the Opponent.
        Args:
            self (Entity) - the attacking Entity instance
            opponent (Entity) - the opponent Entity instance being attacked
        Returns:
            a string for the result
        """
        pass

    def __str__(self) -> str:
        """Gets the string representation of this Dragon.
        Args:
            self (Dragon) - the Dragon instance getting the string representation for
        Returns:
            a string representing this Dragon
        """
        return super().__str__() + "\nSpecial attacks remaining: " + str(self._special_attacks)

    