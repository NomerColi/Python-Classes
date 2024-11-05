""" Hero for Dungeons and Monsters

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random

from entity import Entity
from map import Map


class Hero(Entity):
    """Represents a Hero
    Attributes:
        _loc (int[]): the location of the Hero
    """
    def __init__(self, name) -> None:
        super().__init__(name, 25)
        self._loc = [0, 0]

    @property
    def loc(self):
        return self._loc
    
    def go_north(self) -> str:
        """Moves the Hero to north.
        Args:
            self (Hero) - the Hero instance
        Returns:
            a string representing what is on the moved location
        """
        map = Map()
        
        if self._loc[0] > 0:
            self._loc[0] -= 1

            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
        
    def go_south(self) -> str:
        """Moves the Hero to south.
        Args:
            self (Hero) - the Hero instance
        Returns:
            a string representing what is on the moved location
        """
        map = Map()
        
        if self._loc[0] < len(map) - 1:
            self._loc[0] += 1

            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
    
    def go_west(self) -> str:
        """Moves the Hero to west.
        Args:
            self (Hero) - the Hero instance
        Returns:
            a string representing what is on the moved location
        """
        map = Map()
        
        if self._loc[1] > 0:
            self._loc[1] -= 1

            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
    
    def go_east(self) -> str:
        """Moves the Hero to east.
        Args:
            self (Hero) - the Hero instance
        Returns:
            a string representing what is on the moved location
        """
        map = Map()
        
        if self._loc[1] < len(map) - 1:
            self._loc[1] += 1

            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
        
        
    def attack(self, entity):
        """Enemy attacks hero - randomize damage in the range 1 - 4.
        Hero should take the damage.
        Args:
            self
        Returns:
            a string representing the event
        """
        dmg = random.randint(2, 5)
        entity.take_damage(dmg) 
        return f"{self.name} attacks a {entity.name} for {dmg} damage."