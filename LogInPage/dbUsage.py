import sqlite3

db = sqlite3.connect("company.db")
c = db.cursor()
comnt = """INSERT INTO idpsw VALUES ('Ali','1234')"""
c.execute(comnt)
comnt = """INSERT INTO idpsw VALUES ('Ahmet','5423')"""
c.execute(comnt)
comnt = """INSERT INTO idpsw VALUES ('Fatma','1010')"""
c.execute(comnt)
comnt = """INSERT INTO idpsw VALUES ('Hatice','5555')"""
c.execute(comnt)
db.commit()

comnt = """select * from idpsw"""

c.execute(comnt)

dat = c.fetchall()
print(dat)
db.close