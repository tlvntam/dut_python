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
            snake = Turtle(shape="square")
            snake.color("White")
            snake.penup()
            snake.goto(point)
            self.body.append(snake)

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part - 1].xcor()
            new_y = self.body[part - 1].ycor()
            self.body[part].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        # if self.head.setheading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # if self.head.setheading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # if self.head.setheading() != RIGHT:
            self.head.setheading(LEFT)

    def right (self):
        # if self.head.setheading() != LEFT:
            self.head.setheading(RIGHT)



