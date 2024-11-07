""" Door Factory for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc


class DoorFactory(abc.ABC):
    """Represents a door factory
    """
    @abc.abstractmethod
    def create_door(self):
        """Creates a door
        """
        pass
