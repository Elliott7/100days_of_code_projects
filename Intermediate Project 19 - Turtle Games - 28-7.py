"""
Project Number Nineteen - Turtle Games
This contains both an Etch a sketch game and a turtle racing game.
It uses the turtle module and is ready to go with a creation of the specified class.
"""

from turtle import Turtle, Screen
import random


class EtchASketch:

    def __init__(self):
        self.timmy = Turtle()
        self.screen = Screen()
        self.listen_out()
        self.screen.exitonclick()

    def listen_out(self):
        self.screen.onkey(fun=self.move_forward, key='w')
        self.screen.onkey(self.move_backward, 's')
        self.screen.onkey(self.turn_left, 'a')
        self.screen.onkey(self.turn_right, 'd')
        self.screen.onkey(self.clear, 'c')
        self.screen.listen()

    def move_forward(self):
        self.timmy.forward(30)

    def move_backward(self):
        self.timmy.backward(30)

    def turn_left(self):
        self.timmy.left(11.25)

    def turn_right(self):
        self.timmy.right(11.25)

    def clear(self):
        self.timmy.penup()
        self.timmy.clear()
        self.timmy.home()
        self.timmy.pendown()


# etch_a_sketch = EtchASketch()

class Race:
    """Models a turtle race with 5 different options"""
    def __init__(self):
        self.list_turtles = []
        self.screen = Screen()
        self.screen.setup(height=400, width=500)
        self.get_bet()
        self.create_turts()
        self.locations()
        self.listen_out()
        self.starting_positions()
        self.screen.exitonclick()
        self.current_positions = []
        self.winner = None

    def listen_out(self):
        """Initiates the key listening to begin the race"""
        self.screen.onkey(self.start_race, 'space')
        self.screen.listen()

    def start_race(self):
        """Keeps the race running until the finish line has been reached"""
        while self.check():
            self.move_turtles()
        self.compare()

    def move_turtles(self):
        """Randomly moves the turtle forward"""
        for turt in self.list_turtles:
            self.locations()
            move_number = random.randint(1, 10)
            turt.forward(move_number)

    def starting_positions(self):
        """Sets the starting position for all of the turtles"""
        width = -80
        for turt in self.list_turtles:
            turt.penup()
            turt.setpos(-240, width)
            turt.pendown()
            width += 40

    def create_turts(self):
        """Creates the individual turtles and sets their attributes"""
        colour = ['red', 'blue', 'green', 'orange', 'black']
        for i in range(5):
            temp_turt = Turtle()
            temp_turt.shape('turtle')
            temp_turt.color(colour[i])
            self.list_turtles.append(temp_turt)

    def get_bet(self):
        """Gets the users bet"""
        self.user_bet = self.screen.textinput(title="Make your bet",
                                              prompt="Which turtle will win the race? Enter a color")

    def check(self):
        """Creates a boolean list of the current results, checks that the finish line has not been reached"""
        check_list = []
        for i in range(len(self.current_positions)):
            check_list.append(self.current_positions[i][0] <= 220)
        for x in range(len(check_list)):
            if check_list[x] is False:
                self.winner = x
        return all(check_list)

    def compare(self):
        """Compares the users bet with the actual winner"""
        if self.user_bet.lower() == self.list_turtles[self.winner].color()[0]:
            print(f"The winner is {self.list_turtles[self.winner].color()[0]}")
            print("Congratulations, you got it correct")
        else:
            print(f"The winner is {self.list_turtles[self.winner].color()[0]}")
            print(f"Unlucky, you selected {self.user_bet}")

    def locations(self):
        """Updates the current positions of the turtles"""
        location_list = []
        for turt in self.list_turtles:
            temp = turt.pos()
            location_list.append(temp)
        self.current_positions = location_list


race = Race()

