import shelve, csv, os, datetime, json
from sys import exit

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
	print("Gathering Repos...")
	os.system("gh repo list nuames-cs --json name -L 4444 > temp.json")
	old = []
	d = shelve.open('data.dat')
	tags = d['assignments']
	d.close()
	with open("temp.json") as file:
		repos = json.load(file)
	os.system("rm temp.json")
	print("Filtering Results...")
	for r in repos:
		if r["name"][:3] in tags and r["name"][-3:] != '.py':
			old.append(r['name'])
			print(f"{r['name']} added")
	total = len(old)
	print(f"{total} repos collected")
	if input("Delete?\n").lower() in ('yes','y'):
		c = 0
		print("checking authentication")
		os.system("gh auth refresh -h github.com -s delete_repo")
		for i in old:
			print(f"deleting nuames-cs/{i} ({c}/{total})")
			os.system(f"gh repo delete nuames-cs/{i} --confirm")
	print("Done.")

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
	if os.path.exists('students.txt'):
		print("Loading students...")
		with open('students.txt','r') as f:
			for line in f:
				if "last,first_weber,first_nuames,period,weber,github" in line:
					continue
				last,legal,nuames,period,weber,github = line.split(',')
				name = f"{last}, {legal} ({nuames})"
				students.append(Student(name,period,github.strip()))
		with shelve.open('data.dat') as d:
			new = []
			for stu in students:
				found = False
				for s in d['students']:
					if s.github == stu.github:
						found = True
						break
				if not found:
					new.append(stu)
			d['students'] += new
			print(f"{len(new)} new students loaded")
		#os.system("rm students.txt")
	else:
		print("Couldn't find \"students.txt\" file. Did you import it from NUAMES-CS/RSA-Encryption?")

def select_student(text=None):
	if not text:
		search = input("Enter a part of a student name or '0' to exit:\n")
	else:
		search = text
	if search == '0':
		return None
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

#function to use as a sorting key in choice 5 of mod_student
def fsort(obj):
	return obj.name

def grade_assignment(tag = None):
	if not tag:
		tag = validate_assign()
	d = shelve.open('data.dat')
	students = d['students']
	d.close()
	for stu in students:
		a = stu.assignments[tag]
		if a.score == 10:
			print(f"{stu.name} already has completed assignment")
		else:
			print(f"Cloning {stu.name}")
			grade(stu,tag)
			print(f"{stu.name}: {tag} - {stu.assignments[tag].score}/10")
	print("Grading complete -- saving...")
	with shelve.open('data.dat') as d:
		d['students'] = students
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
		grade(stu, tag, False)
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
			if assign.score < 10:
				print(f'Grading {stu.name} -- on time: {stu.github}')
				grade(stu, tag)
				print(f'{stu.name}: {tag} - {stu.assignments[tag].score}/10')
			elif assign.score == 10:
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
	header = ['Period','Name',]
	for tag in tags:
		header.append(tag)
	stuff = [header]
	for stu in students:
		row = [stu.period,stu.name]
		for a in tags:
			s = str(stu.assignments[a].score)
			row.append(s)
		stuff.append(row)
	with open(f'report.csv','w',newline='') as f:
		w = csv.writer(f, delimiter=',')
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
