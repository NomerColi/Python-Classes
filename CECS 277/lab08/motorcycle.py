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
            self (Motorcycle)
        Return:
            none
        """
        super().__init__(name = 'Swift Bike', initial = 'M', min_speed = 6, max_speed = 8)

    def slow(self, dist):
        """Slows down the Motorcycle to 75%
        Args:
            self (Motorcycle)
            dist (int): the distance to the next obstacle
        Returns:
            a string that describes the event that occurred with the name of the
            Motorcycle and the distance traveled (if applicable)
        """
        speed = random.randint(int(self._min_speed * .75), int(self._max_speed * .75)) # needs to be changed

        # if the Motorcycle goes around an obstacle
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
        """Returns a string with the Motorcycle's stats and abilities
        Args:
            self (Motorcycle)
        Returns:
            a string with the Motorcycle's stats and abilities
        """
        return f"{self._name} - a speedy Motorcycle ({self._min_speed}-{self._max_speed} units). Special: Wheelie (2x speed but there's a chance you'll crash)." # needs to be changed
    def special_move(self, dist):
        """Moves the Motorcycle with 2x speed using 15 energy.
        However, the Motorcycle could fall over by 25%
        Args:
            self (Motorcycle)
            dist (int): the distance to the next obstacle
        Returns:
            a string that describes the event that occurred with the name of the
            Motorcycle and the distance traveled (if applicable)
        """
        if self.energy >= 15:
            self._energy -= 15

            chance = random.randint(0, 3)
            # if the Motorcycle falls over
            if chance == 0:
                speed = 1
                return f"{self._name} pops a wheelie and falls over!"
            # if the Motorcycle speeds up well
            else:
                speed = random.randint(self._min_speed * 2, self._max_speed * 2)

            # if the Motorcycle crashes into an obstacle
            crashed = False
            if speed >= dist:
                crashed = True
                # moves the Motorcycle right up to the obstacle
                speed = dist - 1

            self._position += speed

            if crashed:
                return f"{self._name} CRASHES into an obstacle."
            else:
                return f"{self._name} pops a wheelie and moves {speed} units!"
        else:
            return f"{self._name} doesn't have sufficient energy."