from turtle import Turtle, Screen
import random
import colorgram

# rgb_color = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

# print(rgb_color)

tummy_turtle = Turtle()
tummy_turtle.shape("turtle")
tummy_turtle.color("pink")
tummy_turtle.speed("fastest")

screen = Screen()
screen.colormode(255)

color_list = [(249, 244, 237), (250, 243, 247), (241, 249, 245), (242, 245, 249), (201, 157, 111), (62, 104, 125), (128, 160, 172), (153, 85, 52), (124, 81, 96), (133, 173, 159), (222, 198, 135), (187, 140, 47), (188, 134, 147), (46, 32, 19), (65, 125, 113), (181, 94, 112), (18, 44, 56), (58, 160, 131), (202, 95, 79), (145, 25, 38), (12, 26, 24), (89, 142, 158), (233, 171, 162), (43, 28, 34), (141, 31, 25), (28, 78, 91), (219, 176, 184), (169, 206, 191), (109, 126, 151), (61, 62, 72)]

tummy_turtle.penup()
tummy_turtle.setheading(220)
tummy_turtle.forward(300)
tummy_turtle.setheading(0)

number_of_dot = 100
for i in range(1, number_of_dot + 1):
    tummy_turtle.pendown()
    tummy_turtle.dot(20, random.choice(color_list))
    tummy_turtle.penup()
    tummy_turtle.forward(50)
    if i % 10 == 0:
        tummy_turtle.setheading(90)
        tummy_turtle.forward(50)
        tummy_turtle.setheading(180)
        tummy_turtle.forward(500)
        tummy_turtle.setheading(0)

tummy_turtle.hideturtle()

screen.exitonclick()