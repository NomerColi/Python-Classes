""" Motorcycle for the racing game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
from vehicle import Vehicle
import random
class Motorcycle(Vehicle):
    def __init__(self) -> None:
        """Calls the superclass's init with values for name
        ('Swift Bike'), initial ('M'), min_speed (6), and max_speed(8)
        Args:
            self
        Return:
            none"""
        super().__init__(name = 'Swift Bike', initial = 'M', min_speed = 6, max_speed = 8)

    def slow(self, dist):
        """- overridden method - passes in distance to the next obstacle
        (if there is one). The motorcycle will move at 75% speed, rather than half.
        If there's an obstacle then it will go around it. There is no energy cost.
        Return a string that describes the event that occurred with the name of the
        motorcycle and the distance traveled (if applicable).
        Args:
            self
            dist
        Returns:
            a string that describes the event that occurred with the name of the
            motorcycle and the distance traveled (if applicable)
        """
        speed = random.randrange(int(self._min_speed * .75), int(self._max_speed * .75)) # needs to be changed

        went_around = False
        if speed >= dist:
            went_around = True
            
        self._position += speed

        return_str = self._name + " slowly "
        if went_around:
            return_str += "and safely moves around the obstacle "
        else:
            return_str += "moves "

        return_str += str(speed) + " units!"
            
        return return_str
    def description_string(self):
        """Returns a string with the motorcycle's stats and abilities
        Args:
            self
        Returns:
            a string with the motorcycle's stats and abilities
        """
        return f"{self._name} - a speedy motorcycle ({self._min_speed}-{self._max_speed} units). Special: Wheelie (2x speed but there's a chance you'll crash)." # needs to be changed
    def special_move(self, dist):
        """passes in distance to the next obstacle (if there is one). If there is
        sufficient energy (>= 15), deduct 15 energy, then there is a 75% chance that
        the motorcycle will move at 2x speed, otherwise it will crash and only move one
        space forward. If it was successful but there was obstacle, then it will crash and stops in
        the space just before it, otherwise it moves a randomized distance. Return a string that
        describes the event that occured with the name of the motorcycle and the distance
        traveled (if applicable).
        Args:
            self
            dist
        Returns:
            a string that describes the event that occurred with the name of the
            motorcycle and the distance traveled (if applicable)
        """
        if self.energy >= 15:
            self._energy -= 15
            chance = random.randint(0, 3)
            if chance == 0:
                speed = 1
                return f"{self._name} pops a wheelie and falls over!"
            else:
                speed = random.randint(self._min_speed, self._max_speed) * 2 # needs to be changed
            if speed < dist:
                self.position += int(speed)
                return f"{self._name} pops a wheelie and moves {int(speed)} units!"
            else:
                self.position = dist - 1
                return f"{self._name} CRASHES into an obstacle."
        else:
            return f"{self._name} doesn't have sufficient energy."