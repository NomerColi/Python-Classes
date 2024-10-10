""" A Yahtzee game that awards the user points for a pair, three-of-a-kind, or a series

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import check_input
import player


def take_turn(player: player.Player):
    """Operates a turn for the player.
    Arguments:
        player (Player): a Player instance playing the game
    Return:
        none
    """
    player.roll_dice()
    print(player)

    # check if the Player earns any point
    if player.has_series():
        print("You got a series of 3!")
    elif player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_pair():
        print("You got a pair!")
    else:
        print("Aww.  Too Bad.")
    
    print("Score = " + str(player.get_points()))


def main():
    print("-Yahtzee-")

    user = player.Player()

    play = True
    while play is True:
        take_turn(user)
        play = check_input.get_yes_no("Play again? (Y/N): ")
        print()

    print("Game Over.")
    print("Final Score = " + str(user.get_points()))


main()