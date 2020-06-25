# Catalog App developed by Cinar Ioan
# Date of creation 25.06.2020
# New test comment
from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Cinar Ioan")
myLabel2.grid(row=1, column=1)

myLabel.grid(row=0, column=0)

root.mainloop()