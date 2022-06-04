import shelve, csv, os, datetime
from subprocess import run
from github import Github
from dotenv import load_dotenv
from os import environ as env
from sys import exit

class Student():
	def __init__(self, name = "Student, Sample", period = 0, github = 'username'):
		self.name = name
		self.period = period
		self.github = github
		self.assignments = {}
		self.add_assignments()

	def __str__(self):
		rep = f"{self.name}: {self.github}\n"
		rep += f"{self.period}\n"
		return rep

	def add_assignments(self):
		with shelve.open('data.dat') as d:
			tags = d['assignments']
		for t in tags:
			self.assignments[t]=Assignment(t)

	def clone(self, tag):
		return f"nuames-cs/{tag}-{self.github}"

	def print_assignments(self):
		rep = f"/tAssignments"
		rep += "|Tag|Score|\t|Tag|Score|\n"
		rep +="___________\t___________\n"
		keys = list(self.assignments.keys())
		for i in range(0,len(self.assignments),2):
			a1 = self.assignments[keys[i]]
			a2 = self.assignments[keys[i+1]]
			rep += f"|{a1.tag}|{a1.score:>5}|\t|{a2.tag}|{a2.score:>5}|\n"
		a = self.assignments[-1]
		rep += f"|{a.tag}|{a.score>5}|"
		return rep

class Assignment():
	def __init__(self, tag):
		self.tag = tag
		self.score = 0.0

	def __str__(self):
		rep = f"Assignment {self.tag}\n"
		rep += f"Score: {self.score}/10\n"
		return rep

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

def clean():
	#get user credentials from .env
	print("Logging into GitHub...")
	load_dotenv()
	if (token := env.get('TOKEN')) == None:
		exit("Edit .env file to have your personal access token.")
	#make github object
	g = Github(token)
	print(f"Loaded credentials for {g.get_user().name}")
	#makedir for clone - set name to current date time
	repos = g.get_user().get_repos()
	print("Gathering Repos...")
	old = []
	total = len(list(repos))
	d = shelve.open('data.dat')
	tags = d['assignments']
	d.close()
	print("Starting Search...")
	for r in repos:
		if r.name[:3] in tags:
			print(f"{r.name} added")
			old.append(r)
	print(f"{len(old)} repos collected")
	if input("Delete?\n").lower() in ('yes','y'):
		for i in old:
			print(f"deleting {i.name}")
			i.delete()
	print("Done.")

def reset_data():
	d = shelve.open('data.dat')
	d['assignment'] = []
	for i in range(26):
		d['assignment'].append(f"{i:02}p")
	for i in range(1,12):
		d['assignments'].append(f"P{i:02}")
	d['students'] = []
	d.close()
	print("Data has been reset")

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
	assign = []
	with shelve.open('data.dat') as d:
		assign += d['assignments']
		assign.append('done')
	a = ''
	print(assign)
	while a not in assign:
		a = input("Enter an assignment tag:\n").lower()
	return a

def set_students():
	students = []
	try:
		f = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'r',newline='')
		print("Loading students...")
		#format: time, first, last, period, github
		raw = csv.reader(f, delimiter= ',', quotechar = '"')
		for row in raw:
			if row[0] == "Timestamp":
				continue #skip the header
			students.append(Student(f"{row[2].strip()}, {row[1].strip()}", int(row[3]), row[4].strip()))
		f.close()
		d = shelve.open('data.dat')
		d['students'] = students
		d.close()
		print(f"{len(students)} loaded")
	except FileNotFoundError as e:
		print(e)
		print("Exiting program -- goodbye.")
		exit()

def display_student():
	stu = select_student()
	if stu:
		print(f"{stu.name} Assignments - P{stu.period}")
		print(stu.print_assignments())

def select_student(text=None):
	if not text:
		search = input("Enter a part of a student name or '0' to exit:\n")
	else:
		search = text
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	while search != '0':
		results = []
		for i in students:
			if search.lower() in i.name.lower():
				results.append(i)
		if len(results)>1:
			print("0 - Quit")
			for i in range(len(results)):
				print(f"{i+1} - {results[i].name}")
			n = validate_num("Which student?")-1
			if n >= 0:
				return results[n]
			else:
				return None
		elif len(results)==1:
			return results[0]
		else:
			if search != '0':
				print(f"No students matched \"{search}\"")
				search = input("Enter a part of a student name or '0' to exit:\n")

