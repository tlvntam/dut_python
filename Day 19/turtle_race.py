from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 480)

bot_color = ["Yellow", "Red", "Blue", "Black", "Green"]
n = 0
all_turtle = []
for i in range(0,5):
    color_turle = Turtle(shape="turtle")
    color_turle.color(bot_color[i])
    color_turle.penup()
    color_turle.goto(x= -200, y= 100 - n)
    n += 50
    all_turtle.append(color_turle)

player_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if player_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            win_turtle = turtle.pencolor()
            if win_turtle == player_bet:
                print(f"You win! The {win_turtle} turtle is the winner!")
            else:
                print(f"You lose! The {win_turtle} turtle is the winner!")
        ran_dis = random.randint(0, 10)
        turtle.forward(ran_dis)

screen.exitonclick()