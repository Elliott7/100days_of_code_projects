"""
Project Twenty Six - NATO Project
This project takes an input and then using dictionary/list comprehensions returns the
appropriate NATO code of the letter
"""
import pandas as pd

nato_input = pd.read_csv("./nato_phonetic_alphabet.csv")

my_dict = nato_input.to_dict('records')

x = {item['letter']: item['code'] for item in my_dict}

get_input = input("Name: \n")

y = [x[code.upper()] for code in get_input]

print(y)

# Different ways to do dictionary comprehension
# new_dict = {new_key:new_value for item in list}
#
# # creating a new dict based on the values in an existing dict
# new_dict = {new_key:new_value for (key, value) in mydict.items()}
#
# new_dict = {new_key:new_value for (key, value) in mydict.items() if test}

