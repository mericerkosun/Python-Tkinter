# Write a Python program that displays messages in a messagebox using Tkinter.
from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Exercise 5")
root.geometry('250x300')

def show_message():
    messagebox.showinfo("Message","Hello!")

def show_askokcancel():
    messagebox.askokcancel("Message","Hello!")

def show_askyesnocancel():
    messagebox.askyesnocancel("Message","Hello!")

button1 = Button(root, text="Show Info",command=show_message)
button1.pack()

button2 = Button(root, text="Ask Ok Cancel",command=show_askokcancel)
button2.pack()

button3 = Button(root, text="Click Here",command=show_askyesnocancel)
button3.pack()

root.mainloop()