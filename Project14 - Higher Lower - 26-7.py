"""
Project Fourteen - The Higher or Lower game
Terminal rendition of the popular higher lower game. Shows several options to the user, gets their input and then
compares the results. If they are correct, the correct answer persists through to more comparison until they get
it wrong.
"""
import random
import os
import time
count = 0

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

logo = """
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/

"""

vs = """

 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

"""


"""
Plan / To do list
Retrieve a comparison option from the data (This needs to happen twice for the very first option
but then it only occurs for the second option second option)
Ask the user which person has a higher amount. Then compare the two entered values into that function to compare. If
the user gets it wrong then return a 0 and have the game end there. If the user gets it right return a 1 and then
have the correct answer saved as the comparison answer.
"""


def print_options(a, b):
    """
    Takes in a and b and then prints out the greeting.
    :param a: Option a
    :param b: Option b
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    if count != 0:
        print(f"You're right, Current score: {count}")

    print(logo, f"Compare: {a}", vs, f"Against: {b}")


def get_data(data_list):
    """
    Randomly selects some data from the dictionary and then returns it
    :param data_list: List containing all of the dictionaries containing all of the data
    :return name, follower_count, desc, country:
    """
    rand_num = random.randint(0, len(data_list)-1)
    selection = data_list[rand_num]
    name = selection["name"]
    follower_count = selection["follower_count"]
    desc = selection["description"]
    country = selection["country"]
    return name, follower_count, desc, country


def count_inc():
    """
    Increments the count by 1
    """
    return count + 1


def user_guess():
    """
    Gets the users answer and then returns it.
    :return either 0 or 1: This is to be used as a comparison
    """
    while True:
        user_answer = input(" Who has more followers? Type 'A' or 'B'\n ")
        if user_answer.lower() == 'a':
            return 0
        elif user_answer.lower() == 'b':
            return 1
        else:
            print("Please enter a valid response")


def compare_options(option1, option2, useranswer):
    """
    Takes in the current data and user response, then compares them and determines whether the user is correct
    Returns either True or False so the game can be continued or ended
    :param option1: Dict data from option 1
    :param option2: Dict data from option 2
    :param useranswer: Users response from the user_guess function
    :return True or False:
    """
    option1 = int(option1)
    option2 = int(option2)
    global count
    if useranswer == 0 and option1 > option2:
        count = count_inc()
        return 1
    elif useranswer == 1 and option2 > option1:
        count = count_inc()
        return 2
    else:
        print("That was the wrong answer. Game over")
        return False


def main():
    carry_through = None
    while True:
        time.sleep(1)
        if carry_through is None:
            a_name, a_follower_count, a_desc, a_country = get_data(data)
            a = f"{a_name}, a {a_desc}, from {a_country}"
        else:
            a_name, a_follower_count, a_desc, a_country = carry_through
            a = f"{a_name}, a {a_desc}, from {a_country}"

        b_name, b_follower_count, b_desc, b_country = get_data(data)
        b = f"{b_name}, a {b_desc}, from {b_country}"

        print_options(a, b)
        guess = user_guess()
        compare = compare_options(a_follower_count, b_follower_count, guess)

        if compare == 1:
            carry_through = [a_name, a_follower_count, a_desc, a_country]
            continue
        elif compare == 2:
            carry_through = [b_name, b_follower_count, b_desc, b_country]
            continue
        print(f"Your final score was {count}")
        break


if __name__ == "__main__":
    main()
