from tkinter import *

tk = Tk()
tk.title("Ticker - Label")
tk.geometry("400x300")

lbl = Label(tk, text="Entry")
lbl.pack()

entry = Entry(tk, width=25)
entry.pack()

entry2 = Entry(tk, textvariable=StringVar(),show="*", width=25)
entry2.pack()

tk.mainloop()