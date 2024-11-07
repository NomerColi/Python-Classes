""" Locked Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import door


class LockedDoor(door.Door):
    """Represents a locked door that the user needs to find a key to unlock.
    """
    def __init__(self) -> None:
        self._solution = random.randint(1, 3)
        self._input = 0

    def examine_door(self) -> str:
        return "A locked door. Look around, the key is hidden nearby."

    def menu_options(self) -> str:
        return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock."

    def get_menu_max(self) -> int:
        return 3

    def attempt(self, option) -> str:
        self._input = option
        if option == 1:
            result_str = "You look under the doormat."
        elif option == 2:
            result_str = "You look under the flower pot."
        else:
            result_str = "You look under the fake rock."
        return result_str

    def is_unlocked(self) -> bool:
        return self._solution == self._input

    def clue(self) -> str:
        return "Look somewhere else."

    def success(self) -> str:
        return "You found the key and opened the door."