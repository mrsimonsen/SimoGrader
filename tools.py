import datetime, database, csv

def get_date():
	ok = False
	while not ok:
		year = validate_num("Year:(####)")
		month = validate_num("Month:(##)")
		day = validate_num("Day:(##)")
		try:
			d = datetime.datetime(year, month, day)
			ok = True
		except ValueError as e:
			print(e)
	return d

def validate_num(question):
	number = None
	while not number:
		try:
			number = int(input(f"{question}\n"))
		except ValueError:
			print("That wasn't a number")
	return number

def ask_yn(question):
	r = ''
	while r not in ('y','n'):
		r = input(f"{question} (Y/n)\n").lower()
	return r

def change_float(q1, thing):
	complete = 'n'
	while complete == 'n':
		new = input(f"{q1}\n")
		try:
			new = float(new)
			complete = ask_yn(f"Change \"{thing}\" to \"{new}\"?")
		except ValueError:
			print("That wasn't a number")
	return new

def change(q1, thing, num = False):
	complete = 'n'
	while complete == 'n':
		if num:
			new = validate_num(q1)
		else:
			new = input(f"{q1}\n")
		complete = ask_yn(f"Change \"{thing}\" to \"{new}\"?")
	return new

def validate_assign():
	raw = database.read(database.connect(), "SELECT tag FROM assignments;")
	assigns = []
	for i in raw:
		assigns.append(i[0])
	a = ''
	print(assigns)
	while a not in assigns and a != 'q':
		a = input("Enter an assignment tag (or 'q'uit):\n").lower()
	return a

def select_student():
	search = input("Enter a part of a student name (or '0' to exit):\n")
	while search != '0':
		results = database.read(database.connect(),
		f"SELECT last, first_weber, first_nuames, github FROM students WHERE last LIKE %{search}% OR first_weber LIKE %{search}% OR first_nuames LIKE %{search}%;")
		if len(results)>1:
			print("0 - Quit")
			for i in range(len(results)):
				print(f"{i+1} - {results[i]}")
			n = validate_num("Which result?")-1
			if n >= 0:
				return results[n][3]
			else:
				return
		elif len(results)==1:
			return results[0][3]
		else:
			if search != '0':
				print(f"No students matched \"{search}\"")
				search = input("Enter a part of a student name (or '0' to exit):\n")

def report():
	c = database.connect()
	tags = database.read(c, 
	"SELECT tag FROM assignments;")
	students = database.read(c,
	f"SELECT * FROM students;")
	header = ['Period','Last Name','Weber First', 'NUAMES First']
	for t in tags:
		header.append(t[0])
	stuff = [header]
	for github, first_weber, first_nuames, last, period in students:
		row = [period, last, first_weber, first_nuames]
		for a in tags:
			s = database.read(c, f"SELECT earned FROM scores WHERE github = '{github}' AND tag = '{a[0]}';")
			if s:
				row.append(s[0][0])
			else:
				row.append('-')
		stuff.append(row)
	with open(f'report.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',', quotechar='|')
		w.writerows(stuff)
	print("Report complete")
report()