from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        self.left(MOVE_DISTANCE)

    def move_right(self):
        self.right(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)

