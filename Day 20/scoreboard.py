from turtle import Turtle, Screen

ALIGN_FONT= ("Arial", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score = {self.score}",align="center",font=ALIGN_FONT)
        self.hideturtle()

        self.plus_score()

    def plus_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 10, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 10, "normal"))
