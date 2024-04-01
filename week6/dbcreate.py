import sqlite3

conn = sqlite3.connect('ABCcompany.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS DailySales (
                    pld INTEGER,
                    date DATE,
                    qua INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS MonthlySales (
                    pld INTEGER,
                    m INTEGER,
                    qua INTEGER
                )''')

conn.commit()
conn.close()

