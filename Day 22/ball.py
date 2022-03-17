from turtle import Turtle, Screen
import random

class Ball(Turtle):
    def __init__(self, point):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid= 1, stretch_len= 1)
        self.penup()
        self.goto(point)
        self.x_ball = 10
        self.y_ball = 10
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_ball
        new_y = self.ycor() + self.y_ball
        self.goto(new_x, new_y)

    def ball_bounce(self):
        self.y_ball *= -1

    def ball_bounce_paddle(self):
        self.x_ball *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.ball_bounce_paddle()
