""" Deadbolt Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
import random
import door


class DeadboltDoor(door.Door):
    """Represents a locked door that the user needs to find a key to unlock.
    """
    def __init__(self) -> None:
        self._bolt1 = bool(random.getrandbits(1))
        self._bolt2 = bool(random.getrandbits(1))

    def examine_door(self) -> str:
        return "A double deadbolt door. Both need to be unlocked to open the door, but you can't tell by looking at them if they're locked or unlocked."

    def menu_options(self) -> str:
        return "1. Toggle bolt 1\n2. Toggle bolt 2"

    def get_menu_max(self) -> int:
        return 2

    def attempt(self, option) -> str:
        self._input = option
        result_str = "You toggle the first bolt."
        if option == 2:
            result_str = "You toggle the second bolt."
        return result_str

    def is_unlocked(self) -> bool:
        return self._bolt1 and self._bolt2
    
    def clue(self) -> str: # needs to be checked for correctness
        result_str = "You jiggle the door..."
        if self._bolt1 or self._bolt2:
            return result_str + " it seems like one of the bolts is unlocked."
        else:
            return result_str + " it seems like it's completely locked."

    def success(self) -> str:
        return "You unlocked both deadbolts and opened the door."