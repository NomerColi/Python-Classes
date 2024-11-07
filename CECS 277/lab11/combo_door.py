""" Combo Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import door


class ComboDoor(door.Door):
    """Represents a combo door that the user can spin the dial of.
    Attributes:
        _solution (int): the solution of this Door
        _input (int): the input
    """
    def __init__(self) -> None:
        """Initiates the solution with a random value between 1 and 10.
        Args:
            self (ComboDoor)
        Returns:
            none
        """
        self._solution = random.randint(1, 10)
        self._input = 0

    def examine_door(self) -> str:
        return "A door with a combination lock. You can spin the dial to a number 1- 10."

    def menu_options(self) -> str:
        return "Enter # 1-10: "

    def get_menu_max(self) -> int:
        return 10

    def attempt(self, option) -> str:
        self._input = option
        
        return "You turn the dial to... " + str(option)

    def is_unlocked(self) -> bool:
        return self._solution == self._input

    def clue(self) -> str:
        return_str = "Try a lower value"
        if self._solution > self._input:
            return_str = "Try a higher value"

        return return_str

    def success(self) -> str:
        return "You found the correct value and opened the door."