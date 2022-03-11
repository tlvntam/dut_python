from turtle import Turtle, Screen
from replit import clear

tum = Turtle()
screen = Screen()

def move_forward():
    tum.forward(10)

def move_backward():
    tum.backward(10)

def move_left():
    tum.left(10)

def move_right():
    tum.right(10)

def move_clear():
    tum.clear()
    tum.penup()
    tum.home()
    tum.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=move_clear)

screen.exitonclick()

