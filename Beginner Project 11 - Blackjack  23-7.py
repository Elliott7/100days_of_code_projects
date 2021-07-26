"""
Project Number Eleven - This is the Blackjack Capstone project
This is the
"""
import random
import time

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |
      `------'                           |__/
"""

cards_count = {
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    8: True,
    9: True,
    10: True,
    "J": True,
    "Q": True,
    "K": True,
    "A": True
}


def create_cards():
    cards = {
        "hearts": cards_count.copy(),
        "diamonds": cards_count.copy(),
        "clubs": cards_count.copy(),
        "spades": cards_count.copy()}
    return cards


def card_selector(cards):
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    while True:
        suit_selector = suits[random.randint(0, 3)]
        num_selector = numbers[random.randint(0, 12)]

        if cards[suit_selector][num_selector]:
            cards[suit_selector][num_selector] = False
            return num_selector, suit_selector


def name_players():
    """
    Gets input from user and returns the number of players in the game
    """
    while True:
        try:
            players = int(input("How many players are there? \n"))
            if 5 >= players >= 1:
                break
            print("Please enter a valid number between 1 and 5")
        except ValueError:
            print("Please enter a valid number between 1 and 5")
    names = []
    for i in range(1, players+1):
        temp = input(f"Enter player {i}'s name\n")
        names.append(temp)
    return names


def compare():
    pass


def log_results(names):
    """
    Takes in the participants names and returns a dict for storing results

    :param names: Names of people participating
    :return results_dict: Base dictionary for data logging
    """
    names.append('Dealer')
    results_dict = {}
    for name in names:
        results_dict[name] = {
            'count': 0,
            'cards': [],
            'aces': [],
            'win': 'no'

        }
    return results_dict


def check_num(card_number):
    """
    Takes in the card number and checks whether it is an int or a str. If it's a string it returns the
    appropriate number

    :param card_number:
    :return:
    """
    try:
        return int(card_number)

    except ValueError:
        if card_number != "A":
            return 10
        else:
            return 1


def ace_check():

    pass


def ace_dict_inserter(one_or_eleven):
    """
    Checks the users input to see whether they would like to use their ace as a 1 or an 11
    :param one_or_eleven: User input
    :return: number
    """
    if one_or_eleven == '1':
        return 1
    else:
        return 11


def card_number(turn):
    if turn == 0:
        return 'first'
    else:
        return 'second'


def check_total(users_total):
    if users_total == 21:
        return None
    elif users_total > 21:
        print("You've bust")
        time.sleep(2)
        return None
    return True


def main():
    print(logo)
    players = name_players()
    while True:
        current_hand = log_results(players)
        cards = create_cards()
        # Round 1

        for deal_cards in range(2):
            for i in range(len(players)):
                card1num, card1suit = card_selector(cards)
                if not (deal_cards == 1 and players[i] is 'Dealer'):
                    print(f"{players[i]}, your {card_number(deal_cards)} card is the {card1num} of {card1suit} ")
                correct_type_num = check_num(card1num)
                time.sleep(2)

                if correct_type_num == 1 and players[i] != 'Dealer':
                    num = ace_dict_inserter(input('Would you like to use this Ace as a 1 or an 11?\n'))
                    current_hand[players[i]]['count'] += num
                    current_hand[players[i]]['cards'].append(f'The {card1num} of {card1suit}')
                    current_hand[players[i]]['aces'].append(f'The {card1num} of {card1suit} as {num}')

                elif correct_type_num == 1 and players[i] == 'Dealer':
                    current_hand[players[i]]['count'] += num
                else:
                    current_hand[players[i]]['count'] += int(correct_type_num)
                    current_hand[players[i]]['cards'].append(f'The {card1num} of {card1suit}')

        for name in current_hand:
            while True:
                if check_total(current_hand[name]['count']) is not True:
                    break

                if name == "Dealer":
                    print(f"The dealers second card is {current_hand[name]['cards'][1]}")
                    print(f"The dealer has total count of {current_hand[name]['count']}")
                    if current_hand[name]['count'] < 16:
                        card1num, card1suit = card_selector(cards)
                        correct_type_num = check_num(card1num)
                        print(f"The dealers third card is {card1num} of {card1suit}")
                        if correct_type_num == 1:
                            if current_hand[name]['count'] + 11 <= 21:
                                current_hand[name]['count'] += 11
                                print(f"The dealer has total count of {current_hand[name]['count']}")
                            else:
                                current_hand[name]['count'] += 1
                                print(f"The dealer has total count of {current_hand[name]['count']}")
                        else:
                            current_hand[name]['count'] += correct_type_num
                            print(f"The dealer has total count of {current_hand[name]['count']}")
                    break

                else:
                    another_card = input(f"{name} would you like another card? "
                                         f"Your current total is {current_hand[name]['count']} \n")
                    if another_card is 'y':
                        card1num, card1suit = card_selector(cards)
                        correct_type_num = check_num(card1num)
                        print(f"Your new card is the {card1num} of {card1suit}")
                        if correct_type_num == 1:
                            num = ace_dict_inserter(input('Would you like to use this Ace as a 1 or an 11?\n'))
                            current_hand[name]['count'] += num
                            current_hand[name]['cards'].append(f'The {card1num} of {card1suit}')
                            current_hand[name]['aces'].append(f'The {card1num} of {card1suit}')
                            print(f"Your new total is {current_hand[name]['count']}")
                        else:
                            current_hand[name]['count'] += int(correct_type_num)
                            current_hand[name]['cards'].append(f'The {card1num} of {card1suit}')
                            print(f"Your new total is {current_hand[name]['count']}")
                    else:
                        break
        winners = []
        for person in players:
            winners.append(current_hand[person]['count'])

        if current_hand['Dealer']['count'] == 21:
            print("The dealer wins")
        elif current_hand['Dealer']['count'] > 21:
            winners[-1] = 1
            print("The dealer went bust")

        my_list = []
        for i, num in enumerate(winners):
            if num > winners[-1] and num <= 21:
                my_list.append(players[i])

        if winners:
            print(f"The winners are {my_list}")
        else:
            print("The dealer wins")
        print(current_hand)
        if input('Type "y" to keep playing\n') == 'y':
            continue
        break

    pass


if __name__ == "__main__":
    main()


"""
Welcome logo
Ask how many players there are
Select a card and give it to a player
"""