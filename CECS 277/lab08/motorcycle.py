""" Motorcycle for the racing game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self) -> None:
        """Calls the superclass's init with values for name
        ('Swift Bike'), initial ('M'), min_speed (6), and max_speed(8)
        Args:
            self
        Return:
            none"""
        super().__init__('Swift Bike', 'M', 6, 8)
        pass
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
        pass
    def description_string(self):
        """Returns a string with the motorcycle's stats and abilities
        Args:
            self
        Returns:
            a string with the motorcycle's stats and abilities
        """
        pass
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
        pass