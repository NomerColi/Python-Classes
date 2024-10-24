""" Flying Dragon for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from dragon import Dragon
from flying import Flying
from random import randint

class FlyingDragon(Dragon, Flying):
    """Represents a FlyingDragon.
    """
    def __init__(self) -> None:
        super().__init__(name = "Timberjack", max_hp = 10, num_sp = 3)
    def special_attack(self: Dragon, opponent) -> str:
        """randomly choose one of the two flying attacks.
        Args:
            self (FlyingDragon) - the FlyingDragon instance attacking
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string for the result of attack
        """
        rand = randint(0, 1)
        if rand == 1:
            return self.swoop(opponent)
        else:
            return self.windblast(opponent)