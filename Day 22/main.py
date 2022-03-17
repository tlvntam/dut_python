from turtle import Turtle, Screen
import time

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
""""Set up screen"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
"""Set paddle"""
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

"""Paddle move"""
screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

"""Set Ball"""
ball = Ball((0, 0))

"""Ball move"""


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    if ball.ycor() > 270 or ball.ycor() < -280:
        ball.ball_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_bounce_paddle()

    if ball.xcor() > 350:
        ball.refresh()
        scoreboard.l_score_plus()

    if ball.xcor() < -350:
        ball.refresh()
        scoreboard.r_score_plus()


    if scoreboard.score_l == 2 or scoreboard.score_r == 2:
        scoreboard.game_over()
        ball.hideturtle()

screen.exitonclick()
