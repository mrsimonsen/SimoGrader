import shelve, csv, os, datetime
from student import Student
from assignment import Assignment
from subprocess import run
from github import Github
from dotenv import load_dotenv
from alive_progress import alive_bar
from sys import exit

def mark_late():
	#set assignment
	tag = validate_assign()
	#determine class Periods
	d = shelve.open('data.dat')
	periods = d['periods']
	p = d['python']
	j = d['java']
	w = d['web']
	if tag in p:
		cls = '1030'
	elif tag in j:
		cls = '1400'
	elif tag in w:
		cls = 'Web Dev'
	#load students
	students = d['students']
	#if student assignment grade is 0 and not already late
	counter = 0
	for stu in students:
		if periods[stu.period-1] == cls :
			a = stu.assignments[tag]
			if a.score == 0.0 and not a.late:
				counter += 1
				stu.assignments[tag].late = True
	d['students'] = students
	d.close()
	#display counter
	print(f"{counter} students set to late for {tag}")


def get_date():
	ok = False
	while not ok:
		year = validate_num("Year:(####)")
		month = validate_num("Month:(##)")
		day = validate("Day:(##)")
		try:
			d = datetime.datetime(year, month, day)
			ok = True
		except ValueError as e:
			print(e)
	return d

def not_template(name):
	if name[-3:] != ".py" and name[-5:] != ".java":
		return True
	return False

def clean():
	#get user credentials from .env
	load_dotenv()
	if (token := env.get('TOKEN')) == None:
		exit("Edit .env file to have your personal access token.")
	#make github object
	g = Github(token)
	print(f"Loaded credentials for {g.get_user().name}")
	#makedir for clone - set name to current date time
	repos = g.get_user().get_repos()
	print("Gathering all repos older than what date?")
	date = get_date()
	print("Gathering Repos...")
	old = []
	total = len(list(repos))
	print("Starting Search..")
	with alive_bar(total, bar='classic', spinner='classic') as bar:
		for r in repos:
			if r.organization == "NUAMES-CS" and not_template(r.name) and r.updated_at < date:
				old.append(r)
			bar()
	for i in old:
		print(i)
	print(f"{len(old)} repos collected")
	if a := (input("Delete?\n").lower() in ('yes','y')):
		for i in old:
			print(f"deleting {i.name}")
			i.delete()
	if not a:
		print("Nothing Deleted.")
	print("Done.")

def reset_data():
	d = shelve.open('data.dat')
	#list of 1030 assignment prefixes
	d['python'] = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p')
	#list of 1400 assignment prefixes
	d['java'] = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
	d['web'] = ('web')
	#list of course periods
	periods = []
	for i in range(8):
		periods.append('empty')
	d['periods'] = periods
	d['students'] = []
	d.close()
	print("Data has been reset")

def validate_num(question):
	ok = False
	while not ok:
		try:
			number = int(input(f"{question}\n"))
			ok = True
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
		assign += d['java']
		assign += d['python']
		assign += ['web']
		assign.append('done')
	a = ''
	print(assign)
	while a not in assign:
		a = input("Enter an assignment tag:\n").lower()
	return a

def set_periods():
	r = 'n'
	d = shelve.open('data.dat')
	periods = d['periods']
	#while not correct
	while r == 'n':
		n = validate_num("How many 1030 sections this semester?")
		for i in range(n):
			x = validate_num(f"Enter class period for 1030 section number {i+1}:")
			periods[x-1] = '1030'
		n = validate_num("How many 1400 sections this semester?")
		for i in range(n):
			x = validate_num(f"Enter class period for 1400 section number {i+1}:")
			periods[x-1] = '1400'
		n = validate_num("How many Web Dev sections this semester?")
		for i in range(n):
			x = validate_num(f"Enter class period for web section number {i+1}:")
			periods[x-1] = 'Web Dev'
		print(f"Periods: {periods}")
		r = ask_yn("Is this correct?")
	d['periods'] = periods
	d.close()
	print("Course periods have been saved")

def display_classes():
	with shelve.open('data.dat') as f:
		periods = f['periods']
		p = []
		j = []
		w = []
		for i in range(len(periods)):
			if periods[i] == '1030':
				p.append(i+1)
			elif periods[i] == '1400':
				j.append(i+1)
			elif periods[i] == 'Web Dev':
				w.append(i+1)
		print(f"{len(p)} Python classes, {len(j)} Java classes")
		print(f"\tWeb Dev periods: {w}")
		print(f"\tPython periods: {p}")
		print(f"\tJava periods: {j}")

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
		print(f"{stu.name} Assignments")
		print(stu.print_assignments())

def select_student():
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	search = None
	while search != '0':
		search = input("Enter a part of a student name or '0' to exit:\n")
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

