from os import path
from tkinter import filedialog
dir = filedialog.askdirectory()
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
