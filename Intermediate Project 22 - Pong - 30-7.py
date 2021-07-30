"""
Project Number TwentyTwo - Pong game
This was an interesting and challenging project, the final product works as intended and was enjoyable to make.
"""

from turtle import Turtle, Screen
import random
import time

TIME_DELAY = 0.03


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        # self.center()
        self.normal_stats()
        self.starting_direction()
        self.current_direction = 'left'

    def normal_stats(self):
        self.shape('circle')
        self.color('red')
        self.shapesize(1, 1)

    def starting_direction(self):
        self.home()
        direction1 = random.randint(-75, 75)
        direction2 = random.randint(105, 255)
        selection = random.choice((direction1, direction2))
        self.setheading(selection)
        if selection == direction1:
            self.current_direction = 'right'
        self.speed(0)
        self.change_direction()

    def change_direction(self):
        if self.ycor() >= 280 and self.current_direction == 'left':
            difference = 270 - (self.heading() - 85)
            self.setheading(difference)
            self.forward(10)

        elif self.ycor() >= 280 and self.current_direction == 'right':
            difference = 90 - (self.heading() + 85)
            self.setheading(difference)
            self.forward(10)

        elif self.ycor() <= -280 and self.current_direction == 'left':
            difference = 95 + (270 - self.heading())
            self.setheading(difference)
            self.forward(10)

        elif self.ycor() <= -280 and self.current_direction == 'right':
            difference = 95 - (self.heading() - 270)
            self.setheading(difference)
            self.forward(10)

    def center(self):
        self.color('white')
        self.home()
        self.shapesize(0.01, 0.01)

    def score(self, left_score, right_score):
        if self.xcor() >= 300:
            self.center()
            self.write("Left wins this round", align='center', font=("Arial", 25, "bold"))
            time.sleep(2.5)
            self.clear()
            left_score.increase_score()
            self.normal_stats()
            return False

        elif self.xcor() <= -300:
            self.center()
            self.write("Right wins this round", align='center', font=("Arial", 25, "bold"))
            time.sleep(2.5)
            right_score.increase_score()
            self.clear()
            self.normal_stats()
            return False

        else:
            return True

    def rebound_delay(self):
        for _ in range(2):
            time.sleep(TIME_DELAY)
            self.forward(10)

    def left_change(self):
        if self.heading() <= 180:
            difference = 90 - (self.heading() - 90)
            self.setheading(difference)
            self.rebound_delay()

        elif self.heading() > 180:
            difference = 270 + (270 - self.heading())
            self.setheading(difference)
            self.rebound_delay()
        self.current_direction = 'right'

    def right_change(self):
        if self.heading() < 90:
            difference = 90 + (90 - self.heading())
            self.setheading(difference)
            self.rebound_delay()

        elif self.heading() > 270:
            difference = 270 - (self.heading() - 270)
            self.setheading(difference)
            self.rebound_delay()
        self.current_direction = 'left'


class PlayerOne(Turtle):

    def __init__(self):
        super().__init__()
        self.pole = []
        self.ht()
        self.x_loc = -260

    def create_pole(self):
        y_loc = -20
        for _ in range(3):
            temp_turtle = Turtle()
            temp_turtle.speed(0)
            temp_turtle.goto(self.x_loc, y_loc)
            temp_turtle.shape("square")
            temp_turtle.color('white')
            temp_turtle.speed(0)
            temp_turtle.penup()
            temp_turtle.setheading(90)
            y_loc += 20

            self.pole.append(temp_turtle)

    def move_up(self):

        if self.pole[-1].ycor() < 280:
            for pole in self.pole:
                x = pole.xcor()
                y = pole.ycor() + 40
                pole.goto(x, y)

    def move_down(self):
        if self.pole[0].ycor() > -280:
            for pole in self.pole:
                x = pole.xcor()
                y = pole.ycor() - 40
                pole.goto(x, y)

    def deflect_ball(self, ball):
        for pole in self.pole:
            if pole.distance(ball) < 20:
                ball.left_change()


class PlayerTwo(PlayerOne):

    def __init__(self):
        super().__init__()
        self.x_loc = 260
        self.pole = []
        self.create_pole()

    def deflect_ball(self, ball):
        for pole in self.pole:
            if pole.distance(ball) < 40:
                ball.right_change()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(0.01, 0.01)
        self.color('white')
        self.penup()
        self.score = 0

    def move(self):
        self.setpos(-50, 220)

    def increase_score(self):
        self.score += 1

    def write_score(self):
        self.write(f"{self.score}", font=("Ariel", 55, 'normal'), align='center')


class ScoreBoardRight(ScoreBoard):

    def __init__(self):
        super().__init__()

    def move(self):
        self.setpos(50, 220)


def center_line():
    timmy = Turtle()
    timmy.shape('turtle')
    timmy.ht()
    timmy.penup()
    timmy.setpos(0, -300)
    timmy.setheading(90)
    timmy.pensize(10)
    timmy.color('grey')

    for _ in range(9):
        timmy.pendown()
        timmy.forward(30)
        timmy.penup()
        timmy.forward(40)


def main():

    # Set screen
    screen = Screen()
    screen.listen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Pong')
    screen.tracer(0)
    ball = Ball()

    # Set player 1
    player_one = PlayerOne()
    player_one.create_pole()
    screen.onkey(player_one.move_up, 'w')
    screen.onkey(player_one.move_down, 's')

    # Set player 2
    player_two = PlayerTwo()
    screen.onkey(player_two.move_up, 'Up')
    screen.onkey(player_two.move_down, 'Down')

    # Set score
    left_score = ScoreBoard()
    left_score.move()
    right_score = ScoreBoardRight()
    right_score.move()

    center_line()

    screen.update()

    def game_on():
        left_score.clear()
        left_score.write_score()
        right_score.clear()
        right_score.write_score()
        ball.starting_direction()
        while ball.score(left_score, right_score):
            screen.update()
            ball.forward(10)
            ball.change_direction()
            player_one.deflect_ball(ball)
            player_two.deflect_ball(ball)
            screen.update()
            time.sleep(TIME_DELAY)

    screen.onkey(game_on, 'space')
    screen.exitonclick()


if __name__ == "__main__":
    main()
