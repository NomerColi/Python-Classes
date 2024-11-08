""" Basic Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import door


class BasicDoor(door.Door):
    """Represents a basic door that the user can either push or pull.
    Attributes:
        _solution (int): the solution of this Door
        _input (int): the input
    """
    def __init__(self) -> None:
        """Initiates the solution with a random value between 0 and 1.
        Args:
            self (BasicDoor)
        Returns:
            none
        """
        self._solution = random.randint(1, 2)
        self._input = 0

    def examine_door(self) -> str:
        return "A basic door. You can either push or pull it to open."

    def menu_options(self) -> str:
        return "1. Push\n2. Pull"

    def get_menu_max(self) -> int:
        return 2

    def attempt(self, option) -> str:
        self._input = option

        result_str = "You push the door."
        if option == 2:
            result_str = "You pull the door"
        
        return result_str

    def is_unlocked(self) -> bool:
        return self._solution == self._input

    def clue(self) -> str:
        """Displays clue for the user.
        Args:
            self
        Returns:
            Description string describing the hint.
        """
        return "Try the other way."

    def success(self) -> str:
        return "Congratulations, you opened the door."