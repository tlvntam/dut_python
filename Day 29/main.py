import csv
from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import *
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_gene_letter = [choice(letters) for _ in range(randint(8, 10))]
    pass_gene_num = [choice(numbers) for _ in range(randint(2, 4))]
    pass_gene_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = pass_gene_letter + pass_gene_num + pass_gene_symbol

    shuffle(password_list)
    password = "".join(password_list)

    """Used pyperclip to auto copy"""
    pyperclip.copy(password)

    """Insert to pass_input"""
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    web_save = website_input.get()
    user_save = user_input.get()
    pass_save = pass_input.get()
    print(web_save, user_save, pass_save)

    if len(web_save) == 0 or len(user_save) == 0 or len(pass_save) == 0:
        messagebox.showinfo(title="Warning", message="Pls don't leave any fields empty")
    else:
        """Mess box"""
        # messagebox.showinfo(title="Title", message="this is message")
        reply_box = messagebox.askokcancel(title=web_save, message=f"There are details entered: \nEmail: {user_save}"
                                                                   f"\nPassword: {pass_save}\nIs it okay to save? ")

        if reply_box:
            with open("data.txt", "a") as data:
                data.write(f"{web_save} | {user_save} | {pass_save} \n")
                website_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
"""Window"""
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=550)
window.config(padx=50, pady=50)

"""Canvas"""
canvas = Canvas(width=210, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(105, 100, image=logo_img)
canvas.grid(column=2, row=1)

"""Website"""
website_label = Label(text="Website", font=(FONT_NAME, 10))
website_label.grid(column=1, row=2)

website_input = Entry(width=43)
website_input.grid(column=2, row=2, columnspan=3)
website_input.focus()

"""Username"""
user_label = Label(text="Email/Username", font=(FONT_NAME, 10))
user_label.grid(column=1, row=3)

user_input = Entry(width=43)
user_input.insert(0, "abc@gmail.com")
user_input.grid(column=2, row=3, columnspan=3)

"""Password"""
pass_label = Label(text="Password", font=(FONT_NAME, 10))
pass_label.grid(column=1, row=4)

pass_input = Entry(width=25)
pass_input.grid(column=2, row=4)

pass_button = Button(text="Generate Password", command=pass_generator)
pass_button.grid(column=3, row=4)

"""Add"""
add_button = Button(text="Add", width=43, command=save_pass)
add_button.grid(column=2, row=5, columnspan=3)

window.mainloop()
