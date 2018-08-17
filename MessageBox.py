from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
def clicked():
    messagebox.showinfo('are you want to exit', 'Click  for confirmation')
btn = Button(window,text='Exit', command=clicked)


from tkinter import messagebox
messagebox.showwarning('Message title', 'Message content')  #shows warning message
messagebox.showerror('Message title', 'Message content')    #shows error message
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')


btn.grid(column=0,row=0)
window.mainloop()
