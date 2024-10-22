""" Fire for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

""" Flying for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
from dragon import Dragon
from hero import Hero


class Fire:
    def fireblast(self: Dragon, opponent: Hero):
        """if the dragon has any special attacks left, then it blasts the the hero
        with fire and they take a random amount of damage in the range 5-9 and 
        the number of special attacks is decremented.
        Args:
            self (Dragon) - the attacking Dragon instance
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string with a description of the attack and the damage dealt to the hero.
            Otherwise, no damage is done and a string describing the failure is returned.
        """
        return_str = self.name
        if self._special_attacks >= 1:
            self.decrement_special_attacks()
            dmg = random.randint(5, 9)
            opponent.take_damage(dmg)
            
            return_str += " engulfs " + opponent.name + " in flames for " + str(dmg) + " damage!"
        else:
            return_str += " tries to engulf " + opponent.name + " in flames, but it is all out of fuel."
        return return_str

    def fireball(self: Dragon, opponent: Hero):
        """if the dragon has any special attacks left, then it spits a fireball at
        the hero and they take a random amount of damage in the range 4-8 and 
        the number of special attacks is decremented.
        Args:
            self (Dragon) - the attacking Dragon instance
            opponent (Hero) - the Hero instance being attacked
        Returns:
            a string with a description of the attack and the damage dealt to the hero.
            Otherwise, no damage is done and a string describing the failure is returned.
        """
        return_str = self.name
        if self._special_attacks >= 1:
            self.decrement_special_attacks()
            dmg = random.randint(4, 8)
            opponent.take_damage(dmg)
            
            return_str += " spits a fireball at " + opponent.name + " for " + str(dmg) + " damage!"
        else:
            return_str += " tries to spit fire at " + opponent.name + ", but it is all out of fuel."
        return return_str
