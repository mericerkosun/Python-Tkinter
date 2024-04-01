from tkinter import *

tk = Tk()

tk.title("Ticker - Label")

tk.geometry("400x300")

Label(tk, text="Vardana", font="Vardana 12", bg="red", fg="white").pack()
Label(tk, text="Vardana Bold", font="Vardana 12 bold underline").pack()
Label(tk, text="Vardana italic", font="Vardana 12 italic").pack()
Label(tk, text="Vardana roman", font="Vardana 12 roman").pack()

Label(tk, text="Melvetica", font="Melvetica 12", bg="green", fg="yellow").pack()
Label(tk, text="Melvetica bold", font="Melvetica 12 bold").pack()
Label(tk, text="Melvetica italic", font="Melvetica 12 italic").pack()
Label(tk, text="Melvetica roman", font="Melvetica 12 roman").pack()

tk.mainloop()