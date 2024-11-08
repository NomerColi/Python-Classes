""" Deadbolt Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
import random
import door


class DeadboltDoor(door.Door):
    """Represents a deadbolt door that the user needs toggle the keys to unlock.
    Attributes:
        _bolt1 (bool): represents if first bolt is locked or unlocked
        _bolt2 (bool): represents if second bolt is locked or unlocked
    """
    def __init__(self) -> None:
        """Initiates whether the bolts are locked or unlocked.
        Args:
            self (DeadboltDoor)
        Returns:
            none
        """
        self._bolt1 = random.randint(0, 1)
        self._bolt2 = random.randint(0, 1)

    def examine_door(self) -> str:
        return "A double deadbolt door. Both need to be unlocked to open the door, but you can't tell by looking at them if they're locked or unlocked."

    def menu_options(self) -> str:
        return "1. Toggle bolt 1\n2. Toggle bolt 2"

    def get_menu_max(self) -> int:
        return 2

    def attempt(self, option) -> str:
        if option == 1:
            self._bolt1 = 1 - self._bolt1
            result_str = "You toggle the first bolt."
        else:
            self._bolt2 = 1 - self._bolt2
            result_str = "You toggle the second bolt."
        return result_str

    def is_unlocked(self) -> bool:
        return self._bolt1 == 1 and self._bolt2 == 1
    
    def clue(self) -> str:
        """Displays clue for the user.
        Args:
            self
        Returns:
            Description string describing the hint.
        """
        result_str = "You jiggle the door..."
        if self._bolt1 == 1 or self._bolt2 == 1:
            return result_str + " it seems like one of the bolts is unlocked."
        else:
            return result_str + " it seems like it's completely locked."

    def success(self) -> str:
        return "You unlocked both deadbolts and opened the door."