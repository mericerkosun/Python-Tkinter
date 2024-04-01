# Write a Python GUI program to import Tkinter package and create a window. Set its title and add a label to the window.

from tkinter import *

root = Tk()
root.title("Exercise 2")
root.geometry('250x300')

label = Label(root, text="Exercise 2 Label")
label.pack()

root.mainloop()