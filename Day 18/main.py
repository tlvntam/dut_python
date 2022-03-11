# import heroes
# print(heroes.gen())

from turtle import Turtle, Screen
import random


tummy_turtle = Turtle()
tummy_turtle.shape("turtle")
tummy_turtle.color("pink")
tummy_turtle.speed("fastest")

# for i in range(10):
#     tummy_turtle.forward(4)
#     tummy_turtle.penup()
#     tummy_turtle.forward(4)
#     tummy_turtle.pendown()

# color = ["green", "red", "brown", "yellow", "blue", "gray", "black", "violet"]

# for i in range(3, 11):
#     n = 0
#     tummy_turtle.color(random.choice(color))
#     while n < i:
#         tummy_turtle.forward(100)
#         tummy_turtle.right(360/i)
#         n += 1
#         if n == i:
#             break

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tummy_turtle.forward(100)
#         tummy_turtle.right(angle)

screen = Screen()
screen.colormode(255)

def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# direction = [0, 90, 180, 270]
# tummy_turtle.pensize(3)

#
# for n in range (100):
#     tummy_turtle.color(ran_color())
#     tummy_turtle.forward(50)
#     tummy_turtle.setheading(random.choice(direction))

def draw_spirograph(size):
    for i in range(int(360/size)):
        tummy_turtle.color(ran_color())
        tummy_turtle.circle(100)
        tummy_turtle.setheading(tummy_turtle.heading() + size)

draw_spirograph(5)

screen.exitonclick()

