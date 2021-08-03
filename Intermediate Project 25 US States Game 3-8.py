"""
Project 25 - US States Game
This project is mainly around using Pandas to read in CSV data and then check answers against it.
"""

import turtle
import pandas as pd

data = pd.read_csv("Intermediate Project 25 -  50_states.csv")
states = data['state'].to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = './Intermediate Project 25 - blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []

# print(states.find("Texas"))

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"Guess the state {len(guessed_states)}/50",
                              prompt="What's another state's name?")

    if answer.lower() == 'exit':
        break
    if answer in states:
        t = turtle.Turtle()
        t.ht()
        t.penup()
        coords = data[data.state == answer]
        t.goto(int(coords.x), int(coords.y))
        t.write(answer)
        guessed_states.append(answer)

out_list = []
for state in states:
    if state not in guessed_states:
        out_list.append(state)

with open('missed_answers.txt', 'w') as file:
    for item in out_list:
        file.writelines(item+'\n')

screen.exitonclick()



