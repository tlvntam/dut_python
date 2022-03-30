from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/vietnamese_words.csv")
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/vietnamese_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_lang, text="Vietnamese", fill="black")
    canvas.itemconfig(word_lang, text=current_card["Vietnamese"], fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_time = window.after(3000, func=flip_card)


def known_card():
    to_learn.remove(current_card)
    # print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index= False)

    next_card()

def flip_card():
    canvas.itemconfig(title_lang, text="English", fill="white")
    canvas.itemconfig(word_lang, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)


"""Window setup"""
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_time= window.after(3000, func=flip_card)

"""Canvas"""
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400, 263, image=front_img)
back_img = PhotoImage(file="images/card_back.png")

title_lang = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word_lang = canvas.create_text(400, 263, text="word", font=("Arial", 50, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

"""Button"""
unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=known_card)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()
