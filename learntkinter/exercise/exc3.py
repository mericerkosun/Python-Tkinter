# Write a Python GUI program to create a label and change the label font style (font name, bold, size) using tkinter module.

from tkinter import *

root = Tk()

root.title("Exercise 3")
root.geometry('350x200')
root.resizable(0,0) #Disables the resize.

def clicked():
    label.config(text="Button Clicked")

label = Label(root, text="Exercise 3 Label", font=("Ariald Bold",30))
label.pack()

button = Button(root, text="Click", width=30, command=clicked)
button.pack()

root.mainloop()
