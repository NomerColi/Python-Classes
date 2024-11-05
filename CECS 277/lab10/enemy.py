""" Enemy for Dungeons and Monsters

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from entity import Entity
from hero import Hero
import random


class Enemy(Entity):
    def __init__(self) -> None:
        """Randomizes a name from a list of names and randomizes the monster's hp.
        Args:
            self (Enemy)
        Returns:
            none
        """
        enemy_list = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]
        hp = random.randint(4, 8)
        self._name = random.choice(enemy_list)
        super().__init__(name = self._name, max_hp = hp)
    def attack(self, entity: Hero):
        """Enemy attacks hero - randomize damage in the range 1 - 4.
        Hero should take the damage.
        Args:
            self (Enemy)
        Returns:
            a string representing the event
        """
        dmg = random.randint(1, 4)
        entity.take_damage(dmg) 
        return f"{self._name} attacks {entity.name} for {dmg} damage."