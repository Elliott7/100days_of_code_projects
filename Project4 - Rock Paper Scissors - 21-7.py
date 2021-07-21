"""
Project Number Four - Rock Paper Scissors.
Basic Rock Paper Scissors game.
"""



import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def your_choice():
    """
    Prompts the user for a number, prints the corresponding picture and returns the value for use in
    the calculate function.

    :return: user_input (int (0-2))
    """
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    while user_input >= 3 or user_input < 0:
        print("invalid response")
        user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_input == 0:
        print("You picked Rock", rock)
    elif user_input == 1:
        print("You picked Paper", paper)
    else:
        print("You picked Scissors", scissors)
    return user_input


def computer_roll():
    """
    Gets a random int and prints the associated picture, returns roll value for calculation.

    :return: roll (int(0-2))
    """
    roll = random.randint(0, 2)
    if roll == 0:
        print("Computer picked Rock", rock)
    elif roll == 1:
        print("Computer picked Paper", paper)
    else:
        print("Computer picked Scissors", scissors)
    return roll


def calculate(user, computer):
    """
    Takes in both the user answer and computer answer, calculates who the winner is, prints that result and returns
    either -1, 0 or 1 to be used in score calculation.

    :param user: int
    :param computer: int
    :return: None
    """
    if user == computer:
        print("It's a tie")
        return 0
    elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
        print("You lose! HA")
        return -1
    else:
        print("You win! Goodjob")
        return 1


def times_to_play():
    return input("How many times would you like to play?\n")


def main():

    rounds = int(times_to_play())
    your_score = comp_score = 0

    for i in range(rounds):
        answer = your_choice()
        computer_answer = computer_roll()
        calc = calculate(answer, computer_answer)
        if calc == 1:
            your_score += 1
        elif calc == -1:
            comp_score += 1
        print(f"Your score is {your_score}.\nThe computers score is {comp_score}")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()

