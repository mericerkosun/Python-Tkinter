import sqlite3

db = sqlite3.connect("login.db")
c = db.cursor()

comnt = '''INSERT INTO users VALUES (4,'merencelebi','373737')'''
c.execute(comnt)
db.commit()

comnt = '''SELECT * FROM users'''
c.execute(comnt)

dat = c.fetchall()
print(dat)
db.close()
