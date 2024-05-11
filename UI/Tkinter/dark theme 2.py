import tkinter as tk
from tkinter import *
root = Tk()
root.config(bg="AliceBlue")


def dark():
    root.config(bg="#1a1a1a")


def light():
    root.config(bg="AliceBlue")


dark_theme = Button(root, text="🌚 Dark theme", command=dark, bg="whitesmoke")
light_theme = Button(root, text="🌝 Light theme", command=light, bg="whitesmoke")
dark_theme.grid(row=0, column=0)
light_theme.grid(row=0, column=1)


def hover(widget, entrance_bg, entrance_fg, exit_bg, exit_fg):
    widget.bind("<Enter>", func=lambda e: widget.config(
                bg=entrance_bg, fg=entrance_fg))
    widget.bind("<Leave>", func=lambda e: widget.config(
                bg=exit_bg, fg=exit_fg))


ent = Entry(root, width=50, bg="lightblue", borderwidth=5)
ent.grid(row=1, column=0)
ent.insert(0, "Insert name here")
hover(ent, "#aaddff", "black", "lightblue", "black")


def my_click():
    hello = "Hello, " + ent.get()
    my_label = Label(root, text=hello)
    my_label.grid()
    ent.delete(0, tk.END)


myButton = Button(root, text="Enter your name", command=my_click, fg="darkblue", bg="#efffff", borderwidth=1)
myButton.grid(row=2, column=0)
root.mainloop()
