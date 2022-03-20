from tkinter import *

window = Tk()

window.title("GUI - Graphic User Interface")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

"""Label"""
my_label = Label(text="I'm a label", font=("Arial", 20, "bold"))
# my_label.place(x=0, y=0)
my_label.grid(column=1, row=1)

my_label["text"] = "New text"
my_label.config(text="New text")

"""Button"""


def button_click():
    # print("I got clicked")
    new_text = input_box.get()
    my_label.config(text=new_text)



button = Button(text="Click here", command=button_click)
# button.pack()
button.grid(column=2, row=2)

new_button = Button(text="Click here, too")
new_button.grid(column=3, row=1)


"""Entry"""
input_box = Entry()
# input_box.pack()
input_box.grid(column=4, row=4)


window.mainloop()
