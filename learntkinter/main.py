from tkinter import *

root = Tk()

root.title("First Program")
root.geometry('350x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
item.add_command(label='Delete')
menu.add_cascade(label='Menu', menu=item)
root.config(menu=menu)

label = Label(root, text="Hello World!").pack()

frame = Frame(root)
frame.pack()

button = Button(frame, text="Geek")
button.pack()

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.pack()
 
txt = Entry(root, width=10)
txt.pack()

# function to display text when
# button is clicked
def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text = res)
 
# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.pack()

root.mainloop()