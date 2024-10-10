""" Player for the Yahtzee Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import die


class Player:
    """Represents a Player.
    Attributes:
        _dice (Die []): a list of 3 Die objects
        _points (int): the point of the Player
    """
    def __init__(self):
        """Instantiates 3 dies and set the point to 0.
        Args:
            self (Player) - the Player instance being initialized
        Returns:
            none
        """
        self._dice = [die.Die(), die.Die(), die.Die()]
        self._points = 0

    def get_points(self):
        """Returns the Player's points.
        Args:
            self (Player) - the Player instance to get the points from
        Returns:
            an integer for the points.
        """
        return self._points

    def roll_dice(self):
        """Calls roll on each of the Die objects in the dice list and sorts the list.
        Args:
            self (Player) - the Player instance whose dies are being rolled
        Returns:
            none
        """
        for d in self._dice:
            d.roll()
        self._dice.sort()

    def has_pair(self):
        """Returns true if two dice in the list have the same values (uses ==).
        Increments points by 1.
        Args:
            self (Player) - the Player instance to check if the Player has a pair
        Returns:
            a boolean whether the Player has a pair.
        """
        if self._dice[0] == self._dice[1] or self._dice[0] == self._dice[2] or self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False

    def has_three_of_a_kind(self):
        """Returns true if all three dice in the list have the same value (uses ==).
        Increments points by 3.
        Args:
            self (Player) - the Player instance to check if the Player has three of a kind
        Returns:
            a boolean whether the Player has three of a kind.
        """
        if self._dice[0] == self._dice[1] and self._dice[0] == self._dice[2]:
            self._points += 3
            return True
        return False

    def has_series(self):
        """Returns true if the values of each of the dice in the list are a sequence (uses -).
        Increments points by 2.
        Args:
            self (Player) - the Player instance to check if the Player has series
        Returns:
            a boolean whether the Player has series.
        """
        if self._dice[2] - self._dice[1] == 1 and self._dice[1] - self._dice[0] == 1:
            self._points += 2
            return True
        return False

    def __str__(self):
        """Returns a string in the format: 'D1 = 2, D2 = 4, D3 = 6'.
        Args:
            self (Player) - the Player instance to get a string representation for
        Returns:
            a string representing the Player to print.
        """
        s = ""
        for i, d in enumerate(self._dice):
            s += "D" + str(i + 1) + "= " + str(d)
            if i != len(self._dice) - 1:
                s += ", "
        return s