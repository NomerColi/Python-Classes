""" Vehicle for the racing game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc
import random


class Vehicle(abc.ABC):
    """Represents a Vehicle.
    Attributes:
        _name (str): a name
        <get> _initial (str): an initial to display this vehicle in a lane
        _min_speed (int): the minimun speed
        _max_speed (int): the maximum speed
        <get> _position (int): the position
        <get> _energy (int): the energy
    """
    def __init__(self, name, initial, min_speed, max_speed) -> None:
        """Initiates attributes.
        Args:
            self (Vehicle) - the Vehicle instance being initiated
            initial (str): an initial for this vehicle
            min_speed (str): the minimum speed for this vehicle
            max_speed (str): the maximum speed for this vehicle
        Returns:
            none
        """
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed

        self._position = 0
        self._energy = 100

    def fast(self, dist) -> str:
        """Speeds up the Vehicle
        Args:
            self (Vehicle)
            dist (int): the distance to the next obstacle
        Returns:
            a string of the movement result
        """
        if self._energy >= 5:
            self._energy -= 5

            speed = random.randrange(self._min_speed, self._max_speed)

            crashed = False
            if speed >= dist:
                crashed = True
                speed = dist - 1
            
            self._position += speed

            return_str = self._name
            if crashed:
                return_str += " CRASHES into an obstacle!"
            else:
                return_str += " quickly moves " + str(speed)

            return return_str
        
    def slow(self, dist) -> str:
        """Slows down the Vehicle
        Args:
            self (Vehicle)
            dist (int): the distance to the next obstacle
        Returns:
            a string of the movement result
        """
        speed = random.randrange(self._min_speed // 2, self._max_speed // 2) # needs to be changed

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
    
    def __str__(self) -> str:
        return self._name + "[Position - " + str(self._position) + ", Energy - " + str(self._energy) + "]"

    @property
    def initial(self):
        return self._initial
    
    @property
    def position(self):
        return self._position
    
    @property
    def energy(self):
        return self._energy
    
    @abc.abstractmethod
    def description_string(self):
        """Returns a string with the vehicle's stats and abilities
        Args:
            self
        Returns:
            a string with the vehicle's stats and abilities
        """
        # 1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)
        pass
    @abc.abstractmethod
    def special_move(self, dist):
        """Vehicle's special move
        Args:
            self
            dist
        Returns:
            a string that describes the event that occured with the name of
            the vehicle and the distance traveled (if applicable)"""
        # Lightning Car uses nitro boost and moves 9 units!
        pass

