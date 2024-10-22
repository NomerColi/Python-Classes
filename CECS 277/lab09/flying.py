""" Flying for the Dragon Trainer Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
from dragon import Dragon
from hero import Hero


class Flying:
    def swoop(self: Dragon, opponent: Hero):
        """if the dragon has any special attacks left, then it does a 
        swoop attack at the hero and they take a random amount of damage in the range 4-8 and 
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
            
            return_str += " swoops down at " + opponent.name + " and hits them for " + str(dmg) + " damage!"
        else:
            return_str += " tries to swoop down to hit " + opponent.name + ", but failed."
        return return_str
    
    def windblast(self: Dragon, opponent: Hero):
        """if the dragon has any special attacks left, then it blasts wind at
        the hero and they take a random amount of damage in the range 3-7 and 
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
            dmg = random.randint(3, 7)
            opponent.take_damage(dmg)
            
            return_str += " blasts " + opponent.name + " with a windstorm for " + str(dmg) + " damage!"
        else:
            return_str += " tries to blast " + opponent.name + " with a windstorm, but failed."
        return return_str
        '''[name] blasts [player_name] with a windstorm for [damage] damage!
        [name] tries to blast [player_name] with a windstorm, but failed.'''
