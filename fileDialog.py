from tkinter import filedialog
file = filedialog.askopenfilename()

files = filedialog.askopenfilenames()
filetypes = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
