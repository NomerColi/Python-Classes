""" Entity for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc

class Entity(abc.ABC):
    """Represents an entity.
    Attributes:
        _name (str): a name
        _max_hp (int): the maximum health point
        _hp (int): the current health point
    """
    def __init__(self, name, max_hp) -> None:
        """Initiates this Entity.
        Args:
            self (Entity) - the Entity instance being initiated
            name (str): a name of this Entity
            max_hp (int): the maximum health point of this Entity
        Returns:
            none
        """
        self._name = name
        self._hp = self._max_hp = max_hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, dmg) -> None:
        """Takes damage.
        Args:
            self (Entity) - the Entity instance taking damage
            dmg (int): the amount of damage
        Returns:
            none
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self) -> str:
        """Gets the string representation fo this Entity.
        Args:
            self (Entity) - the Entity instace getting the string representation for
        Returns:
            a string representing this Entity
        """
        return f"{self._name}: {self._hp}/{self._max_hp}"

    @abc.abstractmethod
    def basic_attack(self, opponent) -> str:
        """Performs basic attack to the Opponent.
        Args:
            self (Entity) - the attacking Entity instance
            opponent (Entity) - the opponent Entity instance being attacked
        Returns:
            a string for the result
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