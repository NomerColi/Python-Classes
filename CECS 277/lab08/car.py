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
        """Calls the superclass's init with values for name
        ('Lightning Car'), initial ('C'), min_speed (6), and max_speed(8)
        Args:
            self
        Return:
            none"""
        super().__init__(name = 'Lightning Car', initial = 'C', min_speed = 6, max_speed = 8)
    def description_string(self):
        """Returns a string with the car's stats and abilities
        Args:
            self
        Returns:
            a string with the car's stats and abilities
        """
        return f"{self._name} - a fast car ({self._min_speed}-{self._max_speed} units). Special: Nitro Boost (1.5x speed)"

    def special_move(self, dist):
        """Passes in the distance to the next obstacle (if there is one).
        If there is sufficient energy (>= 15), deduct 15 energy and move the car at 1.5x
        speed. If there is an obstacle, then it will crash and stops in the space just before it,
        otherwise it moves the randomized distance. Return a string that describes the event that
        occured with the name of the car and the distance traveled (if applicable).
        Args:
            self
            dist
        Returns:
            a string that describes the event that occured with the name of the car
            and the distance traveled (if applicable)
        """
        if self.energy >= 15:
            self._energy -= 15
            speed = random.randint(self._min_speed, self._max_speed) * 1.5
            if speed < dist:
                self.position += int(speed)
                return f"{self._name} uses nitro boost and moves {int(speed)} units!"
            else:
                self.position = dist - 1
                return f"{self._name} CRASHES into an obstacle."
        else:
            return f"{self._name} doesn't have sufficient energy."