def drop():
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	stu = select_student()
	print(f"Dropping {stu.name.upper()}, {stu.period}")
	if ask_yn("Are you sure? This CANNOT be undone.") == 'y':
		for i in range(len(students)):
			if students[i].name == stu.name:
				students.pop(i)
				break
		d = shelve.open('data.dat')
		d['students'] = students
		d.close()
		f = None
		try:
			f = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'r',newline='')
		except:
			print("response csv not found")
		if f:
			raw = csv.reader(f, delimiter= ',', quotechar = '"')
			new = []
			for row in raw:
				name = f"{row[2]}, {row[1]}"
				if name != stu.name:
					new.append(row)
			f.close()
			a = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'w',newline='')
			w = csv.writer(a, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
			for row in new:
				w.writerow(row)
			a.close()
		print(f"{stu.name} dropped")
	else:
		print("Drop Aborted")

def run_python(simple):
	try:
		p = run(f"python3 Tests.py {'simple' if simple else ''}",shell=True,capture_output=True,text=True)
		if p.stderr:
			print("Tests didn't run")
			score = None
		else:
			out = p.stdout.strip().split("\n")
			if len(out) > 1:
				for i in range(1,len(out)):
					print(out[i])
			score = out[0]
	except KeyboardInterrupt:
		print("Student test terminated")
		score = None
	return score

def grade(stu, tag, simple = True):
	os.system(f"gh repo clone {stu.clone(tag)} student -- -q")
	if os.path.isdir('student'):
		print("Testing...")
		os.chdir('student')
		os.system(f"cp ../Testing/{tag}.py Tests.py")
		stu.assignments[tag] = run_python(simple)
		os.chdir('..')
		run(['rm','-rf','student'])
	else:
		print(f"{stu.name} hasn't started the assignment")

def mod_student():
	stu = select_student()
	choice = -1
	new = Student(stu.name, stu.period, stu.github)
	new.assignments = stu.assignments
	while choice != 0 and stu:
		print(stu)
		print("0 - Save/Back to Main Menu")
		print("1 - Change name")
		print("2 - Change github username")
		print("3 - Change class period")
		choice = -1
		while choice not in range(4):
			choice = validate_num("What would you like to change?")
		if choice == 1:
			print(f"Changing {stu.name} name:")
			new.name = change("Enter a new name:",stu.name)
		elif choice == 2:
			print(f"Changing {stu.name} username:")
			new.github = change("Enter a new github username:",stu.github)
		elif choice == 3:
			print(f"Changing {stu.name} period:")
			new.period = change(f"Enter a new period for {stu.name}:",stu.period, True)
		elif choice == 0:
			d = shelve.open('data.dat')
			students = d['students']
			for i in range(len(students)):
				if students[i].name == stu.name:
					students[i] = new
					break
			d['students'] = students
			d.close()
			print('Data saved')

#function to use as a sorting key in choice 5 of mod_student
def fsort(obj):
	return obj.name

def create():
	print("Adding a student to the roster.")
	correct = 'n'
	d =  shelve.open('data.dat')
	students = d['students']
	d.close()
	while correct == 'n':
		fname = input("What is the student's first name?\n").title()
		lname = input("What is the student's last name?\n").title()
		period = int(input("What class period is the student in?\n"))
		git = input("What is the student's GitHub username?\n")
		print(f"Student: {lname}, {fname}")
		print(f"Period: {period}")
		print(f"GitHub username: {git}")
		correct = ask_yn("Is this information correct?")
	#make the student
	new = Student(f"{lname}, {fname}", period, git)
	print("...student created")
	new.add_assignments()
	print("...assignments created")
	students.append(new)
	students.sort(key=fsort)
	d = shelve.open('data.dat')
	d['students'] = students
	print("Student created and added to database. Data Saved.")

def mod_assign():
	stu = select_student()
	choice = None
	while choice != 0 and stu:
		print(stu)
		print(stu.print_assignments())
		print("0 - Save/Back to Main Menu")
		print("1 - Change a score")
		print("2 - Set as late")
		choice = -1
		while choice not in (0,1,2):
			choice = validate_num("What would you like to do?")
		if choice == 1:
			tag = validate_assign()
			stu.assignments[tag].score = change_float("Enter a new score:", stu.assignments[tag].score)
		elif choice == 2:
			tag = validate_assign()
			l = not stu.assignments[tag].late
			if ask_yn(f"Set {tag} to {l}?") == 'y':
				stu.assignments[tag].set_late()
		elif choice == 0:
			d = shelve.open('data.dat')
			students = d['students']
			for i in range(len(students)):
				if students[i].name == stu.name:
					students[i] = stu
					break
			d['students'] = students
			d.close()
			print('Data saved')

def grade_assignment(tag = None):
	if not tag:
		tag = validate_assign()
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	if tag[-1] == 'j':
		grading = '1400'
	elif tag[-1] == 'p':
		grading = '1030'
	else:
		grading = None
	for stu in students:
		if stu.course == grading:
			a = stu.assignments[tag]
			if a.score < 5 and a.late:
				print(f"Grading {stu.name} - late")
				grade(stu,tag)
				print(f"{stu.name}: {tag} - {stu.assignments[tag].score}/10")
			elif a.score < 10 and not a.late:
				print(f"Cloning {stu.name} - on time")
				grade(stu,tag)
				print(f"{stu.name}: {tag} - {stu.assignments[tag].score}/10")
			elif (a.score == 10 and not a.late) or (a.score == 5 and a.late):
				print(f"{stu.name} already has completed assignment")
			else:
				print("something strange happened in grade_assignment()")
	print("Grading complete -- saving...")
	d = shelve.open('data.dat')
	d['students'] = students
	d.close()
	print("finished")

def grade_all():
	stu = select_student()
	if not stu:
		return
	with shelve.open('data.dat') as d:
		students = d['students']
		tags = d['assignments']
	for tag in tags:
		print(f"Grading {tag}")
		grade(stu, tag)
	for i in range(len(students)):
		if students[i].name == stu.name:
			students[i] = stu
			break
	with shelve.open('data.dat') as d:
		d['students'] = students
		print("Data saved")
	print(f"{stu.name} Assignments: {stu.github}")
	print(stu.print_assignments())


def grade_student(text):
	stu = select_student(text)
	if stu:
		tag = validate_assign()
		try:
			assign = stu.assignments[tag]
			if assign.score < 5 and assign.late:
				print(f'Grading {stu.name} -- late')
				grade(stu,tag, False)
				print(f'{stu.name}: {tag} - {stu.assignments[tag].score}/10')
			elif assign.score < 10 and not assign.late:
				print(f'Grading {stu.name} -- on time: {stu.github}')
				grade(stu, tag, False)
				print(f'{stu.name}: {tag} - {stu.assignments[tag].score}/10')
			elif (assign.score == 10 and not assign.late) or (assign.score == 5 and assign.late):
				print(f"{stu.name} already has completed assignment")
			else:
				print(f"something strange happened in grade_student()")
			print("Grading complete -- saving...")
			d = shelve.open('data.dat')
			students = d['students']
			for i in range(len(students)):
				if students[i].name == stu.name:
					students[i] = stu
					break
			d['students'] = students
			d.close()
			print("Data saved")
		except KeyError as e:
			if tag != "done":
				print("That student doesn't have that assignment")

def report():
	with shelve.open('data.dat') as d:
		students = d['students']
		tags = d['assignments']
	header = ['Period','Last Name','First Name']
	for tag in tags:
		header.append(tag)
	stuff = [header]
	for stu in students:
		if stu.course == course:
			last, first = stu.name.split(',')
			row = [stu.period,last,first]
			for a in tags:
				s = str(stu.assignments[a].score)
				row.append(s)
			stuff.append(row)
	with open(f'{course}.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',', quotechar='|')
		w.writerows(stuff)
	print("Report complete")

def grade_multiple():
	tags = []
	r = ''
	while r != 'done':
		print("Enter assignment tags - type 'done' when finished.")
		r = validate_assign()
		if r != 'done':
			tags.append(r)
			print(tags)
	for tag in tags:
		grade_assignment(tag)
	print(f"Grading and Reporting done for {tags}")
