""" Car for the racing game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

from vehicle import Vehicle
import random


class Car(Vehicle):
    """Represents a Car
    Attributes:
        
    """
    def __init__(self) -> None:
        """Calls the superclass's init with values for
        name ('Lightning Car'), initial ('C'), min_speed (6), and max_speed (8)
        Args:
            self (Car)
        Return:
            none
        """
        super().__init__(name = 'Lightning Car', initial = 'C', min_speed = 6, max_speed = 8)
    def description_string(self):
        """Returns a string with the Car's stats and abilities
        Args:
            self (Car)
        Returns:
            a string with the Car's stats and abilities
        """
        return f"{self._name} - a fast Car ({self._min_speed}-{self._max_speed} units). Special: Nitro Boost (1.5x speed)"

    def special_move(self, dist: int):
        """Moves the Car with 1.5x speed using 15 energy.
        Args:
            self (Car)
            dist (int): the distance to the next obstacle
        Returns:
            a string that describes the event that occured with the name of the Car
            and the distance traveled (if applicable)
        """
        if self.energy >= 15:
            self._energy -= 15

            speed = random.randint(int(self._min_speed * 1.5), int(self._max_speed * 1.5))

            # if the Car crashes into an obstacle
            crashed = False
            if speed > dist:
                crashed = True
                # moves the car right up to the obstacle
                speed = dist - 1

            self._position += speed

            if crashed:
                return f"{self._name} CRASHES into an obstacle."
            else:
                return f"{self._name} uses nitro boost and moves {speed} units!"
        else:
            return f"{self._name} doesn't have sufficient energy."