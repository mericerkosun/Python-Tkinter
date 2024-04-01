import tkinter as tk
import sqlite3

def login():
    
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM idpsw2 WHERE id=? AND psw=?', (username, password))
    user = c.fetchone()
    
    if user:
        login_status.config(text="Başarılı Giriş", fg="green")
    else:
        login_status.config(text="Başarısız Giriş", fg="red")

def cancel():
    root.destroy()


root = tk.Tk()
root.title("Login Ekranı")


username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)


password_label = tk.Label(root, text="Şifre:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)


login_button = tk.Button(root, text="Giriş", command=login)
login_button.grid(row=2, column=0, padx=10, pady=5)


cancel_button = tk.Button(root, text="İptal", command=cancel)
cancel_button.grid(row=2, column=1, padx=10, pady=5)


login_status = tk.Label(root, text="", fg="black")
login_status.grid(row=3, column=0, columnspan=2)


root.mainloop()
