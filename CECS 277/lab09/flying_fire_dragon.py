""" Flying Fire Dragon for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from dragon import Dragon
from flying import Flying
from fire import Fire
from random import randint


class FlyingFireDragon(Dragon, Flying, Fire):
    def __init__(self) -> None:
        super().__init__(name = "Deadly Nadder", max_hp = 20, num_sp = 2)
    def special_attack(self, opponent) -> str:
        """randomly choose one of the four flying and fire attacks.
        Args:
            self
            opponent
        Returns:
            none
        """
        rand = randint(0, 3)
        if rand == 0:
            return self.fireblast(opponent)
        elif rand == 1:
            return self.fireball(opponent)
        elif rand == 2:
            return self.swoop(opponent)
        else:
            return self.windblast(opponent)