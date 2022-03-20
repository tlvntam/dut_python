from tkinter import *

window = Tk()

window.title("Mile to Km")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

"""Label"""
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

note_label = Label(text="is equal to")
note_label.grid(column=1, row=2)

result_label = Label(text="")
result_label.grid(column=2, row=2)

"""Button"""


def button_click():
    # print("I got clicked")
    mile = float(mile_input.get())
    result = mile * 1.609
    result_label.config(text=round(result))


button = Button(text="Calculate", command=button_click)
button.grid(column=2, row=3)

"""Entry"""
mile_input = Entry(width=7)
mile_input.grid(column=2, row=1)


window.mainloop()