from tkinter import *
#from tkinter.ttk import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
chk_state = BooleanVar()
#chk_state.set(True) #set check state
#chk_state = IntVar()
#chk_state.set(0) #uncheck
#chk_state.set(1) #check
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()
