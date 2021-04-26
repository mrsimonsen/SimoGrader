import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('CREATE TABLE students(last text, first text, github text, assignment text, score real)')
cur.execute("INSERT INTO students VALUES ('Simonsen','John','mrsimonsen','00p',10.0)")
con.commit()
con.close()

new = sqlite3.connect('example.db')
cur = new.cursor()
for i in cur.execute('SELECT * FROM students'):
	print(i)
con.close()

def create_table(con, cur):
	cur.execute('CREATE TABLE assignments(ID int NOT NULL, score real DEFAULT 0.0, PRIMARY KEY (ID)')
	cur.execute('CREATE TABLE students(
