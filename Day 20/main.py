from turtle import Turtle, Screen
import time

from snake import Snake
""""Set up screen"""
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""Snake Body"""
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_win = True
while is_win:
    screen.update()
    time.sleep(0.1)

    snake.move()





screen.exitonclick()