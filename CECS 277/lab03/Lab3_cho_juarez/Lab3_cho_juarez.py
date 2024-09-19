"""
A hangman game where the user has to guess a 5-letter word.

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import check_input
from dictionary import words
import random


def display_gallows(num_incorrect):
    """Display the hangman on the gallows.
    Args:
        an integer for the number of incorrect guesses.
    Returns:
        none
    """
    gallows = "========\n||/   | \n||      \n||      \n||      \n||      "
    hangman_parts = ['○', '|', '/', "\\", "\\", '/']
    column_count = 9
    hangman_part_index = [2*column_count + 6, 3*column_count + 6, 4*column_count + 5, 4*column_count + 7, 2*column_count + 5, 2*column_count + 7]
    # as many as the number of incorrect guesses, place the hangman parts in the gallows
    for i in range(num_incorrect):
        idx = hangman_part_index[i]
        # replace a space with a hangman part
        gallows = gallows[:idx] + hangman_parts[i] + gallows[idx + 1:]
    print(gallows)


def display_letters(letters):
    """Display the letters with space between each character.
    Args:
        a string list of letters.
    Returns:
        none
    """
    s = ""
    for l in letters:
        s += l + ' '
    print(s)


def get_letters_remaining(incorrect, correct):
    """Shows the user which letters are remaining.
    Args:
        string lists of each incorrect guesses and correct guesses.
    Returns:
        the string list of remaining letters.
    """
    letters = []
    for i in range(ord('A'), ord('Z')+1):
        c = chr(i)
        if c not in incorrect and c not in correct:
            letters.append(c)

    return letters


def main():
    play = True
    while play is True:
        # gets a random word, then saves it as a string and a list
        random_word = random.choice(words)
        random_word_list = [x for x in random_word]
        # print(random_word_list) # should be deleted or commented later
        print("-Hangman-")
        # initializes lists and variables we'll be needing
        remaining_selection_list = []
        correct_selection_list = []
        incorrect_selection_list = []
        correct_selection_count = 0
        incorrect_selection_count = 0
        result = 0

        while True:
            # only when the player did not win
            if result != 1:
                print("\nIncorrect selections: ", end='')
                display_letters(incorrect_selection_list)
            display_gallows(incorrect_selection_count)
            print()
            # only when the player did not win
            if result != 1:
                # displays the current progress
                for i in random_word_list:
                    s = i
                    if i in correct_selection_list:
                        s = i
                    # if the character is not corrent, prints '_' instead
                    else:
                        s = '_'
                    print(s, end=' ')
                print()
                # gets the remaining selecting list and displays it
                remaining_selection_list = get_letters_remaining(incorrect_selection_list, correct_selection_list)
                print("\nLetters remaining: ", end='')
                display_letters(remaining_selection_list)
                print("")
            # displays if the player wins or loses
            if result != 0:
                if result == -1:
                    print("You lose!")
                    print("The word was " + random_word + " !")
                else:
                    display_letters(random_word_list)
                    print("\nYou win!")
                #prompts user to play again at end of round
                play = check_input.get_yes_no("Play again(Y/N)? ")
                print()
                break

            # gets a letter input and either proceed or go back depending on the validity of the input
            letter_guess = ''
            letter_guess = input("Enter a letter: ").upper()
            # when the length of the letter is not 1 or not an alphabet
            if len(letter_guess) != 1 or ord(letter_guess) not in range(ord('A'), ord('Z') + 1):
                print("This is not a letter")
                continue
            # when the letter has been already used
            elif letter_guess not in remaining_selection_list:
                print("You have already used that letter.")
                continue
            # removes letter given by the user from the remaining selection
            remaining_selection_list.remove(letter_guess)
        
            correct_character_num = random_word_list.count(letter_guess)
            # displays the correct amount of times the letter shows up in the word
            if correct_character_num > 0:
                print("Correct!")
                correct_selection_list.append(letter_guess)
                correct_selection_count += correct_character_num
            else:
                print("Incorrect!")
                incorrect_selection_list.append(letter_guess)
                incorrect_selection_count += 1

            # if correct selection count is 5, player wins
            # if incorrect selection count is 6, player loses
            result = 0
            if correct_selection_count == 5:
                result = 1
            elif incorrect_selection_count == 6:
                result = -1


main()