"""
Project Number Five - Password Generator
This script asks the user for the length and complexity that they would like their password to be. It then returns
a randomized password that is selected from multiple lists of letters, symbols and numbers.
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_user_input():
    """
    Requests input from user - repeats until received.

    :return: num_letters, num_symbols, num_numbers
    """

    while True:
        try:
            num_letters = int(input("How many letters would you like in your password?\n"))
            num_symbols = int(input(f"How many symbols would you like?\n"))
            num_numbers = int(input(f"How many numbers would you like?\n"))
            break

        except ValueError:
            print("Please select a number that is either 0 or above")
    return num_letters, num_symbols, num_numbers


def generate_password(n_let, n_sym, n_num):
    """
    Generates a random password based off of user inputs and letter/symbol/number selection

    :param n_let:(int) Number of letters wanted in password
    :param n_sym:(int) Number of symbols wanted in password
    :param n_num:(int) Number of numbers wanted in password
    :return password: (str) Random password
    """
    password_list = []

    # Had multiple for loops, refactored down into a function
    def selection_loop(number_of_iters, category):
        for i in range(number_of_iters):
            select = random.randint(0, len(category) - 1)
            password_list.append(category[select])

    selection_loop(n_let, letters)
    selection_loop(n_sym, symbols)
    selection_loop(n_num, numbers)

    # Randomizes password
    password = ""
    for i in range(len(password_list)):
        select = random.randint(0, len(password_list)-1)
        password = password + password_list[select]
        password_list.pop(select)

    return password


def main():
    print("Welcome to the PyPassword Generator!")
    lets, syms, nums = get_user_input()
    new_password = generate_password(lets, syms, nums)
    print(f"Your new randomized password with {lets} letters, {syms} symbols "
          f"and {nums} numbers is :\n{new_password}")


if __name__ == "__main__":
    main()
