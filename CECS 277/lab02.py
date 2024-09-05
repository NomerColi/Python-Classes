"""
A rock paper scissors game against the computer.

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import check_input


def weapon_menu():
    """Repeatedly takes in and validates user's input to ensure that it is a weapon.
    Args:
        none
    Returns:
        The valid RPS input.
    """
    val = ''
    valid = False
    while not valid:
        val = input("Choose a weapon:\nR. Rock\nP. Paper\nS. Scissors\nB. Back\n").upper()
        # when the input is only one length and one of the options
        if len(val) == 1 and val in "RPSB":
            valid = True
        else:
            print("Invalid input - should be R, P, S, or B.")
    return val


def comp_weapon():
    """Randomly chooses a weapon of the computer.
    Args:
        none
    Returns:
        The random weapon of the computer.
    """
    weapons = "RPS"
    # randomly choose R, P, or S
    rand_weapon = weapons[random.randint(0, 2)]
    return rand_weapon


def find_winner(player, comp):
    """Compares the two weapons and displays the result.
    Args:
        player: the weapon of the player
        comp: the weapon of the computer
    Returns:
        Who is the winner.
    """
    winner = 0
    player_weapon_name = ""
    comp_weapon_name = ""

    # player chose rock
    if player == "R":
        player_weapon_name = "Rock"
        if player == comp:  # tie
            winner = 0
            comp_weapon_name = player_weapon_name
        elif comp == "P":  # computer chose paper
            winner = 2
            comp_weapon_name = "Paper"
        else:  # computer chose scissors
            winner = 1
            comp_weapon_name = "Scissors"
    # player chose scissors
    elif player == "S":
        player_weapon_name = "Scissors"
        if player == comp:  # tie
            winner = 0
            comp_weapon_name = player_weapon_name
        elif comp == "R":  # computer chose rock
            winner = 2
            comp_weapon_name = "Rock"
        else:  # computer chose paper
            winner = 1
            comp_weapon_name = "Paper"
    # player  chose paper
    elif player == "P":
        player_weapon_name = "Paper"
        if player == comp:  # tie
            winner = 0
            comp_weapon_name = player_weapon_name
        elif comp == "S":  # computer chose scissors
            winner = 2
            comp_weapon_name = "Scissors"
        else:  # computer chose rock
            winner = 1
            comp_weapon_name = "Rock"

    print(f"You chose {player_weapon_name}")
    print(f"Computer chose {comp_weapon_name}")

    result_text = "Tie"
    if winner == 1:
        result_text = "Player wins"
    elif winner == 2:
        result_text = "Computer wins"
    print(result_text)

    return winner


def display_scores(player, comp):
    """Displays the score.
    Args:
        player: the score of the player
        comp: the score of the computer
    Returns:
        none
    """
    print("Player =", player)
    print("Computer =", comp)


def main():
    # initializes win count tallies for player and computer
    player_win_count = 0
    comp_win_count = 0
    end = False
    # main menu loop
    while end is False:
        print("RPS Menu:\n1. Play game\n2. Show Score\n3. Quit")
        menu = check_input.get_int_range("", 1, 3)
        # player chose to play a RPS game
        if menu == 1:
            back = False
            # RPS game loop
            while back is False:
                player = weapon_menu()
                # if player presses 'B', the program goes back to the main menu
                if player == 'B':
                    back = True
                    continue
                comp = comp_weapon()
                winner = find_winner(player, comp)
                if winner == 1:
                    player_win_count += 1
                elif winner == 2:
                    comp_win_count += 1
        # player chose to display scores
        elif menu == 2:
            display_scores(player_win_count, comp_win_count)
        # player chose to quit
        elif menu == 3:
            print("Final Score:")
            display_scores(player_win_count, comp_win_count)
            end = True


main()
