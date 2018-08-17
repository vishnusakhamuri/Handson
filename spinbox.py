
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
spin = Spinbox(window, from_=0, to=100, width=5)

spin1 = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0,row=0)
var =IntVar()
var.set(36)
spin2 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin1.grid(column=10,row=10)
spin2.grid(column=15,row=15)
window.mainloop()
