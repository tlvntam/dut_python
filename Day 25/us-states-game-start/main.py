import turtle
from turtle import Screen, Turtle
import pandas as pd

"""Set up Screen"""
screen = Screen()
screen.title("U.S States Game")
screen.setup(width=750, height=525)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)

"""Data"""
data = pd.read_csv("50_states.csv")
data_state = data.state.to_list()
# print(data_state)
guess_state = []
while len(guess_state) < 50:
    player_answer = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="Enter state's name: ").title()
    # print(player_answer)

    if player_answer in data_state:
        guess_state.append(player_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        statexy = data[data.state == player_answer]
        # print(statexy)
        t.goto(int(statexy.x), int(statexy.y))
        t.write(statexy.state.item())

    if player_answer == "Exit":
        miss_state = []
        for state in data_state:
            if state not in guess_state:
                miss_state.append(state)
        new_data = pd.DataFrame(miss_state)
        new_data.to_csv("State to learn")
        break


