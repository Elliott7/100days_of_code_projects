"""
Project Number Nine - The Silent Auction
Gets a name and a bid from each user, then returns the highest key:value pair
"""
import os


def introduction():
    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\  ''')
    print("Welcome to the secret auction program")


def calculate(users):
    """
    Gets users name and bid, then updates the users dictionary and returns it
    :param users: dictionary of names and bids
    :return users: updated dictionary
    """
    get_name = input("What's your name?\n")
    while users.get(get_name):
        print("Name already used, try again")
        get_name = input("What's your name?\n")

    while True:
        try:
            get_bid = int(input("What's your bid?"))
            break
        except ValueError:
            print("Please enter a valid number")

    users[get_name] = get_bid
    return users


def main():
    introduction()
    users = {}
    while True:
        calculate(users)
        more = input("Are there any other bidders? Type 'Y' or 'N'")
        if more.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif more.lower() == 'n':
            break
        else:
            print(f"Your response {more} has been classed as 'N'")
            break

    max_bidder = max(users, key=lambda x: users[x])
    print(f"The highest bidder is {max_bidder} with a bid of {users[max_bidder]}")


if __name__ == "__main__":
    main()
