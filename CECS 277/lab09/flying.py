""" Flying for Flying Dragons

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
from dragon import Dragon
from hero import Hero


class Flying:
    def swoop(self: Dragon, opponent: Hero):
        """Perforns a swoop to the Hero.
        Args:
            self (Dragon) - the attacking Dragon instance
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string for the result of attack
        """
        return_str = self.name
        if self._special_attacks >= 1:
            self.decrement_special_attacks()
            dmg = random.randint(4, 8)
            opponent.take_damage(dmg)
            
            return_str += " swoops down at " + opponent.name + " and hits them for " + str(dmg) + " damage!"
        else:
            return_str += " tries to swoop down to hit " + opponent.name + ", but failed."
        return return_str
    
    def windblast(self: Dragon, opponent: Hero):
        """Performs a windblast to the Hero.
        Args:
            self (Dragon) - the attacking Dragon instance
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string for the result of attack
        """
        return_str = self.name
        if self._special_attacks >= 1:
            self.decrement_special_attacks()
            dmg = random.randint(3, 7)
            opponent.take_damage(dmg)
            
            return_str += " blasts " + opponent.name + " with a windstorm for " + str(dmg) + " damage!"
        else:
            return_str += " tries to blast " + opponent.name + " with a windstorm, but failed."
        return return_str
