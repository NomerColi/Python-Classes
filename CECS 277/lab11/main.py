""" Difficult Door Factory for Escape Room

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import check_input
import door
import easy_door_factory
import difficult_door_factory

def open_door(door: door.Door):
    """Makes the user open a door.
    Args:
        door (Door): a Door instance the user will try opening
    Returns:
        none
    """
    print(door.examine_door())

    unlocked = False
    while not unlocked:
        selection = check_input.get_int_range(door.menu_options() + "\nEnter choice: ", 1, door.get_menu_max())
        print(door.attempt(selection))
        unlocked = door.is_unlocked()
        if not unlocked:
            print(door.clue())
        else:
            print(door.success())

def main():
    print("Welcome to the Escape Room.")
    print("You must unlock 3 doors to escape...")
    difficulty_selection = check_input.get_int_range("Enter Difficulty (1. Easy 2. Hard): ", 1, 2)

    # construct a factory by the difficulty the user selected
    fact = easy_door_factory.EasyDoorFactory()
    if difficulty_selection == 2:
        fact = difficult_door_factory.DifficultDoorFactory()

    # the user has to open 3 doors
    for i in range(3):
        print()
        door = fact.create_door()
        open_door(door)

    print("\nCongratulations! You escaped...this time.")

main()
