from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.75, stretch_wid= 0.75)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))