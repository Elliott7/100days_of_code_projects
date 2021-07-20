"""
Band name generator.
This is the first challenge from the 100 days of python bootcamp.
Very basic program to recommend a band name based off of your hometown and pets name.
"""

if __name__ == "__main__":
    print("Welcome to the Band Name Generator.")
    city_name = input("What's the name of the city you grew up in?\n")
    pets_name = input("What's your pet's name?\n")
    print(f"Your band name could be {city_name.title()} {pets_name.title()}")