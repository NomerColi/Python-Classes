""" Easy Door Factory for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import door_factory
import random
import basic_door
import locked_door
import combo_door


class EasyDoorFactory(door_factory.DoorFactory):
    """Randomly creates an easy door.
    """
    def create_door(self):
        """Randomly chooses and returns an easy door
        Args:
            self
        Returns:
            a Door instance randomly chosen among easy ones
        """
        door = random.randint(1, 3)
        if door == 1:
            return basic_door.BasicDoor()
        elif door == 2:
            return locked_door.LockedDoor()
        else:
            return combo_door.ComboDoor()
        