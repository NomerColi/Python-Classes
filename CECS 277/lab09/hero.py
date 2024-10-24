""" Hero for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from entity import Entity
import random


class Hero(Entity):
    def basic_attack(self, opponent):
        """The dragon takes a random amount of damage in the range 2D6 (1 - 6 + 1 - 6).
        Args:
            self
            opponent
        Returns:
            a string with the description of the attack and the damage dealt
            to the dragon.
        """
        dmg = random.randint(1, 6) + random.randint(1, 6) # 2D6
        opponent.take_damage(dmg)
        return f"{self.name} slashes the {opponent} with their sword for {dmg} damage!"
    def special_attack(self, opponent):
        """The dragon takes a random amount of damage in the range 1D12
        (1-12).
        Args:
            self
            opponent
        Returns:
            a string with the description of the attack and the damage dealt
            to the dragon.
        """
        dmg = random.randint(1, 12) # 1D12
        opponent.take_damage(dmg)
        return f"{self.name} hits the {opponent} with an arrow for {dmg} damage!"