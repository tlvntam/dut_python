from turtle import Turtle, Screen

STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for point in STARTING_POINT:
            self.add_body(point)

    def add_body(self, point):
        snake = Turtle(shape="square")
        snake.color("White")
        snake.penup()
        snake.goto(point)
        self.body.append(snake)

    def extend_tail(self):
        self.add_body(self.body[-1].position())

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