def run_java(simple):
	try:
		p = run(f"javac Tests.java;java Tests {'simple' if simple else ''}",shell=True,capture_output=True,text=True)
		if p.stderr:
			print("Tests didn't compile")
			score = None
		else:
			out = p.stdout.strip().split('\n')
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
		if tag[-1] == 'j':
			os.system(f"cp ../Testing/{tag}.java Tests.java")
			stu.assignments[tag].set_score(run_java(simple))
		elif tag[-1] == 'p':
			os.system(f"cp ../Testing/{tag}.py Tests.py")
			stu.assignments[tag].set_score(run_python(simple))
		os.chdir('..')
		run(['rm','-rf','student'])
	else:
		print(f"{stu.name} hasn't started the assignment")

def mod_student():
	stu = select_student()
	choice = -1
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
			stu.name = change("Enter a new name:",stu.name)
		elif choice == 2:
			print(f"Changing {stu.name} username:")
			stu.github = change("Enter a new github username:",stu.github)
		elif choice == 3:
			print(f"Changing {stu.name} period:")
			stu.period = change(f"Enter a new period for {stu.name}:",stu.period, True)
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

#function to use as a sorting key in choice 5 of mod_student
def fsort(obj):
	return obj.name

def create():
	print("Adding a student to the roster.")
	correct = 'n'
	d =  shelve.open('data.dat')
	periods = d['periods']
	students = d['students']
	d.close()
	while correct == 'n':
		fname = input("What is the student's first name?\n").title()
		lname = input("What is the student's last name?\n").title()
		period = int(input("What class period is the student in?\n"))
		course = periods[period-1]
		git = input("What is the student's GitHub username?\n")
		print(f"Student: {lname}, {fname}")
		print(f"Period: {period} - {course}")
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
	elif tag == 'web':
		grading = "Web Dev"
	else:
		grading = None
	for stu in students:
		if stu.course == grading:
			if grading == "Web Dev":
				print(f"Cloning {stu.github}")
				os.system(f"gh repo clone nuames-cs/web-dev-{stu.github} web/{stu.github} -- -q")
				continue
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
	d = shelve.open('data.dat')
	students = d['students']
	periods = d['periods']
	if periods[stu.period-1] == '1030':
		tags = d['python']
		d.close()
	elif periods[stu.period-1] == '1400':
		tags = d['java']
		d.close()
	else:
		print('not a grade-able period')
		d.close()
		return
	for tag in tags:
		print(f"Grading {tag}")
		grade(stu, tag)
	d = shelve.open('data.dat')
	students = d['students']
	for i in range(len(students)):
		if students[i].name == stu.name:
			students[i] = stu
			break
	d['students'] = students
	d.close()
	print("Data saved")
	print(f"{stu.name} Assignments")
	print(stu.print_assignments())


def grade_student():
	stu = select_student()
	if stu:
		tag = validate_assign()
		try:
			assign = stu.assignments[tag]
			if assign.score < 5 and assign.late:
				print(f'Grading {stu.name} -- late')
				grade(stu,tag, False)
				print(f'{stu.name}: {tag} - {stu.assignments[tag].score}/10')
			elif assign.score < 10 and not assign.late:
				print(f'Grading {stu.name} -- on time')
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
			print("That student doesn't have that assignment")

def report(course = None):
	# ask for (python, java, all)
	while course not in ('all','1030','1400','web'):
		print("Select a course to report on:")
		print("all - All courses")
		print("1030 - Python")
		print("1400 - Java")
		print("web - Web Dev")
		course = input("What's your selection?\n").lower()
	if course in ('1030','1400','web'):
		write(course)
	if course == 'all':
		write('web')
		write('1030')
		write('1400')
	print("Report complete")

def write(course):
	with shelve.open('data.dat') as d:
		students = d['students']
		python = d['python']
		java = d['java']
		web = d['web']
	header = ['Period','Last Name','First Name']
	if course == '1030':
		for tag in python:
			header.append(tag)
		tags = python
	elif course == '1400':
		for tag in java:
			header.append(tag)
		tags = java
	elif course == 'Web Dev':
		for tag in web:
			header.append(tag)
		tags = web
	stuff = [header]
	for stu in students:
		if stu.course == course:
			last, first = stu.name.split(',')
			row = [stu.period,last,first]
			for a in tags:
				s = str(stu.assignments[a].score)
				if stu.assignments[a].late:
					s += "L"
				row.append(s)
			stuff.append(row)
	with open(f'{course}.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',', quotechar='|')
		w.writerows(stuff)

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
	if 'p' in tags:
		report('1030')
	if 'j' in tags:
		report('1400')
	if 'w' in tags:
		report('Web Dev')
	print(f"Grading and Reporting done for {tags}")
