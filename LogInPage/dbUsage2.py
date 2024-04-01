import sqlite3

db = sqlite3.connect("company.db")
c = db.cursor()
comnt = """INSERT INTO idpsw2 VALUES ('Ali',1243)"""
c.execute(comnt)
comnt = """INSERT INTO idpsw2 VALUES ('Ahmet',5423)"""
c.execute(comnt)
comnt = """INSERT INTO idpsw2 VALUES ('Fatma',1010)"""
c.execute(comnt)
comnt = """INSERT INTO idpsw2 VALUES ('Hatice',5555)"""
c.execute(comnt)
db.commit()

comnt = """select * from idpsw2"""

c.execute(comnt)

dat = c.fetchall()
print(dat)
db.close