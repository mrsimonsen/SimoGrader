import shelve, csv
from student import Student
from assignment import Assignment
from cleanup import main as clean

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

def mod_student():
	stu = select_student()
	choice = -1
	while choice != 0 and stu:
		print(stu)
		print("0 - Save/Back to Main Menu")
		print("1 - Change name")
		print("2 - Change github username")
		print("3 - Change class period")
		print("4 - Drop student")
		choice = -1
		while choice not in (0,1,2,3,4):
			choice = validate_num("What would you like to change?")
		if choice == 1:
			print(f"Changing {stu.name} name:")
			stu.name = change("Enter a new name:",stu.name)
		elif choice == 2:
			print(f"Changing {stu.name} username:")
			stu.github = change("Enter a new github username:",stu.github)
		elif choice == 3:
			print(f"Changing {stu.name} period:")
			stu.period = change("Enter a new period for username:",stu.period)
		elif choice == 4:
			print(f"Drop {stu.name}")
			if ask_yn("Are you sure? This CANNOT be undone.") == 'y':
				drop(stu)
				choice = 0
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

def	drop():
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

def mod_assign():
	stu = select_student()
	choice = None
	if stu:
		index = stu.period-1
		d = shelve.open('data.dat')
		if d['periods'][index] == '1030':
			tags = d['python']
		elif d['periods'][index] == '1400':
			tags = d['java']
		else:
			print(f"{index} isn't set as a programming class")
			choice = 0
		d.close()
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
			code, tag = tag_to_index(tags)
			stu.assignments[code].score = change_float("Enter a new score:", stu.assignments[code].score)
		elif choice == 2:
			code = tag_to_index(tags)
			if ask_yn(f"Set {tag} to late?") == 'y':
				stu.assignments[code].set_late()
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

def tag_to_index(tags):
	tag = None
	while tag not in tags:
		tag = input("What's the assignment tag?\n")
	code = int(tag[:-1])
	return code, tag
	
def main():
	print("Welcome to the Simonsen AutoGrater Data Utility")
	c = 14
	while c != '0':
		print("Main Menu")
		print("0 - Quit")
		print("1 - Grading Menu")
		print("2 - Class Menu")
		print("3 - Student Menu")
		print("4 - Reset Database")
		print("5 - Delete Old Repos")
		c = input("What's your selection?\n")
		
		if c == '0':
			print("Goodbye")
		elif c == '4':
			reset_data()
		elif c == '5':
			clean()
		elif c == '1':
			a = ''
			while a != '0':
				print("Grading Menu")
				print("0 - Return to Main Menu")
				print("1 - Grade an Assignment")
				print("2 - Grade a Single Assignment")
				print("3 - Generate Report")
				a = input("What's your selection?\n")

				if a=='0':
					print("Returning to Main Menu")
				elif a == '1':
					#verify assignment code
					#grade that assignment
						#for each student
							#if student score for that assignment is not max
								#add student url to list
						#clone list
						#for each repo in list
							#replace test file with mine
							#run test
							#update student assignment score
				elif a == '2':
					#validate a student
					#validate an assignment for that student
					#grade that student's assignment
						#clone url
						#replace test with mine
						#run test
						#update student assignment score
				elif a == '3':
					# ask for (python, java, all)
					#create a CSV file w/ header
						#header.append(period, student)
						#for assign in ask:
							#header.append(assign.code)
					#for each student
						#list.append(stu.period, stu.name)
						#for each assignment in stu.assign
							#list.append(stu.assign.score)
						#append data to CSV
				else:
					print("That's not a valid menu option.")
		elif c == '2':
			a = ''
			while a != '0':
				print("Class Menu")
				print("0 - Return to Main Menu")
				print("1 - View Classes")
				print("2 - Set Classes")
				a = input("What's your selection?\n")

				if a == '0':
					print("Returning to Main Menu")
				elif a == '1':
					display_classes()
				elif a == '2':
					set_periods()
				else:
					print("That's not a valid menu option.")
		elif c == '3':
			a = ''
			while a != '0':
				print("Student Menu")
				print("0 - Return to Main Menu")
				print("1 - View a Student")
				print("2 - Import Students")
				print("3 - Modify a Student")
				print("4 - Modify a Student's Assignment")
				a = input ("What's your selection?\n")

				if a == '0':
					print("Returning to Main Menu")
				elif a == '1':
					display_student()
				elif a == '2':
					set_students()
				elif a == '3':
					mod_student()
				elif a == '4':
					mod_assign()
				else:
					print("That's not a valid menu option.")
		else:
			print("That's not a valid menu option.")

if __name__ == "__main__":
	main()

