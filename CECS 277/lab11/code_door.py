""" Code Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import door


class CodeDoor(door.Door):
    """Represents a code door that the user can toggle each key.
    Attributes:
        _solution (char []): the solution of this Door
        _input (char []): the input
    """
    def __init__(self) -> None:
        """Initiates the solutions with a random char between 'O' and 'X'.
        Args:
            self (CodeDoor)
        Returns:
            none
        """
        self._solution = []
        for i in range(3):
            self._solution.append(random.choice(['O', 'X']))
        self._input = ['O', 'O', 'O']

    def examine_door(self) -> str:
        return "A door with a coded keypad with three characters. Each key toggles a value with an ‘X’ or an ‘O’."

    def menu_options(self) -> str:
        return "1. Press Key 1\n2. Press Key 2\n3. Press Key 3"

    def get_menu_max(self) -> int:
        return 3

    def attempt(self, option) -> str:
        # toggle the selected ley
        if self._input[option - 1] == 'O':
            self._input[option - 1] = 'X'
        else:
            self._input[option - 1] = 'O'

        result_str = "You toggled the "
        if option == 1:
            result_str += "first"
        elif option == 2:
            result_str += "second"
        elif option == 3:
            result_str += "third"
        result_str += " character.\n"
        
        result_str += str(self._input)

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
        corrent_num = 0
        corrections = []
        for i in range(3):
            correct = self._solution[i] == self._input[i]
            if correct:
                corrent_num += 1
            corrections.append(correct)

        # if there is no correct character
        if corrent_num == 0:
            return "Nothing is correct."

        return_str = "The "

        # if the first character is correct
        if corrections[0]:
            return_str += "first"

            if corrent_num == 2:
                return_str += " and "

        # if the second character is correct
        if corrections[1]:
            return_str += "second"

            if corrent_num == 2 and "and" not in return_str:
                return_str += " and "

        # if the third character is correct
        if corrections[2]:
            return_str += "third"

        return_str += " character is " if corrent_num == 1 else " characters are "
        return_str += "correct."

        return return_str

    def success(self) -> str:
        return "You entered the correct code and opened the door."