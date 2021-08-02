"""
Project Twenty Three - Turtle Crossing
Imitating the fun game road crossing. This project uses the Turtle module and three classes - The player, the cars
and the score.
"""

from turtle import Turtle, Screen
import random
import time

time_delay = 0.2
speed = 10
car_increase = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.speed(0)
        self.shapesize(.7, 0.6)
        self.positioning()
        self.setheading(90)
        self.color('blue')
        self.reach_finish()
        self.alive = True

    def move(self):
        self.forward(20)

    def reach_finish(self):
        if self.ycor() >= 300:
            print('Level Completed')
            return True

    def positioning(self):
        self.setpos(0, -280)


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(.9, 2)
        self.randomize_color()
        self.randomize_location()
        self.setheading(180)
        self.speed(0)

    def randomize_location(self):
        x_loc = 300
        y_loc = random.randrange(-240, 300, 20)
        self.setpos(x_loc, y_loc)

    def randomize_color(self):
        r = random.randint(10, 250)
        g = random.randint(10, 250)
        b = random.randint(10, 250)
        self.fillcolor(r, g, b)

    def move(self):
        self.forward(10)

    def detect_left_boarder(self):
        if self.xcor() < -300:
            return True

    def distance_from(self, user):
        if self.distance(user) < 21 and self.ycor() - user.ycor() < 20 and self.ycor() - user.ycor() > -20:
            print("Game Over")
            return True


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.01, 0.01)
        self.color('black')
        self.level = 1
        self.setpos(-260, 260)

    def inc_level(self):
        self.level += 1

    def write_level(self):
        self.write(f"Level: {self.level}", font=("Ariel", 15, 'normal'), align='center')


def main():
    screen = Screen()
    screen.listen()
    screen.setup(width=600, height=600)
    screen.bgcolor('white')
    screen.title('Turtle Crossing')
    screen.colormode(255)
    screen.tracer(0)
    player = Player()
    screen.onkey(player.move, 'w')
    level = Level()
    level.clear()

    on = True
    car_list = []

    def game():
        level.write_level()
        while player.alive:
            car = Cars()
            car_list.append(car)

            for car in car_list:
                if car.distance_from(player):
                    player.alive = False
                    global on
                    on = False

                car.move()
                if car.detect_left_boarder():
                    car.ht()
                    car_list.remove(car)

            if player.reach_finish():
                player.positioning()
                level.inc_level()
                level.clear()
                global time_delay
                time_delay -= 0.03
                # global speed
                # speed += 5
                break
            time.sleep(time_delay)
            screen.update()
    while on:
        game()

    screen.exitonclick()


if __name__ == "__main__":
    main()
