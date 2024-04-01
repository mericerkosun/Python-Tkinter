from tkinter import *
import sqlite3

def login():

    username = name_entry.get()
    password = pass_entry.get()

    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()

    if user:
        login_status.config(text="Başarılı Giriş", fg="green")
    else:
        login_status.config(text="Başarısız Giriş", fg="red")

def cancel():
    root.destroy()


root = Tk()

root.title("Login")
root.geometry('350x200')

name_lbl = Label(root, text="Username : ")
name_lbl.pack()

name_entry = Entry(root, width=20)
name_entry.pack()

pass_lbl = Label(root, text="Password : ")
pass_lbl.pack()

pass_entry = Entry(root, show="*", width=20)
pass_entry.pack()

login_btn = Button(root, text="Login", command=login)
login_btn.pack()

cancel_btn = Button(root, text="Cancel", command=cancel)
cancel_btn.pack()

login_status = Label(root, text="", fg="black")
login_status.pack()

root.mainloop()