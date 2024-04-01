# Write a Python program that creates a basic menu bar with menu items using Tkinter.

from tkinter import *

root = Tk()
root.title("Exercise 4")
root.geometry('200x300')

menu = Menu(root)
item = Menu(menu)
item.add_command(label="File")
item.add_command(label='Edit')
item.add_command(label='Settings')
menu.add_cascade(label="Menu", menu=item)
root.config(menu=menu)

root.mainloop()
