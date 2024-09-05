"""
A basic game where you guess a number.

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import random
import check_input


def main():
    # Author: Yunjae Cho
    # Date: Aug 27 2024 10:20 AM
    # Description: Generates random number in a range from 1 to 100
    #              and prints game starting prompts
    rand_num = random.randint(1, 100)
    print("- Guessing Game -")
    num = check_input.get_int_range(
        "I'm thinking of a number.  Make a guess (1-100): ", 1, 100)
    count = 1

    # Author: Omar Juarez
    # Date: Aug 27 2024 10:40 AM
    # Description: Checks if the number is correct, too high, or too low.
    #              Tells the user to guess again if not correct
    #              and keeps count of how many tries.
    while rand_num != num:
        if num > rand_num:
            num = print("Too high!", end=" ")
        else:
            num = print("Too low!", end=" ")

        num = check_input.get_int_range("Guess again (1-100): ", 1, 100)
        count += 1

    print("Correct!   You got it in", count, "tries.")


main()
