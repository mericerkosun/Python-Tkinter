from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Ticker - Label")
tk.geometry("400x300")

def show():
    messagebox.showinfo("Label","İnfo")
    messagebox.showerror("Label","Error")
    messagebox.showwarning("Label","Warning")

def ask():
    messagebox.askyesno("Label","askyesno")
    messagebox.askokcancel("Label","askokcancel")
    messagebox.askquestion("Label","askquestion")
    messagebox.askretrycancel("Label","askretrycancel")
    messagebox.askyesnocancel("Label","askyesnocancel")

L1 = Label(tk,text="MESSAGEBOX", font="Verdana 12 bold")
L1.pack()

B1 = Button(tk, text="show", command=show)
B1.pack()

B2 = Button(tk, text="ask", command=ask)
B2.pack()
tk.mainloop()