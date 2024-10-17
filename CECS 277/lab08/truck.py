""" Truck for the racing game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
from vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self) -> None:
        """calls the superclass’s init with values for name ('Behemoth Truck'),
        initial ('T'), min_speed (4), and max_speed (8).
        Args:
            self
        Returns:
            none"""
        super().__init__('Behemoth Truck', 'T', 4, 8)
        pass
    def description_string(self):
        """Returns a string with the truck's stats and abilities.
        Args:
            self
        Returns:
            a string with the truck's stats and abilities.
        """
        pass
    def special_move(self, dist):
        """passes in the distance to the next obstacle (if there is one). If there is sufficient 
        energy (>= 15), deduct 15 energy and move the truck 2x speed, even if there is an obstacle
        ('ram' bashes through the obstacle). Return a string that describes the event that occurred
        with the name of the truck and the distance traveled(if applicable).
        Args:
            self
            dist
        Returns:
            a string that describes the event that occured with the name of the truck and the
            distance traveled (if applicable).
        """
        pass