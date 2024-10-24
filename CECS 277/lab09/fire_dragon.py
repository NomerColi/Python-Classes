""" Fire Dragon for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from dragon import Dragon
from fire import Fire
from random import randint


class FireDragon(Dragon, Fire):
    """Represents a FireDragon.
    """
    def __init__(self) -> None:
        super().__init__(name = "Gronkle", max_hp = 15, num_sp = 3)
    def special_attack(self: Dragon, opponent) -> str:
        """randomly choose one of the two fire attacks.
        Args:
            self (FireDragon) - the FireDragon instance attacking
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string for the result of attack
        """
        # choose a random action
        rand = randint(0, 1)
        if rand == 1:
            return self.fireblast(opponent)
        else:
            return self.fireball(opponent)