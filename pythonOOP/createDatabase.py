import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS students
    (name TEXT, age INTEGER)"""
)