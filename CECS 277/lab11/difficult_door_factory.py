""" Difficult Door Factory for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
import door_factory
import random
import combo_door
import deadbolt_door
import code_door
class DifficultDoorFactory(door_factory.DoorFactory):
    """Randomly selects an easy door
    """
    def create_door(self):
        """Randomly chooses and returns a difficult door
        Args:
            self
        Returns:
            a difficult door
        """
        door = random.randint(1, 3)
        if door == 1:
            return combo_door.ComboDoor()
        elif door == 2:
            return deadbolt_door.DeadboltDoor()
        else:
            return code_door.CodeDoor()