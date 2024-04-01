# Write a Python program that customizes the appearance of labels and buttons (e.g., fonts, colors) using Tkinter.

from tkinter import *

root = Tk()
root.title("Exercise 6")
root.geometry('300x300')
root.resizable(0,0)

def change_label():
    label.configure(text="Meriç Erkoşun", font=("Arial", 20),fg="red",bg="white")

label = Label(root, text="Meriç", font=("Arial", 20),fg="blue",bg="white")
label.pack()

button = Button(text="Click",font=20,width=20,command=change_label)
button.pack()

root.mainloop()