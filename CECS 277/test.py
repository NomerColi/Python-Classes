"""
A basic game where you guess a number.

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
        if val in ['R', 'P', 'S', 'B']:
            valid = True
        else:
            print("Invalid input - should be R, P, S, or B.")
    return val

def comp_weapon():
    """Randomly chooses a weapon of the computer
    Args:
        none
    Returns:
        The random weapon of the computer.
    """
    weapons = ['R', 'P', 'S']
    rand_weapon = weapons[random.randint(0, 2)]
    return rand_weapon

def find_winner(player, comp):
    """Compare the two weapons and display the result
    Args:
        player: the weapon of the player
        comp: the weapon of the computer
    Returns:
        Who is the winner
    """
    
    print(f"You chose {player}")
    print(f"Computer chose {comp}")
    
    weapons: str = "RPS"
    player_weapon_idx = weapons.index(player)
    comp_weapon_idx = weapons.index(comp)

    winner = 0
    dif = player_weapon_idx - comp_weapon_idx
    if abs(dif) == 1:
        winner = 1 if dif > 0 else 2
    elif abs(dif) == 2:
        winner = 2 if dif > 0 else 1

    if winner == 0:
        print("Tie")
    elif winner == 1:
        print("Player wins")
    elif winner == 2:
        print("Computer Wins")

    return winner

def display_scores(player, comp):
    """Displays the score
    Args:
        player: the score of the player
        comp: the score of the computer
    Returns:
        none
    """
    print("Player =", player)
    print("Computer =", comp)

def main():

    end = False
    while end == False:
        print("RPS Menu:\n1. Play game\n2. Show Score\n3. Quit")
        menu = check_input.get_int_range("", 1, 3)
        player_win_count = 0
        comp_win_count = 0

        if menu == 1:
            back = False
            while back == False:
                player = weapon_menu()
                if player == 'B':
                    back = True
                    continue
                comp = comp_weapon()
                winner = find_winner(player, comp)
                if winner == 1:
                    player_win_count += 1
                elif winner == 2:
                    comp_win_count += 1
        elif menu == 2:
            display_scores(player_win_count, comp_win_count)
        elif menu == 3:
            print("Final Score:")
            display_scores(player_win_count, comp_win_count)
            end = True


main()
