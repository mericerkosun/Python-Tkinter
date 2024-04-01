import sqlite3

db = sqlite3.connect("school.db")
c = db.cursor()
comnt = """INSERT INTO students VALUES ('Ali',24)"""
c.execute(comnt)
comnt = """INSERT INTO students VALUES ('Mustafa',21)"""
c.execute(comnt)
db.commit()

comnt = """select * from students"""

c.execute(comnt)

dat = c.fetchall()
print(dat)
db.close