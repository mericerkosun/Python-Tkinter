import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS idpsw2
    (id TEXT, psw INTEGER)"""
)