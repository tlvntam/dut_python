from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, point):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        """Normal sz is 20x20 -> 5:1 = l:100xw:20"""
        self.penup()
        self.goto(point)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





