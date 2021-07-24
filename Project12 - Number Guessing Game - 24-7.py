"""
Project Number Twelve - Number Guessing Game
This game prompts the user for the difficulty of the game they would like to play, then proceeds to ask them for input
and compares it to the current grand_number
"""


import random
import os


def get_grand_number():
    """
    Returns a random number between 1 and 100
    This is the computers number that the users responses will be compared against
    """
    return random.randint(1, 100)


def get_user_difficulty():
    """
    Prompts the user for the difficult they would like to use. Returns a number that is then fed into the
    repetitions function
    :return 10 or 5:
    """
    while True:
        response = input("Choose a difficulty. Type 'easy' or 'hard'")
        if response.lower() == 'easy':
            return 10
        elif response.lower() == 'hard':
            return 5
        else:
            continue


def number_of_repetitions(repetitions, function, grand_number):
    """
    Takes a number (repetitions) and runs the function that many times
    :param repetitions: Number of times the function should be repeated
    :param function: Function to be repeated
    :return: Null
    """
    for i in range(repetitions, 0, -1):
        if not function(grand_number, i):
            continue
        else:
            break


def guess(grand_number, user_count):
    """
    Gets the users guess and compares it to the current number. Prints higher, lower or correct.
    :return:
    """
    counter(user_count)
    user_guess = int(input("Make a guess\n"))
    if user_guess == grand_number:
        print("You are correct! Congratulations")
        return True
    elif user_guess > grand_number:
        print('You have guessed too high.')
        return False
    else:
        print("You have guessed too low.")
        return False


def counter(number_of_turns):
    """
    Tracks the users turns and prints out the number
    """
    if number_of_turns == 10 or number_of_turns == 5:
        print(f"You have {number_of_turns} turns")
    elif number_of_turns == 1:
        print("Last turn")
    else:
        print(f"You have {number_of_turns} turns remaining")


def main():
    while True:
        print("Welcome to the Number Guessing Game.\nI'm thinking of a number between 1 and 100.")
        the_grand_number = get_grand_number()
        difficulty = get_user_difficulty()
        number_of_repetitions(difficulty, guess, the_grand_number)
        if input("Would you like to play again? Enter 'y' or 'n'\n") == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        break


if __name__ == "__main__":
    main()
