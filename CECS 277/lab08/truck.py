""" Truck for the racing game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from vehicle import Vehicle
import random


class Truck(Vehicle):
    def __init__(self) -> None:
        """calls the superclass’s init with values for name ('Behemoth Truck'),
        initial ('T'), min_speed (4), and max_speed (8).
        Args:
            self (Truck)
        Returns:
            none
        """
        super().__init__(name = 'Behemoth Truck', initial = 'T', min_speed = 4, max_speed = 8)
    def description_string(self):
        """Returns a string with the truck's stats and abilities.
        Args:
            self (Truck)
        Returns:
            a string with the truck's stats and abilities.
        """
        return f"{self._name} - a heavy truck ({self._min_speed}-{self._max_speed} units). Special: Ram (2x speed and it smashes through obstacles.)"
    
    def special_move(self, dist):
        """Makes the Truck bash through obstacles with 2x speed using 15 energy.
        Args:
            self (Truck)
            dist (int): the distance to the next obstacle
        Returns:
            a string that describes the event that occurred with the name of the
            Truck and the distance traveled (if applicable)
        """
        if self.energy >= 15:
            self._energy -= 15

            speed = random.randint(self._min_speed * 2, self._max_speed * 2)
            self._position += speed

            if speed < dist:
                return f"{self._name} rams forward and moves {speed} units!"
            else:
                return f"{self._name} rams forward bashing through the Obstacle to go {speed} units!"
        else:
            return f"{self._name} doesn't have sufficient energy."