""" Door for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import abc


class Door(abc.ABC):
    """Represents a Door
    """
    @abc.abstractmethod
    def examine_door(self) -> str:
        """Returns a string description of this Door.
        Args:
            self (Door) - the Door instance
        Returns:
            a string for description
        """
        pass

    @abc.abstractmethod
    def menu_options(self) -> str:
        """Returns a string with the menu options.
        Args:
            self (Door) - the Door instance
        Returns:
            a string with the menu options
        """
        pass

    @abc.abstractmethod
    def get_menu_max(self) -> int:
        """Returns the number of options in the above menu.
        Args:
            self (Door) - the Door instance
        Returns:
            an integer of the number
        """
        pass

    @abc.abstractmethod
    def attempt(self, option) -> str:
        """Passes in the user's menu selection.
        Args:
            self (Door) - the Door instance
            option (int): the selected option
        Returns:
            a string describing the user's attempt
        """
        pass

    @abc.abstractmethod
    def is_unlocked(self) -> bool:
        """Checks to see if the Door is unlocked.
        Args:
            self (Door) - the Door instance
        Returns:
            whether the Door is unlocked
        """
        pass

    @abc.abstractmethod
    def clue(self) -> str:
        """Returns a hint for the user.
        Args:
            self (Door) - the Door instance
        Returns:
            a string for the hint
        """
        pass

    @abc.abstractmethod
    def success(self) -> str:
        """Returns a congratulatory message.
        Args:
            self (Door) - the Door instance
        Returns:
            a string of the message
        """
        pass
    