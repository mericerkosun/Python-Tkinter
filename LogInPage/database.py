import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS idpsw
    (id STRING, psw STRING)"""
)