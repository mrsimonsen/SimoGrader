import shelve, csv, os
from student import Student
from assignment import Assignment
from subprocess import run

def reset_data():
	d = shelve.open('data.dat')
	#list of 1030 assignment prefixes
	d['python'] = ('00p','01p','02p','03p','04p','05p','06p','07p','08p','09p','10p','11p','12p','13p','14p','15p')
	#list of 1400 assignment prefixes
	d['java'] = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
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
	a = ''
	while a not in assign:
		a = input("Enter an assignment tag:\n")
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
		for i in range(len(periods)):
			if periods[i] == '1030':
				p.append(i+1)
			elif periods[i] == '1400':
				j.append(i+1)
		print(f"{len(p)} Python classes, {len(j)} Java classes")
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
			students.append(Student(f"{row[2]}, {row[1]}", int(row[3]), row[4]))
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
	search = input("Enter a part of a student name:\n")
	results = []
	for i in students:
		if search in i.name.lower():
			results.append(i)
	if len(results):
		print("0 - Quit")
		for i in range(len(results)):
			print(f"{i+1} - {results[i].name}")
		n = validate_num("Which student?")-1
		if n >= 0:
			return results[n]
		else:
			return None
	else:
		print(f"No students matched \"{search}\"")
		return None


def drop():
	stu = select_student()
	d = shelve.open('data.dat')
	students = d['students']
	for i in range(len(students)):
		if students[i].name == stu.name:
			students.pop(i)
			break
	d['students'] = students
	d.close()
	f = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'r',newline='')
	raw = csv.reader(f, delimiter= ',', quotechar = '"')
	new = []
	for row in raw:
		name = f"{row[2]}, {row[1]}"
		if name != stu.name:
			new.append(row)
		else:
			print(f"{stu.name} dropped")
	f.close()
	a = open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'w',newline='')
	w = csv.writer(a, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
	for row in new:
		w.writerow(row)
	a.close()

def run_python():
	try:
		p = run("python3 Tests.py",shell=True,capture_output=True,text=True)
		if p.stderr:
			print("Tests didn't run")
			score = None
		else:
			score = p.stdout.strip()
	except KeyboardInterrupt:
		print("Student test terminated")
		score = None
	return score

def run_java():
	try:
		p = run(f'javac Tests.java;java Tests',shell=True,capture_output=True)
		if p.stderr:
			print("Tests didn't compile")
			score = None
		else:
			score = p.stdout
	except KeyboardInterrupt:
		print("Student test terminated")
		score = None
	return score

def grade(stu,tag):
	os.system(f"gh repo clone {stu.clone(tag)} student")
	if os.path.isdir('student'):
		print("Testing...")
		os.chdir('student')
		if tag[-1] == 'j':
			os.system(f"cp ../Testing/{tag}.java Tests.java")
			stu.assignments[tag].set_score(run_java())
		elif tag[-1] == 'p':
			os.system(f"cp ../Testing/{tag}.py Tests.py")
			stu.assignments[tag].set_score(run_python())
		os.chdir('..')
		run(['rm','-rf','student'])
	else:
		print(f"{stu.name} hasn't startd the assignment")

