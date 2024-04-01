from tkinter import *

tk = Tk()
tk.title("Ticker - Label")
tk.geometry("400x300")

G1 = Label(tk, text="Grid Label 1")
G1.grid(row=0, column=0, pady=5, padx=5)

G2 = Button(tk, text="Grid Button 1")
G2.grid(row=0, column=1, pady=5, padx=5)

G3 = Label(tk, text="Grid Label 2")
G3.grid(row=1, column=0)

G4 = Button(tk, text="Grid Button 2")
G4.grid(row=1, column=1)

P1 = Label(tk, text="Place Label")
P1.place(x=170, y=140)

P2 = Button(tk, text="Place Button")
P2.place(x=165, y=165)

tk.mainloop()