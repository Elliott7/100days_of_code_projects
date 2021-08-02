"""
Project Twenty/Twenty One - Snake Game
This game encompasses the classical snake game.
"""

from turtle import Turtle, Screen
import time
import random


class Snake:

    def __init__(self):
        self.screen = Screen()
        self.run_screen()
        self.snake_food = Turtle()
        self.write_score = Turtle()
        self.score_count = 0
        self.high_score = 0
        self.get_high_score()
        self.score()
        self.list_of_snakes = []
        self.init_snakes()
        self.log_of_locations = []
        self.food()
        self.move_food()

        self.listen_out()
        self.start_game()
        self.screen.exitonclick()

    def get_high_score(self):
        with open("score.txt", mode='r') as file:
            self.high_score = int(file.read())

    def update_high_score(self):
        with open("score.txt", mode='w') as file:
            file.write(str(self.high_score))
            # self.high_score = file.read()

    def score(self):
        self.write_score.clear()
        self.write_score.write(f"Score: {self.score_count} - High Score: {self.high_score}",
                               align="center")
        self.write_score.setpos(0, 280)
        self.write_score.color('white')
        self.write_score.shape('square')
        self.write_score.shapesize(0.01, 0.01)

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
        self.score_count = 0
        self.update_high_score()
        self.score()

    def run_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

    def start_game(self):
        while True:
            self.move_forward()
            self.compare()
            self.screen.update()
            if self.touch_wall() or self.touch_body():
                self.write_score.clear()
                self.write_score.penup()
                self.write_score.home()
                self.write_score.write(f"GAME OVER\nFinal Score"
                                       f" {self.score_count}", align='center')
                time.sleep(2)
                self.write_score.setpos(0, 280)
                self.reset()
                self.reset_location()
            time.sleep(.1)

    def reset_location(self):
        for sn in self.list_of_snakes[3:]:
            sn.ht()
        self.list_of_snakes[3:] = []
        self.list_of_snakes[0].setpos(0, 0)

    def touch_wall(self):
        if self.list_of_snakes[0].xcor() > 280 or self.list_of_snakes[0].xcor() < -280:
            return True

        if self.list_of_snakes[0].ycor() > 280 or self.list_of_snakes[0].ycor() < -280:
            return True

    def touch_body(self):
        x_loc = int(self.list_of_snakes[0].xcor())
        y_loc = int(self.list_of_snakes[0].ycor())
        coords = (x_loc, y_loc)
        if coords in self.log_of_locations:
            return True

    def compare(self):
        if self.list_of_snakes[0].distance(self.snake_food) < 15:
            self.score_count += 1
            self.create_new_snake()
            self.move_food()
            self.score()

    def init_snakes(self):
        pos = 0
        for _ in range(3):
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(pos, 0)
            snake.speed(0)
            pos -= 20
            self.list_of_snakes.append(snake)
        self.screen.update()

    def move_forward(self):
        locations = []
        for i in range(len(self.list_of_snakes)-1, 0, -1):
            x = self.list_of_snakes[i-1].xcor()
            y = self.list_of_snakes[i-1].ycor()
            self.list_of_snakes[i].goto(x, y)
            locations.append((int(x), int(y)))
        self.list_of_snakes[0].forward(20)
        self.log_of_locations = locations

    def listen_out(self):
        self.screen.onkey(self.turn_up, 'Up')
        self.screen.onkey(self.turn_left, 'Left')
        self.screen.onkey(self.turn_down, 'Down')
        self.screen.onkey(self.turn_right, 'Right')
        self.screen.listen()

    def turn_up(self):
        if self.list_of_snakes[0].heading() == 0:
            self.list_of_snakes[0].left(90)
        elif self.list_of_snakes[0].heading() == 180:
            self.list_of_snakes[0].right(90)

    def turn_left(self):
        if self.list_of_snakes[0].heading() == 90:
            self.list_of_snakes[0].left(90)
        elif self.list_of_snakes[0].heading() == 270:
            self.list_of_snakes[0].right(90)

    def turn_down(self):
        if self.list_of_snakes[0].heading() == 180:
            self.list_of_snakes[0].left(90)
        elif self.list_of_snakes[0].heading() == 0:
            self.list_of_snakes[0].right(90)

    def turn_right(self):
        if self.list_of_snakes[0].heading() == 270:
            self.list_of_snakes[0].left(90)
        elif self.list_of_snakes[0].heading() == 90:
            self.list_of_snakes[0].right(90)

    def food(self):
        self.snake_food.shape("circle")
        self.snake_food.penup()
        self.snake_food.shapesize(0.5, 0.5)
        self.snake_food.color('red')
        self.snake_food.speed("fastest")

    def move_food(self):
        random_x = int(random.randrange(-280, 280, 20))
        random_y = int(random.randrange(-280, 280, 20))
        self.snake_food.goto(random_x, random_y)

    def create_new_snake(self):
        x = self.list_of_snakes[-1].xcor()
        y = self.list_of_snakes[-1].ycor()
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(x, y)
        snake.speed(0)
        self.list_of_snakes.append(snake)


def main():
    snake = Snake()


if __name__ == "__main__":
    main()

