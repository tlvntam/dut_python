from turtle import Turtle, Screen

ALIGN_FONT= ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_l} : {self.score_r}", align="center", font=ALIGN_FONT)

    def l_score_plus(self):
        self.score_l += 1
        self.update_scoreboard()

    def r_score_plus(self):
        self.score_r += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "normal"))