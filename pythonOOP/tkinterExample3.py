from tkinter import *

tk = Tk()
tk.title("Ticker - Label")
tk.geometry("400x300")

def buton():
        lbl["text"] = "1. Button Clicked"

def buton2():
        lbl["text"] = "2. Button Clicked"


btn1 = Button(tk,
              text="Buton",
              padx="20",pady="5",
              command=buton)

btn1.pack()

btn2 = Button(tk,
              text="Buton2", font="Times 12 bold",
              padx="25",pady="10",
              bg="blue", fg="red", cursor="hand2",
              activeforeground="green", activebackground="black",
              command=buton2)

btn2.pack()

lbl = Label(tk)
lbl.pack()
tk.mainloop()